from flask import Flask, render_template, request, flash, redirect, url_for
from forms import ContactForm
from flask_mail import Message, Mail





app = Flask(__name__)

#load development configuration
app.config.from_pyfile('development.py')

#load production configuration 
# app.config.from_pyfile('production.py')


#set up mail
mail = Mail()
# app.debug = 0 
mail.init_app(app)

#During testing, this function needs to be commented out since the Flask development server users HTTP
#When in production, you want to uncomment this function to redirect all calls to HTTPS
#to force all requests to HTTPS
# @app.before_request
# def before_request():
# 	if request.url.startswith('http://'):
# 		url = request.url.replace('http://', 'https://',1)
# 		code = 301
# 		return redirect(url, code = code)

@app.route("/", methods=['GET'])
@app.route("/home/", methods=['GET'])
def home():
	return render_template('home.html', title='Rene Figueroa', nav='home')

@app.route("/projects/")
def projects():
	return render_template('projects.html', title='Projects')

@app.route("/projects/project_1")
def project_1():
	return render_template('project_1.html', title='Project_1')


@app.route("/projects/project_2")
def project_2(): 
	return render_template('project_2.html', title='Project_2')


@app.route("/projects/project_3")
def project_3():
	return render_template('project_3.html', title='Project_3')


@app.route("/contact/", methods=['GET', 'POST'])
def contact():
	form = ContactForm(request.form)
	#obtaining data from forms 
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		subject = request.form['subject']
		message = request.form['message']
		#if all the data has been entered and is valid, then send email
		if form.validate_on_submit():
			flash(f"Thank you for your message. I'll get back to you soon", "success")

			msg = Message(form.subject.data, sender='youremailaddress', recipients=['youremailaddress'])
			msg.body = """
			From: {} <{}>
			{}

			""".format(form.name.data, form.email.data, form.message.data)
			mail.send(msg)
			#we were able to send the email
			#and redirect user to the contact page again
			return redirect(url_for('contact'))
		return render_template('contact.html', title='Contact Me', form = form )
		
		
	elif request.method == 'GET':
		return render_template('contact.html', title='Contact Me', form = form )

#not found route 
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html', title="Not Found"), 404


if __name__ == '__main__':
	app.run()





