# swea 13090 '베이비진 게임'

def check(player_cards, card):
    if player_cards[card] == 3:
        return True
    
    for i in range(8):
        if player_cards[i] and player_cards[i + 1] and player_cards[i + 2]:
            return True
    
    return False


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        cards = list(map(int, input().split()))

        p1 = [0 for _ in range(10)]
        p2 = [0 for _ in range(10)]
        
        result = 0
        for i in range(6):
            p1_card = cards[2*i]
            p2_card = cards[2*i + 1]

            p1[p1_card] += 1
            p2[p2_card] += 1

            if i < 3:
                continue

            if check(p1, p1_card):
                result = 1
                break
            
            if check(p2, p2_card):
                result = 2
                break
        
        print(f'#{t} {result}')
