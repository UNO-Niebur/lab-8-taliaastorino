#ProcessData.py
#Name: Talia Astorino
#Date: 03/29/2026
#Purpose: Taking messy data and converting it into something useful.

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for line in inFile:
    line = line.strip()

    if line == "":
      continue

    parts = line.split()

    if len(parts) < 7:
      continue

    first = parts[0]
    last = parts[1]
    studentID = parts[3]
    year = parts[5]
    major = " ".join(parts[6:])

    # userID
    lastPart = last.lower()
    while len(lastPart) < 5:
      lastPart += "X"

    last3 = studentID[-3:]
    userID = first[0].lower() + lastPart + last3

    #Major and Year
    majorCode = major[:3].upper()

    if year == "Freshman":
      yearCode = "FR"
    elif year == "Sophomore":
      yearCode = "SO"
    elif year == "Junior":
      yearCode = "JR"
    elif year == "Senior":
      yearCode = "SR"

    majorYear = majorCode + "-" + yearCode

    # Write to file
    outFile.write(last + "," + first + "," + userID + "," + majorYear + "\n")
    
  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
