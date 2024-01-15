NOT_FOUND = "NOT_FOUND"
def part1():
    dic = {"five" : [],
           "four" : [],
           "full" : [],
           "three" : [],
           "two" : [],
           "one" : [],
           "high" : []}
    f = open("input", "r")
    # f = open("input_x", "r")
    for line in f:
        cards = line.split()[0]
        print(cards)
        if five_of_a_kind_check(cards) != NOT_FOUND:
            dic["five"] = add_in_correct_order(dic["five"], "{},{}".format(cards, line.split()[1]))
            # print("five found")
        elif four_of_a_kind_check(cards) != NOT_FOUND:
            # print("four found")
            dic["four"] = add_in_correct_order(dic["four"], "{},{}".format(cards, line.split()[1]))
        elif full_house_check(cards) != NOT_FOUND:
            dic["full"] = add_in_correct_order(dic["full"], "{},{}".format(cards, line.split()[1]))
            # print("full house found")
        elif three_of_a_kind_check(cards) != NOT_FOUND:
            # print("three found")
            dic["three"] = add_in_correct_order(dic["three"], "{},{}".format(cards, line.split()[1]))
        elif two_pair_check(cards) != NOT_FOUND:
            dic["two"] = add_in_correct_order(dic["two"], "{},{}".format(cards, line.split()[1]))
            # print("two pair found")
        elif one_pair_check(cards) != NOT_FOUND:
            dic["one"] = add_in_correct_order(dic["one"], "{},{}".format(cards, line.split()[1]))
            # print("one pair found")
        elif high_card_check(cards) != NOT_FOUND:
            dic["high"] = add_in_correct_order(dic["high"], "{},{}".format(cards, line.split()[1]))
            # print("high card found")
        print("=============")
    # print(dic)
    answer = 0
    kinda_index = 1
    for section_index, section in enumerate(reversed(dic)):
        # print(section)
        if not dic[section]:
            print("nothing to see here")
        for part in (dic[section]):
            point = int(part.split(",")[1])
            # print("{} + ({} * {}) : cards = {}".format(answer, point, kinda_index, part.split(",")[0]))
            answer = answer + (point * kinda_index)
            kinda_index+=1
        # answer = answer + dic[section]
    print(answer) 
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

def return_cards_int_value(card):
        if card.isnumeric():
            return int(card)
        else:
            if card == "A":
                return 14
            elif card == "K":
                return 13
            elif card == "Q":
                return 12
            elif card == "J":
                return 11
            elif card == "T":
                return 10

def add_in_correct_order(listy, line):
    # print(type(listy))
    print("listy before added {}".format(listy))
    if not listy:
        return [line]
    for element_index, element in enumerate(listy):
        cards = element.split(",")[0]
        for char_index, char in enumerate(cards): 
            # print("cards: " + cards)
            # print("line split: " + line.split(",")[0])
            if return_cards_int_value(char) > return_cards_int_value(line.split(",")[0][char_index]):
                print("add ahead")
                print("listy before insert {}".format(listy))
                listy.insert(element_index, line)
                print("listy after insert {}".format(listy))
                return listy
            elif return_cards_int_value(char) == return_cards_int_value(line.split(",")[0][char_index]):
                print("go to the next element")
            else:
                print("{} and {} compared".format(char, return_cards_int_value(line.split(",")[0][char_index])))
                break
                # print("add behind")
                # listy.insert(element_index + 1, line)
                # return listy
    listy.append(line)
    print("at the end of the list for {}".format(line))
    return listy



def part2():
    pass

def main():
    print("part 1 : {} ".format(part1()))
    # print("part 2 : {} ".format(part2()))

if __name__ == "__main__":
    main()