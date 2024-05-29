import re

from compsci260lib import get_fasta_dict


def run_cloning():
    """Function demonstrating the procedure of extracting a gene and inserting
    into a plasmid using restriction enzymes.
    """
    aim2_fasta_path = "aim2_plus_minus_1kb.fasta"
    pRS304_fasta_path = "pRS304.fasta"

    # Read in the Aim2 genomic sequence from the fasta file along with its
    # upstream and downstream regions.
    #
    # Your code goes here
    #

    # Creat dictionary and fetch
    aim2_genomic = get_fasta_dict(aim2_fasta_path)["aim2"]

    # Store the beginning and end locations of the Aim2 gene as Python indices.

    # Assumption: Aim2 is in the only longest open reading frame
    # regex assuming DNA is coding strand
    start1 = "(atg)"
    middle1 = "((?!((tag)|(taa)|(tga)))([atcg]{3}))+"
    end1 = "((tag)|(taa)|(tga))"
    prog1 = re.compile(start1 + middle1 + end1)
    it1 = prog1.finditer(aim2_genomic)

    # regex assuming DNA is template strand
    start2 = "((cta)|(tta)|(tca))"
    middle2 = "((?!((cta)|(tta)|(tca)))([atcg]{3}))+"
    end2 = "(cat)"
    prog2 = re.compile(start2 + middle2 + end2)
    it2 = prog2.finditer(aim2_genomic)

    # looking for the longest match
    length = [0, 0, 0]
    for mat in it1:
        mylength = mat.end() - mat.start()
        if mylength > length[0]:
            length[0] = mylength
            length[1] = mat.start()
            length[2] = mat.end()

    for mat in it2:
        mylength = mat.end() - mat.start()
        if mylength > length[0]:
            length[0] = mylength
            length[1] = mat.start()
            length[2] = mat.end()
    aim2_beg = length[1]  # Your value goes here
    aim2_end = length[2]  # Your value goes here

    # Report start, end, length in nucleotides, and length in amino acids.
    #
    # Your code goes here
    #
    print("Aim2 gene")
    print("Start to end on Aim2 plus minus 1kb(in nucleotides and inclusive): {}-{}".format(aim2_beg + 1, aim2_end))
    print("Length (in amino acids): {}".format(int((aim2_end-aim2_beg)/3) - 1))
    # Define regular expression terms for each restriction enzyme
    r_enzymes = get_restriction_enzymes_regex()

    # Store coordinates of restriction sites found upstream, downstream, and
    # within the aim2 gene
    r_enzyme_sites = find_restriction_sites(aim2_genomic, window_beg=aim2_beg,
                                            window_end=aim2_end, r_enzymes=r_enzymes)

    # Report the found restriction enzyme sites
    #
    # Your code goes here
    #
    print("\nRestriction enzyme sites of Aim2 plus minus 1kb")
    print("Start and end in nucleotides and inclusive")
    for key in list(r_enzyme_sites):
        print(key + ":")
        print()
        for site in r_enzyme_sites[key]:
            print("    Start:", site["start"])
            print("    End:", site["end"])
            print("    Sequence:", site["sequence"])
            print("    Location:", site["location"])
            print()

    # Read in the pRS304 plasmid sequence and find restriction sites
    # in the entire plasmid
    mcs_start = 1891 - 1  # Your value here
    mcs_end = 1993  # Your value here
    prs304_genomic = get_fasta_dict(pRS304_fasta_path)["pRS304"]  # Your code here
    all_prs304_sites = find_restriction_sites(prs304_genomic, window_beg=mcs_start,
                                              window_end=mcs_end, r_enzymes=r_enzymes)

    # Report relevant summary information
    report_pRS304_MCS_sites(all_prs304_sites)

    # Extract aim2 gene and insert into the plasmid, report its length
    #
    # Your code goes here
    #
    # site index in nucleotides
    p_start = 1923
    p_end = 1928
    a_start_u = 459
    a_end_u = 464
    a_start_d = 2607
    a_start_d = 2612

    # The start and end index of excised fragment in nucleotides
    print("\nIn nucleotides")
    print("Start of excised fragment:", a_start_u + 1)
    print("End of excised fragment:", a_start_d)

    # Convert to string indices
    e_start = (a_start_u + 1) - 1
    e_end = a_start_d
    fragment = aim2_genomic[e_start:e_end]

    # plasmid cut index in nucleotides
    p_end_u = p_start
    p_start_d = p_start + 1

    # Convert to string indices
    p_start_d -= 1

    # combine
    new_plasmid = prs304_genomic[:p_end_u] + fragment + prs304_genomic[p_start_d:]

