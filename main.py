from fastapi import FastAPI
from fastapi import Response
from fastapi.responses import HTMLResponse
from markupsafe import escape

app = FastAPI()


@app.get("/item", response_class=HTMLResponse)
async def read_items(itemname: str):
    # proruleid: tainted-direct-response-fastapi
    return f"""
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>{itemname}</h1>
        </body>
    </html>
    """
