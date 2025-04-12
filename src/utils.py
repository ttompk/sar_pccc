import helper

def validate_safety_devices(user_devices, required_devices):
    return all(device in user_devices for device in required_devices)

def flare_count(flares: int):
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

def heaving_line_length(boat_length):
    if boat_length >= 78.8:
        return str(30)
    else:
        return str(15)

def compass_extra(boat_length): 
    if boat_length <= 26.247:   # 8m
        return "[not required if less than 8m (26ft 3 in) and within sight of navigation marks]"
    else:
        return ''

def radar_extra(boat_length):
    if boat_length <= 20:   # 8m
        return "[not required if the small size of the boat OR its operation away from radar navigation makes it impossible to install or use a radar reflector.]"
    else:
        return ''

# required safety devices by length and type

# common devices
def get_common_devices(boat_length): 
    return {'jacket': 'Life jackets: one for every person, transport canada approved, not modified, not damaged', 
            'reboard': 'Reboarding Device: 1 [if freeboard is 0.5m (1ft 8in) or more]', 
            'line': f'Bouyant heaving line: {heaving_line_length(boat_length)}m',
            'radar': f'Radar reflector: 1 [mounted properly?] {radar_extra(boat_length)}',
            'nav': 'Navigation lights present and operational',
            'compass': f'Magnetic compass: 1 {compass_extra(boat_length)}'}

def get_required_safety_devices_by_length(boat_type, boat_length):
    if boat_type == 'Sailboat' or boat_type == 'Powerboat':
        # Sailboats and powerboats have similar requirements
        if boat_length < 20:  # 6m
            return {'flare': f'Watertight flashlight OR flares: {flare_count(3)}  (up to {flare_count(1)} type D)', 
                    'prop': 'Manual propelling device OR anchor: 15m', 
                    'bilge': 'Bailer OR manual bilge pump: 1', 
                    'sound': 'Sound signalling device: 1',
                    'fire':'Fire extinguisher: 1 = type 5BC [required if equipped with an inboard engine OR a fixed fuel tank of any size OR a fuelburning cooking, heating or refrigerating appliance] '}
        elif boat_length >= 20 and boat_length <= 29.5:   # 6m to 9m
            return {'buoy': 'IF no heaving line, lifebouy attached to a buoyant line: 15m', 
                    'flashlight': 'Watertight flashlight: 1',
                    'flare': f'Flares: {flare_count(6)}  (up to {flare_count(2)} type D)', 
                    'prop': 'Manual propelling device OR anchor: 15m rode', 
                    'bilge': 'Bailer OR manual bilge pump: 1', 
                    'sound': 'Sound signalling device: 1',
                    'fire1': 'Fire extinguisher: 1  (type 5BC, if equipped with a motor)',
                    'fire2': 'Fire extinguisher: 1  (type 5BC, if equipped with a fuel-burning cooking, heating or refrigerating appliance) '}
        elif boat_length > 29.5 and boat_length < 39.5:     # 9m to 12m
            return {'buoy': 'Lifebouy attached to a buoyant line: 15m', 
                    'flashlight': 'Watertight flashlight: 1',
                    'flare': f'Flares: {flare_count(12)}  (up to {flare_count(6)} type D)', 
                    'anchor': 'Anchor: 30m rode (98ft 5in)', 
                    'bilge': 'Manual bilge pump: 1 OR bilge-pumping arrangements', 
                    'sound': 'Sound signalling device: 1',
                    'fire1': 'Fire extinguisher: 1  (type 10BC, if equipped with a motor)',
                    'fire2': 'Fire extinguisher: 1  (type 10BC, if equipped with a fuel-burning cooking, heating or refrigerating appliance) '}
        elif boat_length > 39.5 and boat_length < 78.8:     # 12m to 24m
            return {'buoy': 'Lifebouy: must have self-igniting light OR attached to a buoyant line: 15m', 
                    'flashlight': 'Watertight flashlight: 1',
                    'flare': f'Flares: {flare_count(12)}  (up to {flare_count(6)} type D)', 
                    'anchor': 'Anchor: 50m rode (164ft)', 
                    'bilge': 'Bilge-pumping arrangements', 
                    'sound': 'Sound signalling device: 1 [2 required if boat 20m and over] [devices meet applicable standards in collision regulations]',
                    'fire1': 'Fire extinguisher: 1  (type 10BC, at access to machinery space)',
                    'fire2': 'Fire extinguisher: 1  (type 10BC, at access to any accommodation space)',
                    'fire3': 'Fire extinguisher: 1  (type 10BC, at access to any fuel-burning cooking, heating or refrigerating appliance) ',
                    'axe': 'Axe: 1',
                    'bucket': 'Bucket: 2 (of at least 10L each). Must be dedicated as a fire bucket.'}
        elif boat_length >= 78.8:     # > 24m
            return {'buoy1': 'SOLAS lifebuoy: 1 (attached to a 30m buoyant line)',
                    'buoy2': 'SOLAS lifebuoy: 1 (equipped with a self-igniting light)',
                    'harness': 'Lifting harness with appropriate rigging', 
                    'flashlight': 'Watertight flashlight: 1',
                    'flare': f'Flares: {flare_count(12)}  (up to {flare_count(6)} type D)', 
                    'anchor': 'Anchor: 50m rode (164ft)', 
                    'bilge': 'Bilge-pumping arrangements', 
                    'sound': 'Sound signalling devices: 2 [devices meet applicable standards in collision regulations]',
                    'faire1': 'Fire extinguisher: 1  (type 10BC, at access to machinery space)',
                    'fire2': 'Fire extinguisher: 1  (type 10BC, at access to any accommodation space)',
                    'fire3': 'Fire extinguisher: 1  (type 10BC, at access to any fuel-burning cooking, heating or refrigerating appliance) ',
                    'fire4': 'Power-driven fire pump: 1 (located outside the machinery space, with one fire hose and nozzle that can direct water into any part of the boat)',
                    'axe': 'Axe: 2',
                    'bucket': 'Bucket: 4 (of at least 10L each). Must be dedicated as a fire bucket.'}

    elif boat_type == 'Personal Watercraft':
        return {'jacket': 'Life jackets:  one for every person, inflatable NOT allowed, transport canada approved, not modified, not damaged',
                'sound': 'Sound signalling device: 1',
                'flare': 'Watertight flashlight OR Flares: 3 (up to 1 type D)', 
                'compass': 'Magnetic compass: 1 [if out of sight of navigation marks]',
                'nav': 'Navigation lights present and operational [if operating after sunset, before sunrise or in periods of restricted visibility (fog, falling snow, etc.)]'}     
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

