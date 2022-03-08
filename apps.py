import os,threading,time

def app():
	os.system('python manage.py runserver 4000')
def chrome():
	os.system('start chrome http://127.0.0.1:4000/')

t1 = threading.Thread(target=app)
t1.start()
time.sleep(5)
t2 = threading.Thread(target=chrome)
t2.start()


