import pytest 
from claims_ml.src.data_loader import DataLoader

@pytest.fixture
def data_loader():
    return DataLoader()



def test_check_if_file_extension_supported(data_loader):
    assert data_loader._DataLoader__check_if_file_extension_supported("data.csv") == ".csv"
    with pytest.raises(ValueError):
        data_loader._DataLoader__check_if_file_extension_supported("data.txt")