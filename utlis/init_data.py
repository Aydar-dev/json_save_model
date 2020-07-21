import json
from job.settings import DATA_JSON_FILE_ADDRESS
from basic_app.models import *


def initData():
    with open(DATA_JSON_FILE_ADDRESS, 'r') as read_data:
        data = read_data.read()
    data_list = json.loads(data)
    for item in data_list:
        task_obj = Task()
        task_obj.rank = item["rank"]
        task_obj.employer = item["employer"]
        task_obj.employeesCount = item["employeesCount"]
        task_obj.medianSalary = item["medianSalary"]
        task_obj.save()

    return json.dumps(
        {
            'status': 'success',
            'msg': 'init data'
        }
    )