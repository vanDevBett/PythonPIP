import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get("/contact", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Bett INC</title>
        </head>
        <body>
            <h1>Bett Industries INC</h1>
            <p>Bett is the best!!!</p>
            <hr>
            <p>Best Python developer van Dev Bett</p>
            <p>@vanDevBett!!!</p>
            <p>papu!!!!</p>
        </body>
    </html>
    """


def run():
    store.get_categories()

if __name__ == '__main__':
    run() 