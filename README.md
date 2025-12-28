# QR Attendance System 📊

## A Secure, Efficient QR Code-Based Attendance Management System for Educational Institutions

The **QR Attendance System** is a robust backend server built with **Django** and **Django REST Framework (DRF)**. It streamlines classroom attendance by enabling instructors to generate **time-sensitive QR codes** for sessions, allowing students to mark attendance instantly via mobile devices.

This solution eliminates manual roll calls, reduces administrative overhead, and provides accurate, real-time attendance records.

**Key Workflow:**
Instructor generates QR code → Displays in class → Students scan → Attendance automatically recorded

---

## Features

* **Dynamic QR Code Generation** — Unique, time-bound QR codes per class session to prevent proxy attendance
* **Instant Attendance Marking** — Students scan via any QR scanner and submit through API
* **Comprehensive Attendance Records** — Track by student, class, date, and session
* **Role-Based Access** — Separate endpoints for instructors and students
* **Class & Session Management** — Organize classes, subjects, and timetables
* **Secure Authentication** — Login and protected API endpoints
* **Extensible Design** — Ready for integration with mobile apps and admin dashboards

---

## Technology Stack

| Component          | Technology                             |
| ------------------ | -------------------------------------- |
| Framework          | Django 4.x + Django REST Framework     |
| API                | RESTful endpoints with JSON            |
| Database           | SQLite (development), PostgreSQL-ready |
| QR Code Generation | Python `qrcode` library + Pillow       |
| Authentication     | Django Authentication / JWT support    |
| Deployment         | Gunicorn, Nginx, Docker compatible     |

---

## Project Structure

```
Qr_Attendence_Server/
├── account/                # User management and authentication
├── attendance/             # Core QR generation and marking logic
├── classes/                # Class sessions and timetable management
├── academics/              # Academic models (years, departments, etc.)
├── college_attendance/     # Project settings and root URLs
├── manage.py
└── db.sqlite3
```

---

## API Endpoints

All endpoints are prefixed with `/api/` and require authentication where applicable.

| Method | Endpoint                   | Description                                               |
| ------ | -------------------------- | --------------------------------------------------------- |
| POST   | `/account/login/`          | Authenticate user (returns token/session)                 |
| GET    | `/classes/list/`           | Retrieve active/upcoming class sessions                   |
| POST   | `/attendance/generate-qr/` | Generate dynamic QR for current session (Instructor only) |
| POST   | `/attendance/mark/`        | Mark attendance using scanned QR data                     |
| GET    | `/attendance/view/`        | View attendance records (by class, student, or date)      |

---

## Installation & Setup

```bash
git clone https://github.com/charitraa/Qr_Attendence_Server.git
cd Qr_Attendence_Server

# Create virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Install dependencies
pip install django djangorestframework qrcode[pil] pillow

# Apply migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

**Server:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
**Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Future Enhancements

* Dedicated mobile app (Flutter / React Native) for QR scanning
* Real-time attendance dashboard with analytics
* Export attendance reports (PDF / Excel)
* Geolocation verification for added security
* Email/SMS alerts for low attendance
* LMS integration for institutions

---

## Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request with a clear description

---

## License

Released under the **MIT License**. See `LICENSE` file for details.

🔗 Repository: [https://github.com/charitraa/Qr_Attendence_Server](https://github.com/charitraa/Qr_Attendence_Server)

A modern solution for efficient and accurate attendance management in educational environments 🚀
