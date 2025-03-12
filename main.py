from src.collect_data import collect_data
from loguru import logger

def main():
    logger.info("Collecting IPCA data...")
    collect_data()
    logger.success("Execution completed!")

if __name__ == "__main__":
    main()
