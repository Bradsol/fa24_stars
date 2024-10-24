import sys

if len(sys.argv) < 4:
    print("Usage: python file.py <input_fastq_file_1> <input_fastq_file_2> <output_genome_file>")
    sys.exit(1)


# open the file 
fastq1_Input = sys.argv[1]
fastq2_Input = sys.argv[2]
# allowing access to write on genome text file 
cleanGenome_Input = sys.argv[3]


def write_clean(inputFile, outputFile):
  count = 0
  lineCount = 0
  validCount = 0
  while True:
    line = inputFile.readline()
    if not line: 
      break
    
    if lineCount % 4 == 1:
      if 'N' not in line:
        outputFile.write(line.strip() + "\n")
        validCount += 1
      count += 1

    lineCount +=1

  inputFile.close()
  return validCount




# goes through specified number of SEQUENCE lines 
validCount = 0
try:
    with open(fastq1_Input, 'r') as fastq1:
        with open(cleanGenome_Input, 'w') as cleanGenome:

          validCount += write_clean(fastq1, cleanGenome)
    with open(fastq2_Input, 'r') as fastq2:
          # Open the output genome file in write mode
        with open(cleanGenome_Input, 'a') as cleanGenome:
          validCount += write_clean(fastq2, cleanGenome)
              
except FileNotFoundError:
    print(f"Error: {fastq1_Input} not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print(validCount)


# # open the file 
# fastq1 = open('SRR28797574_1.fastq', 'r')
# fastq2 = open('SRR28797574_2.fastq', 'r')
# # allowing access to write on genome text file 
# cleanGenome = open('cleanGenome.txt', 'w')
# genome = open('genome.txt', 'w')

# count = 0 # identifies the amount of sequence lines
# lineCount = 0  # variable for all lines 

# # goes through specified number of SEQUENCE lines 
# while True:
#   line = fastq.readline() 
#   if not line:
#     break 

#   if lineCount % 4 == 1:  #gets second line or SEQUENCE line 
#     #if 'N' not in line: 
#     #  cleanGenome.write(line)
#     genome.write(line.strip() + "\n")  
#     count += 1

#   lineCount += 1  

# fastq.close()

# print(count)