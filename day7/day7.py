def part1():
    answer = 0
    NOT_FOUND = "NOT_FOUND"
    f = open("input_x", "r")
    for line in f:
        cards = line.split()[0]
        if five_of_a_kind_check(cards) != NOT_FOUND:
            print("five found")
        elif four_of_a_kind_check(cards) != NOT_FOUND:
            print("four found")
        elif full_house_check(cards) != NOT_FOUND:
            print("full house found")
        elif three_of_a_kind_check(cards) != NOT_FOUND:
            print("three found")

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
    print(cards)
    if three_of_a_kind_check(cards):
        cards.replace(cards[0],"")
        if one_pair_check(cards):
            return True

    return "NOT_FOUND"

def three_of_a_kind_check(cards):
    for card in cards:
        if cards.count(card) == 3:
            return card 

    return "NOT_FOUND"

def one_pair_check(cards):
    for card in cards:
        if cards.count(card) == 2:
            return card

    return "NOT_FOUND"

def part2():
    pass

def main():
    print("part 1 : {} ".format(part1()))
    # print("part 2 : {} ".format(part2()))

if __name__ == "__main__":
    main()