import html.parser


class HrefParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.href_data = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href")
            if href:
                self.href_data.append(href)