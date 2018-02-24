class DeDuplicator:
    async def check(self, data=None, seeds=None):
        if not any(data, seeds):
            return "require data or seeds, but not found"
        return data, seeds
