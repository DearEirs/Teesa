from common.mixins import SeedExtractorMixin, DataExtractorMixin
from deduplicator import DeDuplicator


class Extractor(SeedExtractorMixin, DataExtractorMixin):
    def __init__(self):
        self.d = DeDuplicator()
        self.r = Redis()

    async def extract(self, seed):
        seed_rule, data_rule = await self.r.get_rules(seed)
        self.seeds = self.extract_seed(seed['response'], data_rule)
        self.data = self.extract_data(seed['response'], seed_rule)
        # self.d.deduplicate(self.seeds)
        # self.d.deduplicate(self.data)
        return self.seeds, self.data
