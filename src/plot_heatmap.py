import plotly.express as px
import pandas as pd

def plot_heatmap(df: pd.DataFrame) -> None:
    fig = px.density_mapbox(
        df,
        lat="extra_source_attributes.world_data.latitude",
        lon="extra_source_attributes.world_data.longitude",
        z="engagement",  # optional für Gewichtung
        radius=60,
        center=dict(lat=25.2048, lon=55.2708),  # Zentrum: Dubai
        zoom=1.5,
        mapbox_style="carto-positron",
        title="Dubai Chocolate - Globale Heatmap"
    )
    fig.show()
