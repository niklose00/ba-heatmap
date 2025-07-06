"""Utilities for loading Talkwalker Excel exports."""

from pathlib import Path
import pandas as pd

def load_excel_data(filename: str) -> pd.DataFrame:
    """Load an Excel file from the repository's data directory."""
    data_dir = Path(__file__).resolve().parent.parent / "data"
    file_path = data_dir / filename

    df = pd.read_excel(file_path, engine="openpyxl")

    columns_needed = [
        "extra_source_attributes.world_data.continent",
        "extra_source_attributes.world_data.country",
        "extra_source_attributes.world_data.country_code",
        "extra_source_attributes.world_data.region",
        "extra_source_attributes.world_data.city",
        "extra_source_attributes.world_data.longitude",
        "extra_source_attributes.world_data.latitude",
        "published",
        "engagement",
        "reach"
    ]

    df = df[columns_needed]
    df = df.dropna(subset=[
        "extra_source_attributes.world_data.longitude",
        "extra_source_attributes.world_data.latitude"
    ])
    df["extra_source_attributes.world_data.longitude"] = df["extra_source_attributes.world_data.longitude"].astype(float)
    df["extra_source_attributes.world_data.latitude"] = df["extra_source_attributes.world_data.latitude"].astype(float)

    return df


def load_all_excel_data() -> pd.DataFrame:
    """Load and combine all Excel files from the data folder."""
    data_dir = Path(__file__).resolve().parent.parent / "data"
    all_dfs = []

    for file in sorted(data_dir.glob("*.xlsx")):
        try:
            df = load_excel_data(file.name)
            df["source_file"] = file.name  # Optional: zur Nachverfolgbarkeit
            all_dfs.append(df)
        except Exception as e:
            print(f"⚠️ Fehler beim Laden von {file.name}: {e}")

    if not all_dfs:
        raise ValueError("Keine Excel-Dateien konnten geladen werden.")

    return pd.concat(all_dfs, ignore_index=True)
