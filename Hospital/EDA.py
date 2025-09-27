import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Path to your cleaned CSVs
data_folder = r"D:\360digiTMG\Hospital_Project\hospital\Dataset_2\Preprossessing"

# List your cleaned CSVs
csv_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]

# Function to run EDA on each dataset
def run_eda(file_path):
    print(f"\n{'='*70}")
    print(f"📄 EDA for: {os.path.basename(file_path)}")
    print(f"{'='*70}")

    df = pd.read_csv(file_path)

    # 1. Basic Info
    print("\n🧾 Shape:", df.shape)
    print("\n🧠 Column Data Types:\n", df.dtypes)
    print("\n🧼 Missing Values:\n", df.isnull().sum())
    print("\n🔁 Duplicate Rows:", df.duplicated().sum())

    # 2. Descriptive Stats (Numerical only)
    numeric_cols = df.select_dtypes(include='number')

    if not numeric_cols.empty:
        print("\n📊 Descriptive Statistics (Numerical):\n", numeric_cols.describe())

        # 2.1 Central Tendency Metrics
        print("\n📌 Central Tendency (Numerical Columns):")
        print("\n🔹 Mean:\n", numeric_cols.mean())
        print("\n🔸 Median:\n", numeric_cols.median())
        print("\n🔻 Mode:\n", numeric_cols.mode().iloc[0])  # first mode row

    # 3. Top Value Counts for Categorical Columns
    print("\n📋 Top 3 value counts for categorical columns:")
    for col in df.select_dtypes(include='object').columns:
        print(f"\n🟦 {col}")
        print(df[col].value_counts().head(3))

    # 4. Correlation Heatmap
    if not numeric_cols.empty:
        plt.figure(figsize=(10, 6))
        sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm')
        plt.title("Correlation Heatmap")
        plt.show()

        # 5. Histograms
        numeric_cols.hist(figsize=(12, 8), bins=20)
        plt.suptitle("Histograms for Numeric Columns")
        plt.tight_layout()
        plt.show()

        # 6. Boxplots for Outlier Detection
        for col in numeric_cols.columns:
            plt.figure(figsize=(6, 3))
            sns.boxplot(x=df[col])
            plt.title(f"Boxplot - {col}")
            plt.show()

    # 7. Bar plots for top 3 categorical features
    cat_cols = df.select_dtypes(include='object').columns
    for col in cat_cols[:3]:   # only first 3 categorical columns
        plt.figure(figsize=(8, 4))
        df[col].value_counts().head(10).plot(kind='bar')
        plt.title(f"Top 10 Categories in '{col}'")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# Run EDA on all cleaned CSVs
for csv in csv_files:
    file_path = os.path.join(data_folder, csv)
    run_eda(file_path)
