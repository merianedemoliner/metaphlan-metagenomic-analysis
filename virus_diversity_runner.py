
def build_command(filename_r1, filename_r2):
    auxiliary_name = filename_r1.split('_')[0] + '_R1_R2'
    #"metaphlan
    metaphlan_cmd = "metaphlan"
    
    #./input/67713_S1_L001_R1_001.fastq.gz,./input/67713_S1_L001_R2_001.fastq.gz
    filenames_arg = " ./input/" + filename_r1 + "," + "./input/" + filename_r2

    #--bowtie2out
    bowtie2_arg = " --bowtie2out ./bowtie2_files/" + auxiliary_name + ".bowtie2.bz2"
    
    #--nproc 2
    nproc2_arg = " --nproc 2"

    #--input_type fastq
    input_type_arg = " --input_type fastq"

    #--add_viruses
    add_viruses_flag = " --add_viruses"

    #--ignore some stuffs
    ignore_some_stuffs = " --ignore_eukaryotes --ignore_bacteria --ignore_archaea"

    #-o ./output/67713.txt
    output_arg = " -o ./output/" + auxiliary_name + ".txt"

    return metaphlan_cmd + filenames_arg + bowtie2_arg + nproc2_arg + input_type_arg + add_viruses_flag + ignore_some_stuffs + output_arg

import os
from os import listdir
from os.path import isfile, join
import subprocess

#to run shell commands in python we use on the following:
#os.system("metaphlan ./input/67713_S1_L001_R1_001.fastq.gz,./input/67713_S1_L001_R2_001.fastq.gz --bowtie2out ./bowtie2_files/67713_R1_R2.bowtie2.bz2 --nproc 2 --input_type fastq --add_viruses -o ./output/67713.txt")
#subprocess.run(["cmd", "each argument", "other argument"])

#list all files from directory


inputfiles = [f for f in listdir("./input") if isfile(join("./input/", f))]
inputfiles.sort()

last_position = len(inputfiles)-1

for index_for_r1 in range(0, last_position, 2):
    
    index_for_r2 = index_for_r1 + 1

    filename_r1 = inputfiles[index_for_r1]
    filename_r2 = inputfiles[index_for_r2]
    command = build_command(filename_r1, filename_r2)
    
    print("**************************************")
    print(command)
    
    print("--------------------------------------")
    print(index_for_r1, filename_r1, filename_r2)

    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    out = process.communicate()[0]
    
    print(out)
