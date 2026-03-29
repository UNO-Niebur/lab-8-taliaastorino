#ProcessData.py
#Name: Talia Astorino
#Date: 03/29/2026
#Assignment: 

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for line in inFile:
    line = line.strip()
    parts = line.split(",")

    first = parts[0]
    last = parts[1]
    major = parts[2]
    year = parts[3]

    userID = first[0].lower() = last.lower() + str(random.randint(10,99))

    majorYear = major + "-" + year

    outFile.write(first + "," + last + "," + userID + "," + majorYear + "\n")

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
