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

## Tools
Python, Biopython, pandas, matplotlib (run in Google Colab)

## Files
- `bio_toolkit.py`: my own functions for GC content, transcription, translation and reverse complement
- `gc_results.csv`: results table
- `gc_chart.png`: bar chart

## What I learned
Built from scratch as a beginner project, starting with hand-written sequence
functions and then using Biopython to work with real NCBI data.
