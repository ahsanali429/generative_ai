from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/hello")
def get_hello():
    return {"Hello": "Ahsan"}


if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 8000)

    # https://60hnnhhl-8000.inc1.devtunnels.ms/