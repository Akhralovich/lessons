"""
Создать генератор и/или итератор простой геометрической прогрессии.
"""
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def my_generator(power: int, limit: int):
    for current in range(1, limit + 1):
        yield current * power


if __name__ == "__main__":
    my_geo = my_generator(power=2, limit=5)
    logger.info(next(my_geo))
    logger.info(next(my_geo))
    logger.info(next(my_geo))
    for item in my_geo:
        logger.info(item)