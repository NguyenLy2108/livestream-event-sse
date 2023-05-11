import asyncio
import json
from fastapi import APIRouter, Body, Request
from sse_starlette import EventSourceResponse
import config as config
from livestream_status.handle import LivestreamStatusService

cfg = config.Settings()

router = APIRouter()

@router.get('/')
async def message_stream(request: Request):
    def new_messages():
        # Add logic here to check for new messages
        yield 'livestream_status'
    async def event_generator():
        while True:
            # If client closes connection, stop sending events
            if await request.is_disconnected():
                break

            # Checks for new messages and return them to client if any
            if new_messages():
                livestreams = LivestreamStatusService()
                data = livestreams.livestreams_of_currentday()
                yield {
                        "event": "livestream_status",                       
                        "retry": int(cfg.retry_timeout),
                        "data": json.dumps(data, default=str)
                    }                          

            await asyncio.sleep(int(cfg.stream_delay))

    return EventSourceResponse(event_generator()) 