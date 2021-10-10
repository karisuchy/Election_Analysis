# Election_Analysis

## Project Overview
Complete an audit for one US Congressional Precint for the Coloardo Board of Elections so the election results can be certified. The following information was verified through this audit: 

- Total number of votes cast
- A complete list of canddidates who received votes 
- Total number of votes each candidate received
- Percentage of votes each candidate won 
- The winner of the election based on popular vote 
- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout

## Resources
- Data Source: election_results_csv
- Software: Python 3.7, Visual Studio Code 1.61.0

## Method
Using Visual Studio Code and Python, I was able to create a code for one US Congressional Precint in Coloardo for their Board of Elections. 
The code... looped through all election data to 
The code was written in a manner that could easily be expanded to other elections. 
Code and results were committed to GitHub so they can be reviewed and used by others. 

The program iterates through each row of the csv file using a for loop. Accumulators, as shown below, are used to count votes by candidate and county as each row is read.

![accumulators](https://user-images.githubusercontent.com/90162669/136705455-49f47fa1-62b2-4f59-a3a7-e78b6f8c2df5.png)

The votes are stored in two seperate dictionaries for candidates and counties, as shown below. 

![dictionaries](https://user-images.githubusercontent.com/90162669/136705421-e4c53478-8e99-424b-a1e9-b919e8e0b5e9.png)

The program then calculates the percentage of votes for each candidate and county. 

![Percentage calculations](https://user-images.githubusercontent.com/90162669/136705638-4d2220dc-8a94-4012-8d7c-e7a137efe8d1.png)

The end product is a txt file with elections results clearly outlined as follows:

![Results](https://user-images.githubusercontent.com/90162669/136705732-9e855de1-33af-4d76-b539-77c80eea774b.png)

## Election-Audit Results

### Candidate Summary
The analysis of the election show that: 
- There were 369,711 votes cast in the election
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGete
  - Raymon Anthony Doane
- The candidate results were: 
  - Charles Casper Stockham received 23.8% of the votes and 85,213 number of votes
  - Diana DeGete received 73.8% of the votes and 272,892 number of votes
  - Raymon Anthony Doane received 3.1% of the votes and 11,606 number of votes
- The winnder of the election was:
  - Diana DeGete received 73.8% of the votes and 272,892 number of votes
  
### County Summary 
Votes breakdown by County:
- Jefferson: 10.5% (38,855)
- Denver: 82.8% (306,055)
- Arapahoe: 6.7% (24,801)
  
Denver had the largest number of votes with 82.8% of the votes and 306,055 number of votes. 
  
## Election-Audit Summary
** In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.**
  
