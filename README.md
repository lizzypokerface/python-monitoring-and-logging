# python-monitoring-and-logging

This project demonstrates the basics of logging in Python, including the use of different logging levels, logging variables, handling exceptions, and configuring log handlers and formatters.

## Requirements

* Python 3.x

## Setup

No additional libraries are required other than the standard Python library.

## Usage

### Basic Logging

The script uses a module-level logger to log messages at different levels:

```python
import logging

# Creating a logger
logger = logging.getLogger(__name__)

# Configuring the logging system
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")

# Logging messages at different levels
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
```

### Logging Variables

The script logs variables within messages to provide more context:

```python
x = 2
y = "hello world"
logger.debug(f"The value of x is {x} and the value of y is {y}")
```

### Logging Exceptions

Exceptions are logged with their tracebacks to help diagnose issues:

```python
try:
    1 / 0
except ZeroDivisionError as e:
    logger.exception("An exception occurred: ZeroDivisionError")
```

### Custom Logger with Handlers and Formatters

The script demonstrates how to create a custom logger that sends logs to a file:

```python
# Creating a custom logger
custom_logger = logging.getLogger("custom-logger")

# Creating a file handler
file_handler = logging.FileHandler("test.log")

# Defining a log message format
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Adding the handler to the custom logger
custom_logger.addHandler(file_handler)

# Logging a message with the custom logger
custom_logger.info("This log message is sent to the file")
```

## Output

```
% python main.py
DEBUG - This is a debug message
INFO - This is an info message
WARNING - This is a warning message
ERROR - This is an error message
CRITICAL - This is a critical message
DEBUG - The value of x is 2 and the value of y is hello world
ERROR - An exception occurred: ZeroDivisionError
Traceback (most recent call last):
  File "/Users/glennlum/Desktop/python-monitoring-and-logging/main.py", line 36, in <module>
    1 / 0
ZeroDivisionError: division by zero
INFO - This log message is sent to the file
```

## Explanation of Concepts

### Logger

A logger is an object used to log messages for a specific part of an application. It can have multiple handlers, which determine where the log messages are sent (e.g., console, file).

### Logging Levels

* **DEBUG:** Detailed information, typically of interest only when diagnosing problems.
* **INFO:** Confirmation that things are working as expected.
* **WARNING:** An indication that something unexpected happened, or indicative of some problem in the near future.
* **ERROR:** Due to a more serious problem, the software has not been able to perform some function.
* **CRITICAL:** A very serious error, indicating that the program itself may be unable to continue running.

### Handlers and Formatters

* **Handler:** Determines where the log messages are sent. Common handlers include `StreamHandler` for console output and `FileHandler` for writing to a file.
* **Formatter:** Defines the layout of the log messages. It can include timestamps, log levels, logger names, and the actual log message.

By following this example, you will understand how to implement logging in your Python applications, making it easier to diagnose and troubleshoot issues.
