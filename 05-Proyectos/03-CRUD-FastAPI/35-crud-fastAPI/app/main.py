from fastapi import FastAPI, Depends, HTTPException, Path
from sqlalchemy.orm import Session
import crud
import schemas
from database import SeccionmLocal


app = FastAPI()


def get_db():
    db = SeccionmLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/productos", response_model=list[schemas.ProductoResponse])
def listar_productos(db: Session = Depends(get_db)):
    return crud.obtener_productos(db)

@app.post("/productos", response_model=schemas.ProductoResponse)
def agregar_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.crear_producto(db, producto)

@app.get("/productos/{producto_id}", response_model=schemas.ProductoResponse)
def obtener_un_producto(producto_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    producto = crud.obtener_producto(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@app.put("/productos/{producto_id}", response_model=schemas.ProductoResponse)
def actualizar_producto(
    producto_id: int = Path(..., gt=0),
    datos: schemas.ProductoUpdate = None,
    db: Session = Depends(get_db)
):
    producto = crud.actualizar_producto(db, producto_id, datos)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    resultado = crud.eliminar_producto(db, producto_id)
    if not resultado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": "Producto eliminado correctamente"}

# ===== ENDPOINTS CATEGORIAS =====

@app.post("/categorias", response_model=schemas.CategoriaResponse)
def crear_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    return crud.crear_categoria(db, categoria)

@app.get("/categorias", response_model=list[schemas.CategoriaResponse])
def listar_categorias(db: Session = Depends(get_db)):
    return crud.obtener_categorias(db)

@app.get("/categorias/{categoria_id}", response_model=schemas.CategoriaResponse)
def obtener_una_categoria(categoria_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    categoria = crud.obtener_categoria(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

# ===== ENDPOINTS USUARIOS =====

@app.post("/usuarios", response_model=schemas.UsuarioResponse)
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return crud.crear_usuario(db, usuario)

@app.get("/usuarios", response_model=list[schemas.UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return crud.obtener_usuarios(db)

@app.get("/usuarios/{usuario_id}", response_model=schemas.UsuarioResponse)
def obtener_un_usuario(usuario_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    usuario = crud.obtener_usuario(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario