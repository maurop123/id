import sms_msging

class id_msging():
  # test workflow
  def main(self):
    msger = sms_msging.msging('305-776-4431')
    todos = ['visit pierre', 'get high']
    for todo in todos: msger.send_sms(todo)

if __name__ == '__main__': id_msging().main()
