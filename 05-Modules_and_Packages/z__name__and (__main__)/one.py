#If you run this file directly, like this:
#python one.py
#You can make sure that this is true:
#__name__ == "__main__"
#So, we can create something interesting like this:

def func():
	print("Func() in one.py")

print("Top level in one.py")

if __name__ == '__main__':
	print('one.py is being run directly')
else:
	print('one.py has been imported')