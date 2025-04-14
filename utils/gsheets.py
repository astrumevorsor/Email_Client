from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get configuration from environment
SPREADSHEET_ID = os.getenv("GOOGLE_SHEET_ID")
RANGE_NAME = os.getenv("GOOGLE_SHEET_RANGE", "Sheet1!A1:D1")  # Default value as fallback

def append_to_google_sheet(values):
    try:
        if not SPREADSHEET_ID:
            raise ValueError("Google Sheet ID not configured in environment variables")
            
        # Authenticate using the service account credentials
        credentials = Credentials.from_service_account_file("credentials.json")
        service = build("sheets", "v4", credentials=credentials)
        sheet = service.spreadsheets()

        # Append data to the sheet
        body = {"values": values}
        result = sheet.values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE_NAME,
            valueInputOption="RAW",
            body=body
        ).execute()

        updated_cells = result.get("updates", {}).get("updatedCells", 0)
        return updated_cells
    except Exception as e:
        raise RuntimeError(f"Error interacting with Google Sheets: {str(e)}")