import datetime
from django.http import HttpResponse
from django.core.files.storage import  FileSystemStorage
from myapp.models import *
from django.shortcuts import render, redirect


#  LOGIN PAGE

def loging(request):
    return render(request,'login_page.html')

def loginp(request):
    var1 = request.POST['uname']
    var2 = request.POST['pass']
    res = login.objects.filter(username=var1,password=var2)

    if res.exists():
        obj = login.objects.get(username=var1, password=var2)

        if obj.type=='admin':
            request.session['lid']=obj.id
            return redirect('/myapp/adminpage/')

        elif obj.type== 'rcunit':
            request.session['lid'] = obj.id
            return redirect('/myapp/rcunithpage/')

        elif obj.type== 'user':
            request.session['lid'] = obj.id
            return redirect('/myapp/userhpage/')

        elif obj.type== 'pickup':
            request.session['lid'] = obj.id
            return redirect('/myapp/pickuphpage/')

        elif obj.type== 'worker':
            request.session['lid'] = obj.id
            return redirect('/myapp/workerhpage/')

        else:
         return HttpResponse('Error')

    else:
        return HttpResponse("no user found")


# PAGES
def admin_page(request):
    return render(request, 'ADMIN.html')

def rcunit_page(request):
    return render(request, 'RECYCLE_UNIT.html')

def user_page(request):
    return render(request, 'USER.html')

def pickup_page(request):
    return render(request, 'PICKUP.html')

def worker_page(request):
    return render(request, 'WORKER.html')



#                     MODULE 1
#  ADMIN

# Change Password
def admin_changepassword(request):
    return render(request, 'admin/change_password.html')

def admin_changepasswordp(request):
    var1 = request.POST['p1']
    var2 = request.POST['p2']
    var3 = request.POST['p3']
    res = login.objects.filter(id=request.session['lid'],password=var1)
    if res.exists():
        if var2 == var3:
            obj = login.objects.filter(id=request.session['lid']).update(password=var2)
            return HttpResponse('''<script>alert("changed");windows.location='/myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert("error");windows.location='/myapp/achange/'</script>''')

    else:
        return HttpResponse('''<script>alert("error");windows.location='/myapp/achange/'</script>''')


# View Recycle Unit

def view_rcunit(request):
    res = recycle_unit.objects.all()
    return render(request, 'admin/view_recycle_unit.html',{'data':res})



# 2. Add Waste Management

def add_wasteg(request):
    res = waste.objects.all()
    return render(request,'admin/add_waste_management.html', {'data':res})

def add_wastep (request):
    num1 = request.POST['type']
    num2 = request.POST['rate']


    obj = waste()
    obj.type = num1
    obj.rate = num2

    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/addwastep/'</script>''')


# View Waste Management

def view_waste(request):
    res = waste.objects.all()
    return render(request, 'admin/view_waste_management.html',{'data':res})

# Edit Waste Management

def edit_wasteg(request,ew):
    res = waste.objects.get(id=ew)
    return render(request,'admin/edit_waste_management.html',{'data':res})

def edit_wastep (request):
    var1 = request.POST ['type']
    var2 = request.POST ['rate']

    ed =request.POST['ewaste']

    obj= waste.objects.get(id=ed)
    obj.type = var1
    obj.rate = var2
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/editwastep/'</script>''')

# Delete Waste Management

def delete_waste(request,dw):
    res = waste.objects.get(id=dw).delete()
    return redirect('/myapp/viewwaste')




# . Add Notification

def add_notifig(request):
    res = notifications.objects.all()
    return render(request,'admin/add_notification.html', {'data':res})

def add_notifip (request):
    num1 = request.POST['date']
    num2 = request.POST['noti']


    obj = notifications()
    obj.date = num1
    obj.notification = num2

    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/addnotifip/'</script>''')

# View Noti

def view_notifi(request):
    res = notifications.objects.all()
    return render(request, 'admin/view_notification.html',{'data':res})

# Edit Noti

def edit_notifig(request,enf):
    res = notifications.objects.get(id=enf)
    return render(request,'admin/edit_notification.html',{'data':res})

def edit_notifip (request):
    var1 = request.POST ['date']
    var2 = request.POST ['noti']

    e =request.POST['enoti']

    obj= notifications.objects.get(id=e)
    obj.date = var1
    obj.notification = var2
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/addnotifip/'</script>''')

