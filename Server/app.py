from google.appengine.ext.webapp import template
import webapp2
import os

from google.appengine.api import channel


class DefaultHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {
      'channel': channel.create_channel('master')
    }
    path = os.path.join(os.path.dirname(__file__), 'templates/desktop.html')
    self.response.out.write(template.render(path, template_values))


class MobileHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    path = os.path.join(os.path.dirname(__file__), 'templates/mobile.html')
    self.response.out.write(template.render(path, template_values))
  
  def post(self):
    channel.send_message('master', self.request.body)


app = webapp2.WSGIApplication([
  ('/mobile/?', MobileHandler),
  ('.*', DefaultHandler)
], debug=True)