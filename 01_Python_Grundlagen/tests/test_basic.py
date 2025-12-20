"""
Tests für die Python-Grundlagen Woche 1
"""

import pytest
import pandas as pd
import sys
import os

# Füge den Parent-Ordner zum Python-Pfad hinzu
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_dataframe_creation():
    """Teste die Erstellung eines DataFrames"""
    daten = {
        'Produkt': ['Laptop', 'Handy'],
        'Preis': [800, 600],
        'Kategorie': ['Computer', 'Telefon']
    }
    df = pd.DataFrame(daten)

    assert len(df) == 2
    assert list(df.columns) == ['Produkt', 'Preis', 'Kategorie']
    assert df['Produkt'].iloc[0] == 'Laptop'


def test_data_filtering():
    """Teste Datenfilterung"""
    daten = {
        'Produkt': ['Laptop', 'Handy', 'Tablet'],
        'Kategorie': ['Computer', 'Telefon', 'Computer']
    }
    df = pd.DataFrame(daten)

    computer_df = df[df['Kategorie'] == 'Computer']
    assert len(computer_df) == 2
    assert all(computer_df['Kategorie'] == 'Computer')


def test_calculations():
    """Teste grundlegende Berechnungen"""
    daten = {
        'Preis': [800, 600, 400]
    }
    df = pd.DataFrame(daten)

    assert df['Preis'].mean() == 600.0
    assert df['Preis'].max() == 800
    assert df['Preis'].min() == 400


if __name__ == "__main__":
    pytest.main([__file__])