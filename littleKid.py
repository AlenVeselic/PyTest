print('What is your name?')
name = input()
print('How old are you?')
age=input()
if name == 'Alice':
    print('Hi, Alice')
elif int(age) < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')
    