# Delete Noti

def delete_notifi(request,dnf):
    res = notifications.objects.get(id=dnf).delete()
    return redirect('/myapp/viewnotifi')


# . Add Area Allocation to Worker
def add_worker_allocg(request):
    res = worker.objects.all()
    return render(request, 'admin/add_worker_allocation.html', {'data':res})

def add_worker_allocp(request):
    var1 = request.POST['wlid']

    var2 = request.POST['area']
    var3 = request.POST['date']

    obj = allocation()
    obj.WORKER_id= var1
    obj.area = var2
    obj.date = var3
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/addwallocp/'</script>''')


# View Area Allocation to Worker
def view_worker_alloc(request):
    res = allocation.objects.all()
    return render(request, 'admin/view_worker_allocation.html', {'data':res})

# Edit Area Allocation to Worker
def edit_worker_allocg(request,ewa):
    re = allocation.objects.get(id=ewa)
    res = worker.objects.all()
    return render(request,'admin/edit_worker_allocation.html',{'data':re, 'data2':res})

def edit_worker_allocp (request):
    var1 = request.POST ['wlid']

    var2 = request.POST ['area']
    var3 = request.POST ['date']

    num =request.POST['ewalloc']

    obj= allocation.objects.get(id=num)
    obj.LOGIN_id = var1
    obj.area = var2
    obj.date = var3
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/editwallocp/'</script>''')


# Delete Alloc
def delete_work_alloc(request, dwa):
    res = allocation.objects.get(id= dwa).delete()
    return redirect('/myapp/viewwalloc')



# View User By Admin
def view_user_admin(request):
    res = user.objects.all()
    return render(request, 'admin/view_users.html', {'data':res})


# View complaint of User by Admin
def view_complaint(request):
    res = complaint.objects.all()
    return render(request, 'admin/view_complaint.html', {'data':res})


# Sent Reply by admin
def sent_replyg(request,id):
    res = complaint.objects.get(id=id)
    return render(request, 'admin/sent_reply.html',{'data':res})

def sent_replyp(request):
    var1 = request.POST['reply']

    comid= request.POST['comid']

    cobj = complaint.objects.get(id=str(comid))
    cobj.reply = var1
    cobj.status='Replied'
    cobj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/sentreplyp/'</script>''')


# . Add Category Management

def add_categoryg(request):
    res = category.objects.all()
    re = worker.objects.all()
    return render(request,'admin/add_category.html', {'data':res,'data2':re})

def add_categoryp (request):
    num1 = request.POST['catname']
    num2 = request.POST['wrkid']

    obj = category()
    obj.category_name = num1
    obj.WORKER_id = num2
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/addcatp/'</script>''')

# View Category

def view_category(request):
    res = category.objects.all()
    return render(request, 'admin/view_category.html',{'data':res})

# Edit Category

def edit_categoryg(request,ecat):
    res = category.objects.get(id=ecat)
    re = worker.objects.all()
    return render(request,'admin/edit_category.html',{'data':res, 'data2':re})

def edit_categoryp (request):
    var1 = request.POST ['catname']
    var2 = request.POST ['wrkid']


    ed =request.POST['ecate']

    obj= category.objects.get(id=ed)
    obj.category_name = var1
    obj.WORKER_id = var2
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/editcatp/'</script>''')

# Delete Category

def delete_category(request,dcat):
    res = category.objects.get(id=dcat).delete()
    return redirect('/myapp/viewcat')


# View Feedback of User

def view_feedback(request):
    res = feedback.objects.all()
    return render(request, 'admin/view_feedback.html',{'data':res})


#                          MODULE 2
#  PICKUP


# Change Password
def pickup_changepassword(request):
    return render(request, 'pickup/change_password.html')

def pickup_changepasswordp(request):
    var1 = request.POST['q1']
    var2 = request.POST['q2']
    var3 = request.POST['q3']
    res = login.objects.filter(id=request.session['lid'],password=var1)
    if res.exists():
        if var2 == var3:
            obj = login.objects.filter(id=request.session['lid']).update(password=var2)
            return HttpResponse('''<script>alert("changed");windows.location='/myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert("error");windows.location='/myapp/pchange/'</script>''')

    else:
        return HttpResponse('''<script>alert("error");windows.location='/myapp/pchange/'</script>''')




