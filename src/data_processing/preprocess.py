import pickle
import pandas as pd

def load_pickle_file(file_path):
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

def flatten_data(data):
    records = []
    for syndrome_id, subjects in data.items():
        for subject_id, images in subjects.items():
            for image_id, embedding in images.items():
                records.append({
                    'syndrome_id': syndrome_id,
                    'subject_id': subject_id,
                    'image_id': image_id,
                    'embedding': embedding
                })
    return records

def create_dataframe(records):
    df = pd.DataFrame(records)
    embeddings_df = pd.DataFrame(df['embedding'].tolist(), index=df.index)
    df = pd.concat([df.drop('embedding', axis=1), embeddings_df], axis=1)
    return df

def save_dataframe(df, file_path):
    df.to_csv(file_path, index=False)
    print(f"Data successfully saved to {file_path}")

if __name__ == "__main__":
    file_path = 'data/raw/mini_gm_public_v0.1.p'
    data = load_pickle_file(file_path)
    records = flatten_data(data)
    df = create_dataframe(records)
    print(f"Dataset processed with {len(df)} samples.")
    save_dataframe(df, 'data/processed/processed_data.csv')
    print("pré processamento finalizado!!")
