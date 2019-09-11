# -*- coding: utf8 -*-
import climax
import os

@climax.group()
def main():
    pass

@main.command()
@climax.argument("--bed", help="Bed file to be filtered.")
@climax.argument("--gene_list", help="Gene list to be selected - Ex.: 'BRCA1|DMD' ")
@climax.argument("--code", help="Analysis identification.")
def filter_bed(bed, gene_list, code):
    genes = gene_list.split("|")
    for i in genes:
        os.system("grep -w '{}' '{}' >> {}.selected_genes.bed".format(i.upper(), bed, code))
    print("The selected bed file is done: {}.selected_genes.bed\n".format(code))

@main.command()
@climax.argument("--bed", help="Bed file with the selected genes.")
@climax.argument("--bam", help="Bam file to be filtered.")
@climax.argument("--code", help="Analysis identification.")
def filter_bam(bed,bam,code):
    os.system("samtools view -b -L {} {} > {}.filtered_genes.bam".format(bed,bam,code))
    print("The filtered bam file is done: {}.filtered_genes.bam\n".format(code))

if __name__=='__main__':
    main()
