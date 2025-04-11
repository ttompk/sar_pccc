global flare_reduction
flare_reduction = False

def reduce_flares(radio_select, plb_select, epirb_select):
    global flare_reduction
    if radio_select == 'Yes' or plb_select == 'Yes' or epirb_select == 'Yes':
        flare_reduction = True
    else: 
        flare_reduction = False
    return flare_reduction

def get_flare_reduction():
    return flare_reduction