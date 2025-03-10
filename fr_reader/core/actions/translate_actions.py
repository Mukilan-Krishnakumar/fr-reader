import requests


class TranslateSourceAction:
    def __init__(self, url):
        self.url = url

    def get_site_content(self):
        html_content = requests.get(self.url)
        html_content = html_content.text
        return html_content

    def execute(self):
        html_content = self.get_site_content()
