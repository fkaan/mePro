from csv import reader
from math import e
import re
from typing import Optional
from venv import logger
import pandas as pd
from pathlib import Path
import os
import logging
from .error_messages import DataReadingErrorMessages as EM, SUPPORTTED_FILE_EXTENSIONS
from typing import Union, Optional


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

data_reader_functions = {
    ".csv": pd.read_csv,
    ".parquet": pd.read_parquet
}
class DataLoader:
    def load_data(self, file_path : Union[str, Path] ) -> Optional[pd.DataFrame]: 
        """
        Loads a dataset from a file.
        Supports CSV (.csv), Excel (.xlsx, .xls), and NumPy (.npy) files.
        Additional keyword arguments are passed to the respective loader.

        Raises:
            TypeError: If the file path is not a string or Path object.
        """
        self.__validate_file_path(file_path)
        ext = self.__check_if_file_extension_supported(file_path)

        reader_function = data_reader_functions.get(ext)
        data :pd.DataFrame = reader_function(file_path)
        
        if data.empty:
            logger.error(EM.DATA_LOAD_ERROR.value)
            raise ValueError(EM.DATA_LOAD_ERROR.value)
        
        
        
    def __validate_file_path(self, file_path : Union[str, Path]) -> str:
        """
        Validates the file path.
        Checks if the file exists and if the extension is supported.
        """
        if not isinstance(file_path, (str, Path)):
            raise TypeError(EM.INVALID_FILE_PATH_TYPE.value)

        if not Path(file_path).exists():
            raise FileNotFoundError(EM.FILE_NOT_FOUND.value)

        ext = Path(file_path).suffix
        if ext not in EM.SUPPORTTED_FILE_EXTENSIONS:
            raise ValueError(EM.UNSUPPORTED_FILE_EXTENSION.value)

        return True
    def __check_if_file_extension_supported(self, filename):
        """
        Checks if the file extension is supported.
        Returns the extension if supported, otherwise raises ValueError.
        """
        supported_extensions = [".csv", ".xlsx", ".xls", ".npy"]
        ext = Path(filename).suffix.lower()
        if ext in supported_extensions:
            return ext
        raise ValueError(f"Unsupported file extension: {ext}")
