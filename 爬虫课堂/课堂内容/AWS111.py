# import asyncio
# import logging
# from datetime import datetime
# from aiowebsocket.converses import AioWebSocket
#
#
# async def startup(uri):
#     async with AioWebSocket(uri) as aws:
#         converse = aws.manipulator
#         message = b'AioWebSocket - Async WebSocket Client'
#         while True:
#             await converse.send(message)
#             print("{time}-Client send: {message},'连接'"
#                   .format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), message=message))
#             mes = await converse.receive()
#             print('{time}-Client receive: {rec}'
#                   .format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), rec=mes))
#
#
# if __name__ == '__main__':
#     remote = 'ws://echo.websocket.org'
#     try:
#         asyncio.get_event_loop().run_until_complete(startup(remote))
#     except KeyboardInterrupt as exc:
#         logging.info('Quit.')


# import asyncio
# import logging
# from datetime import datetime
# from aiowebsocket.converses import AioWebSocket
#
#
# async def startup(uri):
#     async with AioWebSocket(uri) as aws:
#         converse = aws.manipulator
#         while True:
#             mes = await converse.receive()
#             print('{time}-Client receive: {rec}'
#                   .format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), rec=mes))
#
#
# if __name__ == '__main__':
#     remote = 'wss://api.bbxapp.vip/v1/ifcontract/realTime'
#     try:
#         asyncio.get_event_loop().run_until_complete(startup(remote))
#     except KeyboardInterrupt as exc:
#         logging.info('Quit.')


# import asyncio
# import logging
# from datetime import datetime
# from aiowebsocket.converses import AioWebSocket
#
#
# async def startup(uri):
#     async with AioWebSocket(uri) as aws:
#         converse = aws.manipulator
#         # 客户端给服务端发送消息
#         await converse.send('{"action":"subscribe","args":["QuoteBin5m:14"]}')
#         while True:
#             mes = await converse.receive()
#             print('{time}-Client receive: {rec}'
#                   .format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), rec=mes))
#
#
# if __name__ == '__main__':
#     remote = 'wss://api.bbxapp.vip/v1/ifcontract/realTime'
#     try:
#         asyncio.get_event_loop().run_until_complete(startup(remote))
#     except KeyboardInterrupt as exc:
#         logging.info('Quit.')

import websocket
import json

if __name__ == '__main__':
    ws = websocket.create_connection('wss://ws.bitforex.com/mkapi/coinGroup1/ws', timeout=10)
    ws.send(
        '[{"type": "subHq", "event": "trade", "param": {"businessType": "coin-usdt-btc", "dType": 0, "size": 100}}]')  # 订阅交易数据
    while True:
        content = ws.recv()
        for data in json.loads(content).get("data"):
            print(data)
    ws.close()
