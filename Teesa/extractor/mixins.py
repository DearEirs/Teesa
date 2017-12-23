class SeedExtractorMixin:
    def extract(self, response):
        return seeds


class DataExtractorMixin:
    def extract(self, response):
        return data
