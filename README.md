# Bioinfo useful

**Under Contruction!**

This repo contains a set of bioinformatics tools compiled to improve and facilitate the flollowing analyzes:

- Filter BED file
- Filter BAM file



## Installation using miniconda:

  1- [Install miniconda](https://conda.io/miniconda.html)

  2 - Create conda env using Python3:
  ```
  $ conda create -n bioinfo-useful python=3
  ```
  3- In/Out conda the environment:
  ```
  $ conda activate bioinfo-useful
  $ conda deactivate
  ```
  4- Install packages using conda:
  ```
   conda install --file requirements.txt
  ```
## Usage:

### Overview:
```
$ python bioinfo_useful.py -h

usage: bioinfo_useful.py [-h] {filter_bed,filter_bam} ...

positional arguments:
  {filter_bed,filter_bam}
    filter_bed
    filter_bam

optional arguments:
  -h, --help            show this help message and exit
```
### Filter BED file:
```
$ python bioinfo_useful.py filter_bed -h

usage: bioinfo_useful.py filter_bed [-h] [--code CODE] [--gene_list GENE_LIST]
                                    [--bed BED]

optional arguments:
  -h, --help            show this help message and exit
  --code CODE           Analysis identification.
  --gene_list GENE_LIST
                        Gene list to be selected - Ex.: 'BRCA1|DMD'
  --bed BED             Bed file to be filtered.
```

### Filter BAM file:
```
$ python bioinfo_useful.py filter_bam -h

usage: bioinfo_useful.py filter_bam [-h] [--code CODE] [--bam BAM] [--bed BED]

optional arguments:
  -h, --help   show this help message and exit
  --code CODE  Analysis identification.
  --bam BAM    Bam file to be filtered.
  --bed BED    Bed file with the selected genes.
```
