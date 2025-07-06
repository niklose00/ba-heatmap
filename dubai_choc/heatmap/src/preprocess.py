import pandas as pd

LONG_COL = "extra_source_attributes.world_data.longitude"
LAT_COL = "extra_source_attributes.world_data.latitude"


def preprocess_data(df: pd.DataFrame, freq: str = "W") -> pd.DataFrame:
    """Clean and aggregate Talkwalker data.

    Parameters
    ----------
    df : pd.DataFrame
        Raw dataframe from :func:`load_excel_data`.
    freq : str, optional
        Pandas offset alias for aggregation frequency, by default "W".

    Returns
    -------
    pd.DataFrame
        Aggregated dataframe with a new ``date`` column.
    """
    df = df.copy()

    if "published" in df.columns:
        df["published"] = pd.to_datetime(df["published"], errors="coerce")
    else:
        raise KeyError("'published' column not found in data")

    df["date"] = df["published"].dt.to_period(freq).dt.start_time

    grouped = (
        df.dropna(subset=[LONG_COL, LAT_COL, "date"])
        .groupby(["date", LONG_COL, LAT_COL], as_index=False)
        .agg({"engagement": "sum", "reach": "sum"})
    )
    return grouped
