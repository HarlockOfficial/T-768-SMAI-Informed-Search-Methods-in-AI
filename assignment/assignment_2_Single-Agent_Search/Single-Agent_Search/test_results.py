import os.path
import subprocess
import argparse


def save_to_file(file_name, content):
    """
    Save the content to a file.
    :param file_name: The file name.
    :param content: The content to save.
    """
    if not os.path.exists(os.path.dirname(file_name)):
        os.makedirs(os.path.dirname(file_name))
    if not os.path.isfile(file_name):
        open(file_name, 'w').close()
    with open(file_name, 'w') as f:
        f.write(content)


def generate_output_file_name(run_arguments: list[str], test_number: int, test_iteration: int):
    """
    Generate the output file name.
    :param run_arguments: The arguments used to run the simulation.
    :param test_number: The test number.
    :param test_iteration: The test iteration.
    :return: The output file name.
    """
    if len(run_arguments) == 0:
        run_arguments = ["default"]
    return "test_results/test_" + '_'.join([arg.strip('-') for arg in run_arguments]) + "/test_" + str(test_number) + "_" + str(test_iteration) + ".txt"


def run_test(run_arguments: list[str], test_number: int, test_iteration: int):
    """
    Run a test.
    :param run_arguments: The arguments used to run the simulation.
    :param test_number: The test number.
    :param test_iteration: The test iteration.
    """
    print("Running Test Number " + str(test_number) + " Iteration " + str(test_iteration))
    out = subprocess.run(["python", "main.py"] + run_arguments, capture_output=True, text=True)
    if out.returncode != 0 or out.stderr != "":
        print(out.stderr)
        exit(-1)
    assert out.returncode == 0 and out.stderr == ""
    out_file_name = generate_output_file_name(run_arguments, test_number, test_iteration)
    save_to_file(out_file_name, out.stdout)


def pretty_print(content: dict[str, float]):
    out = ""
    for key in content:
        out += key + ": " + str(content[key]) + "\n"
    return out


def compute_test_average(run_arguments: list[str], test_index: int):
    """
    Compute the average of all tests of a given type.
    :param run_arguments: The arguments used to run the simulation.
    :param test_index: The test index.
    """
    print("Computing Average for Test Number " + str(test_index))
    out_file_name = generate_output_file_name(run_arguments, test_index, 0)
    file_contents = dict()
    for file in os.listdir(os.path.dirname(out_file_name)):
        if file.endswith(".txt"):
            with open(os.path.join(os.path.dirname(out_file_name), file), 'r') as f:
                content = f.read().splitlines()[2:-1]
                for line in content:
                    if not line:
                        continue
                    assert ':' in line
                    line = line.strip().split(':')
                    key = line[0].strip()
                    value = float(line[1].strip())
                    if key not in file_contents:
                        file_contents[key] = list()
                    file_contents[key].append(value)
    for key in file_contents:
        file_contents[key] = sum(file_contents[key]) / len(file_contents[key])
    save_to_file(os.path.dirname(out_file_name) + "/average.txt", pretty_print(file_contents))


