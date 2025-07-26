import uvicorn
from loguru import logger
from fastapi import FastAPI

class APIService:

    def __init__(self):
        self._app = FastAPI()
        self._register_routers()

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

    def _register_routers(self):
        from api.v1.ping import router as ping_router

        self._app.include_router(ping_router)
    

        
