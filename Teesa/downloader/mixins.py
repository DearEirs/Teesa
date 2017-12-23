class UrlNormalizationMixin:
    def url_normal(url):
        return url


class HeaderSetterMixin:
    def set_header(self, header):
        self.header = header
        return self.header

    def get_header(self, url):
        pass
        return header
