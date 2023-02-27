from django.db import models


class Category(models.Model):
    """
    Категории товара
    """
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Good(models.Model):
    """
    Товар
    """
    name = models.CharField(max_length=250, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to='goods', blank=True, null=True, default='goods/default.jpg')

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class Location(models.Model):
    """
    Аптеки
    """
    address = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.address


class Stock(models.Model):
    """
    Остатки
    """
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False)

    def __str__(self):
        return f"{self.location.address} ({self.good.name}) - {self.qty} шт"

