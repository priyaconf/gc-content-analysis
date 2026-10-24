import time
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
from Bio import Entrez, SeqIO
from Bio.SeqUtils import gc_fraction

Entrez.email = "your_email@example.com"

genes = {"Insulin": "NM_000207", "Hemoglobin beta": "NM_000518", "p53": "NM_000546",
         "BRCA1": "NM_007294", "EGFR": "NM_005228", "GAPDH": "NM_002046", "ACTB": "NM_001101"}

rows = []
for name, accession in genes.items():
    handle = Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text")
    text = handle.read()
    handle.close()
    record = SeqIO.read(StringIO(text), "fasta")
    rows.append({"Gene": name, "Accession": accession, "Length": len(record.seq), "GC_percent": round(gc_fraction(record.seq) * 100, 2)})
    time.sleep(1)

df = pd.DataFrame(rows)
print(df)
df.to_csv("gc_results.csv", index=False)

plt.figure(figsize=(9, 5))
plt.bar(df["Gene"], df["GC_percent"])
plt.ylabel("GC content (%)")
plt.title("GC content of human genes (NCBI mRNA records)")
plt.xticks(rotation=30)
plt.savefig("gc_chart.png", bbox_inches="tight")
plt.show()