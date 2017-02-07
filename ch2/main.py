import webapp2
<<<<<<< HEAD:ch2/main.py
import validation
import cgi

form="""
<form method="post">
    What is your birthday?
    <br>

    <label>Month<input type="text" name="month" value={1}></label>
    <br>
    <label>Day<input type="text" name="day" value={2}></label>
    <br>
    <label>Year<input type="text" name="year" value={3}></label>
    <div>{0}</div>
    <br>
    <input type="submit">
</form>
"""
=======
import valid

form = """
<!DOCTYPE html>
<html>
    <head>
        <title>Sign Up</title>
    </head>
<body>
    <h2>Sign Up</h2>
    <form method="post">
        <label>Username<input type="text" name="username" value={0}></label>{4}
        <br>
        <label>Password<input type="password" name="password" value={1}></label>{5}
        <br>
        <label>Password Check<input type="password" name="verify" value={2}></label>{6}
        <br>
        <label>Email (optional)<input type="text" name="email" value={3}></label>{7}
        <br>
        <input type="submit" value="sign up dude!">
    </form>
</body>
    """

>>>>>>> f36d250974dd74d8098cbd4e07b7eed0d6b3517e:main.py

def escape_html(s):
    return cgi.escape(s, quote=True)

class MainHandler(webapp2.RequestHandler):
<<<<<<< HEAD:ch2/main.py
    def writeform(self, error="", month="", day="", year=""):
        self.response.write(form.format(error,
                                        escape_html(month),
                                        escape_html(day),
                                        escape_html(year)))
=======

    def writeform(self, username="", password="", verify="", email="", error="", error_pw="",error_valid="", error_email=""):
         self.response.write(form.format(valid.escaped_html(username),
                                         valid.escaped_html(password),
                                         valid.escaped_html(verify),
                                         valid.escaped_html(email),
                                         error,
                                         error_pw,
                                         error_valid,
                                         error_email))
>>>>>>> f36d250974dd74d8098cbd4e07b7eed0d6b3517e:main.py

    def get(self):
        self.writeform()

    def post(self):
<<<<<<< HEAD:ch2/main.py
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        # verify the user's input
        month = validation.valid_month(user_month)
        day = validation.valid_day(user_day)
        year = validation.valid_year(user_year)

        # on error, render form again
        if not (month and day and year):
            self.writeform("<p style=color:red;> That doesn't look valid to me friend.</p>", user_month, user_day, user_year)
        else:
            self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thanks, that data is totally valid!")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/thanks', ThanksHandler)
=======

        have_error = False

        errorDict = {"username":"",
                     "password":"",
                     "pw_match":"",
                     "email":""}

        # month_abbvs = dict((m[:3].lower(), m) for m in months) Sooooo Pythonic

        # get the users input for the 4 fields
        username = self.request.get("username")
        password = self.request.get("password")
        password_check = self.request.get("verify")
        email = self.request.get("email")

        # verify the inputs
        valid_username = valid.verify_username(valid.escaped_html(username))
        valid_password = valid.verify_password(valid.escaped_html(password))
        valid_email = valid.verify_email(valid.escaped_html(email))

        if not valid_username:
            have_error = True
            errorDict["username"] = "<b style=color:red;> Not a valid username </b>"

        if not valid_password:
            have_error = True
            errorDict["password"] = "<b style=color:red;> Not a valid password </b>"

        if password != password_check:
            have_error = True
            errorDict["pw_match"] = "<b style=color:red;> Passwords don't match </b>"

        if not valid_email:
            errorDict["email"] = "<b style=color:red;> Not a valid email </b>"


        if have_error == True:
            self.writeform(username, "", "", email, errorDict["username"], errorDict["password"], errorDict["pw_match"], errorDict["email"])

        if have_error == False:
            self.redirect('/welcome?username=' + username)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("username")
        content = "Welcome " + username
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
>>>>>>> f36d250974dd74d8098cbd4e07b7eed0d6b3517e:main.py
], debug=True)
