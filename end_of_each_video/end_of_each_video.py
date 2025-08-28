#Video-1 Getting Started
# features of the web app that we are building
# 'Flask_Blog' - THE NEW PROJECT DIRECTORY/FOLDER
# 'flaskblog.py' - New file in above project directory
# install 'flask' on cmd prompt.
# import 'Flask' from 'flask' & running it in debug mode
# Hello World Example
# 3 New 'routes' - /, /home, /about in 'flaskblog.py'
# 17:09


#Video-2 Templates
# New Directory/folder - 'templates' in 'Flask_Blog'
# 2 New files in 'templates' - 'home.html', 'about.html' 
# importing 'render_template' from 'flask' in 'flaskblog.py'
# 'render_template' and '.html' file that is passed in 'return' function in 'routes' work in sync.
# use of Jinja Template Engine
# 3rd New file in 'templates' folder - 'layout.html'
# use of 'extends' keyword in 'about.html', 'home.html'.
# Meta tags, Bootstrap CSS ; Bootstrap, Popper & JavaScript from 'Starter template' of Bootstrap Documentation.
# Copy Code from 'navigation.html', 'main.html' from 'snippets' folder from GITHUB & Paste it in 'layout.html'.
# New Directory/folder - 'static' in 'Flask_Blog'
# 1 New file in 'static' - 'main.css' - Copy Code from 'main.css' from 'snippets' folder from GITHUB & Paste it in 'main.css' in 'static' folder.
# importing 'url_for' from 'flask' in 'flaskblog.py'
# Copy Code from 'article.html' from 'snippets' folder from GITHUB & Paste it in 'home.html' in 'templates' folder.
# 31.42


#Video-3 Forms & User Input
# install 'flask-wtf' on cmd prompt.
# 'forms.py' - New file in project directory
# importing 'FlaskForm' from 'flask_wtf' in 'forms.py'
# 1st CLASS in 'forms.py' - 'RegistrationForm' inherited from 'FlaskForm'  
# importing 'StringField' from 'wtforms' in 'forms.py'
# importing 'DataRequired', 'Length', 'Email' from 'wtforms.validators' in 'forms.py'
# importing 'PasswordField' from 'wtforms' in 'forms.py'
# importing 'EqualTo' from 'wtforms.validators' in 'forms.py'
# importing 'SubmitField' from 'wtforms' in 'forms.py'
# 2nd CLASS in 'forms.py' - 'LoginForm' inherited from 'FlaskForm'
# importing 'BooleanField' from 'wtforms' in 'forms.py'
# importing 'secrets' on cmd prompt (Python-REPL), generating 'SECRET_KEY' using 'secrets.token_hex(16)'
# Copy the Output of 'secrets.token_hex(16)' from cmd prompt and Paste it in 'flaskblog.py' in 'app.config'.
# importing 'RegistrationForm', 'LoginForm' from 'forms' in 'flaskblog.py'
# 2 New 'routes' - /register, /login in 'flaskblog.py'
# 2 New files in 'templates' - 'register.html', 'login.html'
# use of methods like 'GET', 'POST' in 'flaskblog.py' in '/register' route
# use of 'validate_on_submit' method in '/register' route
# importing 'flash' from 'flask' in 'flaskblog.py' 
# importing 'redirect' from 'flask' in 'flaskblog.py' 
# Making necessary changes and designing the 'register.html', 'login.html'
# use of methods like 'GET', 'POST' in 'flaskblog.py' in '/login' route
# use of 'validate_on_submit' method in '/login' route
# 48:16


#Video-4 Database with Flask-SQLAlchemy
# install 'flask-sqlalchemy' on cmd prompt.
# importing 'SQLAlchemy' from 'flask_sqlalchemy' in 'flaskblog.py'
# set path to 'SQLALCHEMY_DATABASE_URI' in 'app.config' in 'flaskblog.py'
# 1st CLASS in 'flaskblog.py' - 'User' inherited from 'db.Model'
# use of '__repr__' method in class 'User' in 'flaskblog.py'
# 2nd CLASS in 'flaskblog.py' - 'Post' inherited from 'db.Model'
# importing 'datetime' from 'datetime' in 'flaskblog.py'
# use of '__repr__' method class 'Post' in 'flaskblog.py'
# Follow the cmd prompt instructions as per the paper
# 29:58


