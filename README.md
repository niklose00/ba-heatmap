# Dubai Chocolate Heatmap Analysis

This project analyses online engagement for the "Dubai Chocolate" product using Talkwalker data. It loads the dataset, aggregates it by week, and visualises the geographic distribution of engagement with an animated heatmap.

## Project structure
```
BusinessAnalytics/
├── dubai_choc/
│   └── heatmap/
│       ├── data/        # raw data files
│       ├── src/         # source code
│       ├── output/      # generated visualisations
│       └── ...
├── requirements.txt     # Python dependencies
└── README.md            # this file
```

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the analysis:
   ```bash
   python -m dubai_choc.heatmap.src.main
   ```
   The animated heatmap is saved to `dubai_choc/heatmap/output/heatmap.html`.
   A video of the animation is written to `dubai_choc/heatmap/output/heatmap.mp4`.
   For video export you need a Chromium based browser for Kaleido. Run
   `plotly_get_chrome -y` once if no Chrome is available.

