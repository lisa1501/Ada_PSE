def hamming_distance(a, b):
    nucleotides = ["A", "C", "G", "T"]
    if len(a) != len(a):
        raise Exception("String lengths are not equal.")
    a_cap = a.upper()
    b_cap = b.upper()    
    total = 0
    for i in range(len(a_cap)):
        if a_cap[i] not in nucleotides or b_cap[i] not in nucleotides:
            raise Exception("Not a valid nucleotide.")
        if a_cap[i] != b_cap[i]:
            total += 1

    return total

answer_1=hamming_distance("gact", "agct")
# answer_2=hamming_distance("", "CATCGTAATGACGGCCT")
# "ACTG","AACTG"
print(answer_1)
print('abcd'.upper())
# print(("5").isnumeric())
#1. egde case length , if there is empty string ,range of the string
#2. len not equal to each other
#3. if user input a letter is not A G C T , white space
#4. how is the format of the output data type string/int
#5. time or space complexity 
#valid the inputs 
# Is there any request for time comlexity and space comlexity?
# How to validated input data and What is the length of the input datas?
# What should happen if two input data length are not equal?
# what should happen if input letter is not A, G, C, T or letter is white spase , or letters are lower case a, g, c, t.
# what is the format of the output data type str or init?


# Example one
# input ("GAHCTAC", "CATCGTA")
# output Exception: Not a valid nucleotide.
# Example one
#input ("GATCTAC", "CATCGTA")
#output 4