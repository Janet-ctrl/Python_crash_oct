from employees import Employees
from accounting import Accounting
from engineering import Engineering


emp1 = Accounting('suzan', 'roux', 1234565679, 'suzan@here.com','manager', 80_000 ,'NC')
emp2 = Engineering('ben', 'smith', 5206245119, 'ben@engin.com', 'developer', 95_000, 'GP')
emp3 = Accounting('blair', 'black', 2469354287, 'blair@here.com', 'trainer', 75_000, 'FS')
emp4 = Engineering('dawn', 'doe', 4561122345, 'dawn@engin.com', 'manager', 98_000, 'WP' )



emp1.displayInfo()
emp2.displayInfo()
emp3.displayInfo()
emp4.displayInfo()