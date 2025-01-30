from pydantic import BaseModel


class Empresa(BaseModel):
    nombre_empresa: str
    region_matriz: str
    rut_empresa: str
    regiones_opera: list[str] | None = None


class VentasImpuestos(BaseModel):
    ventas: int
    exportaciones: int
    importaciones: int
    primera_cat: int
    iva: int
    otros_impuestos: int


class ProveedoresBienes(BaseModel):
    num_proveedores_bienes: int
    insumos: list[str] | None = None
    gasto_total_bienes: int
    num_local_bienes: int
    gasto_local_bienes: int
    num_proveedores_internacional_bienes: int
    gasto_internacional_bienes: int


class ProveedoresServicios(BaseModel):
    num_proveedores_servicios: int
    servicios: list[str] | None = None
    gasto_total_servicios: int
    num_local_servicios: int
    gasto_local_servicios: int
    num_proveedores_internacional_servicios: int
    gasto_internacional_servicios: int


class GastoInversionPersonas(BaseModel):
    remuneraciones_brutas: int
    num_empleados_permanentes: int
    num_empleados_esporadicos: int
    inversion_comunidades: int
    inversion_ambiental: int


class DataAnual(BaseModel):
    agno: int
    empresa: Empresa
    ventas_impuestos: VentasImpuestos
    proveedores_bienes: ProveedoresBienes
    proveedores_servicios: ProveedoresServicios
    gasto_inversion_personas: GastoInversionPersonas

    def flat_numeric_dump(self):
        result = {"agno": self.agno}
        result = result | self.ventas_impuestos.model_dump()
        result = result | self.proveedores_bienes.model_dump()
        result = result | self.proveedores_servicios.model_dump()
        result = result | self.gasto_inversion_personas.model_dump()
        return result

