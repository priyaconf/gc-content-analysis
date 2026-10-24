# GC Content Analysis of Human Genes

A small Python project that downloads human gene mRNA records from NCBI,
calculates their GC content, and compares them in a table and bar chart.

## What it does
- Fetches sequences by accession number using Biopython (Entrez)
- Calculates sequence length and GC content
- Saves results to a CSV file and a bar chart

## Genes analysed
| Gene | Accession | Length | GC % |
|------|-----------|--------|------|
| Insulin | NM_000207 | 465 | 63.87 |
| Hemoglobin beta | NM_000518 | 628 | 51.27 |
| p53 | NM_000546 | 2512 | 53.38 |
| BRCA1 | NM_007294 | 7088 | 41.77 |
| EGFR | NM_005228 | 9905 | 47.78 |
| GAPDH | NM_002046 | 1285 | 56.11 |
| ACTB | NM_001101 | 1812 | 55.19 |

## Tools
Python, Biopython, pandas, matplotlib

## Files
- `gene_gc.py`: downloads the sequences, calculates GC content, saves the table and chart
- `gc_results.csv`: results table
- `gc_chart.png`: bar chart

## How to run
1. Install the packages: `pip install biopython pandas matplotlib`
2. Put your own email address on the `Entrez.email` line (NCBI requires one)
3. Run: `python gene_gc.py`

## What I learned
Insulin had the highest GC content (63.87%) and BRCA1 the lowest (41.77%).
Insulin has 51 amino acids and BRCA1 has 1863 amino acid sequence.So, we can conclude that the longer genes (BRCA1, EGFR) have lower GC content than the short ones. GC content tells about thermostability, so from this perspective Insulin is more thermostable then BRCA1. Insulin has more exons or coding region than BRCA1, which has a lot of repetitive and ALU elements and it is PCR-friendly. 
