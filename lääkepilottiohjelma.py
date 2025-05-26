import os
import pandas as pd
import datetime
import apteekit_funktiot as af
from cleaning_price import clean_price


def get_output_path(base_filename, attempt=0):
    """Generate output file path, appending _1, _2, etc., for retries."""
    if attempt == 0:
        return base_filename
    name, ext = os.path.splitext(base_filename)
    return f"{name}_{attempt}{ext}"


def save_data_with_fallback(data, base_filename, max_attempts=5):
    """Attempt to save DataFrame to Excel, trying alternative filenames if needed."""
    output_dir = os.getcwd()  # Use current working directory
    output_path = os.path.join(output_dir, base_filename)

    # Ensure output directory exists
    try:
        os.makedirs(output_dir, exist_ok=True)
    except PermissionError:
        print(f"Error: Cannot create directory {output_dir}. Check permissions.")
        return False

    # Check if directory is writable
    if not os.access(output_dir, os.W_OK):
        print(f"Error: No write permission for directory {output_dir}.")
        return False

    # Try saving with original and fallback filenames
    for attempt in range(max_attempts):
        current_path = get_output_path(output_path, attempt)
        try:
            # If file exists, try to make it writable
            if os.path.exists(current_path):
                os.chmod(current_path, 0o666)  # Attempt to make writable (Windows may ignore)
            data.to_excel(current_path, index=False)
            print(f"\nFile saved successfully: {current_path}")
            return True
        except PermissionError as e:
            print(f"PermissionError for {current_path}: {e}. Trying next filename...")
        except Exception as e:
            print(f"Error saving {current_path}: {e}. Trying next filename...")

    print(f"Failed to save file after {max_attempts} attempts.")
    return False


def main():

    af.keraa_tiedot()

    data = pd.DataFrame(af.medication, columns=['Tuote', 'Hinta', 'Valuutta', 'Valmisteen osoite', 'Verkko-osoite'])
    date_now = datetime.datetime.now().date()
    data['Päivämäärä'] = date_now
    data = data.reindex(columns=['Päivämäärä', 'Tuote', 'Hinta', 'Valuutta', 'Valmisteen osoite', 'Verkko-osoite'])
    print(data.to_string())

    uncleaned_filename = f'lääkehinnat_{date_now}.xlsx'
    cleaned_filename = f'lääkehinnat_clean_{date_now}.xlsx'

    # Save uncleaned data (only original price column)
    success_uncleaned = save_data_with_fallback(data, uncleaned_filename)

    data['Hinta'] = data['Hinta'].apply(clean_price)
    data['Hinta'] = pd.to_numeric(data['Hinta'], errors='coerce')

    success_cleaned = save_data_with_fallback(data, cleaned_filename)

    # Report outcome
    if not (success_uncleaned and success_cleaned):
        print("Could not save one or both files. Please check directory permissions or close any open Excel files.")
    elif not success_uncleaned:
        print("Failed to save uncleaned data file.")
    elif not success_cleaned:
        print("Failed to save cleaned data file.")

if __name__ == "__main__":
    main()