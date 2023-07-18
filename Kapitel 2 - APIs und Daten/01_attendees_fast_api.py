import bcrypt
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status, Response
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import asyncpg


class Attendee(BaseModel):
    id: str = None
    name: str
    skill_level: str

    def to_json(self):
        return {
            'attendee_id': self.id,
            'name': self.name,
            'skill_level': self.skill_level
        }

    def to_yaml(self):
        return yaml.dump(self.to_json())

    @staticmethod
    def from_json(json):
        return Attendee(id=json['attendee_id'], name=json['name'], skill_level=json['skill_level'])


app = FastAPI()

security = HTTPBasic()

# start up config
attendees = {
    "1d38e455759a11eda3e394de807959fa": {'name': 'James Dean', 'skill_level': 'expert'}
}

users = {
    "john": bcrypt.hashpw("deer".encode('utf-8'), bcrypt.gensalt()),
    "susan": bcrypt.hashpw("sanders".encode('utf-8'), bcrypt.gensalt())
}


async def get_pool():
    return await asyncpg.create_pool(dsn='postgresql://user:password@localhost/dbname')


async def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username in users:
        hashed_password = users[credentials.username]
        if bcrypt.checkpw(credentials.password.encode('utf-8'), hashed_password):
            return credentials.username

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Basic"},
    )


@app.get("/users/me/")
async def read_current_user(username: str = Depends(get_current_username)):
    return {"username": username}


@app.get('/')
async def get_all():
    async with get_pool() as pool:
        async with pool.acquire() as conn:
            attendees_list = await conn.fetch('SELECT * from attendees')
    return {'attendees': [dict(row) for row in attendees_list]}


@app.get('/attendee/{attendee_id}',
         response_model=Attendee,
         responses={
             404: {"description": "The item was not found"},
         })
async def get(attendee_id: str, as_yaml: bool = False):
    pool = await get_pool()
    async with pool.acquire() as conn:
        attendee = await conn.fetchrow('SELECT * from attendees where attendee_id = $1', attendee_id)
    if attendee is None:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
    attendee = Attendee.from_json(dict(attendee))
    print(
        attendee.to_yaml()
    )
    return attendee if not as_yaml else Response(content=attendee.to_yaml(), media_type="application/x-yaml")


@app.post('/attendee/', status_code=201)
async def post(attendee: Attendee):
    async with await get_pool() as pool:
        async with pool.acquire() as conn:
            await conn.execute('INSERT INTO attendees VALUES ($1, $2, $3)', attendee.id, attendee.name, attendee.skill_level)

    return attendee.to_json()


@app.put('/attendee/{attendee_id}')
async def put(attendee_id: str, attendee: Attendee):
    async with await get_pool() as pool:
        async with pool.acquire() as conn:
            await conn.execute("UPDATE attendees SET name = $1, skill_level = $2 WHERE attendee_id = $3",
                                attendee.name, attendee.skill_level, attendee_id)
    return attendee.to_json()


@app.delete('/attendee/{attendee_id}')
async def delete(attendee_id: str):
    async with await get_pool() as pool:
        async with pool.acquire() as conn:
            await conn.execute("DELETE FROM attendees WHERE attendee_id = $1", attendee_id)
    return {'attendee_id': attendee_id}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
