from datetime import date, timedelta
from app.create import Office, Sale, Agent, Commission, House
from app.insert_data import session
from sqlalchemy.sql import func


def current_month(month):
    """
    Helper function that creates a date object used to filter sales
    :param month: a month of the current year
    :return: date object
    """
    current_date = date.today().replace(month=month, day=1)
    return current_date


def top_5_offices(month):
    """
    Prints top 5 offices with most sales for a certain month
    :param month: a month of the current year
    """
    for office, sales in session.query(Office, func.sum(Sale.price)).join(Sale).filter(Office.id == Sale.office_id).\
            filter(Sale.date_sell >= current_month(month)).filter(Sale.date_sell < current_month(month + 1)).\
            group_by(Office.id).order_by(func.sum(Sale.price).desc()).limit(5).all():
        print(office, 'has {} USD in sales'.format(sales))


def top_5_agents(month):
    """
    Prints top 5 agents with most sales for the a certain month
    :param month: a month of the current year
    """
    for agent, sales in session.query(Agent, func.sum(Sale.price)).join(Sale).filter(Agent.id == Sale.agent_id).\
            filter(Sale.date_sell >= current_month(month)).filter(Sale.date_sell < current_month(month + 1)).\
            group_by(Agent.id).order_by(func.sum(Sale.price).desc()).limit(5).all():
        print('Agent {0} has record sales of {1} USD. Email - {2}, Phone - {3}'.\
              format(agent.name, sales, agent.email, agent.number))


def commision_calc(month):
    """
    Print the amount of commission for each agent for a certain month
    :param month: a month of the current year
    """
    for sale in session.query(Sale).filter(Sale.date_sell >= current_month(month)).\
            filter(Sale.date_sell < current_month(month + 1)).all():

        # For each sale, calculate the commission
        commission = sale.price * sale.commission_rate.rate

        # If there isn't an entry for this agent, create a new Commission entry
        if session.query(Commission).filter(Commission.agent_id == sale.agent_id).all() == []:
            session.add(Commission(agent_id=sale.agent_id, amount=commission))
            session.commit()
        # If an entry already exists for this agent, query and update the existing entry
        else:
            agent_commission = session.query(Commission).filter(Commission.agent_id == sale.agent_id).first()
            agent_commission.amount = agent_commission.amount + commission
            session.commit()
    # Prints info on the agents and their corresponding commission amount
    for commission in session.query(Commission).order_by(Commission.amount.desc()).all():
        print('Agent {0} has {1} USD in commission'.format(commission.agent.name, commission.amount))


def avg_days_on_market(month):
    """
    Returns the average number of days houses sold are on the market in a certain month
    :param month: a month of the current year
    :return: average number of days
    """
    durations = []
    for sale in session.query(Sale).filter(Sale.date_sell > current_month(month)).\
            filter(Sale.date_sell < current_month(month + 1)).all():
        # Subtract the date sold by the date listed to get the duration
        delta = sale.date_sell - sale.house.date_list
        durations.append(delta)
    # Create an empty "timedelta" object to accumulate
    sum_days = timedelta()
    for days in durations:
        sum_days += days
    return "The average #days on the market for the month is {}".format(sum_days/len(durations))


def avg_price_on_market(month):
    """
    Returns the average price of the houses sold in a certain month
    :param month: a month of the current year
    :return: average price of the houses
    """
    prices = []
    for sale in session.query(Sale).filter(Sale.date_sell >= current_month(month)).\
            filter(Sale.date_sell < current_month(month + 1)).all():
        prices.append(sale.price)
    return "The average selling price for the month is {} USD".format(sum(prices)/len(prices))


def top_5_zip(month):
    """
    Prints the top 5 zip codes with the most sales in a certain month
    :param month: a month of the current year
    """
    for house, avg_price in session.query(House, func.avg(Sale.price)).join(Sale).filter(House.id == Sale.house_id).\
            filter(Sale.date_sell >= current_month(month)).filter(Sale.date_sell < current_month(month + 1)).\
            group_by(House.zip).order_by(func.avg(Sale.price).desc()).limit(5).all():
        print('Houses in zip area of {0} have an average selling price of {1} USD'.format(house.zip, avg_price))


print('===================== Top 5 Offices ======================')
print("/For March/")
top_5_offices(3)
print('')
print("/For April/")
top_5_offices(4)
print('')
print('')

print('===================== Top 5 Estate Agents ======================')
print("/For March/")
top_5_agents(3)
print('')
print("/For April/")
top_5_agents(4)
print('')
print('')

print('===================== Monthly Commission ======================')
print("/For March/")
commision_calc(3)
print('')
print("/For April/")
commision_calc(4)
print('')
print('')

print('===================== Average # days on the market ======================')
print("/For March/")
print(avg_days_on_market(3))
print('')
print("/For April/")
print(avg_days_on_market(4))
print('')
print('')

print('===================== Average price on the market ======================')
print("/For March/")
print(avg_price_on_market(3))
print('')
print("/For April/")
print(avg_price_on_market(4))
print('')
print('')

print('===================== Top 5 zip codes ======================')
print("/For March/")
top_5_zip(3)
print('')
print("/For April/")
top_5_zip(4)