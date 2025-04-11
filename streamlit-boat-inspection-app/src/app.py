import streamlit as st
import database
import utils 
from helper import reduce_flares


def main():

    st.markdown("""
    <style>
    @media only screen and (max-width: 600px) {
    .your-class { font-size: 14px; }
    }
    </style>
    """, unsafe_allow_html=True)

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
            st.session_state["charts_select"] = "N/A"
            st.session_state["charts_date_select"] = False
            st.session_state["notes"] = ""
            st.session_state["ais_select"] = "N/A"
            st.rerun()  # Rerun the app to reflect the cleared state

            # Reset dynamically generated keys for checkboxes in "Required Safety Devices"
            for key in list(st.session_state.keys()):
                if key.startswith("device_"):  # Assuming keys for devices start with "device_"
                    del st.session_state[key]


    
    # Top screen that never moves
    st.title("Canadian Lifeboat Institution")
    st.header("Boat Inspection App")
    st.write("Organizational number 1700")
    
    tab1, tab2, tab3= st.tabs(["Basic Info", "Optional Equipment", "Required Safety Devices"])


    # BOAT DETAILS
    with tab1:
        st.header("Basic Vessel Info")
        
        boat_name = st.text_input("Boat Name:", key="boat_name", value="")
        boat_type = st.radio("Boat Type:", ["Sailboat", "Powerboat", "Personal Watercraft"], key="boat_type", index=0)
        if boat_type == "Sailboat":
            motor = st.toggle("Is there a motor?", value=True, key="motor")
        
        #if boat_type != "Personal Watercraft":
        boat_length = st.number_input("Enter Boat Length (in feet):", min_value=1, key="boat_length")
        boat_license_select = st.selectbox("Is boat licensed/registered? : ", options=["None", "Licensed", "Registered"], key="boat_license_select")
        if boat_license_select != "None":
            boat_license_date = st.date_input("Date boat last licensed/registered: ", value=None, key="boat_license_date")


    # OPTIONAL SAFETY EQUIPMENT
    with tab2:
        
        # User input of Operator Info
        st.subheader("Operator Info")
        competency_select = st.selectbox("Operator Competency? : ", options=["PCOC", "Proof of Course", "Rental Boat Checklist", "Marine Safety Certificate"], key="competency_select")
        
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
        

    # Diplay required safety devices and checkboxes
    with tab3:
        # is there a flare reduction?
        reduce = reduce_flares(radio_select, plb_select, epirb_select)
        if reduce:
            st.write("*** NOTE: Flare reduction applies ***")
        
        st.header("Required Safety Devices")
        
        # Display required safety devices by boat length and type
        # sailboats and powerboats only
        if boat_type in ["Sailboat", "Powerboat"]:
            if boat_name and boat_type and boat_length:
                common_devices = utils.get_common_devices(boat_length)
                for key, device in common_devices.items():
                    st.checkbox(device, key=key)

                required_devices = utils.get_required_safety_devices_by_length(boat_type, boat_length)
                for key, device in required_devices.items():
                    st.checkbox(device, key=key)

            # inflatable PFDs
            inflate_select = st.toggle("Inflatable PFDs?", value=False, key="inflate_select")
            if inflate_select:
                col11, col22 = st.columns([1, 15])  # Adjust the ratio for spacing
                with col22:
                    inlfate_approved_select = st.toggle("Transport Canada approved?", value=False, key="inflate_approved_select")
                    inflate_serviced_select = st.toggle("CO2 not expired?", value=False, key="inflate_serviced_select")
                    inflate_16_select = st.toggle("16 years or older?", value=False, key="inflate_16_select")
        else:
            # Personal Watercraft
            if boat_type == "Personal Watercraft":
                if boat_name and boat_type and boat_length:
                    required_devices = utils.get_required_safety_devices_by_length(boat_type, boat_length)
                    for key, device in required_devices.items():
                        st.checkbox(device, key=key)



        # Radio buttons for confirming presence of safety devices
        st.header("File Report")
        presence_confirmation = st.radio("Are all required safety devices present?", ("Yes, boat passes courtesy inspection", "No"))

        # Notes section
        notes = st.text_area("Additional Notes:", key="notes")

        col1, col2, col3 = st.columns(3)  # Create three columns
        with col1:
            if st.button("File Report", key="file_report"):
                # add boat and retrieve the unique boat id from the database
                boat_id = database.add_to_boat_table(boat_name, boat_type, motor, boat_length, boat_license_select, boat_license_date)

                # add optional equipment to the boat
                database.add_optional_equipment_to_boat(boat_id, equipment_id)

        #    save_inspection_data(boat_name, boat_type, boat_length, required_devices, presence_confirmation, notes, "Passed")
        #    st.success("Inspection Passed!")
        
        # if raft has a motor 10hp needs a license
        # license lasts 10 years, registration lasts 3 years


    col01, col02 = st.columns([3,1])  # Adjust the ratio for spacing
    with col02: 
        if st.button("Clear Form", key='"clear_form"'):
            reset_state_values()

if __name__ == "__main__":
    main()