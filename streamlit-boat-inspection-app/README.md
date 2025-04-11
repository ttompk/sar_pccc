# Streamlit Boat Inspection App

This project is a Streamlit application designed for inspecting boats and ensuring they meet safety requirements. Users can input boat details, confirm the presence of safety devices, and record inspection results.

## Project Structure

```
streamlit-boat-inspection-app
├── src
│   ├── app.py            # Main entry point of the Streamlit application
│   ├── database.py       # Database connection and query execution
│   ├── utils.py          # Utility functions for safety requirements
│   └── styles
│       └── custom.css    # Custom styles for the application
├── requirements.txt       # Project dependencies
├── .streamlit
│   └── config.toml       # Streamlit configuration settings
├── README.md              # Project documentation
└── .env                   # Environment variables for sensitive information
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd streamlit-boat-inspection-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure the database:**
   - Create a `.env` file in the root directory and add your PostgreSQL connection details.

5. **Run the application:**
   ```
   streamlit run src/app.py
   ```

## Usage

- Enter the boat's name, type, and length in the provided fields.
- The application will display the required safety devices based on the input.
- Confirm the presence of safety devices using the radio buttons.
- Add any notes in the designated section.
- Click the "Pass" or "Fail" button to record the inspection result, with the option to provide a failure reason.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.