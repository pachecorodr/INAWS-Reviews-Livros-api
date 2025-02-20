from fastapi import APIRouter, HTTPException, Request, Query
from fastapi.responses import JSONResponse

from src.controllers.http_types.http_request import HttpRequest

from src.main.composer.criar_livro_composer import criar_livro_composer
from src.main.composer.listar_todos_composer import listar_todos_composer
from src.main.composer.atualizar_nota_composer import atualizar_nota_composer
from src.main.composer.deletar_livro_composer import deletar_livro_composer

router = APIRouter(
    prefix="/livros",
    tags=["livros"],
    responses={
        200: {"description": "OK"},
        201: {"description": "Created"},
        204: {"description": "No Content"},
        400: {"description": "Bad Request"},
        404: {"description": "Not found"},
        422: {"description": "Unprocessable Entity"},
        500: {"description": "Internal Server Error"}}
)

@router.post("/novo/")
async def criar_lembrete(request: Request):
    try:
        body = await request.json()
        
        http_request = HttpRequest(body)
        controller = criar_livro_composer()
        http_respose = controller.handle(http_request)
        return JSONResponse(status_code=http_respose.status_code, content=http_respose.body)
    
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/")
async def listar_todos_livros():
    try:
        http_request = HttpRequest()
        controller = listar_todos_composer()
        http_respose = controller.handle(http_request)
        return JSONResponse(status_code=http_respose.status_code, content=http_respose.body)
    
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{id}")
async def atualizar_lembrete(id: int, nota: int = Query (le = 5, ge= 0, description="A nota para o livro")):
    try:
        
        http_request = HttpRequest(param={"id": id, "nota": nota})
        controller = atualizar_nota_composer()
        http_respose = controller.handle(http_request)
        return JSONResponse(status_code=http_respose.status_code, content=http_respose.body)
    
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/{id}")
async def deletar_lembrete(id: int):
    try:
        http_request = HttpRequest(param={"id": id})
        controller = deletar_livro_composer()
        http_respose = controller.handle(http_request)
        return JSONResponse(status_code=http_respose.status_code, content=http_respose.body)
    
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
