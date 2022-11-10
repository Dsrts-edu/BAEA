import sys

# Function Definitions 

# basic difference function 
def returnDiff(a,b):
        if(a > b):
                return a - b
        else:
                return b - a        

# Obtain file from user in, if invalid, keep asking 
# Works with data copied from NYT's election page 
# Check for errors in accessing the file

isValidFile = False
invalidEntriesCount = 0
while not isValidFile:
        try: 
                file = open(input("Enter filepath of analysis file: "))
                isValidFile = True
        except:
                # Sys exit if user tries too many invalid entries 
                if invalidEntriesCount > 10:
                        sys.exit("Too many invalid attempts, closing program...")

                print("Please enter a valid filepath")
                invalidEntriesCount += 1


# Values for tracking estimated votes 
counties = file.readlines()
votesFor = 0
votesAgainst = 0

# Track the total vote count to get an estimated outcome
totalOverallVotes = 0
totalOverallFor = 0
totalOverallAgainst = 0

count = 0
# Strips the newline character
for line in counties:
        # process the current line, split on spaces
    curline = line.split(' ')

     # Strip metrics from the document 
    percetFor = int(curline[1][1:])
    percentAgainst = int(curline[2][1:]) 
    curVotes = int(curline[3][1:].replace(",",""))

    # Add to total overall votes
    totalOverallVotes += curVotes
    totalOverallFor += percetFor / 100 * curVotes 
    totalOverallAgainst += percentAgainst / 100 *  curVotes

        # If the current line has a > then it is a county with >95% votes in
        # These are omitted 
    if curline[4][1] == ">" :
       continue 
       # Below, calculate the possible results per county, increment total 
       # votes remaining for and against for each 
    else:

       # only available if no ">", strip from doc here 
        reportedPercent = int(curline[4][1:3])

        # Calculate missing values for estimation calculaiton 
        totalEst = curVotes * 100 / reportedPercent
        remaining = totalEst - curVotes
        votesFor += percetFor / 100 * remaining
        votesAgainst += percentAgainst / 100 * remaining

        # Display county by county results 
        print("County:", curline[0])
        print("\tTotal Estimated: %.2f " % totalEst )
        print("\tEst votes remaining: %.2f " % remaining)
        print("\tFor: %.2f" % (percetFor / 100 * remaining))
        print("\tAgainst: %.2f" % (percentAgainst / 100 * remaining))
        print()

# Print overall results 
print("ESTIMATED REMAINING RESULTS:\n---------------------------- \n")
print("Total votes    : %d" % totalOverallVotes)
print("Total for      : %d" % totalOverallFor)
print("Total against  : %d" % totalOverallAgainst)
print("\n---------------------------- \n")
print("Remaining votes for     : %.2f" % votesFor)
print("Remaining votes against : %.2f" % votesAgainst)

totalEST = votesFor + votesAgainst

diff = 0
forPercent = votesFor / totalEST
againstPercent = votesAgainst / totalEST


diff = returnDiff(votesFor, votesAgainst)

print("Total Remaining EST      : %.2f" % totalEST)
print("Remaining Vote Difference: %.2f" % diff)
print("Remaining For    : %.4f" % forPercent)
print("Remaining Against: %.4f\n" % againstPercent)
print("---------------------------- \n")

# Add remaining to total overall, calculate % outcome 

totalFinalVotes = totalEST + totalOverallVotes
totalFinalFor = totalOverallFor + votesFor
totalFinalAgainst = totalOverallAgainst + votesAgainst
finalForPercent = totalFinalFor / totalFinalVotes
finalAgainstPercent = totalFinalAgainst / totalFinalVotes


diff = returnDiff(totalFinalFor, totalFinalAgainst)


print("Total Final EST: %.2f" % totalFinalVotes)
print("Final Vote Difference: %.2f" % diff)
print("Final For    : %.4f" % finalForPercent)
print("Final Against: %.4f\n" % finalAgainstPercent)
print("---------------------------- \n")