# 1.  Add/REGISTER Pickup

def add_pickupg(request):
    res = pickup.objects.all()
    return render(request, 'pickup/pickup_registration_add.html', {'data':res})

def add_pickupp(request):

    var1 = request.POST['name']
    var2 = request.POST['phno']
    var3 = request.POST['idproof']
    var4 = request.POST['quali']
    var5 = request.POST['exp']

    lobj = login()
    lobj.username = var1
    lobj.password= var2
    lobj.type = 'pickup'
    lobj.save()

    obj = pickup()
    obj.name = var1
    obj.phone_number = var2
    obj.id_proof = var3
    obj.qualification = var4
    obj.experiance = var5

    obj.LOGIN_id = lobj.id
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/addpickupp/'</script>''')


# View Pickup
def view_pickup(request):
    re = login.objects.all()
    res = pickup.objects.all()
    return render(request, 'pickup/pickup_registration_view.html', {'data':res, 'data2':re})

# Edit Pickup

def edit_pickupg(request,ep):
    res = pickup.objects.get(id=ep)
    return render(request, 'pickup/pickup_registration_edit.html', {'data':res})

def edit_pickupp (request):
    num =request.POST['epk']

    var1 = request.POST ['name']
    var2 = request.POST ['phno']
    var3 = request.POST ['idproof']
    var4 = request.POST ['quali']
    var5 = request.POST ['exp']


    obj= pickup.objects.get(id=num)
    obj.name = var1
    obj.phone_number = var2
    obj.id_proof = var3
    obj.qualification = var4
    obj.experiance = var5
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/editpickupp/'</script>''')

# Delete Pickup

def delete_pickup(request, dp):
    res = pickup.objects.get(id = dp).delete()
    return redirect('/myapp/viewpickup')

# View Profile of Pickup

def pickup_profile_view(request):
    res = pickup.objects.get(LOGIN_id  =request.session['lid'])
    return render(request, 'pickup/pickup_view_profile.html',{'data':res})



# View User Waste Request and Collect
def view_request(request):
    res = waste_request.objects.all()
    return render(request, 'pickup/view_waste_request.html',{'data':res})






#                  Module 3

#Worker


# Change Password
def worker_changepassword(request):
    return render(request, 'worker/change_password.html')

def worker_changepasswordp(request):
    var1 = request.POST['p1']
    var2 = request.POST['p2']
    var3 = request.POST['p3']
    res = login.objects.filter(id=request.session['lid'],password=var1)
    if res.exists():
        if var2 == var3:
            obj = login.objects.filter(id=request.session['lid']).update(password=var2)
            return HttpResponse('''<script>alert("changed");windows.location='/myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert("error");windows.location='/myapp/changepasswordw/'</script>''')

    else:
        return HttpResponse('''<script>alert("error");windows.location='/myapp/changepasswordw/'</script>''')

# . Add/REGISTER Worker

def add_workerg(request):
    res = worker.objects.all()
    return render(request, 'worker/add_worker.html', {'data':res})

def add_workerp(request):

    var1 = request.POST['name']
    var2 = request.POST['phno']
    var3 = request.POST['gender']
    var4 = request.POST['quali']
    var5 = request.POST['dob']
    var6 = request.POST['place']
    var7 = request.POST['post']
    var8 = request.POST['pin']
    var9 = request.POST['dist']
    var10 = request.POST['email']
    var11 = request.FILES['photo']
    var12 = request.POST['idproof']

    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + '.jpg'
    fn = fs.save(date, var11)

    lobj = login()
    lobj.username = var1
    lobj.password= var2
    lobj.type = 'worker'
    lobj.save()

    obj = worker()
    obj.name = var1
    obj.phone_number = var2
    obj.gender = var3
    obj.qualification = var4
    obj.dob = var5
    obj.place = var6
    obj.post = var7
    obj.pin = var8
    obj.district = var9
    obj.email_id = var10
    obj.status = "pending"
    obj.photo = fs.url(date)
    obj.id_proof = var12

    obj.LOGIN_id = lobj.id
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/addworkerp/'</script>''')

# View Worker
def view_worker(request):
    res = worker.objects.all()
    return render(request, 'worker/view_worker.html', {'data':res})


