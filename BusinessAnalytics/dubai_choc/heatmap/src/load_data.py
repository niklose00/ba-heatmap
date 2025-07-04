"""Utilities for loading Talkwalker Excel exports."""

from pathlib import Path

import pandas as pd

def load_excel_data(filename: str) -> pd.DataFrame:
    """Load an Excel file from the repository's data directory."""

    # Absoluten Pfad zur Datei berechnen (ausgehend vom aktuellen Skriptverzeichnis)
    data_dir = Path(__file__).resolve().parent.parent / "data"
    file_path = data_dir / filename

    # Datei laden
    df = pd.read_excel(file_path, engine="openpyxl")

    # Relevante Spalten extrahieren
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

    # Filter auf relevante Spalten
    df = df[columns_needed]

    # Leere Koordinaten rausfiltern
    df = df.dropna(subset=[
        "extra_source_attributes.world_data.longitude",
        "extra_source_attributes.world_data.latitude"
    ])

    # Koordinaten in float konvertieren
    df["extra_source_attributes.world_data.longitude"] = df["extra_source_attributes.world_data.longitude"].astype(float)
    df["extra_source_attributes.world_data.latitude"] = df["extra_source_attributes.world_data.latitude"].astype(float)

    return df
