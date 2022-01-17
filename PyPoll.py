#Add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []

# Candidate votes
candidate_votes = {}

# Winning Candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    #Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to candidate list
            candidate_options.append(candidate_name)

            # Track vote count per candidate
            candidate_votes[candidate_name] = 0

            # Tally votes
        candidate_votes[candidate_name] += 1
    
    #Determine percentage of votes for each candidate
    # 1. Loop through candidate's list
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count
        votes = candidate_votes[candidate_name]
        # 3. Calculate percentage
        vote_percentage = float(votes) / float(total_votes) *100 
        # 4. Print percentage per candidate
        print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

        # Determine winning vote count and candidate
        # If votes greater than winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true, set winning count and winning percentage equal to votes and vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set winning candidate
            winning_candidate = candidate_name 

    # Winning candidate summary
    winning_candidate_summary = (
        f'-------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'-------------------------\n')
    print(winning_candidate_summary)

    # Print the total votes
    #print(total_votes)

    # Print the candidate list
    #print(candidate_options)

    # Print candidate votes (dictionary)
    #print(candidate_votes)