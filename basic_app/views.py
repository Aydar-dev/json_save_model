from django.shortcuts import render
from django.views.generic.base import View

from basic_app.models import *
from utlis.init_data import *
import json
# Create your views here.


class IndexView(View, ):
    def get(self, request):
        status = request.GET.get("status")
        msg = ""
        if status == "init_data":
            result_string = initData()
            result = json.loads(result_string)
            if result['status'] == "success":
                msg = "init data"
            else:
                msg = "error"
        elif status == "delete_data":
            all_obj = Task.objects.all()
            all_obj.delete()
            msg = "delete data"
        return render(request, 'index.html', {
            "msg": msg
        })


class DataView(View):
    def get(self, request):
        filter_type = request.GET.get("filter_type", )
        data = Task.objects.all()
        if filter_type == "rank":
            data = data.order_by("-rank")
        if filter_type == "employer":
            data = data.order_by("employer")
        if filter_type == "employeesCount":
            data = data.order_by("employeesCount")
        return render(request, 'data_list.html', {
            'all_data': data
        })


class DataDetailView(View):
    def get(self, request, uid):
        data = Task.objects.get(id=int(uid))
        return render(request, 'detail-data.html', {
            'data': data,
        })
