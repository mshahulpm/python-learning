import time
import asyncio


class EventManager:
    def high_compute(self) -> None:
        time.sleep(5)
        print("compute finished")


class EventManagerAsync:
    def __init__(self):
        self.loop = asyncio.get_event_loop()

    async def high_compute(self) -> None:
        await asyncio.sleep(5)
        print("compute finished")

    def run_high_compute_async(self):
        # Schedule the task in the event loop — fire and forget
        self.loop.create_task(self.high_compute())
