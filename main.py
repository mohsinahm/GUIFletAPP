from flet import *
import flet_fastapi

async def main(page: Page):
    await page.add_async(Text("Hi This is web test for Flet APP", size=30, weight="bold"))

app = flet_fastapi.app(main)