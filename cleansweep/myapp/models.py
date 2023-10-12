from django.db import models

class login(models.Model):
    username = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default="")
    type = models.CharField(max_length=100, default="")

class recycle_unit(models.Model):
    unit_name = models.CharField(max_length=100, default="")
    place = models.CharField(max_length=100, default="")
    post = models.CharField(max_length=100, default="")
    pin = models.CharField(max_length=100, default="")
    district = models.CharField(max_length=100, default="")
    phone_number = models.CharField(max_length=100, default="")
    email_id = models.CharField(max_length=100, default="")
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE, default=2)

class waste(models.Model):
    type = models.CharField(max_length=100, default="")
    rate = models.CharField(max_length=100, default="")

class worker(models.Model):
    name = models.CharField(max_length=100, default="")
    phone_number = models.CharField(max_length=100, default="")
    gender = models.CharField(max_length=100, default="")
    qualification = models.CharField(max_length=100, default="")
    dob = models.CharField(max_length=100, default="")
    place = models.CharField(max_length=100, default="")
    post = models.CharField(max_length=100, default="")
    pin = models.CharField(max_length=100, default="")
    district = models.CharField(max_length=100, default="")
    email_id = models.CharField(max_length=100, default="")
    photo = models.CharField(max_length=100, default="")
    id_proof = models.CharField(max_length=100, default="")
    status = models.CharField(max_length=100, default="pending")
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE, default=4)

class notifications(models.Model):
    date = models.CharField(max_length=100, default="")
    notification = models.CharField(max_length=100, default="")

class allocation(models.Model):
    WORKER = models.ForeignKey(worker, on_delete=models.CASCADE, default=4)
    area = models.CharField(max_length=100, default="")
    date = models.CharField(max_length=100, default="")
    status = models.CharField(max_length=100, default="pending")

class user(models.Model):
    name = models.CharField(max_length=100, default="")
    phone_number = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    place = models.CharField(max_length=100, default="")
    post = models.CharField(max_length=100, default="")
    pin = models.CharField(max_length=100, default="")
    district = models.CharField(max_length=100, default="")
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE, default=4)


class complaint(models.Model):
    date = models.CharField(max_length=100, default="")
    complaint = models.CharField(max_length=100, default="")
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=4)
    reply = models.CharField(max_length=100, default="")
    status = models.CharField(max_length=100, default="")

class category(models.Model):
    category_name = models.CharField(max_length=100, default="")
    WORKER = models.ForeignKey(worker, on_delete=models.CASCADE, default=4)

class feedback(models.Model):
    date = models.CharField(max_length=100, default="")
    feedback = models.CharField(max_length=100, default="")
    status = models.CharField(max_length=100, default="pending")
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=4)

class pickup(models.Model):
    name = models.CharField(max_length=100, default="")
    phone_number = models.CharField(max_length=100, default="")
    id_proof = models.CharField(max_length=100, default="")
    qualification = models.CharField(max_length=100, default="")
    experiance = models.CharField(max_length=100, default="")
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE, default=4)

class waste_request(models.Model):
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=4)
    status = models.CharField(max_length=100, default="pending")
    request = models.CharField(max_length=100, default="")

class product(models.Model):
    product_name = models.CharField(max_length=100, default="")
    amount = models.CharField(max_length=100, default="")
    RECYCLE_UNIT = models.ForeignKey(recycle_unit, on_delete=models.CASCADE, default=4)

class cart(models.Model):
    PRODUCT = models.ForeignKey(product, on_delete=models.CASCADE, default=4)
    date = models.CharField(max_length=100, default="")
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)


class order_main(models.Model):
    PRODUCT = models.ForeignKey(product, on_delete=models.CASCADE, default=4)
    order_date = models.CharField(max_length=100, default="")
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=4)


class order_sub(models.Model):
    ORDER_MAIN = models.ForeignKey(order_main, on_delete=models.CASCADE, default=4)
    amount = models.CharField(max_length=100, default="")


class payment(models.Model):
    date = models.CharField(max_length=100, default="")
    amount = models.CharField(max_length=100, default="")
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=4)
    ORDERMAIN = models.ForeignKey(order_main, on_delete=models.CASCADE, default=1)






