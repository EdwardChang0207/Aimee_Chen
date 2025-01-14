username = 'hello'
password = '123'
login = False
while not login:
	username_input = input()
	password_input = input()
	if username_input == username and password_input == password:
		login = True
		print('已登入')
	else:
		print('錯誤') 