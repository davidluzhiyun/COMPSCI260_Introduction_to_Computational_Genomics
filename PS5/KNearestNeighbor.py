from math import sqrt


def run_k_nearest_neighbor():
    """Run K Nearest neighbors against the training and test sets."""
    input_patients = read_training_data("gene_expression_training_set.txt")
    new_patients = read_test_data("gene_expression_test_set.txt")
    solve_k_nearest(input_patients, new_patients, k=5)


def solve_k_nearest(input_patients, new_patients, k):
    """
    Read in the input patients as training data to use to determine and report
    the prognosis of the 10 new patients.

    Args:
        input_patients (list of dicts): dictionaries of training patient
            data. see: `read_training_data`

        new_patients (list of dicts): dictionaries of test patient data.
            see: `read_test_data`
        k (int): number of nearest neighbors to use to predict the prognosis
        for an unlabeled patient
    """
    
    #
    # YOUR CODE HERE
    #
    print("k = 5. Predicting class for 10 new patients. \'R\' for responsive to treatment, \'N\' for non-responsive.")
    print("Patient    Class")
    for i in range(len(new_patients)):
        patient = new_patients[i]
        k_nearest_helper(input_patients, patient, k)
        print("Patient {}  {}".format(i+1, patient['class']))


# helper function for solving the problem for one patient
def k_nearest_helper(input_patients, new_patient, k):
    """
    Read in the input patients as training data to use to determine and report
    the prognosis of the 1 new patient.

    Args:
        input_patients (list of dicts): dictionaries of training patient
            data. see: `read_training_data`

        new_patient (dict): dictionary of test patient data.
            see: `read_test_data`
        k (int): number of nearest neighbors to use to predict the prognosis
        for an unlabeled patient
    """
    # sort base on distance
    input_sorted = sorted(input_patients, key=lambda entry: compute_dist(entry['expression'], new_patient['expression']))
    n_count = 0
    r_count = 0
    # Just take the first k in the sorted list to break tie
    for i in range(k):
        if input_sorted[k]['class'] == 'N':
            n_count += 1
        else:
            r_count += 1
    # Fill in entry
    # prefer 'N' for even k
    if n_count >= r_count:
        new_patient['class'] = 'N'
    else:
        new_patient['class'] = 'R'


def read_training_data(file_name):
    """Read the training gene expression data from a text file. Note: the
    patients in the training data are classified as "R" (responsive to
    treatment) or "N" (non-responsive to treatment).  For example,
    input_patients[0]["class"] = the class of the first patient (R or N)
    input_patients[0]["expression"][0] = the expression of the first
    gene for the first patient.

    Returns:
        (list of dicts): list of patients as a class and expression data. The
        dictionary of each patient will be in the form of:
            'class' -> string with values strictly 'N' or 'R' for
            non-responsive or responsive to the treatment
            'expression' -> list of floats of gene expression values

        and look something like:
            {'class': 'N', 'expression': [9.049, 8.313, ..., 6.428700888]}
    """
    return read_data(file_name, test_data=False)


def read_test_data(file_name):
    """Read the test gene expression data from a text file. Note: the
    patients in the test data are not classified.

   Returns:
    (list of dicts): list of patients as a class and expression data. The
    dictionary of each patient will be in the form of:
        'class' -> string with only 'unknown' as its value
        'expression' -> list of floats of gene expression values

    and look something like:
        {'class': 'unknown', 'expression': [9.049, 8.313, ..., 6.428700888]}
    """
    return read_data(file_name, test_data=True)


def read_data(file_name, test_data=False):
    with open(file_name, "r") as f:
        lines = f.readlines()

    patients = []

    for line in lines:
        line = line.strip()
        data = line.split()  # check that you are splitting on "\t"

        if test_data:
            class_name = "unknown"
        else:
            class_name = data.pop(0)

        float_data = [float(datum) for datum in data]
        patient = {"class": class_name, "expression": float_data}
        patients.append(patient)

    return patients


def compute_dist(tuple_1, tuple_2):
    """Return the Euclidean distance between two points in any number of
    dimensions."""
    
    if len(tuple_1) != len(tuple_2):
        raise ValueError("Cannot compute Euclidean distance between tuples of different sizes!")
    
    dist = 0
    for i in range(len(tuple_1)):
        dist += (tuple_1[i] - tuple_2[i]) * (tuple_1[i] - tuple_2[i])
      
    return sqrt(dist)


if __name__ == "__main__":
    run_k_nearest_neighbor()
