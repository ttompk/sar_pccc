import streamlit as st
import database
import utils 
from helper import reduce_flares
import datetime
from dateutil.relativedelta import relativedelta


def main():

    st.markdown("""
    <style>
    @media only screen and (max-width: 600px) {
    .your-class { font-size: 14px; }
    }
    </style>
    """, unsafe_allow_html=True)

    required_select = {}
    common_select = {}

    def reset_state_values():
            # Reset all session state variables
            st.session_state.clear()
            st.session_state["boat_name"] = ""
            st.session_state["boat_type"] = "Sailboat"
            st.session_state["motor"] = True
            st.session_state["boat_length"] = 1
            st.session_state["boat_license_select"] = "None"
            st.session_state["boat_license_date"] = None
            st.session_state["radio_select"] = False
            st.session_state["plb_select"] = False
            st.session_state["epirb_select"] = False
            st.session_state["competency_select"] = "PCOC"
            st.session_state["charts_select"] = "None"
            st.session_state["charts_date_select"] = False
            st.session_state["notes"] = ""
            st.session_state["ais_select"] = False
            st.session_state["pass_fail"] = "Yes, boat passes courtesy inspection"
            st.session_state["tender_select"] = False
            st.session_state["inflate_select"] = False
            st.session_state["inflate_approved_select"] = False
            st.session_state["inflate_serviced_select"] = False
            st.session_state["inflate_16_select"] = False
            st.rerun()  # Rerun the app to reflect the cleared state

            # Reset dynamically generated keys for checkboxes in "Required Safety Devices"
            for key in list(st.session_state.keys()):
                if key.startswith("device_"):  # Assuming keys for devices start with "device_"
                    del st.session_state[key]

    def check_expired_license(boat_license_select, boat_license_date):
        # Get today's date
        today = datetime.date.today()

        three_years_ago = today - relativedelta(years=3)        
        ten_years_ago = today - relativedelta(years=10) 
        
        if boat_license_select == "Licensed":
            if boat_license_date < ten_years_ago:
                st.write("The boat license is EXPIRED. More than 10 years old.")

        elif boat_license_select == "Registered":
            if boat_license_date < three_years_ago:
                st.write("The boat license is EXPIRED. More than 3 years old.")

    
    # Top screen that never moves
    st.title("Canadian Lifeboat Institution")
    st.header("Boat Inspection App")
    st.write("Organization number 1700")
    st.write("Select the tabs below to navigate through the forms. Press 'File Report' to save the inspection report.")
    
    tab1, tab2, tab3= st.tabs(["Basic Info", "Optional Equipment", "Required Safety Devices"])


    # BOAT DETAILS
    with tab1:
        st.header("Basic Vessel Info")
        
        boat_name = st.text_input("Boat Name:", key="boat_name", value="")
        boat_type = st.radio("Boat Type:", ["Sailboat", "Powerboat", "Personal Watercraft"], key="boat_type", index=0)
        if boat_type == "Sailboat":
            motor = st.toggle("Is there a motor?", value=True, key="motor")
        else:
            motor = True
        
        #if boat_type != "Personal Watercraft":
        boat_length = st.number_input("Enter Boat Length (in feet):", min_value=1, key="boat_length")
        
        # boat licensed? Registered? Are they up to date?
        boat_license_select = st.selectbox("Is boat licensed/registered? : ", options=["None", "Licensed", "Registered"], index=1, key="boat_license_select")
        if boat_license_select != "None":
            boat_license_date = st.date_input("Date boat last licensed/registered: ", value=None, key="boat_license_date")
            # license lasts 10 years, registration lasts 3 years
            if boat_license_date != None:
                check_expired_license(boat_license_select, boat_license_date)
        else:
            boat_license_date= None
        
        # is there a motorized tender?
        tender_select = st.toggle("Is there a motorized tender?", value=False, key="tender_select")
        if tender_select == True:
            st.write("A motorized tender of 10hp (7.5 kw) or more requires a license.")
            #tender_motor = st.text_input("Tender motor size: ", key="tender_motor", value="")



    # OPTIONAL SAFETY EQUIPMENT
    with tab2:
        
        # User input of Operator Info
        st.subheader("Operator Info")
        competency_select = st.selectbox("Operator Competency? : ", options=["PCOC", "Proof of Course", "Rental Boat Checklist", "Marine Safety Certificate", "None"], key="competency_select")
        
        # Optional Equipment
        st.subheader("Optional Equipment")
        radio_select = st.toggle(label="VHF radio?: ", value=False, key="radio_select") # affects the number of flares required
        epirb_select = st.toggle("EPIRB?", value=False, key="epirb_select") # affects the number of flares required
        plb_select = st.toggle("Operator wears a personal locator beacon? ", value=False, key="plb_select") # affects the number of flares required
        ais_select = st.toggle("AIS onboard?", value=False, key="ais_select")


        #st.subheader("Navigation Equipment (optional)")
        charts_select = st.radio("Charts present? ", ["None", "Paper", "Electronic"], key="charts_select")  
        if charts_select in ["Paper","Electronic"]:
            # charts up to date? 
            charts_date_select = st.toggle("Charts up to date?", value=False, key="charts_date_select")
        else:
            charts_date_select = None
        

    # Diplay required safety devices and checkboxes
    with tab3:
        # is there a flare reduction?
        reduce = reduce_flares(radio_select, plb_select, epirb_select)
        if reduce:
            flare_reduce = st.write("*** NOTE: Flare reduction applies ***")
        
        st.header("Required Safety Devices")
        
        # Display required safety devices by boat length and type
        # sailboats and powerboats only
        if boat_type in ["Sailboat", "Powerboat"]:
            if boat_name and boat_type and boat_length:
                common_devices = utils.get_common_devices(boat_length)
                for key, device in common_devices.items():
                    common_select.update( {key: st.checkbox(device, key=key)} ) 

                required_devices = utils.get_required_safety_devices_by_length(boat_type, boat_length)
                for key, device in required_devices.items():
                    required_select.update( {key: st.checkbox(device, key=key)} )
                
            # inflatable PFDs
            inflate_select = st.toggle("Operator uses Inflatable PFDs?", value=False, key="inflate_select")
            if inflate_select:
                col11, col22 = st.columns([1, 15])  # Adjust the ratio for spacing
                with col22:
                    inlfate_approved_select = st.toggle("Transport Canada approved?", value=False, key="inflate_approved_select")
                    inflate_serviced_select = st.toggle("CO2 not expired?", value=False, key="inflate_serviced_select")
                    inflate_16_select = st.toggle("User is 16 years old or older?", value=False, key="inflate_16_select")
        else:
            # Personal Watercraft
            if boat_type == "Personal Watercraft":
                if boat_name and boat_type and boat_length:
                    required_devices = utils.get_required_safety_devices_by_length(boat_type, boat_length)
                    for key, device in required_devices.items():
                        required_select = st.checkbox(device, key=key)
                    

        # Radio buttons for confirming presence of safety devices
        st.header("File Report")
        pass_fail = st.radio("Are all required safety devices present?", ("Yes, boat passes courtesy inspection", "Yes, with deficiencies as noted", "No"))

        # Notes section
        notes = st.text_area("Additional Notes:", key="notes")

        col1, col2, col3 = st.columns(3)  # Create three columns
        with col1:
            if st.button("File Report", key="file_report"):
                
                # BOAT INFO
                # add boat and retrieve the unique boat id from the database
                boat_id = database.add_to_boat_table(
                    boat_name, 
                    boat_type, 
                    motor, 
                    boat_length, 
                    boat_license_select, 
                    boat_license_date, 
                    tender_select, 
                    competency_select)

                # OPTIONAL EQUIPMENT 
                # update database with optional equipment to the boat
                # the keys for optional_eq are the equipment id's in the database, do not change
                optional_eq = {
                    "Radio Radio": radio_select, 
                    "EPIRB": epirb_select, 
                    "Personal Locator Beacon": plb_select, 
                    "AIS": ais_select, 
                    "Charts": charts_select, 
                    "Chart Date": charts_date_select}
                database.add_optional_equipment_to_boat(boat_id, optional_eq)

                # REQURED DEVICES
                # update the inspections table - note, there is an autogenerated timestamp in table
                inspector_name = "CLI Staff"
                inspection_id = database.add_inspection_info_to_db(boat_id, inspector_name, pass_fail, notes)

                # Use the inspection_id to update the inspection_devices table
                for device_name, device_descr in common_devices.items():
                    database.add_safety_device(inspection_id, device_name, device_descr, common_select[device_name])
                for device_name, device_descr in required_devices.items():
                    database.add_safety_device(inspection_id, device_name, device_descr, required_select[device_name])
                database.add_safety_device(inspection_id, "Inflatable PFD", "Inflatable PFDs present?", inflate_select)
                if inflate_select:
                    database.add_safety_device(inspection_id, "Inflatable PFD", "Transport Canada approved?", inlfate_approved_select)
                    database.add_safety_device(inspection_id, "Inflatable PFD", "CO2 not expired?", inflate_serviced_select)
                    database.add_safety_device(inspection_id, "Inflatable PFD", "16 years or older?", inflate_16_select)
        
        with col3:
            if st.button("Clear Form", key="reset_button"):
                reset_state_values()
        
        # if raft has a motor 10hp needs a license

if __name__ == "__main__":
    main()