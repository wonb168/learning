#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets

import psycopg2

conn = psycopg2.connect(dbname="autoetl", user="autoetl",password="pQkQeHLJjSHbGcSN", host="192.168.200.201", port="5432")
c = conn.cursor()

sql="""
客户未接电话	2	9050
待与客户确认	342	1473382
待付款	3	11402
待发货	5	21056
无参加活动意向	8	37070
"""

async def time(websocket, path):
    while True:
        # now = datetime.datetime.utcnow().isoformat() + "Z"
        now=sql
        await websocket.send(now)
        await asyncio.sleep(random.random() * 10)

start_server = websockets.serve(time, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()