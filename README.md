# Mock database application

A database set-up written in SQLAlchemy for a mock real-estate company.

## General Instructions:

Clone the repo, cd to repo:
```
$ cd folder/to/clone/into
$ git clone https://github.com/hu-ng/real-estate-db.git
$ cd real-estate-db
```

From the command line and in `real-estate-db`, run these lines:
```cmd
$ python -m pip install -r requirements.txt   # install the required dependencies
$ python create.py  # create model classes
$ python insert_data.py  # create the database connection and insert fake data to test out queries
$ python query_data.py  # run the queries
```

## Discussion:

The database was created to satisfy the following constraints/relationships:
- A real estate agent can be associated with many offices, and an office can have many agents.
- An agent can take charge of many houses and their corresponding sales. Houses and sales have a 1-1 relationship.
- For every sale, an agent receives a commission based on how much the sale was. There are 5 commission brackets.

With data normalization in mind, the following tables and relationships were created:
- `Agent` and `Office` tables have a many-to-many relationship using an association table
- `Agent` and `House` has a one-to-many relationship using a FK in `House`
- `Sale` and `House` has a one-to-one relationship using a FK in `Sale`
- `Agent` and `Sale` has a one-to-many relationship using a FK in `Sale`
- `CommissionRate` and `Sale` has a one-to-many relatioship using a FK in `Sale`
- `Commission` and `Agent` has one-to-one relationship using an FK in `Commission`

For every month, the following queries are ran:
- Find the top 5 offices with the most sales.
- Find the top 5 estate agents who have sold the most and their contact details.
- Calculate the commission that each estate agent must receive and store the results in a separate table.
- For all houses that were sold that month, calculate the average number of days that the house was on the market.
- For all houses that were sold that month, calculate the average selling price.
- Find the zip codes with the top 5 average sales prices.
