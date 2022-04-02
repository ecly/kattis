class Player:
    def __init__(self, player, life=2):
        self.player = player
        self.life = life


def main():
    s, p = map(int, input().split())
    players = [Player(i + 1) for i in range(p)]
    turn_idx = 0
    while len(players) > 1:
        turn_idx = (turn_idx + s - 1) % len(players)
        player = players[turn_idx]
        if player.life == 2:
            player.life -= 1
            players.insert(turn_idx, Player(player.player, player.life))
        elif player.life == 1:
            player.life -= 1
            turn_idx += 1
        else:
            players.pop(turn_idx)

    print(players[0].player)


if __name__ == "__main__":
    main()
