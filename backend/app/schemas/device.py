from pydantic import BaseModel

class DeviceCreate(BaseModel):
    name: str
    model: str
    os_version: str
