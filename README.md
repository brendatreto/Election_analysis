# Election_analysis

## Overview of Election Audit
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congresional election. The purpose of the audit was to find the winner of the election without relying solely on manual methods, and avoid mistakes in the process. The assigned tasks were:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.38.1

## Election-Audit Results
The analysis of the election shows that:
- There were 369,711 votes cast in the election.

![Total_Votes](https://user-images.githubusercontent.com/22451540/150659013-41df5557-88d2-4094-8903-6434171eb81e.PNG)

This information was possible to get using the csv file with the election results and substracting the header. All the other data represented votes casted.

- The number of votes and percentage of total votes for each county was distributed in the following fashion:

![County_votes](https://user-images.githubusercontent.com/22451540/150659104-99cf8437-a9f3-4864-9e0b-71d2eb01c427.PNG)

In order to get this information, we wrote a for loop to get the county from the csv file and add it to the total count of each county declared in the dictionary.

- Following this process, we were able to see that **Denver** was the county with the largest voter turnout with **82.8%** of the total votes (**306,055 votes**). 

- The candidates were:
-   Charles Casper Stockham
-   Diana DeGette
-   Raymon Anthony Doane

- The results were:
-   Candidate Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
-   Candidate Diana DeGette received 73.8% of the vote and 272,892 votes.
-   Candidate Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.

![candidate_votes](https://user-images.githubusercontent.com/22451540/150659211-d6591ea9-e58b-46d4-8c96-bb994aaf9f8b.PNG)

We followed the same process used in the county count. Wrote a for loop to retrieve the number of times a candidate's name came up in the election_results file and add it to the assigned name.

- The winner of the election was:
-   Candidate Diana DeGette, who received 73.8% of the vote and 272,892 votes.

![winner](https://user-images.githubusercontent.com/22451540/150659272-39d9e21f-99a6-4aca-a975-ec6ce27cc735.PNG)

The winner was evident from the previous count by candidate name, but we needed to verify the information and to do that we used a decision statement that went over the following conditions:

![winning_bts](https://user-images.githubusercontent.com/22451540/150659319-f282df9f-c324-437a-90b3-40ad37c554c1.PNG)

## Election-Audit Summary: 
This audit served its purpose, and can certainly be repurposed in order to make the voting counting process more efficient and proficient. However, when using this script in different districts some modifications are in order:
* Get more demographic information from the voters in order to enrich the result and discover voting trends.
* A more in depth analysis of the voting pattern by county. Using the for loop for each candidate inside the county loop could help us visualize the results.
