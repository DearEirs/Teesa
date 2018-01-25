from mixins import SeedExtractorMixin, DataExtractorMixin


class Extractor(SeedExtractorMixin, DataExtractorMixin):
    async def get_rules(self):
        rules = None
        return rules

    async def extract(self, response):
        seed_rules, data_rules = await self.get_rules()
        self.seeds = self.extract_seed(response, data_rules)
        self.data = self.extract_data(response, seed_rules)
        return self.seeds, self.data
