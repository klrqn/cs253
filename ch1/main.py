import webapp2

form="""
<form method="post" action="/testform">
    <input name="q">
    <input type="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
		content = "<h1>Enter some text to ROT13:</h1>"
        # self.response.headers['Content-Type'] = 'text/plain
        self.response.out.write(content + form)

class TestHandler(webapp2.RequestHandler):
    def post(self):
        q = self.request.get("q")
        self.response.out.write(q)

        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write.out(self.request)

app = webapp2.WSGIApplication([('/', MainHandler),
								('/testform', TestHandler)],
								debug=True)
