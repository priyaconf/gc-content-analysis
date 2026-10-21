def gc_content(seq):
    g_count = seq.count("G")
    c_count = seq.count("C")
    return (g_count + c_count) / len(seq) * 100

def transcribe(dna):
    return dna.replace("T", "U")

codon_table = {
    "AUG": "M", "GCC": "A", "UUU": "F", "UAA": "*",
    "GGC": "G", "CAU": "H", "AUA": "I", "UUA": "L"
}

def translate(rna):
    protein = ""
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        protein += codon_table[codon]
    return protein

def reverse_complement(dna):
    pairs = {"A": "T", "T": "A", "G": "C", "C": "G"}
    complement = ""
    for base in dna:
        complement += pairs[base]
    return complement[::-1]
