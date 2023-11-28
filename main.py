

def reverse_complement(input_string : str, original_alphabet : list[str], replace_aplhabet: list[str]) -> str:

    output_string = ""
    for nucleotide in input_string:
        #print(char)
        if nucleotide in original_alphabet:
            index = original_alphabet.index(nucleotide)
            output_string = output_string + replace_aplhabet[index]
        else:
            output_string = output_string + "_"

    # reverse the string and return it
    return output_string[::-1]

if __name__ == "__main__":
    input_string = "CGAzT"
    print(input_string)
    print(reverse_complement(input_string,["A","T","C","G","a"],["T","A","C","G","t"]))
    # assert reverse_complement("CGAT",["A","T","C","G","a"],["T","A","C","G","t"]) == "ATCG"