from django.urls import path
from myapp import views


urlpatterns = [

    path('achange/', views.admin_changepassword),
    path('acp/', views.admin_changepasswordp),

    path('pchange/', views.pickup_changepassword),
    path('pcp/', views.pickup_changepasswordp),

    path('changepasswordr/', views.rcunit_changepassword),
    path('rcp/', views.rcunit_changepasswordp),

    path('changepasswordu/', views.user_changepassword),
    path('ucp/', views.user_changepasswordp),

    path('changepasswordw/', views.worker_changepassword),
    path('wcp/', views.worker_changepasswordp),




    path('login/', views.loging),
    path('loginp/', views.loginp),

    # PAGES
    path('adminpage/', views.admin_page),
    path('rcunithpage/', views.rcunit_page),
    path('userhpage/', views.user_page),
    path('pickuphpage/', views.pickup_page),
    path('workerhpage/', views.worker_page),

    #      MODULE 1
     #      ADMIN

    #Recycle Unit
    path('viewrcunit/', views.view_rcunit),


    #Waste
    path('addwaste/', views.add_wasteg),
    path('addwastep/', views.add_wastep),
    path('viewwaste/', views.view_waste),

    # Edit
    path('editwasteg/<str:ew>', views.edit_wasteg),
    path('editwastep/', views.edit_wastep),
    path('deletewaste/<str:dw>', views.delete_waste),


    #Noti
    path('addnotifi/', views.add_notifig),
    path('addnotifip/', views.add_notifip),
    path('viewnotifi/', views.view_notifi),

    # Edit Worker
    path('editnotifi/<str:enf>', views.edit_notifig),
    path('editnotifip/', views.edit_notifip),
    path('deletenotifi/<str:dnf>', views.delete_notifi),


    #Work Allocation
    path('addwalloc/', views.add_worker_allocg),
    path('addwallocp/', views.add_worker_allocp),
    path('viewwalloc/', views.view_worker_alloc),

    # Edit Worker Allocation
    path('editwalloc/<str:ewa>', views.edit_worker_allocg),
    path('editwallocp/', views.edit_worker_allocp),
    path('deletewalloc/<str:dwa>', views.delete_work_alloc),

    # View User
    path('viewuseradmin/', views.view_user_admin),


    # view Complaint by Admin
    path('viewcomplaint/', views.view_complaint),
    # Sent Reply
    path('sentreply/<str:id>', views.sent_replyg),
    path('sentreplyp/', views.sent_replyp),


    # Category Management
    path('addcat/', views.add_categoryg),
    path('addcatp/', views.add_categoryp),
    path('viewcat/', views.view_category),

    # Edit User
    path('editcat/<str:ecat>', views.edit_categoryg),
    path('editcatp/', views.edit_categoryp),
    path('deletecat/<str:dcat>', views.delete_category),

    #View Feedback of User
    path('viewfeedback/', views.view_feedback),


    #      MODULE 2
    #      PICKUP

    # Category Management
    path('addpickup/', views.add_pickupg),
    path('addpickupp/', views.add_pickupp),
    path('viewpickup/', views.view_pickup),

    # Edit User
    path('editpickup/<str:ep>', views.edit_pickupg),
    path('editpickupp/', views.edit_pickupp),
    path('deletepickup/<str:dp>', views.delete_pickup),

    # View Profile of Pickup
    path('pickupview/', views.pickup_profile_view),


    # USER WASTE REQUEST AND COLLECT
    path('addrequest/', views.add_requestg),
    path('addrequestp/', views.add_requestp),
    path('viewrequest/', views.view_request),

    # Edit User
    path('editrequest/<str:er>', views.edit_requestg),
    path('editrequestp/', views.edit_requestp),
    path('deleterequest/<str:dr>', views.delete_request),



    #      MODULE 3
    #      WORKER

    # Worker
    path('addworker/', views.add_workerg),
    path('addworkerp/', views.add_workerp),
    path('viewworker/', views.view_worker),

    # Edit Worker
    path('editworkerg/<str:ewr>', views.edit_workerg),
    path('editworkerp/', views.edit_workerp),
    path('deleteworker/<str:dwkr>', views.delete_worker),

    # View Profile of Worker
    path('workerview/', views.worker_profile_view),

    # View User Request And Update Status
    path('viewuserrequest/', views.view_user_request_update),
    # Approve Reject by Worker
    path('approve/<str:id>', views.approve),
    path('reject/<str:id>', views.reject),

    # View Allocated Area
    path('viewallocatedarea/', views.view_allocated_area),



    #      MODULE 4
    #      USER

    # Add/REGISTER User
    path('adduser/', views.add_userg),
    path('adduserp/', views.add_userp),
    path('viewuser/', views.view_user),

    # Edit User
    path('edituser/<str:eu>', views.edit_userg),
    path('edituserp/', views.edit_userp),
    path('deleteuser/<str:du>', views.delete_user),

    # View Profile of User
    path('userview/', views.view_profile_user),


    # Sent Complaint By User
    path('sentcomplaint/', views.sent_complaintg),
    path('sentcomplaintp/', views.sent_complaintp),

    # view Complaint By User
    path('viewreplyuser/', views.view_reply_user),


    # Feedback
    path('addfeedback/', views.add_feedbackg),
    path('addfeedbackp/', views.add_feedbackp),
    path('viewfeedbackuser/', views.view_feedback_user),

    # Edit
    path('editfeedback/<str:ef>', views.edit_feedbackg),
    path('editfeedbackp/', views.edit_feedbackp),
    path('deletefeedback/<str:df>', views.delete_feedback),


     # View Worker Category
    path('viewcategory/', views.view_worker_category_user),



    # Product
    path('addproduct/', views.add_productg),
    path('addproductp/', views.add_productp),
    path('viewproduct/', views.view_product),

    # Edit
    path('editproduct/<str:epd>', views.edit_productg),
    path('editproductp/', views.edit_productp),
    path('deleteproduct/<str:dpd>', views.delete_product),



    # Cart
    path('addcart/', views.add_cartg),
    path('addcartp/', views.add_cartp),
    path('viewcart/', views.view_cart),

    # Edit
    path('editcart/<str:ect>', views.edit_cartg),
    path('editcartp/', views.edit_cartp),
    path('deletecart/<str:dct>', views.delete_cart),



    # Payment
    path('addpayment/', views.add_paymentg),
    path('addpaymentp/', views.add_paymentp),
    path('viewpayment/', views.view_payment),

    # Edit
    path('editpayment/<str:ept>', views.edit_paymentg),
    path('editpaymentp/', views.edit_paymentp),
    path('deletepayment/<str:dpt>', views.delete_payment),


    #View Worker Notification And Apply
    path('viewnotifiuser/', views.view_notifi_user),



    #      MODULE 5
    #      RECYCLE UNIT

    #  Recycle Unit
    path('addrcunit/', views.add_recylce_unitg),
    path('addrcunitp/', views.add_recylce_unitp),

    # Edit
    path('editrcunitg/<str:erc>', views.editdept),
    path('editrcunitp/', views.editdeptp),
    path('deletedt/<str:drcu>', views.deletedept),


    #RCUNIT Profile View
    path('rcunitview/', views.rcunit_profile_view),

    # View Product
    path('viewproductrcunit/', views.view_productrcunit),

    #  Order Main
    path('addomain/', views.add_omaing),
    path('addomainp/', views.add_omainp),
    path('viewomain/', views.view_omain),

    # Edit
    path('editomain/<str:ect>', views.edit_omaing),
    path('editomainp/', views.edit_omainp),
    path('deleteomain/<str:dct>', views.delete_omain),



    #  Order Sub
    path('addosub/', views.add_osubg),
    path('addosubp/', views.add_osubp),
    path('viewosub/', views.view_osub),

    # Edit
    path('editosub/<str:ect>', views.edit_osubg),
    path('editosubp/', views.edit_osubp),
    path('deleteosub/<str:dct>', views.delete_osub),



    #Admin Searches
    path('svrcunit/', views.search_recycle_unit),
    path('svusers/', views.search_users),
    path('svcomplaints/', views.search_complaints),
    path('svfeedback/', views.search_feedback),


    # Recycle Unit Searches
    path('svproduct/', views.search_product),
    path('svordermain/', views.search_ordermain),


    # User Searches
    path('svpayment/', views.search_payment),
    path('svreply/', views.search_reply),
    path('svnotifi/', views.search_notification),


    # Worker Searches
    path('svuserrequest/', views.search_user_request_update),
    path('svallocatedarea/', views.search_allocated_area),

]