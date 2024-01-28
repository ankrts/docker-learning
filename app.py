import uvicorn
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles

api = FastAPI()

if __name__ == "__main__":
    uvicorn.run("app:api", reload=False)


@api.get("/")
async def root():
    return RedirectResponse(url="/login")


@api.get("/login", response_class=HTMLResponse)
async def get_login():
    with open("templates/login.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

login = 'root'
psw = 'root'


@api.post("/login", response_class=HTMLResponse)
async def post_login(username: str = Form(""), password: str = Form("")):
    if username == login and password == psw:
        with open("templates/index.html", "r") as file:
            html_content = file.read()
        return HTMLResponse(content=html_content)
    else:
        if not username and not password:
            with open("templates/error400usernamepassword.html", "r") as file:
                html_content = file.read()
            return HTMLResponse(content=html_content)
        elif not username:
            with open("templates/error400username.html", "r") as file:
                html_content = file.read()
            return HTMLResponse(content=html_content)
        elif not password:
            with open("templates/error400password.html", "r") as file:
                html_content = file.read()
            return HTMLResponse(content=html_content)
        elif username == login and password != psw:
            with open("templates/error404password.html", "r") as file:
                html_content = file.read()
            return HTMLResponse(content=html_content)
        elif password == psw and username != login:
            with open("templates/error404username.html", "r") as file:
                html_content = file.read()
            return HTMLResponse(content=html_content)
        else:
            with open("templates/error404.html", "r") as file:
                html_content = file.read()
            return HTMLResponse(content=html_content)

api.mount("/static", StaticFiles(directory="static"), name="static")
