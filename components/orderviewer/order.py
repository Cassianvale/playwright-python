class OrderViewerModal:
    def __init__(self, page: Page, url: str):
        self.page = page
        self.url = url
        self.work_order_details = Details(
            page, locator='div.work-order-details'
        )

    def open(self):
        self.page.goto(self.url)
        self.work_order_details.should_be_visible()