# Edit Worker

def edit_workerg(request, ewr):
    res = worker.objects.get(id =ewr)
    return render(request, 'worker/edit_worker.html', {'data':res})

def edit_workerp(request):
    num1 = request.POST['eworker']

    var1 = request.POST['name']
    var2 = request.POST['phno']
    var3 = request.POST['gender']
    var4 = request.POST['quali']
    var5 = request.POST['dob']
    var6 = request.POST['place']
    var7 = request.POST['post']
    var8 = request.POST['pin']
    var9 = request.POST['dist']
    var10 = request.POST['email']
    var12 = request.POST['idproof']

    obj = worker.objects.get(id = num1)

    if 'photo' in request.FILES:
        var11 = request.FILES['photo']
        fs = FileSystemStorage()
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+'.jpg'
        fn = fs.save(date, var11)
        obj.photo = fs.url(date)

        obj.name = var1
        obj.phone_number = var2
        obj.gender = var3
        obj.qualification = var4
        obj.dob = var5
        obj.place = var6
        obj.post = var7
        obj.pin = var8
        obj.district = var9
        obj.email_id = var10
        obj.id_proof = var12

        obj.save()
        return HttpResponse("Edit Successfully")

    else:
        obj.name = var1
        obj.phone_number = var2
        obj.gender = var3
        obj.qualification = var4
        obj.dob = var5
        obj.place = var6
        obj.post = var7
        obj.pin = var8
        obj.district = var9
        obj.email_id = var10
        obj.id_proof = var12

        obj.save()
        return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/editworkerp/'</script>''')


# Delete Worker

def delete_worker(request, dwkr):
    res = worker.objects.get(id = dwkr).delete()
    return redirect('/myapp/viewworker')


# View Profile of Worker

def worker_profile_view(request):
    res = worker.objects.get(LOGIN_id  =request.session['lid'])
    return render(request, 'worker/worker_profile_view.html',{'data':res})


# View User Request And Update Status

def view_user_request_update(request):
    res = waste_request.objects.all()
    return render(request, 'worker/view_user_request_update.html',{'data':res})


#Approve by Worker
def approve(request, id):
    res = worker.objects.filter(pk=id).update(status = 'Aproved')
    return HttpResponse('''<script>alert("OK APPROVED");windows.location='/myapp/approve/'</script>''')


# Reject by Worker
def reject(request, id):
    res = worker.objects.filter(pk=id).update(status = 'Rejected')
    return HttpResponse('''<script>alert("OK REJECTED");windows.location='/myapp/reject/'</script>''')


# View Allocated Area
def view_allocated_area(request):
    res = allocation.objects.all()
    return render(request, 'worker/view_allocated_area.html', {'data':res})








#                  Module 4

#User

# Change Password
def user_changepassword(request):
    return render(request, 'user/change_password.html')

def user_changepasswordp(request):
    var1 = request.POST['p1']
    var2 = request.POST['p2']
    var3 = request.POST['p3']
    res = login.objects.filter(id=request.session['lid'],password=var1)
    if res.exists():
        if var2 == var3:
            obj = login.objects.filter(id=request.session['lid']).update(password=var2)
            return HttpResponse('''<script>alert("changed");windows.location='/myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert("error");windows.location='/myapp/changepasswordu/'</script>''')

    else:
        return HttpResponse('''<script>alert("error");windows.location='/myapp/changepasswordu/'</script>''')

# . Add/REGISTER User

# . Add/REGISTER User

def add_userg(request):
    res = user.objects.all()
    return render(request, 'user/user_registration_add.html', {'data':res})

def add_userp(request):

    var1 = request.POST['name']
    var2 = request.POST['phno']
    var3 = request.POST['email']
    var4 = request.POST['place']
    var5 = request.POST['post']
    var6 = request.POST['pin']
    var7 = request.POST['dist']

    lobj = login()
    lobj.username = var1
    lobj.password= var2
    lobj.type = 'user'
    lobj.save()

    obj = user()
    obj.name = var1
    obj.phone_number = var2
    obj.email = var3
    obj.place = var4
    obj.post = var5
    obj.pin = var6
    obj.district = var7

    obj.LOGIN_id = lobj.id
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/adduserp/'</script>''')

# View User
def view_user(request):
    res = user.objects.all()
    return render(request, 'user/user_registration_view.html', {'data':res})


