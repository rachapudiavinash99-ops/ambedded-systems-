from fastapi import APIRouter
router = APIRouter()

@router.post("/execute")
def execute_test():
    return {"result": "success"}
