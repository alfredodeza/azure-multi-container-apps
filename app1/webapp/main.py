from os.path import dirname, abspath, join
from fastapi import FastAPI, Response
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


current_dir = dirname(abspath(__file__))
static_path = join(current_dir, "static")

app = FastAPI()
app.mount("/static", StaticFiles(directory=static_path), name="static")


class Body(BaseModel):
    text: str


@app.get('/')
def root():
    html_path = join(static_path, "index.html")
    return FileResponse(html_path)


@app.post('/search')
def predict(body: Body):
    return {"text": body.text}
