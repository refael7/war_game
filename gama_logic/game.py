def create_player(name:str) -> dict:

    if name.strip()=="":
        nams={"name": "ai","hand": [], "won_pile": []}
    else:
        nams = {"name":name,"hand": [], "won_pile": []}
    return nams
def init_game()->dict:


    return {}
def play_round(p1:dict,p2:dict):
    return {}


print(create_player("refael"))