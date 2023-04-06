from django.db import models

class Sucursal(models.Model):
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        return self.descripcion
    
class Tratamiento(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion
    
class Genero(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion
    
class Cliente(models.Model):
    id_cliente = models.CharField(max_length=50)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + " " + self.apellido
    
class Empleado(models.Model):
    id_empleado = models.CharField(max_length=50)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    id_especialidad = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + " " + self.apellido

class Alergias(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion
    
    
class AlergiaCliente(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_alergia = models.ForeignKey(Alergias, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_cliente.nombre + " " + self.id_alergia.descripcion    


class TipoTratamiento(models.Model):
    id = models.AutoField(primary_key=True)
    id_tratamiento = models.IntegerField(unique=True)
    seleccionado = models.BooleanField(default=False)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion


class Cita(models.Model):
    id_sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_tipo_tratamiento = models.ForeignKey(TipoTratamiento, on_delete=models.CASCADE)
    hora = models.CharField(max_length=200)
    fecha = models.DateField()
    
    def __str__(self):
        return self.fecha, self.hora

class CitaCliente(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_cita= models.ForeignKey(Cita, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_cliente.nombre + " " + self.id_cita.fecha+ " " + self.id_cita.hora
    
class CitaTipoTratamiento(models.Model):
    id = models.AutoField(primary_key=True)
    id_cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    id_tratamiento = models.IntegerField()
    tratamiento_seleccionado = models.BooleanField()

    def __str__(self):
        return self.tratamiento_seleccionado