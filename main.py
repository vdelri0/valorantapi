from fastapi import FastAPI
import httpx
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
client = httpx.AsyncClient(base_url="https://valorant-api.com/v1/")

# Allow CORS for all origins
origins = ["*"]

# Add CORS middleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "¡Bienvenido a la aplicación de Valorant!"}

@app.get("/agents")
async def get_agents(is_playable: bool = True):
    params = {}
    if is_playable:
        params["isPlayableCharacter"] = "true"
    response = await client.get("/agents", params=params)
    return response.json()

@app.get("/agents/{agent_id}")
async def get_agent(agent_id: str):
    response = await client.get(f"/agents/{agent_id}")
    return response.json()

@app.get("/weapons")
async def get_weapons():
    response = await client.get("/weapons")
    return response.json()

# Add more routes as needed

