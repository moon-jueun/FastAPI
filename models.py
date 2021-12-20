from dbconn import DBconn
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

dbconn = DBconn()
Base = declarative_base()

class DCM(Base):
    __tablename__ = 'dcm'
    sopinstanceuid = Column(Integer, primary_key=True)
    modality = Column(String(255))
    categories = Column(String(255))
    datasource = Column(String(255))
    name = Column(String(255))

    def __init__(self, id, modality, categories, datasource, name):
        self.id = id
        self.modality = modality
        self.categories = categories
        self.datasource = datasource
        self.name = name

    def __repr__(self):
        return f"<DCM({self.id}, {self.modality}, {self.categories}, {self.datasource}, {self.name})>"
