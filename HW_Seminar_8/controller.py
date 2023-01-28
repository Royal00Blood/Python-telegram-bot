import model as m
import view
import sys

data_global = []

def switch(lang):
    if lang == 1:# Найти сотрудника
        m.find_worker()
    elif lang == 2:# Сделать выборку сотрудников по должности
        m.filter_position()
    elif lang == 3:# Сделать выборку сотрудников по зарплате
        m.filter_salary()
    elif lang == 4:# Добавить сотрудника
        data = m.add_worker()
        data_global.append(data)
        print("Do you want to save the new record? \n")
        print("If yes enter 'y', if no enter 'n' ")
        if input(": ") == "y":
            m.export_data_csv(data_global)
            return data_global
    elif lang == 5:# Удалить сотрудника
        m.del_worker()
    elif lang == 6:  # Обновить данные сотрудника
        m.worker_updata()
    elif lang == 7:  # Экспортировать данные в формате json
        m.export_data_csv(data_global)
        _, data = m.get_data_csv(2)
        m.export_data_json()
    elif lang == 8:  # Экспортировать данные в формате csv
        m.export_data_csv(data_global)
        m.get_data_csv(0)
    elif lang == 9:  # Закончить работу
        sys.exit()
    else:
        print("You had mistake!")

def main():
    answer = view.interface()
    switch(answer)
