"""
Constraint Prompt
A Procedural Spatial Prompt Generator

What this tool does

Constraint Prompt generates small, room-scale spatial design prompts.
Each output is intended to be SKETCHED or REINTERPRETED, not used as a
finished level.

How to run

python constraint_prompt.py

Optional arguments:
--count 20
--risk low|high
--density sparse|medium|dense
--grammar random|linear|loop|branch

Example:
python constraint_prompt.py --count 20 --risk high --density dense --grammar loop
"""

import random
import argparse

# Spatial Grammars

SPATIAL_GRAMMARS = {
    "linear": {
        "description": "Linear space with forward pressure",
        "base_zones": ["entry", "choke point", "terminal space"],
        "prompt": "How does forward progress increase tension?"
    },
    "loop": {
        "description": "Looping space with repeated traversal",
        "base_zones": ["central area", "loop path"],
        "prompt": "How does repetition change player behavior?"
    },
    "branch": {
        "description": "Hub with short branching paths",
        "base_zones": ["hub", "branch A", "branch B"],
        "prompt": "How does partial information affect choice?"
    }
}

# Constraints by Risk

LOW_RISK_CONSTRAINTS = [
    "Mistakes are recoverable",
    "Danger is clearly telegraphed",
    "Safe fallback zone exists"
]

HIGH_RISK_CONSTRAINTS = [
    "Movement slows while carrying objects",
    "Danger escalates if the player lingers",
    "One-way interaction with no reset",
    "Optimal path carries the most risk"
]

# Density Handling

EXTRA_ZONES = [
    "hidden cave",
    "hazard pocket",
    "timing gate",
    "unsafe shortcut",
    "obscured vantage point"
]

DENSITY_COUNTS = {
    "sparse": 0,
    "medium": 1,
    "dense": 2
}

# Generator Logic

def choose_grammar(grammar_choice):
    if grammar_choice == "random":
        return random.choice(list(SPATIAL_GRAMMARS.items()))
    return grammar_choice, SPATIAL_GRAMMARS[grammar_choice]

def generate_room(risk, density, grammar_choice):
    grammar_name, grammar = choose_grammar(grammar_choice)

    zones = list(grammar["base_zones"])

    for _ in range(DENSITY_COUNTS[density]):
        zones.append(random.choice(EXTRA_ZONES))

    if risk == "high":
        constraint = random.choice(HIGH_RISK_CONSTRAINTS)
    else:
        constraint = random.choice(LOW_RISK_CONSTRAINTS)

    return {
        "grammar": grammar_name,
        "grammar_description": grammar["description"],
        "zones": zones,
        "risk": risk,
        "density": density,
        "constraint": constraint,
        "prompt": f"{grammar['prompt']} Constraint: {constraint}"
    }

def generate_batch(count, risk, density, grammar_choice):
    return [generate_room(risk, density, grammar_choice) for _ in range(count)]

# Output Formatting

def print_room(room, index):
    print(f"\n--- Output {index} ---")
    print(f"Grammar: {room['grammar']} ({room['grammar_description']})")
    print(f"Risk: {room['risk']} | Density: {room['density']}")
    print(f"Zones: {', '.join(room['zones'])}")
    print(f"Constraint: {room['constraint']}")
    print(f"Design Prompt: {room['prompt']}")

# Command Line Interface

def main():
    parser = argparse.ArgumentParser(
        description="Constraint Prompt — Procedural Spatial Prompt Generator"
    )

    parser.add_argument("--count", type=int, default=10,
                        help="Number of outputs to generate (default: 10)")
    parser.add_argument("--risk", choices=["low", "high"], default="low",
                        help="Risk level (default: low)")
    parser.add_argument("--density", choices=["sparse", "medium", "dense"], default="medium",
                        help="Spatial density (default: medium)")
    parser.add_argument("--grammar", choices=["random", "linear", "loop", "branch"], default="random",
                        help="Spatial grammar (default: random)")

    args = parser.parse_args()

    rooms = generate_batch(
        count=args.count,
        risk=args.risk,
        density=args.density,
        grammar_choice=args.grammar
    )

    print("\nConstraint Prompt — Generated Outputs")
    print("====================================")

    for i, room in enumerate(rooms, start=1):
        print_room(room, i)

if __name__ == "__main__":
    main()
