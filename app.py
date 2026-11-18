import os
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
import mysql.connector
from mysql.connector import Error
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'change-this-secret-before-deployment')

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD') or 'akk@123',
    'database': os.getenv('DB_NAME', 'student'),
}


def get_db():
    return mysql.connector.connect(**DB_CONFIG)


def query_db(sql, params=(), one=False, commit=False):
    conn = get_db()
    cur = conn.cursor(dictionary=True)
    try:
        cur.execute(sql, params)
        if commit:
            conn.commit()
            return cur.rowcount
        return cur.fetchone() if one else cur.fetchall()
    finally:
        cur.close()
        conn.close()


def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('login'))
        return fn(*args, **kwargs)
    return wrapper


def grade_for(percentage):
    if percentage >= 80: return 'A'
    if percentage >= 60: return 'B'
    if percentage >= 40: return 'C'
    return 'F'


@app.route('/', methods=['GET', 'POST'])
def login():
    if session.get('admin_logged_in'):
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        password = request.form.get('password', '')
        try:
            row = query_db('SELECT password FROM admin LIMIT 1', one=True)
            stored = row['password'] if row else None
            valid = False
            if stored:
                if stored.startswith(('pbkdf2:', 'scrypt:')):
                    valid = check_password_hash(stored, password)
                else:  # supports the plaintext password used by the original college project
                    valid = stored == password
            if valid:
                session['admin_logged_in'] = True
                flash('Welcome back. You are signed in.', 'success')
                return redirect(url_for('dashboard'))
            flash('Incorrect password. Please try again.', 'error')
        except Error as exc:
            flash(f'Database connection failed: {exc}', 'error')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
    stats = {
        'students': query_db('SELECT COUNT(*) AS n FROM student', one=True)['n'],
        'marks': query_db('SELECT COUNT(*) AS n FROM marks', one=True)['n'],
        'courses': query_db('SELECT COUNT(DISTINCT course) AS n FROM student', one=True)['n'],
        'passed': query_db("SELECT COUNT(*) AS n FROM marks WHERE percentage >= 40", one=True)['n'],
    }
    recent = query_db('SELECT rollno, name, course, section FROM student ORDER BY rollno DESC LIMIT 6')
    return render_template('dashboard.html', stats=stats, recent=recent)


@app.route('/students')
@login_required
def students():
    term = request.args.get('q', '').strip()
    if term:
        like = f'%{term}%'
        rows = query_db('SELECT * FROM student WHERE CAST(rollno AS CHAR) LIKE %s OR name LIKE %s OR course LIKE %s ORDER BY rollno', (like, like, like))
    else:
        rows = query_db('SELECT * FROM student ORDER BY rollno')
    return render_template('students.html', students=rows, q=term)


@app.route('/students/add', methods=['GET', 'POST'])
@app.route('/students/<int:rollno>/edit', methods=['GET', 'POST'])
@login_required
def student_form(rollno=None):
    editing = rollno is not None
    record = query_db('SELECT * FROM student WHERE rollno=%s', (rollno,), one=True) if editing else None
    if editing and not record:
        abort(404)
    if request.method == 'POST':
        f = request.form
        values = (f['name'].strip(), f.get('fname','').strip(), f.get('gender',''), f.get('dob') or None,
                  f.get('address','').strip(), f.get('phone','').strip(), f.get('course','').strip(), f.get('section','').strip())
        try:
            if editing:
                query_db('UPDATE student SET name=%s,fname=%s,gender=%s,dob=%s,address=%s,phone=%s,course=%s,section=%s WHERE rollno=%s', values + (rollno,), commit=True)
                flash('Student record updated.', 'success')
            else:
                new_roll = int(f['rollno'])
                query_db('INSERT INTO student (rollno,name,fname,gender,dob,address,phone,course,section) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)', (new_roll,) + values, commit=True)
                flash('Student added successfully.', 'success')
            return redirect(url_for('students'))
        except (Error, ValueError) as exc:
            flash(f'Could not save student: {exc}', 'error')
    return render_template('student_form.html', student=record, editing=editing)


@app.post('/students/<int:rollno>/delete')
@login_required
def student_delete(rollno):
    try:
        query_db('DELETE FROM student WHERE rollno=%s', (rollno,), commit=True)
        flash('Student record deleted.', 'success')
    except Error as exc:
        flash(f'Could not delete student: {exc}', 'error')
    return redirect(url_for('students'))


@app.route('/marks')
@login_required
def marks():
    term = request.args.get('q', '').strip()
    if term:
        like = f'%{term}%'
        rows = query_db('SELECT * FROM marks WHERE CAST(rollno AS CHAR) LIKE %s OR name LIKE %s ORDER BY rollno', (like, like))
    else:
        rows = query_db('SELECT * FROM marks ORDER BY rollno')
    return render_template('marks.html', records=rows, q=term)


