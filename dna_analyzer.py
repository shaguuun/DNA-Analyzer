
Samples = "/Users/shagun/Desktop/Python_Projects/dna_analyzer/sample_dna.txt"

def validate_dna(dna):
     for base in dna:
        if base not in "ATGC":
            return False
     return True

def nucleotide_count(dna):
     return{
        "A": dna.count("A"),
        "T": dna.count("T"),
        "G": dna.count("G"),
        "C": dna.count("C")
     }
        
def gc_content(dna):
     g = dna.count("G")
     c = dna.count("C")
     return round((g + c) / len(dna) * 100, 2)

def codon_frequency(dna):
     codons = {}
     for i in range(0, len(dna)-2, 3):
         codon = dna[i:i+3]
         if len(codon) == 3:
            codons[codon] = codons.get(codon, 0) + 1
     return codons


if __name__ == '__main__':
    with open(Samples, "r") as file:
        dna = file.read().strip().upper()

    if not validate_dna(dna):
        print(" INVALID DNA SEQUENCE - contains characters other than A, T, G, C")
    else:
        print('=' * 50)
        print('             DNA ANALYZER RESULTS')
        print('=' * 50)
        print(f"Sequence Length = {len(dna)} bp")
        print(f'Nucelotide counts = {nucleotide_count(dna)}')
        print(f'GC Content = {gc_content(dna)}%')
        print(f'Codon Frequency = {codon_frequency(dna)}')
        print('=' * 50)

