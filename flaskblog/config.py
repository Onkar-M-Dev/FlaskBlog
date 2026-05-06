import os


class Config:
    # ==========================================
    # Core Flask Configuration
    # ==========================================
    SECRET_KEY = os.environ.get(
        'SECRET_KEY',
        'devkey'
    )

    # ==========================================
    # Database Configuration
    # ==========================================
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI',
        'sqlite:///site.db'
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ==========================================
    # Mail Configuration (SendGrid)
    # ==========================================
    MAIL_SERVER = 'smtp.sendgrid.net'
    MAIL_PORT = 587

    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    # SendGrid SMTP Credentials
    MAIL_USERNAME = 'apikey'
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    # Verified Sender Email (same email verified in SendGrid)
    MAIL_DEFAULT_SENDER = 'dontreply.flaskblog@gmail.com'

    # Prevent long SMTP hangs
    MAIL_MAX_EMAILS = 5
    MAIL_SUPPRESS_SEND = False
    MAIL_ASCII_ATTACHMENTS = False