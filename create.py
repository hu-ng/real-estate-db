from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Date, Float, Table, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


engine = create_engine('sqlite:///database.db', echo=False)

Base = declarative_base()

# Association Table
agent_office = Table('agent_office_table', Base.metadata,
    Column('agent_id', Integer, ForeignKey('agent.id'), primary_key=True),
    Column('office_id', Integer, ForeignKey('office.id'), primary_key=True)
)


class Agent(Base):
    """
    Table for agents
    """
    __tablename__ = 'agent'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    number = Column(String)
    offices = relationship('Office', back_populates='agents', secondary=agent_office)
    houses = relationship('House', back_populates='agent')
    sales = relationship('Sale', back_populates='agent')
    commission = relationship('Commission', back_populates='agent')

    def __init__(self, id, name, email, number):
        self.id = id
        self.name = name
        self.email = email
        self.number = number

    def __repr__(self):
        return "Agent {0}".format(self.name)


class Office(Base):
    """
    Table for offices
    """
    __tablename__ = 'office'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    agents = relationship('Agent', order_by=Agent.id, back_populates='offices', secondary=agent_office)
    sales = relationship('Sale', back_populates='office')

    def __init__(self, id,  name, location):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return "Office {0} from {1}".format(self.name, self.location)


class House(Base):
    """
    Table for houses
    """
    __tablename__ = 'house'
    id = Column(Integer, primary_key=True)
    seller_name = Column(String)
    num_beds = Column(Integer)
    num_bath = Column(Integer)
    price = Column(Integer)
    zip = Column(Integer)
    date_list = Column(Date)
    on_sale = Column(Boolean)
    agent_id = Column(Integer, ForeignKey('agent.id'))
    agent = relationship('Agent', back_populates='houses')
    sale = relationship('Sale', back_populates='house')

    def __init__(self, id, seller_name, num_beds, num_bath, price, zip, date_list, on_sale, agent_id):
        self.id = id
        self.seller_name = seller_name
        self.num_beds = num_beds
        self.num_bath = num_bath
        self.price = price
        self.zip = zip
        self.date_list = date_list
        self.on_sale = on_sale
        self.agent_id = agent_id

    def __repr__(self):
        return "House detail: Seller: {0}, Price: {1}, Current Status: {2}".format(self.seller_name, self.price, self.condition)


class Sale(Base):
    """
    Table for sales
    """
    __tablename__='sale'
    id = Column(Integer, primary_key=True)
    house_id = Column(Integer, ForeignKey('house.id'), unique=True)
    agent_id = Column(Integer, ForeignKey('agent.id'))
    office_id = Column(Integer, ForeignKey('office.id'))
    buyer_name = Column(String)
    price = Column(Integer)
    date_sell = Column(Date, index=True)  # Index is created for this column
    commission_id = Column(Integer, ForeignKey('commission_rate.id'))
    commission_rate = relationship('CommissionRate', back_populates='sales')
    agent = relationship('Agent', back_populates='sales')
    office = relationship('Office', back_populates='sales')
    house = relationship('House', back_populates='sale')

    def __init__(self, id, house_id, agent_id, office_id, buyer_name, price, date_sell, commission_id):
        self.id = id
        self.house_id = house_id
        self.agent_id = agent_id
        self.office_id = office_id
        self.buyer_name = buyer_name
        self.price = price
        self.date_sell = date_sell
        self.commission_id = commission_id

    def __repr__(self):
        return "House sold to {0} for {1} dollars".format(self.buyer_name, self.price)


class CommissionRate(Base):
    """
    Table for commission rates
    """
    __tablename__='commission_rate'
    id = Column(Integer, primary_key=True)
    price_range = Column(String)
    rate = Column(Float)
    sales = relationship('Sale', back_populates = 'commission_rate')

    def __init__(self, id, price_range, rate):
        self.id = id
        self.price_range = price_range
        self.rate = rate

    def __repr__(self):
        return "Rate for house priced within {0} is {1}".format(self.price_range, self.rate)


class Commission(Base):
    """
    Table for commission of each agent.
    """
    __tablename__ = 'commission'
    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey('agent.id'), unique=True)
    amount = Column(Float)
    agent = relationship('Agent', back_populates='commission')

    def __init__(self, agent_id, amount):
        self.agent_id = agent_id
        self.amount = amount

    def __repr__(self):
        return 'Commission for this agent is {} USD'.format(self.amount)