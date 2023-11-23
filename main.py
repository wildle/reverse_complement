input_string = "ATGC"

def reverse_complement(input_string : str) -> str:
    output_string = ""
    for char in input_string:
        if char == "A":
            output_string = output_string + "T"
        elif char == "T":
            output_string = output_string + "A"
        elif char == "G":
            output_string = output_string + "C"
        elif char == "C":
            output_string = output_string + "G"
        else:
            output_string = output_string + ""
    # reverse the string and return it
    return output_string[::-1]

if __name__ == "__main__":
    print(input_string)
    print(reverse_complement(input_string))
    assert reverse_complement("CGAT") == "ATCG"