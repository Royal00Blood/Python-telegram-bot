import csv
import json
import time

def get_data_csv(flag=0):
    if flag == 0:
        with open('data/data.csv') as f:
            data = csv.reader(f)
            for row in data:
                print(row)
        time.sleep(0.5)
    if flag == 1:
        with open('data/data.csv') as f:
            data = csv.DictReader(f)
            for row in data:
                print(row)
                print(row['hostname'], row['model'])
    if flag == 2:
        with open('data/data.csv') as f:
            data = csv.reader(f)
            data_list = list(data)
        return data, data_list
def new_data(bot, message):
    bot.send_message(message.chat.id, text="Enter Name: ")
    name = message.text
    bot.send_message(message.chat.id, text="Enter Name: ")
    surname = message.text
    bot.send_message(message.chat.id, text="Enter Name: ")
    department = message.text
    bot.send_message(message.chat.id, text="Enter Name: ")
    position = message.text
    bot.send_message(message.chat.id, text="Enter Name: ")
    salary = message.text
    return name, surname, department, position, salary
def add_worker(bot,message):
    data = list(new_data(bot,message))
    print(data)
    return data
def export_data_csv(data):
    with open('data/data.csv', 'a', newline='') as state_file:
        writer = csv.writer(state_file)
        for i in range(len(data)):
            writer.writerow(data[i])
def data_transformation():
    _, data = get_data_csv(2)
    data_dict = {}
    data_dict['people'] = []
    for i in range(len(data)):
        data_dict['people'].append({
            'name': data[i][0],
            'surname': data[i][1],
            'department': data[i][2],
            'position': data[i][3],
            'salary': data[i][4]
        })
    return data_dict
def export_data_json():
    open("data/data.json", "w").close()
    dict_new = data_transformation()
    for i in range(len(dict_new)):
        with open('data/data.json', 'w') as outfile:
            json.dump(dict_new, outfile)
def find_worker():
    print("Enter employee details")
    inf_worker = list(new_data())
    _, data = get_data_csv(2)
    rez_list = []
    for i in range(len(data)):
        if inf_worker == data[i]:
            rez_list.append(i)
            print(f"Employee found. List position is {i}. ")
            print(f"Worker: name: {data[i][0]} , "
                  f"surname: {data[i][1]} , "
                  f"department: {data[i][2]} , "
                  f"position: {data[i][3]}, "
                  f"salary: {data[i][4]}")
    print(f"Found {len(rez_list)} employees")
    return rez_list
def print_worker(index):
    _, data = get_data_csv(2)
    print(f"Worker: name: {data[index][0]} , "
              f"surname: {data[index][1]} , "
              f"department: {data[index][2]} , "
              f"position: {data[index][3]}, "
              f"salary: {data[index][4]}")
def clear_file():
    f = open("data/data.csv", "w")
    f.truncate()
    f.close()
def del_worker():
    worker = list(new_data())
    _, data = get_data_csv(2)
    list_new = [x for x in data if worker != x]
    # for i in range(len(data)):
    #     data.remove(worker)
    # print(list_new == data)
    clear_file()
    export_data_csv(list_new)
    print(f"Worker: name: {worker[0]} , "
          f"surname: {worker[1]} , "
          f"department: {worker[2]} , "
          f"position: {worker[3]}, "
          f"salary: {worker[4]}",
          f"deleted")
def filter_position():
    position_find = input("Enter position to search: ")
    rez_list = []
    _, data = get_data_csv(2)
    for i in range(len(data)):
        if position_find == data[i][3]:
            rez_list.append(i)
            print_worker(i)
    print(rez_list)
def filter_salary():
    salary_find = input("Enter salary to search: ")
    rez_list = []
    _, data = get_data_csv(2)
    for i in range(len(data)):
        if salary_find == data[i][4]:
            rez_list.append(i)
            print_worker(i)
    print(rez_list)

def worker_updata():
    index = find_worker()
    _, data = get_data_csv(2)
    position = input("Enter number update position. "
          "0-name, "
          "1-surname, "
          "2-department, "
          "3-position, "
          "4 -salary: ")
    value = input("Enter new value")
    data[index[0]][int(position)] = value
    export_data_csv(data)
