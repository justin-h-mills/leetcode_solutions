import os
import importlib.util
import json
import pytest

# Helper function to load test cases from a test_cases.json file
def load_test_cases(test_cases_file):
    with open(test_cases_file, "r") as file:
        return json.load(file)

# Function to discover problem folders within the solutions directory
def discover_problems(solutions_dir):
    problems = []
    if not os.path.exists(solutions_dir):
        return problems

    for folder in os.listdir(solutions_dir):
        problem_dir = os.path.join(solutions_dir, folder)
        if os.path.isdir(problem_dir):
            problems.append(folder)
    return problems

# Function to discover solutions within a given problem folder
def discover_solutions(difficulty, problem_folder):
    solutions = []
    solutions_dir = os.path.join(difficulty, problem_folder, "solutions")
    if not os.path.exists(solutions_dir):
        return solutions

    for solution_file in os.listdir(solutions_dir):
        if solution_file.endswith(".py"):
            solutions.append(solution_file)
    return solutions

# Define test_solution function at the module level and parameterize it with difficulty
@pytest.mark.parametrize("problem_folder, solution_file, difficulty", [
    (problem, solution, difficulty) for difficulty in ["easy", "medium", "hard"]
    for problem in discover_problems(difficulty)
    for solution in discover_solutions(difficulty, problem)
])
def test_solution(problem_folder, solution_file, difficulty):
    solution_path = os.path.join(difficulty, problem_folder, "solutions", solution_file)

    if not os.path.exists(solution_path):
        return

    # Load the solution module dynamically
    spec = importlib.util.spec_from_file_location("solution_module", solution_path)
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)

    # Assuming the class name is 'Solution'
    solution_class = solution_module.Solution

    # Load test cases for the specific problem
    test_cases_file = os.path.join(difficulty, problem_folder, "test_cases.json")
    if not os.path.exists(test_cases_file):
        return

    test_cases = load_test_cases(test_cases_file)

    # Extract the function to test from the test_cases.json file
    func_name = test_cases.get("func", "test_solution")

    # Get the function from the class
    test_function = getattr(solution_class(), func_name)

    # Iterate over test cases and assert the results
    for case_id, test_case in test_cases.get("tests", {}).items():
        result = test_function(**test_case.get("input"))
        expected = test_case.get("expected")
        assert result == expected
