import ORM
import asyncio
from models import User,Blog,Comment

@asyncio.coroutine
def test():
	yield from ORM.create_pool(loop = loop,host = 'localhost', user = 'root',password = 'HUANGzeng123',db = 'awesome')

	u = User(name = 'Test133',email = 'test2233@example.com',passwd = '123456',image = 'abou:blank')

	yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()