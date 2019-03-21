import time
import os
class Player:

    def __init__(self, name, cards, balance=1000, last_bet=0, code=0, a=0, b=0, c=0, d=0, e=0):
        self.name = name
        self.cards = cards
        self.balance = balance
        self.last_bet = last_bet
        self.code = code
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.flushcard = [a, b, c, d, e]

    def setflush(self, anew, bnew, cnew, dnew, enew):
        self.flushcard = [anew, bnew, cnew, dnew, enew]

    def newcode(self, newcode):
        self.code = newcode

    def bet(self, bet):
        if self.balance >= bet:
            self.balance -= bet
            self.last_bet += bet
            print(self.name, 'bet for', bet)
            print('Amount of money left:', self.balance, '\n')
        elif self.balance < bet:
            print('Cannot bet, balance is too small')

    def earn(self, earn):
        self.balance += earn
        print(self.name, 'earn', earn)
        print('Amount of money left', self.balance)
        
    def newlastbet(self,newlastbet):
        self.last_bet = newlastbet

def poker_carddistribution():
    from random import shuffle,randint
    list_of_cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    cardtype = ['diamond', 'clover', 'heart', 'spade']
    cardcombination = []
    for i in list_of_cards:
        for j in cardtype:
            a = [i, j]
            cardcombination.append(' '.join(a))
    shuffle(cardcombination)
    while True:
        try:
            amountOfPlayer = int(input('Enter the amount of player: '))
        except:
            print('Please enter an integer')
            continue
        else:
            break
    playerlist=[]
    tablecards=[]
    for i in range(amountOfPlayer):
        a=[]
        for b in range(0,2):
            cards = randint(0,len(cardcombination)-1)
            a.append(cardcombination[cards])
            cardcombination.pop(cards)
        playerlist.append(Player(('player' + str(i + 1)), a))
    for num in range(0,5):
        cards = randint(0,len(cardcombination)-1)
        tablecards.append(cardcombination[cards])
        cardcombination.pop(cards)
    return playerlist,tablecards

def poker_bet_stats(betting_amount,table_maxbet,playerlist,i,tablebet,bet_counting,check_counting,turn):
    if playerlist[i].last_bet == 0:
        tablebet += betting_amount+table_maxbet
        playerlist[i].bet(betting_amount+table_maxbet)
        table_maxbet += betting_amount
        bet_counting = 0
        check_counting = 0
    else:
        tablebet += (betting_amount+table_maxbet-playerlist[i].last_bet)
        playerlist[i].bet(betting_amount+table_maxbet-playerlist[i].last_bet)
        table_maxbet += betting_amount
        bet_counting = 0
        check_counting = 0

    return tablebet,table_maxbet,bet_counting,check_counting 

def poker_allin_stats(table_maxbet,tablebet,playerlist,i,bet_counting,turn):
    if table_maxbet == 0:
        table_maxbet += playerlist[i].balance
        tablebet += playerlist[i].balance
        playerlist[i].bet(playerlist[i].balance)
        bet_counting = 0

    elif table_maxbet > 0:
        if playerlist[i].balance >= (table_maxbet-playerlist[i].last_bet):
            tablebet += playerlist[i].balance
            table_maxbet = playerlist[i].balance - (table_maxbet-playerlist[i].last_bet)
            playerlist[i].bet(playerlist[i].balance)
            bet_counting = 0
        else:
            print("You don't have enough money for ALL-IN!")
            print("You have folded")
            turn.pop(turn.index(i))
    return tablebet,table_maxbet,bet_counting,turn

def turn_statement(playerlist,i,tablebet,table_maxbet):
    #this function states which turn is it at that time and other sort of informations
    time.sleep(1)
    os.system('cls')
    print(playerlist[i].name, 'turn')
    print("Player's cards are",playerlist[i].cards)
    print(playerlist[i].name, 'balance:', playerlist[i].balance)
    print('Current bet:', table_maxbet)
    print('Current money on the table is:', tablebet)

