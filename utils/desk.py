def create_card(rank:str,suite:str) -> dict:
    if rank=="a":
        value="14"
    elif rank=="j":
        value="11"
    elif rank=="Q":
        value="12"
    elif rank=="k":
        value="13"
    else:
        value=rank
    card={"rank":str(rank), "suite":str(suite), "value":value}
    return card
def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card["value"] > p2_card["value"]:
        return "p1 win"
    elif p1_card["value"] < p2_card["value"]:
        return "p2 win"
    else:
        return "war"
def create_deck() -> list[dict]:
    cards = []
    rank1=["A",'2','3','4','5','6','7','8','9','J','Q','K']
    suite1=['S','D','H','C']
    j=0
    for i in range(len(rank1)):
        for j in range(len(suite1)):
            cards.append(create_card(rank1[i],suite1[j]))
    return cards
def shuffle(deck:list[dict]) -> list[dict]:
    import random
    for i in range(1000):
        index1 = (random.randrange(1, 54))
        index2 = (random.randrange(1, 54))
        if index1 == index2:
            continue
        deck[index1], deck[index2] = deck[index2], deck[index1]
    return deck