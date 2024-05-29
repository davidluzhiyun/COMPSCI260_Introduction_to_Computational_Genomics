import re

def run_plasmid():
    seq="atgacatgacgtga"
    seq2 = "tgaatgacaatgacatgaatgaca"
    ml = orf_help1(seq2 + seq2)
    print(orf_help3_process(ml, len(seq2)))



def orf_help1(seq,min_length_aa=0, strand="W"):

    #DNA
    re_start1 = "(atg)"
    re_mid1 = "((?!((tag)|(taa)|(tga)))([atcg]{3}))"
    re_end1 = "((tag)|(taa)|(tga))"

    #

    # calculate the repetition
    rep = max(min_length_aa - 1, 0)
    # resulting re
    re_rep = "{" + str(rep) + ",}"
    regex1 = "(?=(" + re_start1 + re_mid1 + re_rep + re_end1 + "))"
    # search
    prog1 = re.compile(regex1)
    it1 = prog1.finditer(seq)
    ls = []
    for mat in list(it1):
        my_start = mat.start(1) + 1
        my_stop = mat.end(1)
        my_stop_codon = seq[mat.end(1) - 3:mat.end(1)].upper()
        my_nlength = mat.end(1) - mat.start(1)
        my_aalength = my_nlength//3 - 1
        my_frame = mat.start(1) % 3
        my_strand = strand
        ls.append({
            "frame": my_frame,
            "stop": my_stop,
            "aalength": my_aalength,
            "start": my_start,
            "stopcodon": my_stop_codon,
            "nlength": my_nlength,
            "strand": my_strand
        })
    return ls

def orf_help2_flip(seq):
    assert isinstance(seq, str)
    ret_seq = ""
    cpl = { "a": "t",
            "t": "a",
            "c": "g",
            "g": "c"}
    for i in range(len(seq) - 1, -1, -1):
        ret_seq = ret_seq + cpl[seq[i]]
    return ret_seq

def orf_help3_process(list1, length):
    # remove duplicated results
    my_list = [orf for orf in list1 if orf["start"] < length]

    tracker = [False for i in range(len(my_list))]
    ret_list = []
    for orf in my_list:
        if orf["stop"] > length:
            orf["stop"] = orf["stop"] - length
    # remove overlap
    for i in range(len(my_list)):
        if tracker[i]:
            continue
        tracker[i] = True
        longest = my_list[i]
        for j in range(i + 1, len(my_list)):
            if tracker[j]:
                continue
            if my_list[j]["stop"] == longest["stop"]:
                tracker[j] = True
                if my_list[j]["nlength"] >= longest["nlength"]:
                    longest = my_list[j]
        ret_list.append(longest)
    return ret_list

if __name__ == "__main__":
    run_plasmid()