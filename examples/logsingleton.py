import logging.config
from pathlib import Path

this_dir = Path(__file__).parent

class LogHub:
    _instance = None

    @staticmethod
    def get_logger():
        if LogHub._instance is None:
            config_path = this_dir / 'logging.conf'
            if not config_path.exists():
                raise FileNotFoundError(f"Logging configuration file not found: {config_path}")
            logging.config.fileConfig(config_path)
            LogHub._instance = logging.getLogger("sampleLogger")
        return LogHub._instance

if __name__ == "__main__":
    logger = LogHub.get_logger()
    logger.info("This is an info message from LogHub singleton.")
    logger.debug("This is a debug message from LogHub singleton.")
    logger.error("This is an error message from LogHub singleton.")