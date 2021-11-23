-- Query 1: Кількість програмістів за типом кави, що вони пьють
select trim(coffee.coffee_type), count(coder.coffee_id) 
from coffee inner join coder on coffee.id=coder.coffee_id
group by coffee.coffee_type;

--Query 2: Частка вирешиних помилок у коді у тих, хто пье американо
select trim(bugs.solve_bugs), count(coffee.id)
from bugs inner join coffee on bugs.id=coffee.id where coffee.coffee_type in ('Americano') 
group by bugs.solve_bugs;

--Query 3: кількість програмістів за кількістю чашок кави, що вини пьють за день
select coffee.cups_per_day, count(coder.coffee_id) 
from coffee inner join coder on coffee.id=coder.coffee_id 
group by coffee.cups_per_day