from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional
del Dict, Union, Optional


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        return ""

    @abstractmethod
    def validate(self, data: Any) -> bool:
        return True

    def format_output(self, result: str) -> str:
        return ""


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError(
                "Invalid list data: expected list of int | float.")
        return (f"Processed {len(data)} numeric values, sum={sum(data)}, "
                f"avg={sum(data) / len(data)}")

    def validate(self, data: Any) -> bool:
        if not isinstance(data, List):
            return False
        for i in data:
            if not isinstance(i, (int, float)):
                return False
        return True

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid text data: expected a string.")
        return (f"Processed text: {len(data)} characters, " +
                f'{len(data.split(" "))} words')

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and len(data.strip()) > 0

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class LogProcessor(DataProcessor):

    LOG_LEVELS: List[str] = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError(
                "Invalid log data: no recognizable log level found."
            )
        detected_level: str = "UNKNOWN"
        for level in self.LOG_LEVELS:
            if level in data.upper():
                detected_level = level
                break
        parts: List[str] = data.split(":", 1)
        message: str = parts[1].strip() if len(parts) > 1 else data
        prefix: str = (
            "[ALERT]"
            if detected_level in ("ERROR", "CRITICAL")
            else f"[{detected_level}]"
        )
        return f"{prefix} {detected_level} level detected: {message}"

    def validate(self, data: Any) -> bool:
        not_in: int = 0
        if not isinstance(data, str):
            return False
        for level in self.LOG_LEVELS:
            if level in data:
                continue
            else:
                not_in += 1
        if not_in == 5:
            return False
        return True

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


def demo_indevidual_Processing() -> None:
    numeric: DataProcessor = NumericProcessor()
    numeric_data: List[int] = [1, 2, 3, 4, 5]
    print("Initializing Numeric Processor...")
    print(f"Processing data: {numeric_data}")
    try:
        if numeric.validate(numeric_data):
            print("Validation: Numeric data verified")
        else:
            raise ValueError("Numeric data invalid")
        result: str = numeric.process(numeric_data)
        print(numeric.format_output(result))
    except ValueError as e:
        print(f"Error: {e}")
    print()

    text: DataProcessor = TextProcessor()
    text_data: str = "Hello Nexus World"
    print("Initializing Text Processor...")
    print(f"Processing data: {text_data}")
    try:
        if text.validate(text_data):
            print("Validation: Text data verified")
        else:
            raise ValueError("Text data invalid")
        result = text.process(text_data)
        print(text.format_output(result))
    except ValueError as e:
        print(f"Error: {e}")
    print()

    log: DataProcessor = LogProcessor()
    log_data: str = "ERROR: Connection timeout"
    print("Initializing Log Processor...")
    print(f"Processing data: {log_data}")
    try:
        if log.validate(log_data):
            print("Validation: Log entry verified")
        else:
            raise ValueError("Log entry invalid")
        result = log.process(log_data)
        print(log.format_output(result))
    except ValueError as e:
        print(f"Error: {e}")
    print()


def demo_multiple_Processing() -> None:
    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]

    data_list: List[Any] = [
        [1, 2, 3],
        "Hello Nexus",
        "INFO: System ready",
    ]

    for i, (processor, data) in enumerate(zip(processors, data_list), 1):
        result: str = processor.process(data)
        print(f"Result {i}: {result}")


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    demo_indevidual_Processing()
    demo_multiple_Processing()
    print("\nFoundation systems online. Nexus ready for advanced streams.")
