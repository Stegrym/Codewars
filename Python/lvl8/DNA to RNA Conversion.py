# Create a function which translates a given DNA string into RNA.

# For example:
# "GCAT"  =>  "GCAU"
# The input string can be of arbitrary length - in particular, it may be empty.
#  All input is guaranteed to be valid, i.e.
# each input string will only ever consist of 'G', 'C', 'A' and/or 'T'.
# "TTTT" --> "UUUU"
# "GCAT" --> "GCAU"


def dna_to_rna(dna:str):
    return dna.replace('T', 'U')


print(dna_to_rna("TTTT"))
print(dna_to_rna("GCAT"))