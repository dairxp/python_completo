from pydantic import BaseModel
from typing import Optional

# ===== SCHEMAS DE PRODUCTO =====

class ProductoBase(BaseModel):
    """Base con campos comunes"""
    nombre: str
    precio: float
    en_stock: bool = True
    categorias_id: int

class ProductoCreate(ProductoBase):
    """Para CREAR producto"""
    pass

class ProductoUpdate(BaseModel):
    """Para ACTUALIZAR producto (todos opcionales)"""
    nombre: Optional[str] = None
    precio: Optional[float] = None
    en_stock: Optional[bool] = None
    categorias_id: Optional[int] = None

class ProductoResponse(ProductoBase):
    """Para RESPONDER producto (desde BD)"""
    id: int
    
    class Config:
        from_attributes = True

# ===== SCHEMAS DE CATEGORIA =====

class CategoriaBase(BaseModel):
    nombre: str

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaResponse(CategoriaBase):
    id: int
    
    class Config:
        from_attributes = True

# ===== SCHEMAS DE USUARIO =====

class UsuarioBase(BaseModel):
    nombre: str
    email: str

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioResponse(UsuarioBase):
    id: int
    
    class Config:
        from_attributes = True