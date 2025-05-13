# Powertron Web Application

A Flask-based web application for educational management system.

## Features

- User Authentication (Students and Lecturers)
- Profile Management
- Course Management
- Assignment Handling
- Event Notifications
- File Uploads (Cloudinary Integration)

## Setup

1. Clone the repository:
```bash
git clone <your-repository-url>
cd powertron_web
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with the following variables:
```
MONGODB_URI=your_mongodb_uri
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
```

4. Run the application:
```bash
python run.py
```

## Project Structure

```
powertron_web/
├── .env                  # Environment variables
├── .gitignore           # Git ignore file
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
├── run.py              # Application entry point
└── powertron/          # Main application package
    ├── __init__.py     # Package initialization
    ├── app.py          # Main application file
    ├── extensions.py   # Flask extensions
    ├── decorators.py   # Custom decorators
    └── models.py       # Database models
```

## Technologies Used

- Flask
- MongoDB Atlas
- Flask-SocketIO
- Cloudinary
- Python-dotenv

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.7 or higher
- MongoDB (for data storage)
- Git

## Environment Variables

Create a `.env` file in the root directory with the following variables:
```
MONGODB_URI=your_mongodb_connection_string
SECRET_KEY=your_secret_key
DEBUG=True/False
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, please open an issue in the GitHub repository.

# Powertron Web Application

## Backup Procedures

### Automatic Backup Script
1. Run the backup script before making major changes:
   ```bash
   python backup_config.py
   ```
2. Backups will be stored in the `backups` directory with timestamps

### Manual Backup Steps
1. Before making major changes:
   - Commit all changes to git
   - Push to GitHub
   - Create a zip file of the entire project

### GitHub Backup
1. Always push changes to GitHub regularly
2. Use meaningful commit messages
3. Create branches for major features

### Local Backup
1. Keep a copy of the project on an external drive
2. Update the external backup weekly
3. Store backup files in a different physical location

## Project Structure
[Project structure will be added once we can access the files]

## Development Guidelines
1. Always commit code before powering off
2. Use UPS for critical development sessions
3. Regular commits to prevent data loss

## Contact
For any issues or questions, please contact the development team.
