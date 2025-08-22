import os
import sys
import logging

# Logging format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Directory for logs
log_dir = "logs"
log_file = os.path.join(log_dir, "logging.log")

# Ensure log directory exists
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_file),      # Save logs to file
        logging.StreamHandler(sys.stdout)   # Print logs to console
    ]
)

logger = logging.getLogger("datasciencelogger")