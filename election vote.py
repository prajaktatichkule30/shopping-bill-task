# Election Vote Calculator

def calculateTotalVotes(a, b, c):
    total = a + b + c
    return total


def calculatePercentage(votes, total):
    percentage = votes * 100 / total
    return percentage


def calculateWinningMargin(a, b):
    margin = a - b
    return margin


def calculateElectionResult(a, b, c):
    total = calculateTotalVotes(a, b, c)

    p1 = calculatePercentage(a, total)
    p2 = calculatePercentage(b, total)
    p3 = calculatePercentage(c, total)

    print("Election Vote Results")
    print("----------------------")
    print("Candidate A Votes:", a)
    print("Candidate B Votes:", b)
    print("Candidate C Votes:", c)
    print("Total Votes:", total)

    print("Candidate A Percentage:", round(p1, 2), "%")
    print("Candidate B Percentage:", round(p2, 2), "%")
    print("Candidate C Percentage:", round(p3, 2), "%")

    votes = [a, b, c]
    sorted_votes = sorted(votes, reverse=True)

    margin = calculateWinningMargin(sorted_votes[0], sorted_votes[1])
    print("Winning Margin:", margin, "votes")


# Main program
calculateElectionResult(500, 350, 150)