from rest_framework import serializers
from SpaWebApi.models import Cliente, Empleado, Sucursales, Cita, Genero, Tratamiento, TipoTratamiento, CitaEmpleado, Alergias, AlergiasCliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'id_cliente','nombre', 'apellido', 'direccion', 'telefono', 'fecha_nacimiento', 'email', 'id_genero')


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('id', 'id_empleado','nombre', 'apellido', 'direccion', 'telefono', 'especialidad', 'email', 'id_genero','id_tratamiento')

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('id', 'id_empleado','id_cliente','id_Sucursales','fecha', 'hora', 'sucursal')
        
class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursales
        fields = ('id', 'direccion')
        
class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ('id', 'descripcion')
        
class AlergiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alergias
        fields = ('id', 'descripcion')
        
class AlergiasClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlergiasCliente
        fields = ('id', 'id_alergia','id_cliente','descripcion')
        
class TratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = ('id', 'descripcion')
        
class TipoTratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTratamiento
        fields = ('id','id_Tratamiento', 'descripcion')
        
class CitaEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitaEmpleado
        fields = ('id','id_empleado', 'id_cita')