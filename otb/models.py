from django.db import models

# # Create your models here.


# class Ejecutivo(models.Model):
#     n_usuario     = models.CharField(max_length=20)
#     contrasena  = models.CharField(max_length=15)
#     def __str__(self):
#         return str(self.n_usuario)
    

# class Genero(models.Model):
#     id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
#     genero     = models.CharField(max_length=20, blank=False, null=False)

#     def __str__(self):
#         return str(self.genero)
    

class Cliente(models.Model):
    rut     = models.CharField(primary_key=True, max_length=10)
    nombre  = models.CharField(max_length=30)
    aPaterno = models.CharField(max_length=30)
    aMaterno = models.CharField(max_length=30)
    fono      = models.IntegerField()
    edad     = models.IntegerField()
    deposito = models.IntegerField()
    email    = models.EmailField(unique=True, max_length=100, blank=True, null=True) 

    # USERNAME_FIELD = 'nombre'+'aPaterno'
    # REQUIRED_FIELDS =[]

#     def __str__(self):
#         return str(self.nombre)+" "+(self.aPaterno)
    
# class Reserva(models.Model):
#     id_reserva = models.IntegerField(primary_key=True)
#     e_reserva = models.CharField(default=" ",max_length=20)
#     rut = models.ForeignKey('Cliente',on_delete=models.CASCADE, related_name='rut_reserva_set', null=True)
#     nombre = models.ForeignKey('Cliente',on_delete=models.CASCADE, related_name='nombre_reserva_set', null=True)

#     def __str__(self):
#         return str(self.nombre)

