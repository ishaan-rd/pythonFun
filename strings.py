message1 = '''Hello World
This is a test for
multiple lines...'''

message = 'Hello1'\
'2World'

print(message)
print(message[3:9])
print(message[1:-10])
print(message[2:-10])
print(message[6:])
print(message.lower())
print(message.count('lo'))
print(message.find('World'))
print(message.replace('Hello12', 'Helloooo '))


greeting = 'Hello'
name = 'Ishaan'

msg = greeting + ' ' + name
print(msg)

msg = '{1}! {0}. What\'s Up?'.format(greeting, name)
print(msg)

msg = f'Heyyyy... {greeting} {name.upper()}! What up?'
print(msg)

print(help(str.lower))