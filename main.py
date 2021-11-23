import psycopg2

USERNAME='kostenko'
PASSWORD='1234'
DATABASE='coffe_and_code'
HOST='localhost'
PORT='5432'


query1='''
select trim(coffee.coffee_type), count(coder.coffee_id) 
from coffee inner join coder on coffee.id=coder.coffee_id
group by coffee.coffee_type
'''

query2='''
select trim(bugs.solve_bugs), count(coffee.id)
from bugs inner join coffee on bugs.id=coffee.id where coffee.coffee_type in ('Americano') 
group by bugs.solve_bugs;
'''

query3='''
select coffee.cups_per_day, count(coder.coffee_id) 
from coffee inner join coder on coffee.id=coder.coffee_id 
group by coffee.cups_per_day
'''

connection=psycopg2.connect(user=USERNAME, password=PASSWORD, dbname=DATABASE, host=HOST, port=PORT)

with connection:
    cursor = connection.cursor()

    print('QUERY 1:')
    cursor.execute(query1)
    for row in cursor:
        print(row)

    print('\nQUERY 2:')
    cursor.execute(query2)
    for row in cursor:
        print(row)

    print('\nQUERY 3:')
    cursor.execute(query3)
    for row in cursor:
        print(row)