import unittest
from unittest.mock import mock_open, patch
from src.transactions_reader import csv_operations, excel_operation


def test_csv_operations():
    mock_file = mock_open(
        read_data="incorrect csv"
    )
    with patch("builtins.open", mock_file):
        result = csv_operations('../data/transactions.csv')
        assert result == []


def test_excel_operation():
    mock_file = mock_open(
        read_data="incorrect excel"
    )
    with patch("builtins.open", mock_file):
        result = excel_operation("../data/transactions_excel.xlsx")
        assert result == []