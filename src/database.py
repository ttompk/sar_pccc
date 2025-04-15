from sqlalchemy import create_engine, Column, Integer, String, Float, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment or .env file")

Base = declarative_base()

#create database 'engine'
engine = create_engine(DATABASE_URL, echo=True)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Function to get a new session
def get_session():
    return Session()


# add a boat to db
def add_to_boat_table(boat_name, boat_type, motor, boat_length, boat_license_select, boat_license_date, tender_select, operator_card):
    session = get_session()
    try: 
        query = text('''
                    INSERT INTO boats (name, type, motorized, length, license_status, license_date, tender_motor, operator_card) 
                    VALUES (:boat_name, :boat_type, :motor, :boat_length, :boat_license_select, :boat_license_date, :tender_select, :operator_card)
                    RETURNING id;
                    ''')
        result = result = session.execute(query, {
                "boat_name": boat_name,
                "boat_type": boat_type,
                "motor": motor,
                "boat_length": boat_length,
                "boat_license_select": boat_license_select,
                "boat_license_date": boat_license_date,
                "tender_select": tender_select,
                "operator_card": operator_card
            })
        boat_id = result.scalar()  # Retrieve the returned ID
        session.commit()
        return boat_id
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def add_optional_equipment_to_boat(boat_id, optional_eq):
    session = get_session()
    try:
        # each piece of eqiupment is associated with a id in teh database
        for equipment_name, value in optional_eq.items():
            if equipment_name is None:
                raise ValueError(f"No equipment ID found for boat type: {optional_eq}")
            
            query = text("""
                INSERT INTO boat_optional_equipment (boat_id, equipment_name, equipment_status)
                VALUES (:boat_id, :equipment_name, :value);
            """)
            session.execute(query, {
                "boat_id": boat_id, 
                "equipment_name": equipment_name, 
                "value": value})
            session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def add_inspection_info_to_db(boat_id, inspector_name, pass_fail, notes):
    session = get_session()
    try:
        query = text("""
            INSERT INTO inspections (boat_id, inspector_name, status, notes)
            VALUES (:boat_id, :inspector_name, :pass_fail, :notes)
            RETURNING id;
        """)
        result = session.execute(query, {
            "boat_id": boat_id,
            "inspector_name": inspector_name,
            "pass_fail": pass_fail,
            "notes": notes
        })
        inspection_id = result.scalar()  # Retrieve the returned ID
        session.commit()
        return inspection_id
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def add_safety_device(inspection_id, device_name, device_desr, is_present):
    session = get_session()
    try:
        query = text("""
            INSERT INTO inspection_devices (inspection_id, device_name, device_descr, is_present)
            VALUES (:inspection_id, :device_name, :device_descr, :is_present);
        """)
        session.execute(query, {
            "inspection_id": inspection_id,
            "device_name": device_name,
            "device_descr": device_desr,
            "is_present": is_present
        })
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def add_operator_info_to_db(boat_id, inspection_id, competency_select, roc_select, hypo_select, heave_select, sailplan_select, co_select,operator_email):
    session = get_session()
    try:
        query = text("""
            INSERT INTO boat_user (boat_id, inspection_id, operator_card, roc, hypothermia, heave_line, sail_plan, carbon_monoxide, operator_email)
            VALUES (:boat_id, :inspection_id, :competency_select, :roc_select, :hypo_select, :heave_select, :sailplan_select, :co_select, :operator_email);
        """)
        session.execute(query, {
            "boat_id": boat_id,
            "inspection_id": inspection_id,
            "competency_select": competency_select,
            "roc_select": roc_select,
            "hypo_select": hypo_select,
            "heave_select": heave_select,
            "sailplan_select": sailplan_select,
            "co_select": co_select,
            "operator_email": operator_email
        })
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
