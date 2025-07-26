import asyncio
from core.api import APIService

async def main():
    api_service = APIService()
    await api_service.serve()

if __name__ == '__main__':
    asyncio.run(main())
