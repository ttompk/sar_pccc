# Pleasure Craft Courtesy Check App
Small application for logging and correctly identifying boat safety equipment required on Canadian Pleasure Craft Vessels.  

Application requirements:
- log static info on the vessel
- produce checklist of equipment need on board dependent on the size of the vessel
- save the outcome of the inspection: eg. pass, requirements not met, recomendations, etc.

## Data Sources
The criteria for passing or failing an inspection is ultimately provided by Canada Coast Guard regulations - tp_511e.pdf

### Python
The program is written in python using the streamlit app.

### Database
Information about vessel is stored in postgres database.

### Serving
The application uses Render.com as the web service provider.


You are a safety inspector for boats. I want to create a python application using streamlit as the user interface. This application will allow me to enter the name, boat type, and length of boat. After entering in this information a series of required safety devices will be displayed that is particular to the type and length of the boat chosen. Each requirement will have a radio button that the user can click to confirm that safety device is present. At the end of the page there should be a notes section and buttons where the user can select whether the boat passes the inspection or fails the inspection. The failure reason should be recorded in a text box. Once the user clicks the save button, the data should be stored in a postgres database. The safety requirements are contained in the attached publication. 