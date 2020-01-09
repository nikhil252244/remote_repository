from django.shortcuts import render

from curdapp.models import ProductData
from curdapp.forms import InsertingDataForm,UpdateForm,DeleteForm
from django.http.response import HttpResponse

def home(request):
    return render(request,'home.html')


def create_view(request):
    if request.method=='POST':


            pid=request.POST.get('product_id')
            pname=request.POST.get('product_name')
            pcost=request.POST.get('product_cost')
            pclass=request.POST.get('product_class')
            nop=request.POST.get('no_of_products')
            cname=request.POST.get('customer_name')
            mobile=request.POST.get('mobile')
            email=request.POST.get('email')
            mnf_date=request.POST.get('manfacturing_date')
            exp_date=request.POST.get('expiry_date')
            data=ProductData(
                product_id=pid,
                product_name=pname,
                product_cost=pcost,
                product_class=pclass,
                no_of_products=nop,
                customer_name=cname,
                mobile=mobile,
                email=email,
                manufacture_date=mnf_date,
                expiry_date=exp_date
            )
            data.save()

            return render(request,'create.html')
    else:
        return render(request,'create.html')



def Retrive_view(request):
    Data=ProductData.objects.all()
    return render(request,'retrive.html',{'Data':Data})


def update_view(request):
    if request.method=='POST':
        pid=request.POST.get('product_id')
        pcost=request.POST.get('product_cost')

        pro_id=ProductData.objects.filter(product_id=pid)
        if not pro_id:
            return HttpResponse('data is not available')
        else:
            pro_id.update(product_cost=pcost)
            return render(request,'curd_update.html')
    else:
        return render(request,'curd_update.html')


def curd_delete(request):
    if request.method=='POST':
        pid=request.POST.get('product_id')
        pro_id=ProductData.objects.filter(product_id=pid)
        if not pro_id:
            return HttpResponse('data is not available')
        else:
            pro_id.delete()
            return render(request,'curd_delete.html')
    else:
        return render(request,'curd_delete.html')
