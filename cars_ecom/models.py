from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Clients(models.Model):
    passport_series = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.PositiveBigIntegerField()
    objects = models.Manager()

    def __str__(self):
        return self.firstname

    @property
    def pay_sum(self):
        a = []
        for item in self.client_items.all():
            total_sum = item.cars.rent_cost * item.days_count
            a.append(total_sum)
        return sum(a)


class Cars(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    rent_cost = models.PositiveIntegerField()
    objects = models.Manager()

    # def __str__(self):
    #     return '{} - model {}'.format(self.brand, self.model)

    def __str__(self):
        return '{}'.format(self.id)

    @property
    def car_count_in_order(self):
        a = []
        for item in self.car_items.all():
            a.append(item.cars)
        return len(a)

    @property
    def total_profit(self):
        a = []
        for item in self.car_items.all():
            a.append(item.days_count)
        return sum(a) * self.rent_cost


class Orders(models.Model):
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name="client_items")
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name="car_items")
    timestamp = models.DateField(auto_now_add=True)
    from_date = models.DateField()
    to_date = models.DateField()
    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.id)

    @property
    def extended_days(self):
        a = []
        for item in self.extend.all():
            a.append(item.extended_to)
        return a

    @property
    def exday(self):
        a = []
        for item in self.extend.all():
            a.append(item.extended_to)
        if len(a) != 0:
            return (a[-1] - self.to_date).days

    @property
    def days_count(self):
        if self.exday is None:
            return (self.to_date - self.from_date).days
        else:
            self.first = (self.to_date - self.from_date).days
            return self.first + self.exday

    @property
    def extend_order_count(self):
        a = []
        for item in self.extend.all():
            a.append(item.order)
        return len(a)


class Extended_orders(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="extend")
    extended_to = models.DateField()
    objects = models.Manager()

    def __str__(self):
        return self.order










