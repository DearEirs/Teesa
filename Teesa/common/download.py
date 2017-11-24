import handler.html


class DownLoader(HtmlHandleMixin):
    async def down(self, pictures):
        '''下载图片至本地磁盘

        Args: pictures, 一个列表, 里边应该包含着需要下载的图片的url
        '''
        for picture in pictures:
            response = await self.get(picture)
            pass
