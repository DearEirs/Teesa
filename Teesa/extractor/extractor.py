from mixins import SeedExtractorMixin, DataExtractorMixin

class Extractor(SeedExtractorMixin, DataExtractorMixin):
    def extract(self, response):
        self.seeds = self.extract_seed(response)
        self.data = self.extract_data(response)
        return data

    def save_seeds(self, seeds):
        pass
