import pandas as pd
import os

# Base directory where original Excel files are stored
base_path = r"D:\360digiTMG\Hospital_Project\hospital\Dataset_2"

# Output directory for cleaned CSVs
output_dir = r"D:\360digiTMG\Hospital_Project\hospital\Dataset_2\New folder"
os.makedirs(output_dir, exist_ok=True)

file_sheet_map = {
    "Enhanced_Hospital_Dataset_20250909_193847.xlsx": ["Hospital", "Departments", "Physicians", "SKUs", "Vendors"],
    "Enhanced_Inventory_20250909_193847.xlsx": ["Sheet1"],
    "Enhanced_Patients_20250909_193847.xlsx": ["Sheet1"],
    "Enhanced_Supply_Chain_20250909_193847.xlsx": ["Purchase_Orders", "Deliveries"],
    "Enhanced_Transactions_2024_20250909_193847.xlsx": ["Sheet1"]
}

def preprocess(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    df = df.drop_duplicates()
    df = df.dropna(thresh=int(df.shape[1] * 0.7))
    df = df.fillna("Unknown")
    for col in df.columns:
        if 'date' in col or 'time' in col:
            try:
                df[col] = pd.to_datetime(df[col], errors='coerce')
            except:
                pass
    return df

for file, sheets in file_sheet_map.items():
    for sheet in sheets:
        try:
            # Construct full path to Excel file
            file_path = os.path.join(base_path, file)

            # Load and process
            df = pd.read_excel(file_path, sheet_name=sheet)
            df_clean = preprocess(df)

            # Output file path
            file_base = os.path.splitext(file)[0].lower()
            sheet_name = sheet.lower().replace(" ", "_")
            output_file = f"{file_base}_{sheet_name}_clean.csv"
            output_path = os.path.join(output_dir, output_file)

            # Save CSV
            df_clean.to_csv(output_path, index=False)
            print(f"✅ Saved: {output_path}")
        except Exception as e:
            print(f"❌ Error processing {file} - {sheet}: {e}")
