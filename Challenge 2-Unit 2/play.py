class BankAccount:
    class Player:
        def play(self):
            print("the player is playing cricket.")

    class Batsman(Player):
        def play(self):
            print("the batsman is batting.")

    class Bowler(Player):
        def play(self):
            print("the bowler is bowling.")

batsman = BankAccount.Batsman()
bowler = BankAccount.Bowler()
batsman.play()
bowler.play()
