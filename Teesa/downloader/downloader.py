import aiohttp

from mixins import HeaderSetterMixin, UrlNormalizationMixin

class HTTPDownloader(HeaderSetterMixin, UrlNormalizationMixin):
    def down(self, url):
        self.url = self.url_normal(url)
        header = self.get_header(url)
        pass
        return response
