NOT_FOUND = "NOT_FOUND"
def part1():
    answer = 0
    dic = {"five" : [],
           "four" : [],
           "full" : [],
           "three" : [],
           "two" : [],
           "one" : [],
           "high" : []}
    f = open("input_x", "r")
    for line in f:
        cards = line.split()[0]
        print(cards)
        if five_of_a_kind_check(cards) != NOT_FOUND:
            dic["five"].append("{},{}".format(cards, line.split()[1]))
            print("five found")
        elif four_of_a_kind_check(cards) != NOT_FOUND:
            dic["four"].append("{},{}".format(cards, line.split()[1]))
            print("four found")
        elif full_house_check(cards) != NOT_FOUND:
            dic["full"].append("{},{}".format(cards, line.split()[1]))
            print("full house found")
        elif three_of_a_kind_check(cards) != NOT_FOUND:
            dic["three"].append("{},{}".format(cards, line.split()[1]))
            print("three found")
        elif two_pair_check(cards) != NOT_FOUND:
            dic["two"].append("{},{}".format(cards, line.split()[1]))
            print("two pair found")
        elif one_pair_check(cards) != NOT_FOUND:
            dic["one"].append("{},{}".format(cards, line.split()[1]))
            print("one pair found")
        elif high_card_check(cards) != NOT_FOUND:
            dic["high"].append("{},{}".format(cards, line.split()[1]))
            print("high card found")
        print("=============")
    print(dic)
    return answer

def five_of_a_kind_check(cards):
    if cards.count(cards[0]) == 5:
        return cards[0]
    
    return "NOT_FOUND"

def four_of_a_kind_check(cards):
    for card in cards:
        if cards.count(card) == 4:
            return card
    
    return "NOT_FOUND"

def full_house_check(cards):
    if three_of_a_kind_check(cards) != NOT_FOUND:
        if one_pair_check(cards.replace(three_of_a_kind_check(cards),"", 3)) != NOT_FOUND:
            return True

    return "NOT_FOUND"

def three_of_a_kind_check(cards):
    for card in cards:
        if cards.count(card) == 3:
            return card 

    return "NOT_FOUND"

def one_pair_check(cards):
    # print("cards: []".format(cards))
    for card in cards:
        if cards.count(card) == 2:
            return card

    return "NOT_FOUND"

def two_pair_check(cards):
    # print("cards: [{}]".format(cards))
    if one_pair_check(cards) != NOT_FOUND:
        if one_pair_check(cards.replace(one_pair_check(cards), "", 2)) != NOT_FOUND:
            return True
    
    return NOT_FOUND

def high_card_check(cards):
    high_card_v = 2
    for card in cards:
        if card.isnumeric():
            cardv = int(card)
        else:
            if card == "A":
                cardv = 14
            elif card == "K":
                cardv = 13
            elif card == "Q":
                cardv = 12
            elif card == "J":
                cardv = 11
            elif card == "T":
                cardv = 10
        if high_card_v < cardv:
            high_card_v = cardv

    return high_card_v

def part2():
    pass

def main():
    print("part 1 : {} ".format(part1()))
    # print("part 2 : {} ".format(part2()))

if __name__ == "__main__":
    main()