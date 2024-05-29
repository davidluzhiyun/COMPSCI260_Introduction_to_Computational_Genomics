import random
import textwrap


def run_language():
    """Call `generate_mm_text` with the provided parameters."""
    """
    file_name = ""
    order = 2
    M = 1000
    generated_text = generate_mm_text(file_name, order, M)
    """
    file_name = "tidy.paradise.lost.txt"
    order = 1
    M = 1000
    generated_text = generate_mm_text(file_name, order, M)
    fh = open("paradise.lost.mm.1.txt", "w")
    fh.write(generated_text)
    fh.close()


def generate_mm_text(file_name, order, M):
    """Create a Markov model for a given text file and output artificially
    generated text from the model.

    Args:
        file_name (str): path of the text to process
        order (int): order of the Markov model
        M (int): the length of the number of characters in the returned generated
        string

    Returns:
        A string of randomly generated text using a Markov model
    """
    # Read the contents of the file
    f = open(file_name, "r")

    if f is None:
        print("Can't open " + file_name)
    else:
        contents = f.read()
        f.close()
        contents = contents.replace("\n", "")
        contents = contents.replace("\r", "")

    # Collect the counts necessary to estimate transition probabilities
    # This dictionary will store all the data needed to estimate the Markov model:
    txt_dict = collect_counts(contents, order)

    # Generate artificial text from the trained model
    seed = contents[0:order]
    text = seed

    for _ in range(M):
        next_character = generate_next_character(seed, txt_dict)
        text += next_character
        seed = seed[1:] + next_character

    text_list = textwrap.wrap(text, 72)
    text = "\n".join(text_list)

    # Return the generated text
    return text


def display_dict(txt_dict):
    """Print the text dictionary as a table of keys to counts.
    Currently accepts a dictionary specified by the return documentation in the
    `build_dict` function.

    You will need to modify this function to accept the dictionary returned by
    the `collect_counts` function.

    Arguments:
        txt_dict (dict) - Mapping keys (as strings) to counts (as ints). After
        modification for `collect_counts`, the txt_dict will map keys (as strings)
        to dictionaries of counts and followers described in the return method
        of `collect_counts`.
    """
    print("key\tcount\tfollower counts")
    for key in txt_dict.keys():
        print("%s\t%d " % (key, txt_dict[key]), "\t", end=" ")


def build_dict(contents, k):
    """Builds a dictionary of k-character (k-tuple) substring counts. Store the
    dictionary mapping from the k-tuple to an integer count.

    Args:
        contents (str): the string contents of to count
        k (int): number of characters in the substring

    Returns:
        a text dictionary mapping k-tuple to an integer
        Example return value with k=2:
        { 
            "ac": 1,
            "cg": 2,
            ... 
        }
    """
    #
    # YOUR CODE HERE
    #
    my_dict = {}
    # every k-tuple except the last
    for i in range(len(contents) - k):
        k_tuple = contents[i:i + k]
        # create new entry if not in dictionary
        if my_dict.get(k_tuple) is None:
            my_dict[k_tuple] = 1
        # increase count if entry exists
        else:
            my_dict[k_tuple] += 1

    return my_dict


def collect_counts(contents, k):
    """Build a k-tuple dictionary mapping from k-tuple to a dictionary of
    of counts and dictionary of follower counts.
    
    Args:
        contents (str): the string contents of to count
        k (int): number of characters in the substring

    Returns:
        a dictionary mapping k-tuple to a dictionary of counts and dictionary
        of follower counts. Example return value with k=2:
        {
            "ac": {
                "count": 1,
                "followers": {"g": 1, "c": 2}
            },
            ...
        }

    Note: This function will similar to `build_dict`. We separated the 
    k-character and follower counting to explain each as distinct concepts. You
    should use the k-character counting code you wrote in `build_dict` as a 
    starting point.

    While the Markov model only needs to use `collect_counts` to generate text,
    our auto-grader will test the behavior of `build_dict` so that function 
    does need to work properly.
    """
    #
    # YOUR CODE HERE
    #
    my_dict = {}
    # every k-tuple except the last
    for i in range(len(contents) - k):
        k_tuple = contents[i:i + k]
        follower = contents[i + k]
        # create new tuple entry if not in dictionary
        if my_dict.get(k_tuple) is None:
            my_dict[k_tuple] = {
                "count": 1,
                "followers": {follower: 1}
            }
        # increase count if tuple exists
        else:
            my_dict[k_tuple]["count"] += 1
            # create new follower entry if not in dictionary
            if my_dict[k_tuple]["followers"].get(follower) is None:
                my_dict[k_tuple]["followers"][follower] = 1
            else:
                # increase count if follower exists
                my_dict[k_tuple]["followers"][follower] += 1
    return my_dict


def generate_next_character(seed, txt_dict):
    """Randomly select the next character of a k-tuple using the follower
    counts to determine the probability.

    Args:
        seed (str): k-tuple to follow from
        txt_dict (dict): k-tuple count follower dictionary

    Returns:
        (str) of the next character
    """
    #
    # YOUR CODE HERE
    #

    followers = txt_dict[seed]["followers"]
    # possible characters as a list
    follower_chars = list(followers.keys())
    # counts in the corresponding order
    weights = [followers[char] for char in follower_chars]
    # choosing based on the weight
    res = random.choices(follower_chars, weights=weights, k=1)[0]
    return res


if __name__ == "__main__":
    """Main method call, do not modify"""
    run_language()
