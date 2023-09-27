from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///soils.db', echo=True)
Base = declarative_base()

class Source(Base):
    __tablename__ = "source"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    release_date = Column(Date)

class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    edaphic = Column(Boolean, unique=False, default=True)
    # chemical or physical
    properties = Column(String)
    # raster or other 
    data_type = Column(String)
    spatial_res = Column(Float) # for now
    temporal_res = Column(Date)
    # global, EU or PT
    extent = Column(String)
    source_id = Column(Integer, ForeignKey('source.id'))

    source = relationship("Source", back_populates="products")

Source.products = relationship("Products", order_by=Products.id, back_populates="source")
Base.metadata.create_all(engine)