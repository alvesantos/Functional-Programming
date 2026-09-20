from enum import Enum
from typing import Any


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


RawCSVData = list[list[object]]
PreparedCSVData = list[list[str]]
CSVStatusResult = tuple[str, PreparedCSVData | str]

# Don't touch above this line


def get_csv_status(status: CSVExportStatus, data: Any) -> CSVStatusResult:
    match status:
        case CSVExportStatus.PENDING:
            return prepare(data)
        case CSVExportStatus.PROCESSING:
            return process(data)
        case CSVExportStatus.SUCCESS:
            return handle_success(data)
        case CSVExportStatus.FAILURE:
            return handle_failure(data)
        case _:
            raise Exception("unknown export status")


def prepare(data: RawCSVData) -> tuple[str, PreparedCSVData]:
    processed_data: PreparedCSVData = list(
        map(lambda lst: list(map(lambda s: str(s), lst)), data)
    )
    return "Pending...", processed_data


def process(prepared_data: PreparedCSVData) -> tuple[str, str]:
    processed_data: str = "\n".join(map(lambda lst: ",".join(lst), prepared_data))
    return "Processing...", processed_data


def handle_success(processed_data: str) -> tuple[str, str]:
    return "Success!", processed_data


def handle_failure(data: RawCSVData) -> tuple[str, str]:
    _, processed_data = process(prepare(data)[1])
    return "Unknown error, retrying...", processed_data
