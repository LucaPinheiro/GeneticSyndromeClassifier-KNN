import pytest
import pandas as pd
import numpy as np
from src.data_processing.preprocess import load_pickle_file, flatten_data, create_dataframe, save_dataframe
import os

def test_load_pickle_file():
    data = load_pickle_file('data/raw/mini_gm_public_v0.1.p')
    assert isinstance(data, dict), "O arquivo carregado deve ser um dicionário."

def test_flatten_data():
    sample_data = {
        'syndrome_1': {
            'subject_1': {
                'image_1': [0.1, 0.2, 0.3]
            }
        }
    }
    records = flatten_data(sample_data)
    assert len(records) == 1, "Deve haver exatamente um registro."
    assert records[0]['syndrome_id'] == 'syndrome_1'
    assert records[0]['subject_id'] == 'subject_1'

def test_create_dataframe():
    records = [
        {'syndrome_id': 'syndrome_1', 'subject_id': 'subject_1', 'image_id': 'image_1', 'embedding': [0.1, 0.2, 0.3]}
    ]
    df = create_dataframe(records)
    assert isinstance(df, pd.DataFrame), "O resultado deve ser um DataFrame."
    assert 'syndrome_id' in df.columns, "A coluna syndrome_id deve existir."
    assert df.shape[1] == 6, "O DataFrame deve ter as colunas corretas."

def test_save_dataframe(tmpdir):
    df = pd.DataFrame({
        'syndrome_id': ['syndrome_1'],
        'subject_id': ['subject_1'],
        'image_id': ['image_1'],
        0: [0.1],
        1: [0.2],
        2: [0.3]
    })
    test_file_path = tmpdir.join('test_processed_data.csv')
    save_dataframe(df, str(test_file_path))
    assert os.path.exists(test_file_path), "O arquivo CSV não foi salvo corretamente."
    loaded_df = pd.read_csv(test_file_path)
    assert len(loaded_df) == 1, "O arquivo salvo deve conter exatamente um registro."

if __name__ == "__main__":
    pytest.main(["-v", "tests/test_preprocessing.py"])
