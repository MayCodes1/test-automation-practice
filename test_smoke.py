from playwright.sync_api import Page

def test_hio_page_loads(page: Page):
    response = page.goto("https://hio.ai/")
    assert response.ok

