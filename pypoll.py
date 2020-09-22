import os
import csv

with open('election_data.csv', 'r') as csvfile:
    f = csv.reader(csvfile, delimiter = ',')

    header = next(f)
    print(f"CSV Header: {header}")

    candidates = {}

    for row in f:
        # total votes
        vote_count += 1

        # dict of votes per candidate
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
    
    won_votes = max(list(candidates.values()))
    won_candidate = candidates[won_votes]

    print(f"Total Votes: {vote_count}")

    for cand, vote in candidates:
        print(f"{cand}: {votes / vote_count * 100}% ({votes}")
    
    print(f"Winner: {won_candidate}")




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