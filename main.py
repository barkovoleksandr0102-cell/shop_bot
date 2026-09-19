# asyncio
import asyncio

# logs
import logging

# loader

from loader import main


logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    asyncio.run(main())