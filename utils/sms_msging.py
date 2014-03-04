import smtplib, re
from datetime import datetime

class msging():
  phone_number = ''
  email = ''
  provider_handles = {
    'tmobile': 'tmomail.net'
  }

  def __init__(self, number=None, provider='tmobile'):
    if number:
      self.phone_number = number
      self.set_email(self.phone_number, provider)

  def send_sms(self, msg):
    server = smtplib.SMTP()
    server.connect('smtp.gmail.com', 587)
    server.starttls()
    server.login('maurop123@gmail.com', 'jnxmamihhrljxkwa')
    message = u'From: {0}\nTo: {1}\nSubject: {2}\nDate: {3}\n\n{4}'.format('maurop123@gmail.com', self.email, 'foobar', datetime.now(), msg)
    server.sendmail('maurop123@gmail.com',self.email,message)
    server.quit()

  def set_email(self, number, provider):
    self.email = '{0}@{1}'.format(re.sub(r'[^0-9]','',number), self.provider_handles[provider])
