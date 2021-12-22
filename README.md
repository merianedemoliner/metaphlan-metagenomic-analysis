
> metaphlan DNA_S1_L001_R1_001.fastq,DNA_S1_L001_R2_001.fastq --bowtie2out DNA_S1_L001_R1_R2_001.bowtie2.bz2 --nproc 2 --input_type fastq --add_viruses -o profiled_metagenome.txt
> metaphlan DNA_S1_L001_R1_001.fastq,DNA_S1_L001_R2_001.fastq --bowtie2out DNA_S1_L001_R1_R2_001.bowtie2.bz2 --nproc 2 --input_type fastq -o profiled_metagenome.txt
> metaphlan DNA_S1_L001_R1_001.fastq,DNA_S1_L001_R2_001.fastq --bowtie2out DNA_S1_L001_R1_R2_001.bowtie2.bz2 --nproc 2 --input_type fastq


#comando para analise metagenomica doutorado 


> metaphlan 67713_S1_L001_R1_001.fastq.gz,67713_S1_L001_R2_001.fastq.gz --bowtie2out DNA_S1_L001_R1_R2_001.bowtie2.bz2 --nproc 2 --input_type fastq --add_viruses -o 67713.txt



> merge_metaphlan_tables.py p2rofiled_metagenome > metaphlan_output3.txt output/merged_abundance_table.txt

