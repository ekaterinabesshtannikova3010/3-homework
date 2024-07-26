import unittest
from unittest.mock import patch
import pandas as pd
from pathlib import Path
import logging

ROOTPATH = "path/to/your/project"
file_xlsx = "transactions.xlsx"


def processing_transaction():
    """Функция для обработки Еxcel файла."""
    try:
        df_excel = pd.read_excel(Path(ROOTPATH, file_xlsx), engine="openpyxl")
        list_dict = df_excel.to_dict(orient="records")
        logging.info("Successfully processed transactions from an Excel file")
        return list_dict
    except Exception as e:
        logging.error(f"Ошибка при обработке транзакций: {e}")
        return []


@patch('pandas.read_excel')
def test_processing_transaction_with_mock(mock_read_excel):
    mock_read_excel.return_value = pd.DataFrame([])

    result = processing_transaction()
    assert result == []


    mock_read_excel.assert_called_once_with(Path(ROOTPATH, file_xlsx), engine="openpyxl")

if __name__ == '__main__':
    unittest.main()
