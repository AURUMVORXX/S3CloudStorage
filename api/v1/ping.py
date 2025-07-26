from fastapi import APIRouter

router = APIRouter()

@router.get('/ping', tags = ['Общее'], summary = 'Проверка статуса API сервиса')
async def ping():
    return {'status': True}
