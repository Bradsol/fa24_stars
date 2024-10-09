fastq = open('SRR28797574_1.fastq', 'r')

genome = open('genome.txt', 'w')

count = 0
lineCount = 0  
while count < 10:
  line = fastq.readline() 
  if not line:
    break 

  if lineCount % 4 == 1:  
    genome.write(line.strip() + "\n")  
    count += 1

  lineCount += 1  

fastq.close()






