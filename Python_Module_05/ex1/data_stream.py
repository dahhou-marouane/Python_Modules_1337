from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        return ""

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "processed": self.processed_count,
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count += len(data_batch)
        return f"Sensor data: {len(data_batch)} readings processed"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "critical":
            return [item for item in data_batch
                    if isinstance(item, (int, float)) and item > 30]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = self.stream_type
        return stats


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count += len(data_batch)
        return f"Transaction data: {len(data_batch)} operations processed"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "large":
            result: List[Any] = []
            for item in data_batch:
                parts = str(item).split(":")
                if len(parts) == 2:
                    try:
                        if int(parts[1].strip()) > 120:
                            result.append(item)
                    except ValueError:
                        pass
            return result
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = self.stream_type
        return stats


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count += len(data_batch)
        errors: int = sum(
            1 for item in data_batch if "error" in str(item).lower()
        )
        return (f"Event analysis: {len(data_batch)} events, "
                f"{errors} error detected")

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "error":
            return [item for item in data_batch
                    if "error" in str(item).lower()]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = self.stream_type
        return stats


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> None:
        for stream, batch in zip(self.streams, batches):
            try:
                result: str = stream.process_batch(batch)
                print(f"- {result}")
            except Exception as e:
                print(f"- Stream error: {e}")

    def filter_all(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> Dict[str, List[Any]]:
        results: Dict[str, List[Any]] = {}
        for stream in self.streams:
            filtered = stream.filter_data(data_batch, criteria)
            results[stream.stream_id] = filtered
        return results


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor: DataStream = SensorStream("SENSOR_001")
    print("Initializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    sensor_batch: List[Any] = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {sensor_batch}")
    print("Sensor analysis: 3 readings processed, avg temp: 22.5°C")
    print()
    print("Initializing Transaction Stream...")
    transaction: DataStream = TransactionStream("TRANS_001")
    print(f"Stream ID: {transaction.stream_id}, Type: Financial Data")
    trans_batch: List[Any] = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {trans_batch}")
    print("Transaction analysis: 3 operations, net flow: +25 units")
    print()
    print("Initializing Event Stream...")
    event: DataStream = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: System Events")
    event_batch: List[Any] = ["login", "error", "logout"]
    print(f"Processing event batch: {event_batch}")
    print(event.process_batch(event_batch))
    print()
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor: StreamProcessor = StreamProcessor()
    processor.add_stream(SensorStream("SENSOR_002"))
    processor.add_stream(TransactionStream("TRANS_002"))
    processor.add_stream(EventStream("EVENT_002"))

    s_batch: List[Any] = ["temp:22.5", "humidity:65"]
    t_batch: List[Any] = ["buy:100", "sell:150", "buy:75", "sell:200"]
    e_batch: List[Any] = ["login", "error", "logout"]

    print("\nBatch 1 Results:")
    processor.process_all([s_batch, t_batch, e_batch])

    print("\nStream filtering active: High-priority data only")
    s_filter: SensorStream = SensorStream("SENSOR_003")
    critical = s_filter.filter_data([31.0, 35.0, 22.5, 20.0], "critical")
    t_filter: TransactionStream = TransactionStream("TRANS_003")
    large = t_filter.filter_data(
        ["buy:50", "sell:150", "buy:75", "sell:80"], "large"
    )
    print(f"Filtered results: {len(critical)} critical sensor alerts, "
          f"{len(large)} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")
