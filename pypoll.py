import os
import csv

with open('election_data.csv', 'r') as csvfile:
    f = csv.reader(csvfile, delimiter = ',')

    header = next(f)
    print(f"CSV Header: {header}")

    candidates = {}
    vote_count = 0

    for row in f:
        # total votes
        vote_count += 1

        # dict of votes per candidate
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
    
    winner = max(candidates, key = candidates.get)


    print(f"Total Votes: {vote_count}")

    for cand, vote in candidates.items():
        print(f"{cand}: {vote / vote_count * 100}% ({vote})")
    
    print(f"Winner: {winner}")




#   
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   