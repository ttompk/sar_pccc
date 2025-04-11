global flare_reduction
flare_reduction = False

def reduce_flares(radio_select, plb_select, epirb_select):
    global flare_reduction
    if radio_select == True or plb_select == True or epirb_select == True:
        flare_reduction = True
    else: 
        flare_reduction = False
    return flare_reduction

def get_flare_reduction():
    global flare_reduction
    return flare_reduction