def get_restriction_enzymes_regex():
    """Returns a dictionary of restriction enzyme regular expressions for
    searching in genomic sequences.

    This function should be used for find_restriction_sites.
    """

    return {
        "BamHI": "ggatcc",
        "BstYI": "[ag]gatc[ct]",
        "SalI": "gtcgac",
        "SpeI": "actagt",
        "SphI": "gcatgc",
        "StyI": "cc[at]{2}gg"
    }


def find_restriction_sites(genomic_seq, window_beg, window_end, r_enzymes):
    """Finds the restriction enzyme sites in a genomic sequence. Stored
    as a dictionary of lists of dictionaries. Each restriction enzyme is
    a key in the outer dictionary corresponding to a list of all its sites.
    Each site has its information represented in a dictionary. Each site
    entry has a key specifying if the site is downstream, upstream, or
    within the parameter-specified window.

    Args:
        genomic_seq (str): genomic sequence to search for sites in
        window_beg (int)
        window_end (int)
        r_enzymes (dict): dictionary where key:value is enzyme:regex (same
        format returned by the get_restriction_enzymes_regex function)

    Each found site will have defined keys:
        sequence (str): the nucleotide sequence matched in the genome
        start (int): the start nucleotide position in the genome
        end (int): the ending position
        location (str): the position of the site relative to the specified window.
            (must be "upstream", "downstream", or "within")

    A valid returned dictionary may look like this:
    {
        "BamHI" : [
            {
                "start": 10,
                "end": 15,
                "sequence": "GGATCC",
                "location": "upstream"
            },
            {
                "start": 100,
                "end": 105,
                "sequence": "GGATCC",
                "location": "downstream"
            }
        ],
        "BstYI" : [
            {
                "start": 30,
                "end": 35,
                "sequence": "AGATCC",
                "location": "within"
            }
        ]
    }
    """

    if type(genomic_seq) is not str:
        raise TypeError(f"the argument 'genomic_seq' must be a string. "
                        "(received {type(genomic_seq)})")

    if window_beg >= window_end:
        raise ValueError("window_beg must be smaller than window_end")

    # Create dictionary to store coordinates
    r_enzyme_sites = {"BamHI": [], "BstYI": [], "SpeI": [],
                      "SphI": [], "StyI": [], "SalI": []}

    #
    # Your code goes here
    #
    for enzyme in list(r_enzyme_sites):
        # match re for each enzyme
        my_re = r_enzymes[enzyme]
        my_prog = re.compile(my_re)
        my_it = my_prog.finditer(genomic_seq)
        my_list = r_enzyme_sites[enzyme]
        for mat in my_it:
            # judge location
            if mat.end() <= window_beg:
                my_location = "upstream"
            elif mat.start() >= window_end:
                my_location = "downstream"
            else:
                my_location = "within"
            # update list
            # start and end in nucleotide
            my_list.append({
                "start": mat.start() + 1,
                "end": mat.end(),
                "sequence": (mat.string[mat.start(): mat.end()]).upper(),
                "location": my_location
            })
    return r_enzyme_sites


def report_pRS304_MCS_sites(p_enzyme_sites):
    """For each restriction enzyme, report how often that enzyme cuts the plasmid
    outside the MCS (upstream or downstream), how often it cuts the plasmid inside
    (within) the MCS, and relevant details about any sites located inside the MCS.
    """
    #
    # Your code goes here
    #
    print("PRS304 MCS sites report:")
    print("Start and end in nucleotides and inclusive\n")
    for key in list(p_enzyme_sites):
        print(key + ":")
        print("    Sites within MCS:\n")
        up = 0
        down = 0
        within = 0
        for site in p_enzyme_sites[key]:
            my_location = site["location"]
            assert isinstance(my_location, str)
            if my_location == "within":
                within += 1
                print("        Start:", site["start"])
                print("        End:", site["end"])
                print("        Sequence:", site["sequence"])
                print()
            elif my_location == "upstream":
                up += 1
            else:
                down += 1
        print("        Total site(s) within:", within)
        print("\n    Other sites:")
        print("        Upstream:", up)
        print("        Downstream:", down)

    return  # placeholder code, for a valid function


if __name__ == "__main__":
    """Run run_cloning(). Do not modify this code"""
    run_cloning()
