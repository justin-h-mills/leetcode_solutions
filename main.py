import subprocess

# Function to run tests for a given difficulty level
def run_tests(difficulty, verbose=False, warning=True):
    # Build the command to run pytest with or without the --verbose and --show-capture options
    command = ["pytest", f"tests/test_solutions.py"]
    if verbose:
        command.append("--verbose")
        command.append("--show-capture=all")  # This enables showing captured output
        command.append("-rf")  # Enable detailed info for failed tests
    if warning:
        command.append("-p no:warnings")

    command.append("-k")
    command.append(f"{difficulty}")

    # Run pytest and capture the results
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Log the results to a file
    log_file_path = f"logs/{difficulty}_test_results.log"
    with open(log_file_path, "w") as log_file:
        log_file.write("Test Output:\n")
        log_file.write(result.stdout)
        log_file.write("\n\nError Output:\n")
        log_file.write(result.stderr)

if __name__ == "__main__":
    difficulties = ["easy", "medium", "hard"]
    verbose = True
    warning = False

    for difficulty in difficulties:
        run_tests(difficulty, verbose, warning)