#Video-5 Package Structure
# 'models.py' - New file in 'Flask_Blog' directory
# Cut Code of class 'User' and 'Post' from 'flaskblog.py' & Paste it in 'models.py'
# importing 'db' from 'flaskblog' in 'models.py'
# Cut 'datetime' import from 'flaskblog.py' & Paste it in 'models.py'
# importing 'User', 'Post' from 'models' in 'flaskblog.py'
# Concept of 'Circular Import'
# 'flaskblog' - New Folder in 'Flask_Blog' Directory/Folder
# '__init__.py' - New File in 'flaskblog' folder 
# Move 'models.py', 'forms.py', 'templates' folder, 'static' folder, 'instance' folder in 'flaskblog' folder (except for 'flaskblog.py' file)
# Copy some Code from 'flaskblog.py' and Paste it in '__init__.py'
# 'routes.py' - New file in 'flaskblog' folder in project directory 'Flask_Blog'
# Copy some Code from 'flaskblog.py' and Paste it in 'routes.py'
# rename the file 'flaskblog.py' as 'run.py'
# importing 'app' from 'flaskblog' in 'run.py'
# Cut the import of 'render_template', 'url_for', 'flash', 'redirect' from 'flask' in '__init__.py' to 'routes.py'
# Cut the import of 'RegistrationForm', 'LoginForm' from 'forms' in '__init__.py' to 'routes.py'
# importing 'app' from 'flaskblog' in 'routes.py'
# importing 'routes' from 'flaskblog' in '__init__.py'
# Follow the cmd prompt instructions as per the paper
# 20:37


#Video-6 User Authentication
# install 'flask-bcrypt' on cmd prompt.
# importing 'Bcrypt' from 'flask_bcrypt' in '__init__.py'
# importing 'db', 'bcrypt' from 'flaskblog' in 'routes.py'
# importing 'User' from 'flaskblog.models' in 'forms.py'
# importing 'ValidationError' from 'wtforms.validators' in 'forms.py'
# install 'flask-login' on cmd prompt.
# importing 'LoginManager' from 'flask_login' in '__init__.py'
# importing 'login_manager' from 'flaskblog' in 'models.py'
# a new decorator 'login_manager.user_loader' in 'models.py'
# importing 'UserMixin' from 'flask_login' in 'models.py'
# importing 'login_user' from 'flask_login' in 'routes.py'
# importing 'current_user' from 'flask_login' in 'routes.py'
# 1 New 'route' - /logout in 'routes.py'
# importing 'logout_user' from 'flask_login' in 'routes.py'
# 1 New 'route' - /account in 'routes.py'
# use of '@login_required' decorator in above newly created route in 'routes.py' 
# 1 New file in 'templates' - 'account.html'
# importing 'login_required' from 'flask_login' in 'routes.py'
# importing 'request' from 'flask' in 'routes.py'
# 47:14


#Video-7 User Account & Profile Picture
# a picture with name 'default.jpg' should be in a New folder named 'profile_pics' in 'static' folder
# 3rd CLASS in 'forms.py' - 'UpdateAccountForm' inherited from 'FlaskForm' 
# importing 'current_user' from 'flask_login' in 'forms.py'
# importing 'current_user' from 'flask_login' in 'forms.py'
# importing 'UpdateAccountForm' from 'flaskblog.forms' in 'routes.py'
# use of methods like 'GET', 'POST' in 'routes.py' in '/account' route
# use of 'validate_on_submit' method in '/account' route
# importing 'FileField' & 'FileAllowed' from 'flask_wtf.file' in 'forms.py'
# use of 'enctype' in 'account.html'
# new function 'save_picture()' in 'routes.py'
# importing 'secrets' in 'routes.py'
# importing 'os' in 'routes.py'
# install 'Pillow' on cmd prompt.
# importing 'Image' from 'PIL' in 'routes.py'
# 42:14


