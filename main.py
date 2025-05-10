import flet as ft
import flet_fastapi

async def main(page: ft.Page):
    await page.add_async(ft.Text("Hi This is web test for Flet APP", size=30, weight="bold"))

app = flet_fastapi.app(main)