from sanic import Sanic
from sanic.response import json
from scheduler import Scheduler


app = Sanic(__name__)


@app.route("/scheduler/start")
async def run(request):
    result = await scheduler.start(app.loop)
    return json(result)


@app.route("/scheduler/stop")
async def stop(request):
    result = await scheduler.stop()
    return json(result)

@app.route("/scheduler/put", methods=["POST"])
async def put(request):
    url = request.json
    result = await scheduler.put(url)
    return json(result)

@app.route("/scheduler/schedule")
async def schedule(request):
    result = await scheduler.schedule()
    return json(result)


if __name__ == "__main__":
    scheduler = Scheduler()
    app.run(host="0.0.0.0", port=9001)
