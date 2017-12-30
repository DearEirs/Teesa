from comman.mixins import HeaderSetterMixin, UrlNormalizationMixin
from comman import httprequest


class HTTPDownloader(HeaderSetterMixin, UrlNormalizationMixin):
    async def down(self, url):
        url = self.url_normal(url)
        header = self.get_header(url)
        response = await httprequest(url, header)
        return response
