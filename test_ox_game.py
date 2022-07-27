
# write your code here
class ScoreChecker:
    winner = []
    players = ["one", "two"]
    num = 1
    str1 = "_________"
    feedback = ""

    def __init__(self):
        pass

    # returns the result of whether someone has won
    def checkWin(self):
        self.check_input_errors(input())
        try:
            self.horizontal_check()
            self.vertical_check()
            self.diagonal_check()
            print(ScoreChecker.winner)
            if self.char_maxed_out() and len(ScoreChecker.winner) != 1:
                lists = [[ScoreChecker.str1[n], ScoreChecker.str1[n + 1], ScoreChecker.str1[n + 2]]
                         for n in range(0, 9, 3)]
                print("-" * 9)
                for aList in lists:
                    print("| {} {} {} |".format(*aList))
                print("-" * 9)
                print("Draw")
                return True
            elif len(ScoreChecker.winner) == 1 and self.character_diff_check():
                lists = [[ScoreChecker.str1[n], ScoreChecker.str1[n + 1], ScoreChecker.str1[n + 2]]
                         for n in range(0, 9, 3)]
                print("-" * 9)
                for aList in lists:
                    print("| {} {} {} |".format(*aList))
                print("-" * 9)
                print("%s wins" % ScoreChecker.winner[0])
                return True
            else:
                return False
        except Exception as e:
            print("there is an error ", e)

    # updates horizontal check
    @staticmethod
    def horizontal_check():
        for num in range(0, 9, 3):
            if ScoreChecker.str1[num] != "_" and ScoreChecker.str1[num + 1] != "_" and ScoreChecker.str1[num] \
                    == ScoreChecker.str1[num + 1] and ScoreChecker.str1[num] == ScoreChecker.str1[num + 2]:
                ScoreChecker.winner.append(ScoreChecker.str1[num])

    # updates vertical check
    @staticmethod
    def vertical_check():
        for num in range(0, 3):
            if ScoreChecker.str1[num] != "_" and ScoreChecker.str1[num + 3] != "_" and ScoreChecker.str1[num] \
                    == ScoreChecker.str1[num + 3] and ScoreChecker.str1[num + 3] == ScoreChecker.str1[num + 6]:
                ScoreChecker.winner.append(ScoreChecker.str1[num])

    # updates diagonal check
    @staticmethod
    def diagonal_check():
        for num in range(0, 3, 2):
            if num == 0:
                d_pos, d_pos1, d_pos2 = ScoreChecker.str1[num], ScoreChecker.str1[num + 4], ScoreChecker.str1[num + 8]
            else:
                d_pos, d_pos1, d_pos2 = ScoreChecker.str1[num], ScoreChecker.str1[num + 2], ScoreChecker.str1[num + 4]
            if d_pos == d_pos1 and d_pos1 == d_pos2 and d_pos1 != "_" and d_pos2 != "_":
                ScoreChecker.winner.append(ScoreChecker.str1[num])

    # counts no of chars in the input string
    @staticmethod
    def character_diff_check():
        char_dict = {}
        for a_char in ScoreChecker.str1:
            char_dict[a_char] = char_dict.get(a_char, 0) + 1
        if abs(char_dict.get("O", 0) - char_dict.get("X", 0)) < 2:
            return True
        return False

    # returns player
    @staticmethod
    def player_set():
        if ScoreChecker.num % 2 == 0:
            player = ScoreChecker.players[1]
            symbol = "O"
        else:
            player = ScoreChecker.players[0]
            symbol = "X"
        return player, symbol

    # checks if cell is updated else updates the result
    def check_if_occupied(self, an_input):
        a_str = list(ScoreChecker.str1)
        if a_str[an_input] == "_":
            a_str[an_input] = self.player_set()[1]
            ScoreChecker.str1 = "".join(a_str)
            return ScoreChecker.str1
        else:
            return "This cell is occupied! Choose another one!"

    # checks if input has errors
    def check_input_errors(self, a_str):
        try:
            result = a_str.split()
            if len(result) == 2 and int(result[0]):
                row, col = int(result[0]), int(result[1])
                if row in range(1, 4) and col in range(1, 4):
                    if row == 1 and col < 4:
                        pos = col - row
                    elif row == 2 and col < 4:
                        pos = col + row
                    else:
                        pos = col + 5
                    ScoreChecker.feedback = self.check_if_occupied(pos)
                    if len(ScoreChecker.feedback) > 9:
                        print(ScoreChecker.feedback)
                        return True
                    else:
                        ScoreChecker.num += 1
                        return False
                else:
                    print("Coordinates should be from 1 to 3!")
            else:
                raise Exception
        except Exception:
            print("You should enter numbers!")

    # checks if there is a draw
    @staticmethod
    def char_maxed_out():
        a_num = 0
        for a_char in ScoreChecker.str1:
            if a_char.lower() == "x" or a_char.lower() == "o":
                a_num += 1
        if a_num == 9:
            return True
        return False

    def __str__(self):
        return "This is a wonderful Tic-Tac-Toe"


# prints the results and feedback
def main():
    while True:
        lists = [[ScoreChecker.str1[n], ScoreChecker.str1[n + 1], ScoreChecker.str1[n + 2]] for n in range(0, 9, 3)]
        print("-" * 9)
        for aList in lists:
            print("| {} {} {} |".format(*aList))
        print("-" * 9)
        if ScoreChecker().checkWin():
            break
        else:
            continue


if __name__ == "__main__":
    main()
