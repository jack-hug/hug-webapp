import ORM
from models import User,Blog,Comment

def test():
	yield from ORM.create_pool(user = 'www-hug',password = 'www-hug',database = 'awesome')

	u = User(name = 'Test',email = 'test@example.com',passwd = '123456',image = 'abou:blank')

	yield from u.save()

for x in test():
	pass