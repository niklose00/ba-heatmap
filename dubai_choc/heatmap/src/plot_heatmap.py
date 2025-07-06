"""Functions to create an animated heatmap visualisation."""

from pathlib import Path
from typing import Optional

import imageio.v2 as imageio
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

LONG_COL = "extra_source_attributes.world_data.longitude"
LAT_COL = "extra_source_attributes.world_data.latitude"


def plot_heatmap(
    df: pd.DataFrame,
    output_html: str = "output/heatmap.html",
    output_video: Optional[str] = None,
) -> None:
    """Generate an animated heatmap and save it as HTML and optionally as video."""
    
    z_min = df["engagement"].min()
    z_max = df["engagement"].max()
    
    fig = px.density_mapbox(
        df,
        lat=LAT_COL,
        lon=LONG_COL,
        z="engagement",
        range_color=(z_min, z_max),
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

    if output_video:
        video_path = Path(__file__).resolve().parent.parent / output_video
        video_path.parent.mkdir(parents=True, exist_ok=True)
        frames = []
        for frame in [None] + list(fig.frames):
            if frame is None:
                g = fig
            else:
                g = go.Figure(data=frame.data, layout=fig.layout)
                if hasattr(frame, "layout"):
                    g.update_layout(frame.layout)
            img = g.to_image(format="png", scale=2)
            frames.append(imageio.imread(img))
        imageio.mimsave(video_path, frames, fps=2)

    return fig