@app.route('/marks/add', methods=['GET', 'POST'])
@app.route('/marks/<int:rollno>/edit', methods=['GET', 'POST'])
@login_required
def marks_form(rollno=None):
    editing = rollno is not None
    record = query_db('SELECT * FROM marks WHERE rollno=%s', (rollno,), one=True) if editing else None
    if editing and not record:
        abort(404)
    student_rows = query_db('SELECT rollno,name,fname,course,section FROM student ORDER BY rollno')
    if request.method == 'POST':
        f = request.form
        try:
            rno = int(f['rollno'])
            student = query_db('SELECT * FROM student WHERE rollno=%s', (rno,), one=True)
            if not student:
                flash('Add this student record before entering marks.', 'error')
                return redirect(request.url)
            subjects, scores = [], []
            for i in range(1, 6):
                subjects.append(f.get(f'subject{i}', '').strip())
                score = int(f[f'marks{i}'])
                if not 0 <= score <= 100:
                    raise ValueError('Each subject mark must be between 0 and 100.')
                scores.append(score)
            total = sum(scores)
            percentage = total / 5
            grade = grade_for(percentage)
            values = (rno, student['name'], student['fname'], student['course'], student['section'],
                      subjects[0], scores[0], subjects[1], scores[1], subjects[2], scores[2],
                      subjects[3], scores[3], subjects[4], scores[4], total, percentage, grade)
            if editing:
                sql = '''UPDATE marks SET name=%s,father_name=%s,class=%s,section=%s,subject1=%s,marks1=%s,
                         subject2=%s,marks2=%s,subject3=%s,marks3=%s,subject4=%s,marks4=%s,subject5=%s,marks5=%s,
                         total_marks=%s,percentage=%s,grade=%s WHERE rollno=%s'''
                query_db(sql, values[1:] + (rollno,), commit=True)
                flash('Marks updated successfully.', 'success')
            else:
                sql = '''INSERT INTO marks (rollno,name,father_name,class,section,subject1,marks1,subject2,marks2,
                         subject3,marks3,subject4,marks4,subject5,marks5,total_marks,percentage,grade)
                         VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                query_db(sql, values, commit=True)
                flash('Marks saved successfully.', 'success')
            return redirect(url_for('marks'))
        except (Error, ValueError, KeyError) as exc:
            flash(f'Could not save marks: {exc}', 'error')
    return render_template('marks_form.html', record=record, students=student_rows, editing=editing)


@app.post('/marks/<int:rollno>/delete')
@login_required
def marks_delete(rollno):
    try:
        query_db('DELETE FROM marks WHERE rollno=%s', (rollno,), commit=True)
        flash('Marks record deleted.', 'success')
    except Error as exc:
        flash(f'Could not delete marks: {exc}', 'error')
    return redirect(url_for('marks'))


@app.route('/reports')
@login_required
def reports():
    term = request.args.get('q', '').strip()
    if term:
        like = f'%{term}%'
        rows = query_db('SELECT m.rollno,m.name,m.class,m.section,m.total_marks,m.percentage,m.grade FROM marks m WHERE CAST(m.rollno AS CHAR) LIKE %s OR m.name LIKE %s ORDER BY m.rollno', (like, like))
    else:
        rows = query_db('SELECT rollno,name,class,section,total_marks,percentage,grade FROM marks ORDER BY rollno')
    return render_template('reports.html', reports=rows, q=term)


@app.route('/reports/<int:rollno>')
@login_required
def report_card(rollno):
    record = query_db('SELECT m.*,s.dob,s.address,s.phone,s.course FROM marks m LEFT JOIN student s ON s.rollno=m.rollno WHERE m.rollno=%s', (rollno,), one=True)
    if not record:
        abort(404)
    subjects = []
    for i in range(1, 6):
        score = record[f'marks{i}']
        subjects.append({'name': record[f'subject{i}'], 'marks': score, 'grade': grade_for(float(score))})
    return render_template('report_card.html', record=record, subjects=subjects)


@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        new = request.form.get('new_password', '')
        confirm = request.form.get('confirm_password', '')
        if len(new) < 8:
            flash('Use a password with at least 8 characters.', 'error')
        elif new != confirm:
            flash('The passwords do not match.', 'error')
        else:
            query_db('UPDATE admin SET password=%s', (generate_password_hash(new),), commit=True)
            flash('Admin password changed.', 'success')
            return redirect(url_for('settings'))
    return render_template('settings.html')


@app.errorhandler(404)
def not_found(_):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
