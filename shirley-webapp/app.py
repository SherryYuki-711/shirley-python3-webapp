# import logging
# logging.basicConfig(level=logging.INFO)
# import asyncio,os,json,time
# from datetime import datetime
# from aiohttp import web
# def index(request):
#     #return web.Rebsponse(body=b'<h1>Shirley</h1>')
#     return web.Response(body=b'<h1>Shirley</h1>', content_type='text/html')
# async def init(loop):
#     app = web.Application(loop=loop)
#     app.router.add_route('GET','/',index)
#     srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
#     logging.info('server started at http://127.0.0.1:9000...')
#     return srv
# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

async def index(request):
    return web.Response(body=b'<h1>Shirley</h1>',content_type='text/html')


async def init(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    apprunner = web.AppRunner(app)
    await apprunner.setup()
    srv = await loop.create_server(apprunner.server, '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()