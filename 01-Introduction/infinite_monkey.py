_ = """
Infinite Monkey Theorem
-----------------------

The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, such as the complete works of William Shakespeare. Well, suppose we replace a monkey with a Python function. How long do you think it would take for a Python function to generate just one sentence of Shakespeare? The sentence we'll shoot for is: “methinks it is like a weasel”

The way we'll simulate this is to write a function that generates a string that is 28 characters long by choosing random letters from the 26 letters in the alphabet plus the space. We'll write another function that will score each generated string by comparing the randomly generated string to the goal.

A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done. If the letters are not correct then we will generate a whole new string.To make it easier to follow your program's progress this third function should print out the best string generated so far and its score every 1000 tries.

See if you can improve upon the program in the self check by keeping letters that are correct and only modifying one character in the best string so far. This is a type of algorithm in the class of 'hill climbing' algorithms, that is we only keep the result if it is better than the previous one.
"""

import random

REQUIRED_STRING = "methinks it is like a weasel"
LEN_OF_REQ_STR = len(REQUIRED_STRING)
ALPHABET = "abcdefghilkmnopqrstuvwxyz "

def compare_strings(generated_string: str) -> int: 
    """Compare the generated string to the required string and return a score."""
    return sum(1 for gen, req in zip(generated_string, REQUIRED_STRING)
               if gen == req)

def generate_string() -> str: 
    """Generate a random string of the same length as the required string."""
    gen_list = [random.choice(ALPHABET)
                for _ in range(LEN_OF_REQ_STR)]
    return "".join(gen_list)

def mutate_string(given_string: str) -> str: 
    """Mutates the given string by replacing incorrect characters with random ones from the alphabet. 
    
    Falls under HILL CLIMIBING class of algorithms.
    """
    mutated_chars = [
        random.choice(ALPHABET) if given != target else given
        for given, target in zip(given_string, REQUIRED_STRING)
    ]
    return "".join(mutated_chars)

def simulate(max_iterations: int = 100_000_000, print_interval: int = 1000) -> None:
    """
    Simulate the Infinite Monkey Theorem, attempting to generate the required string.
    
    :param max_iterations: Maximum number of iterations to attempt.
    :param print_interval: Interval at which to print progress updates.
    """
    best_string = ""
    max_score = 0
    
    for i in range(max_iterations):
        if i == 0: 
            generated_string = generate_string()
        else: 
            generated_string = mutate_string(generated_string)
            
        score = compare_strings(generated_string)
        
        if score > max_score:
            best_string = generated_string
            max_score = score
            print(f"Sentence: {best_string}\tScore: {max_score}\tIteration: {i}")
        
        if score == LEN_OF_REQ_STR:
            print(f"\n\nFound the string at iteration {i}")
            break

        if i % print_interval == 0 and score < LEN_OF_REQ_STR:
            print(f"Iteration {i}: Best string so far: '{best_string}' with score {max_score}")

    else:
        print(f"\nReached max iterations ({max_iterations}) without finding the string.")

if __name__ == "__main__":
    simulate()