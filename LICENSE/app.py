import logging, asyncio
logging.basicConfig(level=logging.INFO)
from aiohttp import web


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '', index)
    srv = yield from loop.create_server(app.make_handler(), 'localhost', 8888)
    logging.info('开启服务:http://127.0.0.1:8888')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
