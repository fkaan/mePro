from enum import Enum
SUPPORTTED_FILE_EXTENSIONS = [".csv", ".parquet"]

class DataReadingErrorMessages(Enum):
    INVALID_FILE_PATH_TYPE = "Invalid file path type. Expected a string."
    FILE_NOT_FOUND = "The specified file does not exist."
    UNSUPPORTED_FILE_EXTENSION = (
        f"Unsupported file extension. Supported extensions are: {', '.join(SUPPORTTED_FILE_EXTENSIONS)}"
    )
    DATA_LOAD_ERROR = "An error occurred while loading the dataset."
    DATA_LOAD_SUCCESS = "Dataset loaded successfully."
    UNEXPECTED_ERROR = "An unexpected error occurred."
