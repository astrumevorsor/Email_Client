# Conference Outreach Automation

An automated system for conference outreach and organization management.

## Features

- Organization data collection using Perplexity API
- Google Sheets integration for data storage
- Email outreach automation (optional)
- Streamlit-based web interface

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with the following variables:
   ```
   PERPLEXITY_API_KEY=your_perplexity_api_key
   GOOGLE_SHEET_ID=your_google_sheet_id
   GOOGLE_SHEET_RANGE=Sheet1!A1:D1
   ```
4. Set up Google Sheets API:
   - Create a Google Cloud Project
   - Enable Google Sheets API
   - Create a service account and download credentials.json
   - Share your Google Sheet with the service account email

## Usage

Run the application:
```bash
streamlit run main.py
```

## Project Structure

- `main.py`: Main application entry point
- `utils/`: Utility modules
  - `gsheets.py`: Google Sheets integration
  - `perplexity.py`: Perplexity API integration
  - `email_agent.py`: Email automation
- `templates/`: Email templates
- `requirements.txt`: Project dependencies

## License

MIT License