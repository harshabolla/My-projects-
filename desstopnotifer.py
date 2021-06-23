from  plyer import notification

title = 'hello harsha'

message = ' drink some water take a break'
notification.notify(title=title,
                     message=message,
                     app_icon=None,
                     timeout= 15,
                     toast = False)
