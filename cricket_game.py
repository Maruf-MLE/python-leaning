import random


class Team:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.wickets = 0

    def play_innings(self, overs):
        for over in range(overs):
            print(f"Over {over + 1}:")
            for ball in range(6):  # 1 over = 6 balls
                if self.wickets == 10:
                    print(f"All out! Final Score: {self.score}/{self.wickets}")
                    return
                run = random.choice([0, 1, 2, 3, 4, 6, 'W'])
                if run == 'W':
                    self.wickets += 1
                    print(f"Wicket! Total Wickets: {self.wickets}")
                else:
                    self.score += run
                    print(f"Runs: {run}, Total Score: {self.score}/{self.wickets}")

            print(f"End of Over {over + 1}: {self.score}/{self.wickets}")
            print()

        print(f"End of Innings: Final Score: {self.score}/{self.wickets}")


def play_match():
    overs = int(input("Enter the number of overs for the match: "))

    # Team 1
    team1 = Team("Team 1")
    print(f"\n{team1.name} is batting first.")
    team1.play_innings(overs)

    # Team 2
    team2 = Team("Team 2")
    print(f"\n{team2.name} is batting second.")
    team2.play_innings(overs)

    # Match Result
    print("\nMatch Result:")
    if team1.score > team2.score:
        print(f"{team1.name} wins by {team1.score - team2.score} runs!")
    elif team2.score > team1.score:
        print(f"{team2.name} wins by {10 - team2.wickets} wickets!")
    else:
        print("The match is a tie!")


if __name__ == "_main_":
    play_match()



