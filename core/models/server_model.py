from configurations.db.abstracts.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Boolean

class Server(BaseModel):
    __tablename__= 'servers'
    
    ip = Column(String(20), nullable=False)
    server_name = Column(String(150), nullable=False)
    username = Column(String(50), nullable=False)
    local_port = Column(Integer(), nullable=False)
    remote_port = Column(Integer(), nullable=False)
    with_key = Column(Boolean(), default=False)
    with_password = Column(Boolean(), default=False)
    with_ssh = Column(Boolean(), default=False)
    password = Column(String(100), nullable=True)
    path_key = Column(String(500), nullable=True)
    ssh_port = Column(Integer(), default=22)
    conection_status = Column(Boolean(), default=False)


