from .load_data import load_all_excel_data
from .preprocess import preprocess_data
from .plot_heatmap import plot_heatmap

def main() -> None:
    """Execute the full analysis pipeline."""

    df = load_all_excel_data()

    processed = preprocess_data(df)
    plot_heatmap(
        processed,
        output_html="output/heatmap.html",
        output_video="output/heatmap.mp4",
    )

if __name__ == "__main__":
    main()
