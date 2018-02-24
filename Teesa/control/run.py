from sanic import Sanic
from sanic.response import json
from downloader import Downloader


app = Sanic(__name__)


@app.route("/downloader/start")
async def run(request):
    result = await downloader.start(app.loop)
    return json(result)


@app.route("/downloader/stop")
async def stop(request):
    result = await downloader.stop()
    return json(result)

@app.route("/downloader/put", methods=['POST'])
async def put(request):
    url = request.json.get('url', None)
    resp = await downloader.put(url)
    return json(resp)

@app.route("/downloader/down")
async def schedule(request):
    result = await downloader.schedule()
    return json(result)


@app.route("downloader/health")
async def health(request):
    result = await downloader.health()
    return json(result)


if __name__ == "__main__":
    downloader = Downloader()
    app.run(host="0.0.0.0", port=9002)