# library for combos
def combo(playerlist, tablecards):
    list_of_straight = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    list_of_straight_full = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    flush_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for i in playerlist:

        combinationNumber = []
        combinationSymbol = []
        combinationNumber.append(((i.cards)[0].split())[0])
        combinationNumber.append(((i.cards)[1].split())[0])
        combinationSymbol.append(((i.cards)[0].split())[1])
        combinationSymbol.append(((i.cards)[1].split())[1])

        for j in tablecards:
            combinationNumber.append((j.split())[0])
            combinationSymbol.append((j.split())[1])

        combinationNumber_sorted = []
        for k in list_of_straight:
            for j in combinationNumber:
                if j == k:
                    combinationNumber_sorted.append(j)
                else:
                    continue

        k = 0
        a = []
        straight_list = []
        while k < len(combinationNumber_sorted):
            if k == 0:
                a.append(combinationNumber_sorted[k])
            elif combinationNumber_sorted[k] == combinationNumber_sorted[k - 1]:
                a.append(combinationNumber_sorted[k])
            elif combinationNumber_sorted[k] != combinationNumber_sorted[k - 1]:
                straight_list.append(a[0])
                a = []
                a.append(combinationNumber_sorted[k])
            if k == len(combinationNumber_sorted) - 1:
                straight_list.append(a[0])
            k += 1

        # generate for straight
        combinationNumber_sorted_straight = []
        for k in list_of_straight_full:
            for j in combinationNumber:
                if j == k:
                    combinationNumber_sorted_straight.append(j)
                else:
                    continue

        k = 0
        a = []
        straight_list_full = []
        while k < len(combinationNumber_sorted_straight):
            if k == 0:
                a.append(combinationNumber_sorted_straight[k])
            elif combinationNumber_sorted_straight[k] == combinationNumber_sorted_straight[k - 1]:
                a.append(combinationNumber_sorted_straight[k])
            elif combinationNumber_sorted_straight[k] != combinationNumber_sorted_straight[k - 1]:
                straight_list_full.append(a[0])
                a = []
                a.append(combinationNumber_sorted_straight[k])
            if k == len(combinationNumber_sorted_straight) - 1:
                straight_list_full.append(a[0])
            k += 1

        k = 0
        a = []
        number_group = []
        while k < len(combinationNumber_sorted):
            if k == 0:
                a.append(combinationNumber_sorted[k])
            elif combinationNumber_sorted[k] == combinationNumber_sorted[k - 1]:
                a.append(combinationNumber_sorted[k])
            elif combinationNumber_sorted[k] != combinationNumber_sorted[k - 1]:
                number_group.append(a)
                a = []
                a.append(combinationNumber_sorted[k])
            if k == len(combinationNumber_sorted) - 1:
                number_group.append(a)
            k += 1

        sortedcombinationSymbol = []

        for v in ['diamond', 'clover', 'heart', 'spade']:
            for index in combinationSymbol:
                if index == v:
                    sortedcombinationSymbol.append(index)
                else:
                    continue

        n = 0
        c = []
        symbol_group = []
        while n < len(sortedcombinationSymbol):
            if n == 0:
                c.append(sortedcombinationSymbol[n])
            elif sortedcombinationSymbol[n] == sortedcombinationSymbol[n - 1]:
                c.append(sortedcombinationSymbol[n])
            elif sortedcombinationSymbol[n] != sortedcombinationSymbol[n - 1]:
                symbol_group.append(c)
                c = []
                c.append(sortedcombinationSymbol[n])
            if n == len(sortedcombinationSymbol) - 1:
                symbol_group.append(c)
            n += 1

        # pair
        pair_count = 0
        threeofakind_count = 0
        fourofakind_count = 0
        for m in number_group:
            if len(m) == 2:
                pair_count += 1
            elif len(m) == 3:
                threeofakind_count += 1
            elif len(m) == 4:
                fourofakind_count += 1

        # find flush
        flush_counting_number = 0
        for yth in symbol_group:
            if len(yth) >= 5:
                flush_counting_number += 1
            else:
                continue

        # highcard
        if pair_count == 0:
            high_card_counting = 1
            for y in list_of_straight:
                for x in straight_list:
                    if y == x:
                        i.newcode(high_card_counting)
                high_card_counting += 1
        # single pair
        if pair_count == 1:
            singla_pair_counting = 14
            for y in list_of_straight:
                for x in number_group:
                    if len(x) == 2 and y == x[0]:
                        i.newcode(singla_pair_counting)
                singla_pair_counting += 1

        # double pair
        if pair_count >= 2:
            double_pair_list = []
            double_pair_list_temporary_index = []
            double_pair_list_index = []
            for m in number_group:
                if len(m) == 2:
                    double_pair_list.append(m[0])
            for m in double_pair_list:
                double_pair_list_temporary_index.append(flush_list.index(m))
            double_pair_list_temporary_index.sort()
            for m in double_pair_list_temporary_index:
                if m == double_pair_list_temporary_index[len(double_pair_list_temporary_index) - 2]:
                    double_pair_list_index.append(m)
                elif m == double_pair_list_temporary_index[len(double_pair_list_temporary_index) - 1]:
                    double_pair_list_index.append(m)
            if double_pair_list_index[0] != double_pair_list_index[1]:
                # generate combo code for double pair
                double_pair_counting = 27
                double_pair_counting_list = []

                for m in list(range(0, len(flush_list))):
                    for n in list(range(0, len(flush_list))):
                        double_pair_temporary_list = []
                        if m == n:
                            break
                        else:
                            double_pair_temporary_list.append(n)
                            double_pair_temporary_list.append(m)
                            double_pair_temporary_list.append(double_pair_counting)
                            double_pair_counting_list.append(double_pair_temporary_list)
                            double_pair_counting += 1

                for g in double_pair_counting_list:
                    m = double_pair_list_index[0]
                    n = double_pair_list_index[1]
                    if m == g[0] and n == g[1]:
                        i.newcode(g[2])
                    else:
                        continue

        if threeofakind_count >= 1:
            threeofakind_list = []
            for k in number_group:
                if len(k) == 3:
                    threeofakind_list.append(k[0])
                else:
                    continue

            if len(threeofakind_list) == 2:
                threeofakind_list.pop(0)

            threeofakind_code = 105
            for k in flush_list:
                if k == threeofakind_list[0]:
                    i.newcode(threeofakind_code)
                    break
                else:
                    threeofakind_code += 1

        # generate straight
        counting_sequence_straight = 118
        m = 0
        if len(straight_list_full) >= 5:
            while m <= len(list_of_straight_full) - 5:
                n = 0
                while n <= len(straight_list_full) - 5:
                    if [list_of_straight_full[m], list_of_straight_full[m + 1], list_of_straight_full[m + 2],list_of_straight_full[m + 3], list_of_straight_full[m + 4]] == [straight_list_full[n],straight_list_full[n + 1],straight_list_full[n + 2],straight_list_full[n + 3],straight_list_full[n + 4]]:
                        i.newcode(counting_sequence_straight)
                    n += 1
                m += 1
                counting_sequence_straight += 1

        flush_number_list = []
        flush_number_list_sorted = []
        for m in symbol_group:
            if len(m) >= 5:
                n = 0
                while n < len(combinationSymbol):
                    if combinationSymbol[n] == m[0]:
                        flush_number_list.append(combinationNumber[n])
                    n += 1
                break
            else:
                continue

        if len(flush_number_list) >= 5:
            for jkt in flush_list:
                for ahok in flush_number_list:
                    if ahok == jkt:
                        flush_number_list_sorted.append(ahok)

        if len(flush_number_list_sorted) >= 5:
            g = len(flush_number_list_sorted) - 5
            i.setflush(flush_number_list_sorted[g], flush_number_list_sorted[g + 1], flush_number_list_sorted[g + 2],flush_number_list_sorted[g + 3], flush_number_list_sorted[g + 4])

        # generate combo for full house
        # (3 of a kind, pair, combo code)
        counter = 141
        fullhouse_list = []
        for x in flush_list:
            for y in flush_list:
                mylist = []
                if x == y:
                    continue
                else:
                    mylist.append(x)
                    mylist.append(y)
                    mylist.append(counter)
                    fullhouse_list.append(mylist)
                    counter += 1

        player_fullhouse_list = []
        if pair_count >= 1 and threeofakind_count == 1:
            for n in number_group:
                if len(n) == 3:
                    player_fullhouse_list.append(n[0])

            m = len(number_group) - 1
            while m >= 0:
                if len(number_group[m]) == 2:
                    player_fullhouse_list.append(number_group[m][0])
                    break
                else:
                    m -= 1

        if threeofakind_count == 2 and pair_count == 1:
            h = len(number_group) - 1
            while h >= 0:
                if len(number_group[h]) == 3:
                    player_fullhouse_list.append(number_group[h][0])
                    break
                else:
                    h -= 1

            j = len(number_group) - 1
            while j >= 0:
                if len(number_group[j]) >= 2:
                    if number_group[j][0] == player_fullhouse_list[0]:
                        j -= 1
                    else:
                        player_fullhouse_list.append(number_group[j][0])
                        break
                else:
                    j -= 1

        if threeofakind_count == 2 and pair_count == 0:
            h = len(number_group) - 1
            while h >= 0:
                if len(number_group[h]) == 3:
                    player_fullhouse_list.append(number_group[h][0])

                h -= 1

        if len(player_fullhouse_list) == 2:
            for m in fullhouse_list:
                if m[0] == player_fullhouse_list[0] and m[1] == player_fullhouse_list[1]:
                    i.newcode(m[2])
                else:
                    continue

        # generate four of a kind
        countering = 297
        fourofakind_list = []
        for m in flush_list:
            temporary_list = []
            temporary_list.append(m)
            temporary_list.append(countering)
            fourofakind_list.append(temporary_list)
            countering += 1

        if fourofakind_count == 1:
            for m in number_group:
                if len(m) == 4:
                    for n in fourofakind_list:
                        if n[0] == m[0]:
                            i.newcode(n[1])

        if flush_counting_number >= 1:
            # generate straight flush
            flush_sample = []
            for m in symbol_group:
                if len(m) >= 5:
                    flush_sample.append(m[0])
                else:
                    continue

            number_straight_flush = []
            number_straight_flush_sorted = []
            num = 0
            while num < len(combinationSymbol):
                if combinationSymbol[num] == flush_sample[0]:
                    number_straight_flush.append(combinationNumber[num])
                num += 1

            for m in list_of_straight_full:
                for n in number_straight_flush:
                    if m == n:
                        number_straight_flush_sorted.append(n)
                    else:
                        continue

            number_straight_flush_sorted_filtered = []
            t = 0
            while t < len(number_straight_flush_sorted):
                if t == 0:
                    number_straight_flush_sorted_filtered.append(number_straight_flush_sorted[t])
                elif number_straight_flush_sorted[t] != number_straight_flush_sorted[t - 1]:
                    number_straight_flush_sorted_filtered.append(number_straight_flush_sorted[t])
                t += 1

            counter_sequence = 320
            m = 0
            if len(number_straight_flush_sorted_filtered) >= 5:
                while m <= len(list_of_straight_full) - 5:
                    n = 0
                    while n <= len(number_straight_flush_sorted_filtered) - 5:
                        if [list_of_straight_full[m], list_of_straight_full[m + 1], list_of_straight_full[m + 2],list_of_straight_full[m + 3], list_of_straight_full[m + 4]] == [number_straight_flush_sorted_filtered[n], number_straight_flush_sorted_filtered[n + 1],number_straight_flush_sorted_filtered[n + 2], number_straight_flush_sorted_filtered[n + 3],number_straight_flush_sorted_filtered[n + 4]]:
                            i.newcode(counter_sequence)
                        n += 1
                    m += 1
                    counter_sequence += 1

    flusher_list = []
    for i in playerlist:
        flusher_list.append(i.flushcard)

    range_list = list(range(0, len(flusher_list)))

    for i in [4, 3, 2, 1, 0]:
        find_max = []
        find_indexmax = []
        find_pop = []
        if len(range_list) > 0:
            for j in range_list:
                if flusher_list[j][i] == 0:
                    find_pop.append(j)
                else:
                    continue

        if len(find_pop) > 0:
            for j in find_pop:
                range_list.pop(range_list.index(j))

        if len(range_list) > 1:
            for j in range_list:
                find_max.append(flusher_list[j][i])
            for j in find_max:
                for k in flush_list:
                    if j == k:
                        find_indexmax.append(flush_list.index(k))
            for j in range_list:
                if flush_list.index(flusher_list[j][i]) < max(find_indexmax):
                    range_list.pop(range_list.index(j))
                elif flush_list.index(flusher_list[j][i]) == max(find_indexmax):
                    continue

        if len(range_list) == 1:
            playerlist[range_list[0]].newcode(128)
            break

        if len(range_list) == 0:
            break

    code_list = []
    for i in playerlist:
        code_list.append(i.code)
    return code_list

