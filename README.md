## PyPoll

This is a python script which takes a set of poll data (election_data.csv), composed of `Voter ID`, `County`, and `Candidate`, and analyzes it. This analysis produces the following output, in the form of both a print statement and a text file:
  * A complete list of candidates who received votes
  * The percentage of votes each candidate won
  * The total number of votes each candidate won
  * The winner of the election based on popular vote.

With the provided data, the resulting file should look as follows:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.0% (2218231)
  Correy: 20.0% (704200)
  Li: 14.0% (492940)
  O'Tooley: 3.0% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

This script was created as part of Assignment 3 (Python) from the USC Viterbi Boot Camp. 
