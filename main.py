from fastapi import FastAPI, Request
import re

app = FastAPI()

@app.post("/extract-email")
async def extract_email(request: Request):
    data = await request.json()
    text = data.get("text", "")
    emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
    return {"emails": emails}
