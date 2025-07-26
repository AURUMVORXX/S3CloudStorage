import uvicorn
from loguru import logger
from fastapi import FastAPI

class APIService:

    def __init__(self):
        self._app = FastAPI()

    async def serve(self):
        '''
            Запуск Uvicorn сервера в действующем asyncio цикле
        '''
        #TODO: Вынести настройки в env файл
        config = uvicorn.Config(self._app,
                                host = '0.0.0.0',
                                port = 8080,
                                loop = 'asyncio',
                                log_level = 'warning')
        server = uvicorn.Server(config)
        logger.info('API сервис успешно запущен')
        await server.serve()
        
