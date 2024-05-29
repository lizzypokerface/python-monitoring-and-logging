import logging

# It's a good practice to use a module-level logger.
# If a logger with the given name already exists, getLogger will return it.
# Otherwise, it will create a new one.
logger = logging.getLogger(__name__)

# Configuring the logging system to display messages of level DEBUG and higher.
# The format specifies how the log messages should be displayed.
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")

# Demonstrating different logging levels:
logger.debug(
    "This is a debug message"
)  # Detailed information, typically of interest only when diagnosing problems.
logger.info(
    "This is an info message"
)  # Confirmation that things are working as expected.
logger.warning(
    "This is a warning message"
)  # An indication that something unexpected happened, or indicative of some problem in the near future.
logger.error(
    "This is an error message"
)  # Due to a more serious problem, the software has not been able to perform some function.
logger.critical(
    "This is a critical message"
)  # A very serious error, indicating that the program itself may be unable to continue running.

# Logging variables with a debug message
x = 2
y = "hello world"
logger.debug(f"The value of x is {x} and the value of y is {y}")

# Logging exceptions
try:
    1 / 0
except ZeroDivisionError as e:
    logger.exception(
        "An exception occurred: ZeroDivisionError"
    )  # Logs the exception with traceback

# Creating a custom logger
custom_logger = logging.getLogger("custom-logger")

# Using Handlers and Formatters to send logs to a file
file_handler = logging.FileHandler(
    "test.log"
)  # Creating a file handler to write log messages to a file
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)  # Defining a custom log message format
file_handler.setFormatter(formatter)  # Setting the formatter for the file handler
custom_logger.addHandler(file_handler)  # Adding the file handler to the custom logger
custom_logger.info("This log message is sent to the file")
