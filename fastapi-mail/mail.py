from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import os
from dotenv import load_dotenv

# Load environment variables from a .env file into the environment
dotenv_path = sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.env')))
load_dotenv(dotenv_path=dotenv_path)


# Retrieve values from environment variables from .env file
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")


print(f"EMAIL_HOST: {EMAIL_HOST}")
print(f"EMAIL_PORT: {EMAIL_PORT}")
print(f"EMAIL_USER: {EMAIL_USER}")
print(f"EMAIL_PASS: {EMAIL_PASS}")

# Ensure all necessary environment variables are set
if not all([EMAIL_HOST, EMAIL_PORT, EMAIL_PASS, EMAIL_USER]):
    raise ValueError("One or more required environment variables are missing")

# Convert EMAIL_PORT to an integer
EMAIL_PORT = int(EMAIL_PORT)

app = FastAPI()

def generate_otp(length=6):
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])

@app.get("/generate-otp")
async def get_otp():
    otp = generate_otp()
    return {"otp": otp}

def send_email(to_email, otp):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = to_email
    msg['Subject'] = "Your OTP Code"

    body = f"Your OTP code is {otp}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        text = msg.as_string()
        server.sendmail(EMAIL_USER, to_email, text)
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

class OTPRequest(BaseModel):
    email: str

@app.post("/generate-otp")
async def generate_and_send_otp(request: OTPRequest):
    otp = generate_otp()
    if send_email(request.email, otp):
        return {'message': 'OTP sent successfully', "otp": otp}
    else:
        raise HTTPException(status_code=500, detail="Failed to send OTP")

