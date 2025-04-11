import streamlit as st
#from database import save_inspection_data
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
    st.title("Boat Inspection App")
    
    # Create three columns
    #col1, col2, col3 = st.columns(3)
    tab1, tab2 = st.tabs(["Basic Info", "Required Safety Devices"])

    # User input for boat details
    with tab1:
        st.header("Basic Info")
        boat_name = st.text_input("Boat Name:", key="boat_name" )
        boat_type = st.radio("Boat Type:", ["Sailboat", "Powerboat", "Personal Watercraft"], key="boat_type")
        if boat_type == "Sailboat":
            motor = st.radio("Is there a motor?", ["Yes", "No"], key="motor")
        else:
            motor = "No"
    
        boat_length = st.number_input("Enter Boat Length (in feet):", min_value=1, key="boat_length")

        # The following affects the number of flares required
        radio_select = st.radio("VHF radio?: ", ["Yes", "No"], key="radio_select")
        plb_select = st.radio("Operator wears a personal locator beacon? : ", ["Yes", "No"], key="plb_select")
        epirb_select = st.radio("EPIRB? : ", ["Yes", "No"], key="epirb_select")

    with tab2:
        # is there a flare reduction?
        reduce = reduce_flares(radio_select, plb_select, epirb_select)
        if reduce:
            st.write("*** NOTE: Flare reduction applies ***")
        
        # Display required safety devices
        if boat_name and boat_type and boat_length:
            required_devices = utils.get_required_safety_devices_by_length(boat_type, boat_length)
            st.header("Required Safety Devices")
            for device in required_devices:
                st.checkbox(device, key=device)

        # Radio buttons for confirming presence of safety devices
        st.header("Confirm Presence of Safety Devices")
        presence_confirmation = st.radio("Are all required safety devices present?", ("Yes", "No"))

        # Notes section
        notes = st.text_area("Additional Notes:", key="notes")

    # Add a "Clear Form" button
    if st.button("Clear Form"):
        # Reset all session state variables
        st.session_state["boat_name"] = ""
        st.session_state["boat_type"] = "Sailboat"
        st.session_state["motor"] = "No"
        st.session_state["boat_length"] = 1
        st.session_state["radio_select"] = "No"
        st.session_state["plb_select"] = "No"
        st.session_state["epirb_select"] = "No"
        st.session_state["notes"] = ""
        st.experimental_rerun()  # Rerun the app to reflect the cleared state


    # uncomment the following code block once database set up
    '''
    # Inspection result buttons
    if st.button("Pass Inspection"):
        save_inspection_data(boat_name, boat_type, boat_length, required_devices, presence_confirmation, notes, "Passed")
        st.success("Inspection Passed!")

    if st.button("Fail Inspection"):
        failure_reason = st.text_area("Reason for Failure:")
        save_inspection_data(boat_name, boat_type, boat_length, required_devices, presence_confirmation, notes, "Failed", failure_reason)
        st.error("Inspection Failed!")
    '''

if __name__ == "__main__":
    main()