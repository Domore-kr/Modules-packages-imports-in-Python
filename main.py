from application.people import get_employees
from application.salary import calculate_salary
import datetime

if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))
