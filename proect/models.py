from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Klass(models.Model):
    nomi=models.CharField(max_length=150)
    narxi=models.PositiveIntegerField()

    def __str__(self):
        return self.nomi

class Mehmonxona(models.Model):
    nomi=models.CharField(max_length=150)
    yulduzlar_soni=models.DecimalField( max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(5)] )
    narxi=models.PositiveIntegerField()

    def __str__(self):
        return self.nomi

class Travel(models.Model):
    nomi=models.CharField(max_length=150)
    izoh=models.TextField()
    muddati=models.DateField()
    narxi=models.PositiveIntegerField()
    klass=models.ForeignKey(Klass,on_delete=models.CASCADE)
    mexmonxona=models.ForeignKey(Mehmonxona,on_delete=models.CASCADE)

    def __str__(self):
        return self.nomi