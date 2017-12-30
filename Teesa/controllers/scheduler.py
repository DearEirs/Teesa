from downloader import DownLoader

class Scheduler:
    def __init__(self, repository):
        self.repository = repository

    async def get_url(self):
        self.url = await self.repository.get_url()
        return self.url

    def push_url(self):
        pass