if __name__ == "__main__":
    """
    This script performs the tests required by the assignment.
    Each Test is performed 10 times and the average is computed.
    1. Test the simulation with the default parameters.
    2. Test the simulation with 3 gates, 1 cars and the improved heuristic.
    3. Test the simulation with 3 gates, 10 cars and the improved heuristic.
    
    For each simulation a folder is created and each run result is stored in a separate file.
    The average is computed and stored in a file called "average.txt".
    
    Further tests can be added to verify the impact of the number of cars, gates and capacity.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", action='store_true', help="Run Tests.")
    parser.add_argument('-a', '--average', action='store_true', help='Compute average for test.')
    parser.add_argument('-d', '--default', action='store_true', help='Run default test.')
    parser.add_argument('-o', '--other', action='store_true', help='Run other tests.')
    args = vars(parser.parse_args())

    print(args)

    default_test_list = [
        ([], 10),
        (['--gates', '3', '--cars', '1', '--improved'], 10),
        (['--gates', '3', '--cars', '10', '--improved'], 10)
    ]
    other_test_list = [
        (['--gates', '2', '--cars', '6', '--boxcap', '1000'], 10),  # default
        (['--gates', '2', '--cars', '6', '--boxcap', '1000', '--improved'], 10),  # default + improved

        (['--gates', '1', '--cars', '6', '--boxcap', '1000'], 10),  # gates 1
        (['--gates', '1', '--cars', '6', '--boxcap', '1000', '--improved'], 10),  # gates 1 + improved

        (['--gates', '10', '--cars', '6', '--boxcap', '1000'], 10),  # gates 10
        (['--gates', '10', '--cars', '6', '--boxcap', '1000', '--improved'], 10),  # gates 10 + improved

        (['--gates', '2', '--cars', '1', '--boxcap', '1000'], 10),  # cars 1
        (['--gates', '2', '--cars', '1', '--boxcap', '1000', '--improved'], 10),  # cars 1 + improved

        (['--gates', '2', '--cars', '10', '--boxcap', '1000'], 10),  # cars 10
        (['--gates', '2', '--cars', '10', '--boxcap', '1000', '--improved'], 10),  # cars 10 + improved

        (['--gates', '2', '--cars', '6', '--boxcap', '500'], 10),  # boxcap 500
        (['--gates', '2', '--cars', '6', '--boxcap', '500', '--improved'], 10),  # boxcap 500 + improved

        (['--gates', '2', '--cars', '6', '--boxcap', '1500'], 10),  # boxcap 1500
        (['--gates', '2', '--cars', '6', '--boxcap', '1500', '--improved'], 10),  # boxcap 1500 + improved

        (['--gates', '1', '--cars', '1', '--boxcap', '1000'], 10),  # gates 1 + cars 1
        (['--gates', '1', '--cars', '1', '--boxcap', '1000', '--improved'], 10),  # gates 1 + cars 1 + improved

        (['--gates', '10', '--cars', '10', '--boxcap', '1000', '--time', '1'], 10),  # gates 10 + cars 10
        (['--gates', '10', '--cars', '10', '--boxcap', '1000', '--improved', '--time', '1'], 10),  # gates 10 + cars 10 + improved

        (['--gates', '1', '--cars', '10', '--boxcap', '1000', '--time', '1'], 10),  # gates 1 + cars 10
        (['--gates', '1', '--cars', '10', '--boxcap', '1000', '--improved', '--time', '1'], 10),  # gates 1 + cars 10 + improved

        (['--gates', '10', '--cars', '1', '--boxcap', '1000', '--time', '1'], 10),  # gates 10 + cars 1
        (['--gates', '10', '--cars', '1', '--boxcap', '1000', '--improved', '--time', '1'], 10),  # gates 10 + cars 1 + improved

        (['--gates', '1', '--cars', '1', '--boxcap', '500', '--time', '1'], 10),  # gates 1 + cars 1 + boxcap 500
        (['--gates', '1', '--cars', '1', '--boxcap', '500', '--improved', '--time', '1'], 10),
        # gates 1 + cars 1 + boxcap 500 + improved

        (['--gates', '10', '--cars', '10', '--boxcap', '500', '--time', '1'], 10),  # gates 10 + cars 10 + boxcap 500
        (['--gates', '10', '--cars', '10', '--boxcap', '500', '--improved', '--time', '1'], 10),
        # gates 10 + cars 10 + boxcap 500 + improved

        (['--gates', '1', '--cars', '10', '--boxcap', '500', '--time', '1'], 10),  # gates 1 + cars 10 + boxcap 500
        (['--gates', '1', '--cars', '10', '--boxcap', '500', '--improved', '--time', '1'], 10),
        # gates 1 + cars 10 + boxcap 500 + improved

        (['--gates', '10', '--cars', '1', '--boxcap', '500', '--time', '1'], 10),  # gates 10 + cars 1 + boxcap 500
        (['--gates', '10', '--cars', '1', '--boxcap', '500', '--improved', '--time', '1'], 10),
        # gates 10 + cars 1 + boxcap 500 + improved

        (['--gates', '1', '--cars', '1', '--boxcap', '1500', '--time', '1'], 10),  # gates 1 + cars 1 + boxcap 1500
        (['--gates', '1', '--cars', '1', '--boxcap', '1500', '--improved', '--time', '1'], 10),
        # gates 1 + cars 1 + boxcap 1500 + improved

        (['--gates', '10', '--cars', '10', '--boxcap', '1500', '--time', '1'], 10),  # gates 10 + cars 10 + boxcap 1500
        (['--gates', '10', '--cars', '10', '--boxcap', '1500', '--improved', '--time', '1'], 10),
        # gates 10 + cars 10 + boxcap 1500 + improved

        (['--gates', '1', '--cars', '10', '--boxcap', '1500', '--time', '1'], 10),  # gates 1 + cars 10 + boxcap 1500
        (['--gates', '1', '--cars', '10', '--boxcap', '1500', '--improved', '--time', '1'], 10),
        # gates 1 + cars 10 + boxcap 1500 + improved

        (['--gates', '10', '--cars', '1', '--boxcap', '1500', '--time', '1'], 10),  # gates 10 + cars 1 + boxcap 1500
        (['--gates', '10', '--cars', '1', '--boxcap', '1500', '--improved', '--time', '1'], 10),
        # gates 10 + cars 1 + boxcap 1500 + improved

        (['--gates', '1', '--cars', '6', '--boxcap', '500', '--time', '1'], 10),  # gates 1 + boxcap 500
        (['--gates', '1', '--cars', '6', '--boxcap', '500', '--improved', '--time', '1'], 10),  # gates 1 + boxcap 500 + improved

        (['--gates', '10', '--cars', '6', '--boxcap', '500', '--time', '1'], 10),  # gates 10 + boxcap 500
        (['--gates', '10', '--cars', '6', '--boxcap', '500', '--improved', '--time', '1'], 10),  # gates 10 + boxcap 500 + improved

        (['--gates', '1', '--cars', '6', '--boxcap', '1500', '--time', '1'], 10),  # gates 1 + boxcap 1500
        (['--gates', '1', '--cars', '6', '--boxcap', '1500', '--improved', '--time', '1'], 10),  # gates 1 + boxcap 1500 + improved

        (['--gates', '10', '--cars', '6', '--boxcap', '1500', '--time', '1'], 10),  # gates 10 + boxcap 1500
        (['--gates', '10', '--cars', '6', '--boxcap', '1500', '--improved', '--time', '1'], 10),
        # gates 10 + boxcap 1500 + improved

        (['--gates', '2', '--cars', '1', '--boxcap', '500', '--time', '1'], 10),  # cars 1 + boxcap 500
        (['--gates', '2', '--cars', '1', '--boxcap', '500', '--improved', '--time', '1'], 10),  # cars 1 + boxcap 500 + improved

        (['--gates', '2', '--cars', '10', '--boxcap', '500', '--time', '1'], 10),  # cars 10 + boxcap 500
        (['--gates', '2', '--cars', '10', '--boxcap', '500', '--improved', '--time', '1'], 10),  # cars 10 + boxcap 500 + improved

        (['--gates', '2', '--cars', '1', '--boxcap', '1500', '--time', '1'], 10),  # cars 1 + boxcap 1500
        (['--gates', '2', '--cars', '1', '--boxcap', '1500', '--improved', '--time', '1'], 10),  # cars 1 + boxcap 1500 + improved

        (['--gates', '2', '--cars', '10', '--boxcap', '1500', '--time', '1'], 10),  # cars 10 + boxcap 1500
        (['--gates', '2', '--cars', '10', '--boxcap', '1500', '--improved', '--time', '1'], 10),
        # cars 10 + boxcap 1500 + improved
    ]

    test_list = list()
    if args['default']:
        test_list.extend(default_test_list)
    if args['other']:
        test_list.extend(other_test_list)

    if args['test']:
        for test_index, test in enumerate(test_list):
            if test_index < 16:
                continue
            for test_iteration in range(test[1]):
                run_test(test[0], test_index, test_iteration)

    if args['average']:
        for test_index, test in enumerate(test_list):
            compute_test_average(test[0], test_index)
