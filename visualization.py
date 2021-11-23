import psycopg2
from matplotlib import pyplot as plt

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
group by coffee.cups_per_day order by coffee.cups_per_day
'''

connection=psycopg2.connect(user=USERNAME, password=PASSWORD, dbname=DATABASE, host=HOST, port=PORT)

with connection:
    cursor = connection.cursor()

    cursor.execute(query1)
    data={}
    for row in cursor:
        data[row[0]]=row[1]
    
    x=range(len(data.keys()))
    figure, bar_ax=plt.subplots()
    bar=bar_ax.bar(x,data.values(), label="Total")
    bar_ax.set_title("Програмісти, що пьють каву")
    bar_ax.set_xlabel("Кількість програмістів")
    bar_ax.set_ylabel("Назва кави")
    bar_ax.set_xticks(x)
    bar_ax.set_xticklabels(data.keys())


    cursor.execute(query2)
    data={}
    for row in cursor:
        data[row[0]]=row[1]
    figure, pie_ax=plt.subplots()  
    pie_ax.pie(data.values(), labels=data.keys())
    pie_ax.set_title("Частка вирішених помилок у коді у тих, хто пье американо")

    print('\nQUERY 3:')
    cursor.execute(query3)
    data={}
    for row in cursor:
        data[row[0]]=row[1]
    
    x=range(len(data.keys()))
    figure, bar_ax=plt.subplots()
    bar=bar_ax.bar(x,data.values(), label="Total")
    bar_ax.set_title("Кількість чашок кави на день")
    bar_ax.set_xlabel("Кількість програмістів")
    bar_ax.set_ylabel("Кількість чашок кави на день")
    bar_ax.set_xticks(x)
    bar_ax.set_xticklabels(data.keys())



plt.show()