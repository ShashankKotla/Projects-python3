from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType #fastapi_mail is a package.
from pydantic import BaseModel, EmailStr
from starlette.responses import JSONResponse
import random
import string

#Email configuration

conf = ConnectionConfig(
    MAIL_USERNAME=" ",
    MAIL_PASSWORD= " ",
    MAIL_FROM= " ",
    MAIL_PORT=465,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)

app = FastAPI()


#Generate a random OTP
def generate_otp(length=6):
    digits = string.digits
    return ''.join(random.choice(digits) for _ in range(length))

class EmailSchema(BaseModel):
    email:EmailStr

@app.post("/signup")
async def signup(email: EmailSchema, background_tasks:BackgroundTasks) -> JSONResponse:

    otp = generate_otp() #to generate otp

    message = MessageSchema( #to create email message
        subject="Your OTP Code",
        recipients=[email.email],
        body=f"Your OTP code is {otp}",
        subtype=MessageType.plain
    )
    fm = FastMail(conf)

    try:
        background_tasks.add_task(fm.send_message, message)

        return JSONResponse(status_code=200, content={"Message": "Signup successful! OTP sent to email.", "otp":otp})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

