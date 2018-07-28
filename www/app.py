import logging; logging.basicConfig(level=logging.INFO)
import asyncio,os,json,time,ORM
from datetime import datetime
from aiohttp import web
from jinja2 import Environment,FileSystemLoader
from webkj import add_routes,add_static

def index(request):
	return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')

@asyncio.coroutine
def init(loop):

	yield from ORM.create_pool(loop = loop,host = '127.0.0.1',port = 3306,use='root',password = 'HUANGzeng123',db = 'awesome')
	app = web.Application(loop = loop,middlewares=[looger_factory,response_factory])
	init_jinja2(app,filters = dict(datetime = datetime_filter))
	add_routes(app,'handlers')
	add_static(app)
	srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
	logging.info('server started at http://127.0.0.1:9000...')
	return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()