# Edit User
def edit_userg(request,eu):
    res = user.objects.get(id=eu)
    return render(request, 'user/user_registration_edit.html', {'data':res})

def edit_userp (request):
    num =request.POST['euser']

    var1 = request.POST ['name']
    var2 = request.POST ['phno']
    var3 = request.POST ['email']
    var4 = request.POST ['place']
    var5 = request.POST ['post']
    var6 = request.POST ['pin']
    var7 = request.POST ['dist']

    obj= user.objects.get(id=num)
    obj.name = var1
    obj.phone_number = var2
    obj.email = var3
    obj.place = var4
    obj.post = var5
    obj.pin = var6
    obj.district = var7
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/edituserp/'</script>''')

# Delete User

def delete_user(request, du):
    res = user.objects.get(id = du).delete()
    return redirect('/myapp/viewuser')

# View Profile of User

def view_profile_user(request):
    res = user.objects.get(LOGIN_id  =request.session['lid'])
    return render(request, 'user/user_profile_view.html',{'data':res})



# Add User Waste Request and Collect

def add_requestg(request):
    re = user.objects.all()
    res = waste_request.objects.all()
    return render(request, 'user/add_waste_request.html', {'data':res, 'data2':re})

def add_requestp (request):
    num1 = request.POST['userid']

    num2 = request.POST['request']


    obj = waste_request()
    obj.USER_id  = num1
    obj.status = 'pending'
    obj.request = num2

    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/addrequestp/'</script>''')



# Edit Waste Request

def edit_requestg(request,er):
    res = waste_request.objects.get(id=er)
    re = user.objects.all()

    return render(request, 'user/edit_waste_request.html', {'data':res, 'data2':re})

def edit_requestp(request):
    var1 = request.POST ['userid']
    var2 = request.POST ['request']

    ed =request.POST['erequest']

    obj= waste_request.objects.get(id=ed)
    obj.type = var1
    obj.rate = var2
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/editrequestp/'</script>''')

# Delete Waste Request

def delete_request(request,dr):
    res = waste_request.objects.get(id=dr).delete()
    return redirect('/myapp/viewrequest')



# Sent Compliant by User

def sent_complaintg(request):
    res = user.objects.all()
    re = complaint.objects.all()
    return render(request, 'user/sent_complaint.html', {'data':res, 'data2':re})

def sent_complaintp(request):

    var2 = request.POST['complaint']
    from  datetime import datetime
    td = datetime.now().strftime('%Y-%m-%d')
    lid = request.session['lid']

    uobj = user.objects.get(LOGIN_id=lid)

    obj = complaint()
    obj.date = td
    obj.complaint = var2
    obj.status = 'pending'
    obj.USER_id= uobj.id
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/sentcomplaintp/'</script>''')


# View Reply by User
def view_reply_user(request):
    res = complaint.objects.all()
    return render(request, 'user/view_reply.html', {'data':res})


# Add FeedBack By User

def add_feedbackg(request):
    re = user.objects.all()
    res = feedback.objects.all()
    return render(request,'user/add_feedback.html', {'data':res, 'data2':re})

def add_feedbackp(request):
    num1 = request.POST['userid']

    num2 = request.POST['date']
    num3 = request.POST['feedback']


    obj = feedback()
    obj.USER_id  = num1

    obj.date = num2
    obj.feedback = num3
    obj.status = 'pending'

    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/addfeedbackp/'</script>''')


# View Feedback of User

def view_feedback_user(request):
    res = feedback.objects.all()
    return render(request, 'user/view_feedback.html',{'data':res})



# Edit FeedBack By User

def edit_feedbackg(request,ef):
    res = feedback.objects.get(id=ef)
    re = user.objects.all()
    return render(request,'user/edit_feedback.html',{'data':res,'data2':re})

def edit_feedbackp(request):
    var1 = request.POST ['userid']

    var2 = request.POST ['date']
    var3 = request.POST ['feedback']


    ed =request.POST['efeedback']

    obj= feedback.objects.get(id=ed)
    obj.USER_id = var1
    obj.date = var2
    obj.feedback = var3
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/editfeedbackp/'</script>''')

# Delete FeedBack By User

def delete_feedback(request,df):
    res = feedback.objects.get(id=df).delete()
    return redirect('/myapp/viewfeedbackuser')


