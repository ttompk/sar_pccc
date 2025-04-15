# Canadian Boat Inspection App

This project is an application designed to aid users in performing pleasure craft courtesey checks for Canadian boats (also known as vessels). Courtesey checks are provided by qualified institutions (such a as the Candian Lifeboat Institution) on vessls to be sure the boat and operators comply with Transport Canada safety regulations. The app user inputs details about the vessel, confirms the presence of safety devices, and saves the inspection results to a database (if a member of the Canadian Lifeboat Institution). The general public is welcome to use the app but the results of the inspection will not be saved in the database and a report will not be sent to the boat operator.

## NOTE TO USERS:
Transport Canada has specified that required safety devices be specific to vessel type and length overall. The app therefore only shows the required safety devices specific to that vessel's confirgutation. The app was built in April 2025 using the Transport Canada publication TP_511e which was published in 2019. 


## Project Structure
This is a python project using streamlit for the user interface.

```
streamlit-boat-inspection-app
├── src
│   ├── app.py            # Main entry point of the Streamlit application
│   ├── database.py       # Database connection and query execution
│   ├── utils.py          # Utility functions for safety requirements
│   ├── helper.py         # Functions that cannot be held in Utility do to circular dependencies
│   └── styles
│       └── custom.css    # Custom styles for the application
├── requirements.txt      # Project dependencies
├── .streamlit
│   └── config.toml       # Streamlit configuration settings
├── README.md             # Project documentation
├── .env                  # Environment variables for sensitive information
├── background
│   └── tp_511e.pdf       # Transport Canada regulations. Copyright 2019.

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

- Enter details about the vessel, such as the boat's name, type, and length in the provided fields.
- Enter details about the operator. 
- Select the optional safety devices that are on board. Note, optional safety devices, such as a VHF radio can impact the number of required safety devices.
- The application will display the required safety devices based on the input.
- The user confirms the presence of safety devices using checkboxes and togle switches.
- Add any notes in the designated section.
- Select whether the vessel passes or fails the inspection and press the 'File Report' button to save the resport to the database. A password is required to do so.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.