def poker_logic(playerlist,tablecards):
    import time
    while True:
        from random import shuffle
        import os
        print('You are player 1')
        turn = list(range(len(playerlist)))
        shuffle(turn)
        tablebet = 0
        table_maxbet = 0

        for z in [1,2,3,4]:
            for p in playerlist:
                p.newlastbet(0)
            bet_counting = 0
            check_counting = 0
            while (check_counting < len(turn) and bet_counting < len(turn)-1):
                for i in turn:
                    if check_counting < len(turn) and bet_counting < len(turn)-1:
                        if playerlist[i].balance == 0:
                            turn.pop(turn.index(i))
                            continue
                        else:
                            turn_statement(playerlist,i,tablebet,table_maxbet)
                            action = input('Action:')

                            if len(turn) == 1:
                                continue

                            elif action == 'check' or action == 'Check' or action == 'CHECK' or action == 'call' or action == 'Call' or action == 'CALL':
                                if table_maxbet == 0:
                                    playerlist[i].bet(0)
                                    check_counting += 1
                                elif table_maxbet > 0:
                                    tablebet += table_maxbet-playerlist[i].last_bet
                                    playerlist[i].bet(table_maxbet-playerlist[i].last_bet)
                                    bet_counting += 1

                            elif action == 'bet' or action == 'Bet' or action == 'BET' or action == 'raise' or action == 'Raise' or action == 'RAISE':
                                while True:
                                    try:
                                        betting_amount = int(input('Enter bet:'))
                                    except:
                                        print('You entered a string, please enter an integer')
                                        continue
                                    else:
                                        x = poker_bet_stats(betting_amount,table_maxbet,playerlist,i,tablebet,bet_counting,check_counting,turn)
                                        tablebet = x[0]
                                        table_maxbet = x[1]
                                        bet_counting = x[2]
                                        check_counting = x[3]
                                        break

                            elif action == 'all in' or action == 'All in' or action == 'All In' or action == 'ALL IN':
                                x = poker_allin_stats(table_maxbet,tablebet,playerlist,i,bet_counting,turn)
                                tablebet = x[0]
                                table_maxbet = x[1]
                                bet_counting = x[2]
                                turn = x[3]


                            elif action == 'fold' or action == 'Fold' or action == 'FOLD':
                                turn.pop(turn.index(i))

                    else:
                        continue
            if len(turn) == 1:
                playerlist[turn[0]].earn(tablebet)
                break

            os.system('cls')
            if z == 1:
                for num in [0,1,2]:
                    print('Table card number',num + 1,'is',tablecards[num])
            elif z == 2:
                for num in [0,1,2,3]:
                    print('Table card number', num + 1, 'is', tablecards[num])
            elif z == 3:
                for num in [0,1,2,3,4]:
                    print('Table card number', num + 1, 'is', tablecards[num])
            elif z == 4:
                code_list = combo(playerlist,tablecards)
                max_code = max(code_list)
                for code in playerlist:
                    if code.code == max_code:
                        print(code.name,'won!')
                        code.earn(tablebet)
                    else:
                        continue


            time.sleep(8)

        playAgain=input('Continue? (YES/NO)')
        if playAgain == 'Yes' or playAgain == 'YES' or playAgain == 'yes':
            continue
        else:
            break

def poker_game():
    print("Welcome to Texas Hold'em Poker")
    x = poker_carddistribution()
    poker_logic(x[0], x[1])

poker_game()