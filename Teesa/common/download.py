import handler.html


class DownLoader(HtmlHandleMixin):
    async def down(self, pictures):
        for picture in pictures:
            response = await self.get(picture)
            pass
