def catvsdog():
    total_cases = int(input())
    for i in xrange(0,total_cases):
        stats = raw_input()
        cats = int(stats.split(" ")[0])
        dogs = int(stats.split(" ")[1])
        viewers = int(stats.split(" ")[2])
        votes = []
        for j in xrange(0,viewers):
            votes.append(raw_input().split(" ")[0])
        set_votes = set(votes)
        tally = []
        for vote in set_votes:
            print vote
            tally.append(votes.count(vote))
        tally.sort()
        print tally[::-1][0]

if __name__ == "__main__":
    catvsdog()