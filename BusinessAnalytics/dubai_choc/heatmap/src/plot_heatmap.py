"""Functions to create an animated heatmap visualisation."""

from pathlib import Path
import pandas as pd
import plotly.express as px

LONG_COL = "extra_source_attributes.world_data.longitude"
LAT_COL = "extra_source_attributes.world_data.latitude"


def plot_heatmap(df: pd.DataFrame, output_html: str = "output/heatmap.html") -> None:
    """Generate an animated heatmap and save it as HTML."""

    fig = px.density_mapbox(
        df,
        lat=LAT_COL,
        lon=LONG_COL,
        z="engagement",
        radius=50,
        center=dict(lat=25.2048, lon=55.2708),
        zoom=1.5,
        mapbox_style="carto-positron",
        animation_frame="date",
        title="Dubai Chocolate - Globale Heatmap",
    )

    output_path = Path(__file__).resolve().parent.parent / output_html
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.write_html(str(output_path))
    return fig