#Video-8 Create, Update & Delete Posts
# 1 New 'route' - /post/new in 'routes.py'
# use of '@login_required' decorator in above newly created route in 'routes.py' (line-134)
# 1 New file in 'templates' - 'create_post.html'
# 4th CLASS in 'forms.py' - 'PostForm' inherited from 'FlaskForm' 
# importing 'TextAreaField' from 'wtforms' in 'forms.py'
# importing 'PostForm' from 'flaskblog.forms' in 'routes.py'
# use of methods like 'GET', 'POST' in 'routes.py' in '/post/new' route
# use of 'validate_on_submit' method in '/post/new' route
# 1 New 'route' - /post/<int:post_id> in 'routes.py'
# 1 New file in 'templates' - 'post.html'
# 1 New 'route' - /post/<int:post_id>/update in 'routes.py'
# use of '@login_required' decorator in above newly created route in 'routes.py' (line-144)
# importing 'abort' from 'flask' in 'routes.py'
# use of methods like 'GET', 'POST' in 'routes.py' in '/post/<int:post_id>/update' route
# use of 'validate_on_submit' method in '/post/<int:post_id>/update' route
# 'Modal' component from Bootstrap Documentation
# 1 New 'route' - /post/<int:post_id>/delete in 'routes.py'
# use of method 'POST' in 'routes.py' in '/post/<int:post_id>/delete' route
# use of '@login_required' decorator in above newly created route in 'routes.py' (line-150)
# 48:12


#Video-9 Pagination
# Either use the process of adding posts from video or manually add 10-20 posts on the web app 
# 1 New 'route' - /user/<string:username> in 'routes.py'
# 1 New file in 'templates' - 'user_posts.html'
# 31:21


#Video-10 Email & Password Reset
# importing 'URLSafeTimedSerializer' as 'Serializer' from 'itsdangerous' in 'models.py'
# importing 'app' from 'flaskblog' in 'models.py'
# use of '@staticmethod' decorator in 'verify_reset_token()' function in 'User' class in 'models.py'
# 5th CLASS in 'forms.py' - 'RequestResetForm' inherited from 'FlaskForm' 
# 6th CLASS in 'forms.py' - 'ResetPasswordForm' inherited from 'FlaskForm' 
# importing 'RequestResetForm', 'ResetPasswordForm' from 'flaskblog.forms' in 'routes.py'
# 1 New 'route' - /reset_password in 'routes.py'
# use of methods like 'GET', 'POST' in 'routes.py' in '/reset_password' route
# use of 'validate_on_submit' method in '/reset_password' route
# 1 New file in 'templates' - 'reset_request.html'
# 1 New 'route' - /reset_password/<token> in 'routes.py'
# use of methods like 'GET', 'POST' in 'routes.py' in '/reset_password/<token>' route
# 1 New file in 'templates' - 'reset_token.html'
# new function 'send_reset_email()' in 'routes.py'
# install 'flask-mail' on cmd prompt.
# importing 'Mail' from 'flask_mail' in '__init__.py'
# importing 'os' in '__init__.py'
# Follow the change of 'app passwords' in the mail settings of the mail mentioned while creating environmemt variable for 
#[Continued from line 181] 'EMAIL_USER' i.e. ('MAIL_USERNAME') and 'EMAIL_PASS' i.e. ('MAIL_PASSWORD') , copy the 
#[Continued from line 181-182] 16-digit code from 'app passwords' in the mail seetings where first you have to 
#[Continued from line 181-182-183] enable two-factor authentication and then paste it in 'EMAIL_PASS' i.e. ('MAIL_PASSWORD').
# importing 'mail' from 'flaskblog' in 'routes.py'
# importing 'Message' from 'flask_mail' in 'routes.py'
# use of 'validate_on_submit' method in '/reset_password/<token>' route
# 42:11


#Video-11 Blueprints & Configurations
# 42.42
































