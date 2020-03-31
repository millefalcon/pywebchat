from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

import socketio

import pathlib
appdir = pathlib.Path(__file__).parent


templates = Jinja2Templates(directory=appdir / 'templates')

async def home(request):
    return templates.TemplateResponse('home.html', {'request': request})

async def chat(request):
    return templates.TemplateResponse('chat.html', {'request': request})



routes = [
    Route("/", home),
    Route("/chat/", chat),
    Mount('/static', StaticFiles(directory=appdir / 'static'), name='static')
]

sio = socketio.AsyncServer(async_mode='asgi')
sapp = Starlette(routes=routes)

app = socketio.ASGIApp(sio, sapp)

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@sio.on('my event')
async def handle_my_custom_event(sid, json, methods=['GET', 'POST']):
    print('received my event: ' + str(sid), json)
    await sio.emit('my response', json, callback=messageReceived)

