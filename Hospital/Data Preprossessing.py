import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# File paths (adjust if needed)
files = {
    "transactions": r"D:\360digiTMG\Hospital_Project\Dataset_2\Enhanced_Transactions_2024_20250909_193847.xlsx",
    "hospitals": r"D:\360digiTMG\Hospital_Project\Dataset_2\Enhanced_Hospital_Dataset_20250909_193847.xlsx",
    "inventory": r"D:\360digiTMG\Hospital_Project\Dataset_2\Enhanced_Inventory_20250909_193847.xlsx",
    "patients": r"D:\360digiTMG\Hospital_Project\Dataset_2\Enhanced_Patients_20250909_193847.xlsx",
    "supply_chain": r"D:\360digiTMG\Hospital_Project\Dataset_2\Enhanced_Supply_Chain_20250909_193847.xlsx"
}

# --- Step 1: Load datasets ---
transactions = pd.read_excel(files["transactions"], sheet_name="Sheet1")
hospitals = pd.read_excel(files["hospitals"], sheet_name=['Hospital', 'Departments', 'Physicians', 'SKUs', 'Vendors'])
inventory = pd.read_excel(files["inventory"], sheet_name="Sheet1")
patients = pd.read_excel(files["patients"], sheet_name="Sheet1")
supply_chain = pd.read_excel(files["supply_chain"], sheet_name=['Purchase_Orders', 'Deliveries'])

# --- Step 2: Clean missing values ---
def clean_missing(df):
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].fillna("Unknown")
        else:
            df[col] = df[col].fillna(df[col].median())
    return df

transactions = clean_missing(transactions)
hospitals = clean_missing(hospitals)
inventory = clean_missing(inventory)
patients = clean_missing(patients)
supply_chain = clean_missing(supply_chain)

# --- Step 3: Process dates in transactions ---
transactions["transaction_datetime"] = pd.to_datetime(
    transactions["transaction_date"].astype(str) + " " + transactions["transaction_time"].astype(str),
    errors="coerce"
)
transactions["day_of_week"] = transactions["transaction_datetime"].dt.day_name()
transactions["is_weekend"] = transactions["transaction_datetime"].dt.weekday >= 5

# --- Step 4: Encode categorical variables ---
def encode_categoricals(df):
    label_encoders = {}
    for col in df.select_dtypes(include="object").columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        label_encoders[col] = le
    return df, label_encoders

transactions, le_trans = encode_categoricals(transactions)
hospitals, le_hosp = encode_categoricals(hospitals)
inventory, le_inv = encode_categoricals(inventory)
patients, le_pat = encode_categoricals(patients)
supply_chain, le_sup = encode_categoricals(supply_chain)

# --- Step 5: Scale numeric features ---
scaler = StandardScaler()

def scale_numeric(df):
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df

transactions = scale_numeric(transactions)
hospitals = scale_numeric(hospitals)
inventory = scale_numeric(inventory)
patients = scale_numeric(patients)
supply_chain = scale_numeric(supply_chain)

# --- Step 6: Merge into master dataset ---
# Example: join transactions with hospitals, patients, and inventory
master = transactions.merge(hospitals, on="hospital_id", how="left") \
                     .merge(patients, on="patient_id", how="left") \
                     .merge(inventory, on="sku_id", how="left")

# --- Step 7: Save cleaned datasets ---
transactions.to_csv("cleaned_transactions.csv", index=False)
hospitals.to_csv("cleaned_hospitals.csv", index=False)
inventory.to_csv("cleaned_inventory.csv", index=False)
patients.to_csv("cleaned_patients.csv", index=False)
supply_chain.to_csv("cleaned_supply_chain.csv", index=False)
master.to_csv("master_dataset.csv", index=False)

print(" Preprocessing complete. Cleaned files saved.")