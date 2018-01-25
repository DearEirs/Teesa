from common.mixins import HeaderSetterMixin, UrlNormalizationMixin
from common import httprequest


class HTTPDownloader(HeaderSetterMixin, UrlNormalizationMixin):
    async def down(self, url, header=None):
        url = self.url_normal(url)
        default_header = self.get_header()
        header = default_header.update(header) if header else default_header
        response = await httprequest(url, header)
        return response
