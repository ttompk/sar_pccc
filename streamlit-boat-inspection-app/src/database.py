from sqlalchemy import create_engine, Column, Integer, String, Float, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

'''
DATABASE_URL = os.getenv('DATABASE_URL')

Base = declarative_base()

#create daabase 'engine'
engine = create_engine(DATABASE_URL, echo=True)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Function to get a new session
def get_session():
    return Session()
'''


# add a boat to db
def add_to_boat_table(boat_name, boat_type, motor, boat_length, boat_license_select, boat_license_date):
    session = get_session()
    try: 
        query = text('''
                    INSERT INTO boats (name, type, motorized, length, license_status, license_date) 
                    VALUES (boat_name, boat_type, motor, boat_length, boat_license_select, boat_license_date)
                    RETURNING id;
                    ''')
        result = result = session.execute(query, {
                "boat_name": boat_name,
                "boat_type": boat_type,
                "motor": motor,
                "boat_length": boat_length,
                "license_status": boat_license_select,
                "license_date": boat_license_date
            })
        boat_id = result.scalar()  # Retrieve the returned ID
        session.commit()
        return boat_id
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def add_optional_equipment_to_boat(boat_id, eq):
    session = get_session()
    try:
        # Retrieve the equipment_id based on the equipment
        equipment_id = return_equip_id(eq)
        if equipment_id is None:
            raise ValueError(f"No equipment ID found for boat type: {eq}")

        query = text("""
            INSERT INTO boat_optional_equipment (boat_id, equipment_id)
            VALUES (:boat_id, :equipment_id);
        """)
        session.execute(query, {"boat_id": boat_id, "equipment_id": equipment_id})
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def return_equip_id():
    # optional equipment map to these ids in the database
    equipment_id_dict = {1: 'radio_select', 2: 'epirb', 3: 'plb', 4: 'ais', 5: 'charts', 6: 'chart_date'}


# add safety devices
'''
INSERT INTO safety_devices (name, description)
VALUES ('Life Jacket', 'Transport Canada approved life jacket for each person'),
       ('Fire Extinguisher', 'Type 5BC fire extinguisher');
'''

# add inspection
'''
INSERT INTO inspections (boat_id, inspector_name, status, failure_reason, notes)
VALUES (1, 'John Doe', 'Pass', NULL, 'All safety devices present');
'''

# record safety devices for the inspection
'''
INSERT INTO inspection_devices (inspection_id, device_id, is_present)
VALUES (1, 1, TRUE),  -- Life Jacket present
       (1, 2, TRUE); -- Fire Extinguisher present
'''

# connect the optional equipemnt to the boat
''''
-- Assume Boat ID 1 exists
-- Associate Boat ID 1 with Equipment IDs 1 (First Aid Kit) and 2 (Radar Reflector)
INSERT INTO boat_optional_equipment (boat_id, equipment_id)
VALUES 
    (1, 1),
    (1, 2);
'''