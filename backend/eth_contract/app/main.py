from fastapi import FastAPI, HTTPException, Depends, Security, APIRouter
from fastapi.security import OAuth2PasswordBearer
from web3 import Web3
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Float, Boolean
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
import jwt
import datetime
from neo3.core import types
from neo3.api.wrappers import GenericContract

contract_hash = types.UInt160.from_string("")
class MagipopMap(GenericContract):
    def post(self, owner: str, map_id: int, name: str, x: float, y: float, tags: str, image: str):
        return self.call_function("post", [owner, map_id, name, "", x, y, tags, image])
    
    def detail_of(self, location_id: int):
        return self.call_function("detail_of", [location_id])



magipop_map = MagipopMap(contract_hash)

app = FastAPI()

# Initialize database
DATABASE_URL = "postgresql://username:password@localhost/magipopmap"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base: DeclarativeMeta = declarative_base()


# Model definition
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    user_public_key = Column(String, unique=True, index=True)
    prestige = Column(Integer, default=0)

class Map(Base):
    __tablename__ = 'maps'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    image = Column(String)


class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True, index=True)
    owner = Column(Integer, ForeignKey('users.id'))
    map_id = Column(Integer, ForeignKey('maps.id'))
    name = Column(String)
    x = Column(Float)
    y = Column(Float)
    tags = Column(String)
    image = Column(String)
    is_on_chain = Column(Boolean, default=False)
    
class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True, index=True)
    nft_address = Column(String, index=True) # Address of the NFT
    owner_address = Column(String, index=True) # Address of the owner of the NFT
    attributes = Column(String) # JSON string of attributes
    image_url = Column(String) # URL to the NFT image

w3 = Web3(Web3.HTTPProvider('DATABASE_URL'))
router = APIRouter()

Base.metadata.create_all(bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/map")
def create_map(name: str, description: str, image: str):
    db = SessionLocal()
    db_map = Map(name=name, description=description, image=image)
    db.add(db_map)
    db.commit()
    db.refresh(db_map)
    return {"map": db_map}


@app.post("/location")
def create_location(owner: int, map_id: int, name: str, x: float, y: float, tags: str, image: str):
    db = SessionLocal()
    db_location = Location(owner=owner, map_id=map_id, name=name, x=x, y=y, tags=tags, image=image)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return {"location": db_location}


@app.get("/map/{map_id}")
def get_map(map_id: int):
    db = SessionLocal()
    db_map = db.query(Map).filter(Map.id == map_id).first()
    if db_map is None:
        raise HTTPException(status_code=404, detail="Map not found")
    return {"map": db_map}


@app.get("/location/{location_id}")
def get_location(location_id: int):
    db = SessionLocal()
    db_location = db.query(Location).filter(Location.id == location_id).first()
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return {"location": db_location}


@app.post("/onchain")
def send_data_to_chain():
    db = SessionLocal()
    db_locations = db.query(Location).filter(Location.is_on_chain == False).all()
    for db_location in db_locations:
        magipop_map.post(db_location.owner,
                         db_location.id,
                         db_location.name,
                         db_location.x,
                         db_location.y,
                         db_location.tags,
                         db_location.image)
        db_location.is_on_chain = True
        db.commit()
    return {"message": "success"}



@router.post("/store_nft_attributes")
def store_nft_attributes(nft_contract_address: str, token_id: int):
    nft_contract = w3.eth.contract(address=nft_contract_address, abi=nft_contract_abi) # You need to define nft_contract_abi
    nft_owner = nft_contract.functions.ownerOf(token_id).call()
    nft_attributes = nft_contract.functions.tokenURI(token_id).call()

    # Here you would normally fetch the actual metadata using the tokenURI
    # For simplicity, let's assume nft_attributes is a JSON string of attributes

    db = SessionLocal()
    character = Character(
        nft_address=nft_contract_address,
        owner_address=nft_owner,
        attributes=nft_attributes,
        image_url="some_image_url" # You need to extract this from the NFT metadata
    )
    db.add(character)
    db.commit()
    db.refresh(character)
    return {"character": character}

def create_jwt_token(data: dict):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    return jwt.encode({"exp": expiration, **data}, "secret", algorithm="HS256")

def decode_jwt_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, "secret", algorithms=["HS256"])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