# View Worker Category By User

def view_worker_category_user(request):
    res = category.objects.all()
    re = worker.objects.all()
    return render(request, 'user/view_worker_category.html',{'data':res})



# View Productt

def view_product(request):
    res = product.objects.all()
    return render(request, 'user/view_product.html',{'data':res})




# . Add Cart

def add_cartg(request):
    r = cart.objects.all()
    re = product.objects.all()
    res = user.objects.all()
    return render(request,'user/add_cart.html', {'data':r,'data2':re,'data3':res})

def add_cartp(request):
    num1 = request.POST['date']

    num2 = request.POST['pid']
    num3 = request.POST['uid']

    obj = cart()
    obj.date = num1
    obj.PRODUCT_id= num2
    obj.USER_id = num3
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/addcartp/'</script>''')

# View Cart

def view_cart(request):
    res = cart.objects.all()
    return render(request, 'user/view_cart.html',{'data':res})

# Edit Cart

def edit_cartg(request,ect):
    r = cart.objects.get(id=ect)
    re = product.objects.all()
    res = user.objects.all()
    return render(request,'user/edit_cart.html',{'data':r, 'data2':re,'data3':res})

def edit_cartp(request):
    ed =request.POST['ecart']

    num1 = request.POST['date']

    num2 = request.POST['pid']
    num3 = request.POST['uid']

    obj= cart.objects.get(id=ed)
    obj.date = num1
    obj.PRODUCT_id = num2
    obj.USER_id = num3
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/editcartp/'</script>''')


# Delete

def delete_cart(request,dct):
    res = cart.objects.get(id=dct).delete()
    return redirect('/myapp/viewcart')



# . Add Payment

def add_paymentg(request):
    r = payment.objects.all()
    re = user.objects.all()
    res = order_main.objects.all()
    return render(request,'user/add_payment.html', {'data':r,'data2':re,'data3':res})

def add_paymentp(request):
    num1 = request.POST['date']
    num2 = request.POST['amount']

    num3 = request.POST['uid']
    num4 = request.POST['omid']

    obj = payment()
    obj.date = num1
    obj.amount = num2
    obj.USER_id= num3
    obj.ORDERMAIN_id = num4
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/addpaymentp/'</script>''')

# View Payment

def view_payment(request):
    res = payment.objects.all()
    return render(request, 'user/view_payment.html',{'data':res})

# Edit Payment

def edit_paymentg(request,ept):
    r = payment.objects.get(id=ept)
    re = user.objects.all()
    res = order_main.objects.all()
    return render(request,'user/edit_payment.html',{'data':r, 'data2':re,'data3':res})

def edit_paymentp(request):
    ed =request.POST['epay']

    num1 = request.POST['date']
    num2 = request.POST['amount']

    num3 = request.POST['uid']
    num4 = request.POST['omid']

    obj= payment.objects.get(id=ed)
    obj.date = num1
    obj.amount = num2
    obj.USER_id = num3
    obj.ORDERMAIN_id = num4
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/editpaymentp/'</script>''')


# Delete

def delete_payment(request,dpt):
    res = cart.objects.get(id=dpt).delete()
    return redirect('/myapp/viewpayment')


#View Worker Notification And Apply--

def view_notifi_user(request):
    res = notifications.objects.all()
    return render(request, 'user/view_notification_user.html',{'data':res})



#                  Module 5

#Rcunit

# Change Password
def rcunit_changepassword(request):
    return render(request, 'recycleunit/change_password.html')

def rcunit_changepasswordp(request):
    var1 = request.POST['p1']
    var2 = request.POST['p2']
    var3 = request.POST['p3']
    res = login.objects.filter(id=request.session['lid'],password=var1)
    if res.exists():
        if var2 == var3:
            obj = login.objects.filter(id=request.session['lid']).update(password=var2)
            return HttpResponse('''<script>alert("changed");windows.location='/myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert("error");windows.location='/myapp/changepasswordr/'</script>''')

    else:
        return HttpResponse('''<script>alert("error");windows.location='/myapp/changepasswordr/'</script>''')

# . Add/REGISTER Recycle Unit
def add_recylce_unitg(request):
    res = recycle_unit.objects.all()
    return render(request, 'recycleunit/add_recycle_unit.html', {'data':res})

