
import helper

def get_required_safety_devices(boat_type, boat_length):
    safety_devices = {
        'sailboat': ['Life jackets', 'Flares', 'Fire extinguisher'],
        'motorboat': ['Life jackets', 'Fire extinguisher', 'First aid kit'],
        'personal watercraft': ['Life jackets', 'Fire extinguisher', 'First aid kit'],
    }
    
    if boat_type in safety_devices:
        required_devices = safety_devices[boat_type]
        
        if boat_length > 20:
            required_devices.append('EPIRB')
        
        return required_devices
    else:
        return []  # No safety devices required for unknown boat types

def validate_safety_devices(user_devices, required_devices):
    return all(device in user_devices for device in required_devices)

# personal lifesaving appliances, visual signals, vessel safety equipment, 
# # navigation equipment, fire fighting equipment
print(helper.get_flare_reduction())

def flare_count(flares):
    # reduce the number of flares if radio present
    if helper.get_flare_reduction():
        if flares == 1:
            return "1"
        elif flares == 3:
            return "2"
        else:
            n_flares = flares / 2
        return str(int(n_flares))
    else: 
        return str(int(flares))


# required safety devices by length and type
def get_required_safety_devices_by_length(boat_type, boat_length):
    if boat_type == 'Sailboat' or boat_type == 'Powerboat':
        # Sailboats and powerboats have similar requirements
        if boat_length < 20:  # 6m
            return ['Life jackets: meet requirements', 
                    'Reboarding Device: 1 (if freeboard is 0.5m (1ft 8in) or more)', 
                    'Bouyant heaving line: 15m', 
                    f'Watertight flashlight OR flares: {flare_count(3)}  (up to {flare_count(1)} type D)', 
                    'Manual propelling device OR anchor: 15m', 
                    'Bailer OR manual bilge pump: 1', 
                    'Sound signalling device: 1',
                    'Navigation lights',
                    'Magnetic compass: 1',
                    'Radar reflector: 1',
                    'Fire extinguisher: 1  (type 5BC, if equipped with an inboard engine, a fixed fuel tank of any size, or a fuelburning cooking, heating or refrigerating appliance) ']
        elif boat_length >= 20 and boat_length <= 29.5:   # 6m to 9m
            return ['Life jackets: meet requirements', 
                    'Reboarding Device: 1', 
                    'Bouyant heaving line: 15m OR lifebouy attached to a buoyant line: 15m', 
                    'Watertight flashlight: 1',
                    f'Flares: {flare_count(6)}  (up to {flare_count(2)} type D)', 
                    'Manual propelling device OR anchor: 15m rode', 
                    'Bailer OR manual bilge pump: 1', 
                    'Sound signalling device: 1',
                    'Navigation lights',
                    'Magnetic compass: 1',
                    'Radar reflector: 1',
                    'Fire extinguisher: 1  (type 5BC, if equipped with a motor)',
                    'Fire extinguisher: 1  (type 5BC, if equipped with a fuel-burning cooking, heating or refrigerating appliance) ']
        elif boat_length > 29.5 and boat_length < 39.5:     # 9m to 12m
            return ['Life jackets: meet requirements', 
                    'Reboarding Device: 1', 
                    'Bouyant heaving line: 15m',
                    'Lifebouy attached to a buoyant line: 15m', 
                    'Watertight flashlight: 1',
                    f'Flares: {flare_count(12)}  (up to {flare_count(6)} type D)', 
                    'Anchor: 30m rode (98ft 5in)', 
                    'Manual bilge pump: 1 OR bilge-pumping arrangements', 
                    'Sound signalling device: 1',
                    'Navigation lights',
                    'Magnetic compass: 1',
                    'Radar reflector: 1',
                    'Fire extinguisher: 1  (type 10BC, if equipped with a motor)',
                    'Fire extinguisher: 1  (type 10BC, if equipped with a fuel-burning cooking, heating or refrigerating appliance) ']
        elif boat_length > 39.5 and boat_length < 78.8:     # 12m to 24m
            return ['Life jackets: meet requirements', 
                    'Reboarding Device: 1', 
                    'Bouyant heaving line: 15m',
                    'Lifebouy: must have self-igniting light OR attached to a buoyant line: 15m', 
                    'Watertight flashlight: 1',
                    f'Flares: {flare_count(12)}  (up to {flare_count(6)} type D)', 
                    'Anchor: 50m (98ft 5in)', 
                    'Bilge-pumping arrangements', 
                    'Sound signalling device: 1 (2 required if boat 20m and over that meets applicable statndards)',
                    'Navigation lights',
                    'Magnetic compass: 1',
                    'Radar reflector: 1',
                    'Fire extinguisher: 1  (type 10BC, at access to machinery space)',
                    'Fire extinguisher: 1  (type 10BC, at access to any accommodation space)',
                    'Fire extinguisher: 1  (type 10BC, at access to any fuel-burning cooking, heating or refrigerating appliance) ',
                    'Axe: 1,'
                    'Bucket: 2 (of at least 10L each)']
        elif boat_length > 78.8:     # 12m to 24m
            return ['Life jackets: meet requirements', 
                    'Reboarding Device: 1', 
                    'Bouyant heaving line: 30m',
                    'SOLAS lifebuoy: 1 (attached to a 30m buoyant line)',
                    'SOLAS lifebuoy: 1 (equipped with a self-igniting light)',
                    'Lifting harness with appropriate rigging', 
                    'Watertight flashlight: 1',
                    f'Flares: {flare_count(12)}  (up to {flare_count(6)} type D)', 
                    'Anchor: 50m (98ft 5in)', 
                    'Bilge-pumping arrangements', 
                    'Sound signalling devices: 2',
                    'Navigation lights',
                    'Magnetic compass: 1',
                    'Radar reflector: 1',
                    'Fire extinguisher: 1  (type 10BC, at access to machinery space)',
                    'Fire extinguisher: 1  (type 10BC, at access to any accommodation space)',
                    'Fire extinguisher: 1  (type 10BC, at access to any fuel-burning cooking, heating or refrigerating appliance) ',
                    'Power-driven fire pump: 1 (located outside the machinery space, with one fire hose and nozzle that can direct water into any part of the boat)',
                    'Axe: 2,'
                    'Bucket: 4 (of at least 10L each)']

    elif boat_type == 'personal watercraft':
        if boat_length < 20:
            return ['Life jackets']
        elif 20 <= boat_length <= 30:
            return ['Life jackets', 'Fire extinguisher']
        else:
            return ['Life jackets', 'Fire extinguisher', 'First aid kit']
    else:
        return []  # No safety devices required for unknown boat types
    

    # All boats: compliance notice, hull serial number, license or registration

    # compliance notices
    '''
    Compliance notices are the manufacturers or importers confirmation that
    the vessel is built according to the Small Vessel Regulations construction
    requirements (see CONSTRUCTION REQUIREMENTS section). Before
    attaching a compliance notice to a vessel, a manufacturer or importer must
    provide Transport Canada with a declaration of conformity for the vessel.
    The Small Vessel Regulations require, with a few exceptions, that all
    pleasure craft of less than 24 metres, that are or can be fitted with a motor,
    have a compliance notice affixed to them in a location visible from the helm.
    Although no law prohibits you from having other types of compliance
    notices affixed to your vessel, you must have an affixed Canadian
    compliance notice if your boat was bought in Canada.
    Compliance notices for pleasure craft up to 6 m (19 feet 8 inches) also have
    information on recommended maximum safe limits. These recommended
    maximum safe limits will tell you:
    • what motor sizes are safe (outboard powered vessels only);
    • how many people can be on board; and
    • how much weight the boat can hold.
    '''

    # hull serial number
    '''All pleasure craft made in Canada, or imported into Canada after
    August 1, 1981 (with or without a motor), must have a hull serial number.
    This number helps to find lost or stolen boats and boats that are subject
    to a recall. The hull serial number must be permanently marked on the
    outside upper starboard (right side) corner of the transom (the boat’s rear,
    flat end – above the waterline), or as close to that area as possible. It is
    12 digits long and each character must be at least 6 mm (¼”) in height
    and width.
    '''

    # license or registration
    ''' 
    If you operate or keep your boat mostly in Canada, and it is powered by
    one or more motors adding up to 7.5 kW (10 hp) or more, you must get it
    licensed, unless you register it. You must also license dinghies or tenders
    you carry aboard or tow behind a larger boat.
    A pleasure craft licence is a document giving your boat a unique licence
    number that is valid for 10 years. The Pleasure Craft Licensing System
    allows Search and Rescue personnel to access information about your boat
    24 hours a day, seven days a week in the event of an emergency. This could
    mean the difference between life and death! If your boat does not need a
    pleasure craft licence, you can choose to get one for safety reasons.

    You must display the pleasure craft licence number on your boat:
    • on both sides of the bow;
    • above the waterline;
    • as far forward as practical; and
    • where it is easy to see.
    The characters must be:
    • in block letters;
    • at least 7.5 cm (3”) high; and
    • of a colour that contrasts with the background.

    Registration is proof of ownership. If registred then no need to license.
    '''

    # PCOC
    ''' part of safety check?'''

