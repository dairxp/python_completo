from sqlalchemy.orm import Session
import models
import schemas


def crear_producto(db: Session, producto: schemas.ProductoCreate) -> models.Producto:
    db_producto = models.Producto(
        nombre=producto.nombre,
        precio=producto.precio,
        en_stock=producto.en_stock,
        categorias_id=producto.categorias_id
    )
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def obtener_producto(db: Session, producto_id: int) -> models.Producto:
    return db.query(models.Producto).filter(models.Producto.id == producto_id).first()

def obtener_productos(db: Session, skip: int = 0, limit: int = 10) -> list:
    return db.query(models.Producto).offset(skip).limit(limit).all()

def actualizar_producto(
    db: Session, 
    producto_id: int, 
    producto_update: schemas.ProductoUpdate
) -> models.Producto:
    db_producto = db.query(models.Producto).filter(models.Producto.id == producto_id).first()
    
    if not db_producto:
        return None
    
    # Actualizar solo los campos que no son None
    if producto_update.nombre is not None:
        db_producto.nombre = producto_update.nombre
    if producto_update.precio is not None:
        db_producto.precio = producto_update.precio
    if producto_update.en_stock is not None:
        db_producto.en_stock = producto_update.en_stock
    if producto_update.categorias_id is not None:
        db_producto.categorias_id = producto_update.categorias_id
    
    db.commit()
    db.refresh(db_producto)
    return db_producto

def eliminar_producto(db: Session, producto_id: int) -> bool:
    db_producto = db.query(models.Producto).filter(models.Producto.id == producto_id).first()
    
    if not db_producto:
        return False
    
    db.delete(db_producto)
    db.commit()
    return True

# ===== OPERACIONES CRUD CATEGORIA =====

def crear_categoria(db: Session, categoria: schemas.CategoriaCreate) -> models.Categoria:
    db_categoria = models.Categoria(nombre=categoria.nombre)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def obtener_categoria(db: Session, categoria_id: int) -> models.Categoria:
    return db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()

def obtener_categorias(db: Session) -> list:
    return db.query(models.Categoria).all()

# ===== OPERACIONES CRUD USUARIO =====

def crear_usuario(db: Session, usuario: schemas.UsuarioCreate) -> models.Usuario:
    """Crear un nuevo usuario"""
    db_usuario = models.Usuario(
        nombre=usuario.nombre,
        email=usuario.email,
        hashed_password=usuario.password  # Aquí deberías hashear la contraseña
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def obtener_usuario(db: Session, usuario_id: int) -> models.Usuario:
    return db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()

def obtener_usuarios(db: Session) -> list:
    return db.query(models.Usuario).all()
