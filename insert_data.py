from app.create import Agent, Office, House, Sale, CommissionRate, Commission, engine, Base
from datetime import date
from sqlalchemy.orm import sessionmaker

engine.connect()
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


def main():
    """
    Insert fictitious data to test out queries
    """
    # id, name, email, number
    agent1 = Agent(1, 'Mark Smith', 'marksmith@mail.com', '202-555-0125')
    agent2 = Agent(2, 'Henry Smith', 'henrysmith@mail.com', '202-555-0186')
    agent3 = Agent(3, 'Bill Smith', 'billsmith@mail.com', '202-555-0169')
    agent4 = Agent(4, 'Charlie Smith', 'charliesmith@mail.com', '202-555-0121')
    agent5 = Agent(5, 'John Smith', 'johnsmith@mail.com', '202-555-0188')
    agent6 = Agent(6, 'Marla Smith', 'marlasmith@mail.com', '202-555-0189')
    agent7 = Agent(7, 'Billy Smith', 'billysmith@mail.com', '410-555-0186')
    agent8 = Agent(8, 'Peter Smith', 'petersmith@mail.com', '410-555-0187')
    agent9 = Agent(9, 'Steve Smith', 'stevesmith@mail.com', '410-555-0109')
    agent10 = Agent(10, 'Phillip Smith', 'phillipsmith@mail.com', '410-555-0140')

    session.add_all([agent1, agent2, agent3, agent4, agent5,
                     agent6, agent7, agent8, agent9, agent10])
    session.commit()

    # id, name, location
    office1 = Office(1, 'Good Crib', 'Berkeley')
    office2 = Office(2, 'Cool House', 'Houston')
    office3 = Office(3, 'Great House', 'New York')
    office4 = Office(4, 'Nice House', 'Dallas')
    office5 = Office(5, 'Amazing House', 'LA')
    office6 = Office(6, 'Nice Place', 'San Francisco')
    office7 = Office(7, 'Get A House', 'Boston')
    office8 = Office(8, 'Meh Apartments', 'Seattle')
    office9 = Office(9, 'Bill\'s Housing', 'Fresno')
    office10 = Office(10, 'Smith\'s Estate', 'South San Fran')

    session.add_all([office1, office2, office3, office4, office5,
                     office6, office7, office8, office9, office10])
    session.commit()

    agent1.offices.append(office1)
    agent1.offices.append(office8)
    agent2.offices.append(office1)
    agent2.offices.append(office2)
    agent3.offices.append(office3)
    agent4.offices.append(office3)
    agent4.offices.append(office4)
    agent5.offices.append(office5)
    agent5.offices.append(office6)
    agent6.offices.append(office6)
    agent6.offices.append(office5)
    agent7.offices.append(office1)
    agent7.offices.append(office2)
    agent7.offices.append(office5)
    agent8.offices.append(office10)
    agent8.offices.append(office9)
    agent8.offices.append(office8)
    agent9.offices.append(office10)
    agent9.offices.append(office9)
    agent9.offices.append(office7)
    agent10.offices.append(office8)
    agent10.offices.append(office6)
    agent10.offices.append(office7)

    session.commit()

    # id, seller name, bedrooms, bathrooms, listing price, zip, listing date, on sale or not, listed agent
    house1 = House(1, 'Bart', 1, 3, 200000, 94102, date(2011, 12, 5), False, 1)
    house2 = House(2, 'Elif', 2, 5, 80000, 94103, date(2010, 11, 4), False, 6)
    house3 = House(3, 'Mark', 5, 6, 400000, 10000, date(2007, 6, 4), False, 5)
    house4 = House(4, 'Carlos',4, 2, 700000, 10000, date(2016, 10, 5), False, 2)
    house5 = House(5, 'Wang', 2, 4, 250000, 94012, date(2018, 9, 5), False, 3)
    house6 = House(6, 'Linh', 7, 8, 1000000, 94103, date(2010, 8, 5), False, 1)
    house7 = House(7, 'Bob', 2, 2, 550000, 60000, date(2015, 10, 18), False, 7)
    house8 = House(8, 'Mike', 2, 2, 600000, 50000, date(2018, 9, 17), False, 8)
    house9 = House(9, 'Mickey', 2, 2, 440000, 70000, date(2018, 8, 16), False, 9)
    house10 = House(10, 'Schmidt', 2, 2, 110000, 50000, date(2018, 7, 15), False, 10)
    house11 = House(11, 'Mitch', 2, 2, 1200000, 60000, date(2018, 6, 14), False, 7)
    house12 = House(12, 'Micah', 2, 2, 6000000, 70000, date(2018, 5, 13), False, 8)
    house13 = House(13, 'Jennifer', 2, 2, 300000, 40000, date(2018, 4, 12), False, 3)
    house14 = House(14, 'Brett', 2, 2, 2400000, 20000, date(2018, 3, 11), False, 9)
    house15 = House(15, 'Ben', 2, 2, 800000, 94012, date(2018, 2, 10), False, 4)

    session.add_all([house1, house2, house3, house4, house5, house6, house7, house8,
                     house9, house10, house11, house12, house13, house14, house15])
    session.commit()

    # id, price range, rate
    commission1 = CommissionRate(1, '0 - 100000', 0.1)
    commission2 = CommissionRate(2, '100000 - 200000', 0.075)
    commission3 = CommissionRate(3, '200000 - 500000', 0.06)
    commission4 = CommissionRate(4, '500000 - 1000000', 0.05)
    commission5 = CommissionRate(5, '1000000 - Infinity', 0.04)

    session.add_all([commission1, commission2, commission3,
                     commission4, commission5])
    session.commit()

    # id, house id, agent id, office id, buyer name, selling price, selling date, commission rate
    sale1 = Sale(1,1,1,8, "Charlie Something", 200000, date(2019, 3, 20), 2)
    sale2 = Sale(2,2,6,5, "Ben Something", 80000, date(2019, 3, 20), 1)
    sale3 = Sale(3,3,5,6, "Nick Something", 400000, date(2019, 4, 20), 3)
    sale4 = Sale(4,4,2,2, "Hopper Something", 700000, date(2019, 2, 20), 4)
    sale5 = Sale(5,5,3,3, "Mike Something", 250000, date(2019, 3, 20), 2)
    sale6 = Sale(6,6,1,1, "Charles Something", 1000000, date(2019, 3, 20), 5)
    sale7 = Sale(7,7,7,2, "Harley Something", 550000, date(2019, 4, 20), 4)
    sale8 = Sale(8,8,8,9, "Bruce Something", 600000, date(2019, 3, 20), 4)
    sale9 = Sale(9,9,9,10, "Henry Something", 440000, date(2019, 4, 20), 3)
    sale10 = Sale(10,10,10,6, "Bill Something", 110000, date(2019, 2, 20), 2)
    sale11 = Sale(11,11,7,2, "Mark Something", 1200000, date(2019, 4, 20), 5)
    sale12 = Sale(12,12,8,9, "Mike Something", 6000000, date(2019, 2, 20), 5)
    sale13 = Sale(13,13,3,3, "Harper Something", 300000, date(2019, 3, 20), 3)
    sale14 = Sale(14,14,9,7, "Kimmy Something", 2400000, date(2019, 4, 20), 5)
    sale15 = Sale(15,15,4,4, "Titus Something", 800000, date(2019, 2, 20), 4)

    session.add_all([sale1, sale2, sale3, sale4, sale5, sale6, sale7, sale8,
                     sale9, sale10, sale11, sale12, sale13, sale14, sale15])
    session.commit()

    # ---------------- Sample transaction ----------------
    # New house on listing, assigned to agent with id 10. Implicit transaction begins here
    house = House(16, 'Nicky', 3, 3, 300000, 34000, date(2019, 1, 20), True, 10)

    # A new new listing can be added without any inconsistency
    session.add(house)
    session.commit()

    # Agent id 10 sold house while working with office id 7, commission calculated and added, house changed to sold
    sale = Sale(16, 16, 10, 7, "Michael Something", 350000, date(2019, 2, 20), 3)
    commission_rate = session.query(CommissionRate).filter(CommissionRate.id == 3).first()
    commission_amt = sale.price * commission_rate.rate
    commission = Commission(sale.agent_id, commission_amt)
    print(commission)  # Should be $21,000
    house.on_sale = False

    # Add to the session and commit. If any of the previous stuff fails, the entire transaction fails.
    # --> No inconsistency in the database.
    session.add_all([sale, commission])
    session.commit()


if __name__ == "__main__":
    main()