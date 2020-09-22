# import csv reader package
import csv
# Note: not importing os package because it was finicky on Windows
# so the file is just stored in the same folder as this script

# open and read csv
with open('election_data.csv', 'r') as csvfile:
    f = csv.reader(csvfile, delimiter = ',')

    # read in hdeader row
    header = next(f)
    #print(f"CSV Header: {header}")

    # initialize variables for for loop
    candidates = {}
    vote_count = 0

    # loop through remainder of file
    for row in f:
        # increment total votes
        vote_count += 1

        # check for candidate in dict
        if row[2] in candidates:
            # increment that candidate by one
            candidates[row[2]] += 1
        else:
            # add new dict entry with 1 vote
            candidates[row[2]] = 1
    
    # 'key' argument is an optional function you can apply to each
    # argument in the iterable before finding the max (but it'll still
    # return the original value in max, not the operated-on one)
    # => look up values and find max value, then return corresponding candidate
    winner = max(candidates, key = candidates.get)

    # output
    final = ("================\n"
            + "ELECTION RESULTS\n" 
            + "================\n" 
            + f"Total Votes: {vote_count} \n \n" 
            + "CANDIDATE BREAKDOWN \n")
    for cand, vote in candidates.items():
        final += f"{cand}: {round(vote / vote_count * 100, 3)}% ({vote}) \n"
    
    final += f"\nWinner: {winner}"

    # print output
    print(final)

    # write output to text file
    with open("results.txt", "w", newline = "") as results:
        results.write(final)

