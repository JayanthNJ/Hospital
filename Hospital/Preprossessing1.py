import pandas as pd
import os

# Define where your Excel files are stored
input_folder = r"D:\360digiTMG\Hospital_Project\Dataset_2\Original"
output_folder = r"D:\360digiTMG\Hospital_Project\Dataset_2\Cleaned"

# Make sure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Define files and sheets to process
datasets = {
    "Enhanced_Hospital_Dataset_20250909_193847.xlsx": ["Hospital", "Departments", "Physicians", "SKUs", "Vendors"],
    "Enhanced_Inventory_20250909_193847.xlsx": ["Sheet1"],
    "Enhanced_Patients_20250909_193847.xlsx": ["Sheet1"],
    "Enhanced_Supply_Chain_20250909_193847.xlsx": ["Purchase_Orders", "Deliveries"],
    "Enhanced_Transactions_2024_20250909_193847.xlsx": ["Sheet1"]
}

# Preprocessing function
def preprocess(df):
    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # Drop duplicate rows
    df = df.drop_duplicates()

    # Drop rows with too many missing values (>30% columns are NaN)
    df = df.dropna(thresh=int(df.shape[1] * 0.7))

    # Fill remaining missing values
    df = df.fillna("Unknown")

    # Convert any 'date' or 'time' columns to datetime
    for col in df.columns:
        if 'date' in col or 'time' in col:
            try:
                df[col] = pd.to_datetime(df[col], errors='coerce')
            except Exception as e:
                print(f"Warning: Could not convert {col} to datetime: {e}")
    
    return df

# Process all files and sheets
for file_name, sheet_names in datasets.items():
    input_path = os.path.join(input_folder, file_name)
    for sheet in sheet_names:
        try:
            # Load the sheet
            df = pd.read_excel(input_path, sheet_name=sheet)

            # Preprocess the data
            df_clean = preprocess(df)

            # Prepare output file name
            base_name = os.path.splitext(file_name)[0].lower()
            sheet_clean = sheet.lower().replace(" ", "_")
            output_file_name = f"{base_name}_{sheet_clean}_clean.csv"
            output_path = os.path.join(output_folder, output_file_name)

            # Save cleaned CSV
            df_clean.to_csv(output_path, index=False)
            print(f"✅ Saved cleaned data: {output_path}")

        except Exception as e:
            print(f"❌ Error processing {file_name} - {sheet}: {e}")
