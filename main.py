from fastapi import FastAPI
import random
import string
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_special=True):
    characters = string.ascii_lowercase
    
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
  
    return password

@app.get("/generate-password/")
async def get_password(length: int = 12, uppercase: bool = True, numbers: bool = True, special: bool = True):
    password = generate_password(length, uppercase, numbers, special)
    return {"password": password}
