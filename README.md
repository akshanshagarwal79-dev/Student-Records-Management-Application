# CampusDesk — Student Management Web Frontend

A clean, responsive, blue-and-white web interface for the supplied Python/MySQL Student Management System. It includes a Flask web layer so the existing console-based scripts are not called directly from HTML.

## Features
- Admin login and logout
- Dashboard with student, marks, course and pass-count summaries
- Student create, list, search, edit and delete
- Five-subject marks entry, edit and delete
- Report-card listing and printable report card (browser Print → Save as PDF)
- Admin password update

## Requirements
- Python 3.10+
- MySQL Server

## Setup
1. Open a terminal in this folder.
2. Create and activate a virtual environment:
   - Windows: `py -m venv .venv` then `.venv\\Scripts\\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Create the database/tables by importing `schema.sql` into MySQL. If you already have the `student` database and tables from the original project, back them up first and do not blindly re-import/alter them. Check that their columns match `schema.sql`.
5. Set environment variables using `.env.example` as a guide. For example in Windows PowerShell:
   `$env:DB_PASSWORD='your_mysql_password'`
   `$env:SECRET_KEY='a-long-random-secret'`
6. Run: `python app.py`
7. Open `http://127.0.0.1:5000` in your browser.

## Initial login
If you are using the included schema and it created the first admin row, the temporary password is `admin123`. Change it from Settings immediately. If you already have an admin row from the original project, its current password can be used; the login supports the original plaintext password format and Werkzeug password hashes.

## Important compatibility notes
- The supplied source files show a `student` table with `rollno, name, fname, gender, dob, address, phone, course, section` and a `marks` table with five subject/marks pairs plus totals and grade. The included schema follows those fields.
- This web version replaces console prompts with browser forms and uses the same MySQL database. It does not import the original console modules because those modules execute `input()` prompts and terminal menu code.
- The employee scripts (`add_emp.py`, `list_emp.py`, etc.) use a separate `company` database and are not part of the student portal workflow, so they are not wired into this frontend.
- The development server uses Flask debug mode. Do not expose it publicly; disable debug mode and use a production WSGI server before deployment.
- For production, use a dedicated MySQL user with limited permissions, a strong `SECRET_KEY`, HTTPS, CSRF protection, and secure password migration.
