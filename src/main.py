from load_data import load_excel_data
from plot_heatmap import plot_heatmap

def main():
    df = load_excel_data("test_data.xlsx")
    
    plot_heatmap(df)

if __name__ == "__main__":
    main()
