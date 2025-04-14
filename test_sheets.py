from utils.gsheets import append_to_google_sheet
import os
from dotenv import load_dotenv

def test_google_sheets():
    print("Testing Google Sheets Integration...")
    
    # Load environment variables
    load_dotenv()
    
    # Test data
    test_data = [
        ["Test Organization", "test@example.com", "Test Date", "Test Status"]
    ]
    
    try:
        # Try to append test data
        updated_cells = append_to_google_sheet(test_data)
        print(f"✅ Success! Updated {updated_cells} cells in Google Sheets")
        print(f"📊 Sheet ID: {os.getenv('GOOGLE_SHEET_ID')}")
        return True
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    test_google_sheets() 