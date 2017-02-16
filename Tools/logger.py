# PythonDecorators/log.py
from datetime import datetime

class log(object):
	def __init__(self, ID , Text=None):
		self.__ID = ID
		self.__Text = Text

	def __call__(self, f):
		def wrapped_f(*args):
			logTemplate =	"\x1b[1;31;47m {time} \x1b[1;37;44m Id:{id} \x1b[0;30;43m {text} \x1b[0m"
			logText = 	logTemplate.format(	time = datetime.now() ,
											id = self.__ID,
											text = f.__name__
										)
			try:
				f(*args)
				logStatus = "\x1b[1;37;42m PASS "
			except:
				logStatus = "\x1b[1;37;41m Fail "
			print (logText+logStatus)

		return wrapped_f



@log( ID = 12)
def sayHello():
		print(0/0)

if __name__ == '__main__':
	for x in range(20):
		sayHello()
