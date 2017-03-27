# Enter script code

winClass = window.get_active_class()
if "terminal" not in str(winClass)	:
    keyboard.send_keys("<ctrl>+c")
else:
    keyboard.send_keys("<ctrl>+<shift>+c")

          