def add_recylce_unitp(request):

    var1 = request.POST['name']
    var2 = request.POST['place']
    var3 = request.POST['dist']
    var4 = request.POST['post']
    var5 = request.POST['pi']
    var6 = request.POST['email']
    var7 = request.POST['phno']


    lobj = login()
    lobj.username = var1
    lobj.password= var7
    lobj.type = 'rcunit'
    lobj.save()

    obj =recycle_unit()
    obj.unit_name = var1
    obj.place = var2
    obj.district = var3
    obj.post = var4
    obj.pin = var5
    obj.email_id = var6
    obj.phone_number = var7


    obj.LOGIN_id = lobj.id
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/addrcunitp/'</script>''')


# Edit Recycle Unit

def editdept(request,erc):
    res = recycle_unit.objects.get(id=erc)
    return render(request, 'recycleunit/edit_recycle_unit.html', {'data':res})

def editdeptp (request):

    var1 = request.POST['name']
    var2 = request.POST['place']
    var3 = request.POST['dist']
    var4 = request.POST['post']
    var5 = request.POST['pi']
    var6 = request.POST['email']
    var7 = request.POST['phno']

    ed =request.POST['ercu']

    obj= recycle_unit.objects.get(id=ed)
    obj.unit_name = var1
    obj.place = var2
    obj.district = var3
    obj.post = var4
    obj.pin = var5
    obj.email_id = var6
    obj.phone_number = var7

    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/editrcunitp/'</script>''')


# Delete Recycle Unit

def deletedept(request,drcu):
    res = recycle_unit.objects.get(id=drcu).delete()
    return redirect('/myapp/viewrcunit')

#Recycle Unit View Profile

def rcunit_profile_view(request):
    res = recycle_unit.objects.get(LOGIN_id  =request.session['lid'])
    return render(request, 'recycleunit/rcunit_profile_view.html',{'data':res})



# . Add Product

def add_productg(request):
    res = product.objects.all()
    re = recycle_unit.objects.all()
    return render(request,'recycleunit/add_product.html', {'data':res,'data2':re})

def add_productp(request):
    num1 = request.POST['pname']
    num2 = request.POST['amount']

    num3 = request.POST['rcid']

    obj = product()
    obj.product_name = num1
    obj.amount = num2
    obj.RECYCLE_UNIT_id = num3
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/addproductp/'</script>''')

# View Product

def view_productrcunit(request):
    res = product.objects.all()
    return render(request, 'recycleunit/view_product.html',{'data':res})



# Edit Product

def edit_productg(request,epd):
    res = product.objects.get(id=epd)
    re = recycle_unit.objects.all()
    return render(request,'recycleunit/edit_product.html',{'data':res, 'data2':re})

def edit_productp (request):
    num1 = request.POST['pname']
    num2 = request.POST['amount']

    num3 = request.POST['rcid']


    ed =request.POST['eproduct']

    obj= product.objects.get(id=ed)
    obj.product_name = num1
    obj.amount = num2
    obj.RECYCLE_UNIT_id = num3
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/editproductp/'</script>''')

# Delete

def delete_product(request,dpd):
    res = product.objects.get(id=dpd).delete()
    return redirect('/myapp/viewproduct')


#Add Order Main

def add_omaing(request):
    r = order_main.objects.all()
    re = product.objects.all()
    res = user.objects.all()
    return render(request,'recycleunit/add_order_main.html', {'data':r,'data2':re,'data3':res})

def add_omainp(request):
    num1 = request.POST['date']

    num2 = request.POST['pid']
    num3 = request.POST['uid']

    obj = order_main()
    obj.order_date = num1
    obj.PRODUCT_id= num2
    obj.USER_id = num3
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/addomainp/'</script>''')

# View Order Main

def view_omain(request):
    res = order_main.objects.all()
    return render(request, 'recycleunit/view_order_main.html',{'data':res})

# Edit Order Main

def edit_omaing(request,ect):
    r = order_main.objects.get(id=ect)
    re = product.objects.all()
    res = user.objects.all()
    return render(request,'recycleunit/edit_order_main.html',{'data':r, 'data2':re,'data3':res})

