import pandas as pd
import streamlit as st

def load_aadhaar_data(file_path):
    """
    Loads and cleans the processed Aadhaar CSV data.
    """
    df = pd.read_csv(file_path)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Total update calculation (dynamic)
    possible_age_cols = [
        'age_0_5', 'age_5_17', 'age_18_greater', 
        'demo_age_5_17', 'demo_age_17_', 
        'bio_age_5_17', 'bio_age_17_'
    ]
    existing_age_cols = [c for c in possible_age_cols if c in df.columns]

    if existing_age_cols:
        df['total_updates'] = df[existing_age_cols].sum(axis=1)
    else:
        df['total_updates'] = 1
        st.warning("No age-related update columns found; using row count instead.")

    # Convert date safely
    df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')

    # Standardize state names
    df['state'] = (
        df['state']
        .str.strip()
        .str.title()
        .str.replace(r'\s+', ' ', regex=True)
    )
    
    valid_states = [
        "Andaman & Nicobar Islands","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar",
        "Chandigarh","Chhattisgarh","Dadra & Nagar Haveli And Daman And Diu","Delhi",
        "Goa","Gujarat","Haryana","Himachal Pradesh","Jammu And Kashmir","Jharkhand",
        "Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Pradesh","Maharashtra",
        "Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab",
        "Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh",
        "Uttarakhand","West Bengal"
    ]
    
    df = df[df['state'].isin(valid_states)]
    df['district'] = df['district'].fillna('Unknown')

    return df