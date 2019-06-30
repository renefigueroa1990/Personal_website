# Personal Webstie
This is a template for a personal website for anyone who would like a simple page to have thier bio, projects, resume, and a contact form. 

# Technology Stack Needed

1. Python 3
2. Flask Microframework
3. Flask WTF extension
4. Flask mail extension
5. Heroku 

# Useful Links

1. Flask: http://flask.pocoo.org/docs/1.0/
2. Heroku: https://devcenter.heroku.com/articles/getting-started-with-python

# Set up for local development

1. Clone this repository:
  git clone https://github.com/renefigueroa1990/Personal_website.git
  
2. This project uses pipenv to setup the virtual environment. If you do not have pipenv installed, then you can install it as follows:
  pip install pipenv 
  
3. Go to the directory where you cloned the repository and install all the dependencies.
  pipenv install <-- This command will install all the requirements listed in the Pipfile
  
4. To activate the virtual environment, do the following:
  pipenv shell
  You should see the following prompt:
 Renes-MacBook-Pro:Personal_website renefigueroa$ pipenv shell
 Launching subshell in virtual environment…
 bash-3.2$  . /Users/renefigueroa/.local/share/virtualenvs/Personal_website-nHcFrnJD/bin/activate
 (Personal_website) bash-3.2$ 
 
 List all the files to make sure everything is correctly installed. 
 (Personal_website) bash-3.2$ ls
 Pipfile		Procfile	app.py		forms.py	static
 Pipfile.lock	README.md	development.py	production.py	templates
 
5. To run the application in the locally, simply enter the virtual environment and do a python app.py:

(Personal_website) bash-3.2$ python app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 264-581-634
 
 Now, open chrome or safary and enter the url and you should see the website. It should look similar to the my website,   renefigueroa.io
 