def edit_omainp(request):
    ed =request.POST['ecart']

    num1 = request.POST['date']

    num2 = request.POST['pid']
    num3 = request.POST['uid']

    obj= order_main.objects.get(id=ed)
    obj.order_date = num1
    obj.PRODUCT_id = num2
    obj.USER_id = num3
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/editomainp/'</script>''')


# Delete

def delete_omain(request,dct):
    res = order_main.objects.get(id=dct).delete()
    return redirect('/myapp/viewomain')


#Add Order Sub

def add_osubg(request):
    r = order_sub.objects.all()
    re = order_main.objects.all()
    return render(request,'recycleunit/add_order_sub.html', {'data':r,'data2':re})

def add_osubp(request):
    num1 = request.POST['omain']

    num2 = request.POST['amt']

    obj = order_sub()
    obj.ORDER_MAIN_id = num1
    obj.amount= num2
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/addosubp/'</script>''')

# View Order Sub

def view_osub(request):
    res = order_sub.objects.all()
    return render(request, 'recycleunit/view_order_sub.html',{'data':res})

# Edit Order Sub

def edit_osubg(request,ect):
    r = order_sub.objects.get(id=ect)
    re = order_main.objects.all()
    return render(request,'recycleunit/edit_order_sub.html',{'data':r, 'data2':re})

def edit_osubp(request):
    ed =request.POST['ecart']

    num1 = request.POST['omain']

    num2 = request.POST['amt']

    obj= order_sub.objects.get(id=ed)
    obj.ORDER_MAIN_id = num1
    obj.amount = num2
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");windows.location='/myapp/editosubp/'</script>''')


# Delete

def delete_osub(request,dct):
    res = order_sub.objects.get(id=dct).delete()
    return redirect('/myapp/viewosub')





# SEARCH



#Admin Search
def search_recycle_unit(request):
    fdate = request.POST['search1']
    tdate = request.POST['search2']
    res = recycle_unit.objects.filter(date__range=[fdate,tdate])
    return render(request, 'admin/view_recycle_unit.html', {'data':res})


def search_users(request):
    fdate = request.POST['search1']
    tdate = request.POST['search2']
    res = user.objects.filter(date__range=[fdate,tdate])
    return render(request, 'admin/view_users.html', {'data':res})


def search_complaints(request):
    fdate = request.POST['search1']
    tdate = request.POST['search2']
    res = complaint.objects.filter(date__range=[fdate,tdate])
    return render(request, 'admin/view_complaint.html', {'data':res})


def search_feedback(request):
    fdate = request.POST['search1']
    tdate = request.POST['search2']
    res = feedback.objects.filter(date__range=[fdate,tdate])
    return render(request, 'admin/view_complaint.html', {'data':res})



#Search Recycle Unit
def search_product(request):
    fdate = request.POST['search1']
    tdate = request.POST['search2']
    res = product.objects.filter(date__range=[fdate,tdate])
    return render(request, 'recycleunit/view_product.html', {'data':res})


def search_ordermain(request):
    fdate = request.POST['search1']
    tdate = request.POST['search2']
    res = order_main.objects.filter(date__range=[fdate,tdate])
    return render(request, 'recycleunit/view_order_main.html', {'data':res})


#Search Users

def search_payment(request):
    fdate = request.POST['search1']
    tdate = request.POST['search2']
    res = payment.objects.filter(date__range=[fdate,tdate])
    return render(request, 'user/view_payment.html', {'data':res})

def search_reply(request):
    fdate = request.POST['search1']
    tdate = request.POST['search2']
    res = complaint.objects.filter(date__range=[fdate,tdate])
    return render(request, 'user/view_reply.html', {'data':res})

def search_notification(request):
    fdate = request.POST['search1']
    tdate = request.POST['search2']
    res = notifications.objects.filter(date__range=[fdate,tdate])
    return render(request, 'user/view_notification_user.html', {'data':res})



#Search Workers

def search_user_request_update(request):
    fdate = request.POST['search1']
    tdate = request.POST['search2']
    res = waste_request.objects.filter(date__range=[fdate,tdate])
    return render(request, 'worker/view_user_request_update.html', {'data':res})


def search_allocated_area(request):
    fdate = request.POST['search1']
    tdate = request.POST['search2']
    res = allocation.objects.filter(date__range=[fdate,tdate])
    return render(request, 'worker/view_allocated_area.html', {'data':res})






