# Procedural Space Generator overview

This tool generates small, room-scale spatial design prompts for games, tabletop scenarios, and interactive fiction.
Spatial structure, sets of zones, constraints that affect movement/interaction, and short design prompts are combined to create outputs that are meant to be interpreted and sketched by the user. The tool is useful for exploring ideas quickly rather than producing finished levels outright.

# How to Run or Access the Tool

Requirements
Python 3.10 or later

No external libraries are required

Setup
1. Download or clone the repository
2. Navigate to the project folder
3. Run:
   python constraint_sketch.py
With the default settings, the tool will generate a batch of ten room prompts with low risk, medium density, random spatial grammar, and print them to the terminal.

There is further detailed comments in the actual file on the exact prompts that the user can change with an example provided for syntax.

# Parameters

1. Risk Level

Low risk:
- Forgiving layout
- Easily identified danger
- Escape paths

High risk:
- Escalated danger
- Congested walkways

Effect:
Higher risk produces more tense rooms


2. Spatial Density

Sparse:
- Fewer zones
- Straight forward paths

Dense:
- More zones
- Lots of interactions
- Requires more planning

Effect:
Higher density increases complexity by requiring more planning ahead.


3. Spatial grammar

(Structural pattern)
- Linear (choke points, dead ends)
- Loop (repeated traversal)
- Branch (hub with short paths)

Effect:
Grammar shapes how players move and make decisions.


# Example Outputs


Constraint Prompt — Generated Outputs


--- Output 1 ---

Grammar: branch (Hub with short branching paths)

Risk: low | Density: medium

Zones: hub, branch A, branch B, unsafe shortcut

Constraint: Mistakes are recoverable

Design Prompt: How does partial information affect choice? Constraint: Mistakes are recoverable

--- Output 2 ---

Grammar: loop (Looping space with repeated traversal)

Risk: low | Density: medium

Zones: central area, loop path, hazard pocket

Constraint: Mistakes are recoverable

Design Prompt: How does repetition change player behavior? Constraint: Mistakes are recoverable

--- Output 3 ---

Grammar: branch (Hub with short branching paths)

Risk: low | Density: medium

Zones: hub, branch A, branch B, timing gate

Constraint: Mistakes are recoverable

Design Prompt: How does partial information affect choice? Constraint: Mistakes are recoverable

--- Output 4 ---

Grammar: branch (Hub with short branching paths)

Risk: low | Density: medium

Zones: hub, branch A, branch B, obscured vantage point

Constraint: Danger is clearly telegraphed

Design Prompt: How does partial information affect choice? Constraint: Danger is clearly telegraphed

--- Output 5 ---

Grammar: linear (Linear space with forward pressure)

Risk: low | Density: medium

Zones: entry, choke point, terminal space, hidden cave

Constraint: Danger is clearly telegraphed

Design Prompt: How does forward progress increase tension? Constraint: Danger is clearly telegraphed

--- Output 6 ---

Grammar: branch (Hub with short branching paths)

Risk: low | Density: medium

Zones: hub, branch A, branch B, timing gate

Constraint: Mistakes are recoverable

Design Prompt: How does partial information affect choice? Constraint: Mistakes are recoverable

--- Output 7 ---

Grammar: loop (Looping space with repeated traversal)

Risk: low | Density: medium

Zones: central area, loop path, unsafe shortcut

Constraint: Danger is clearly telegraphed

Design Prompt: How does repetition change player behavior? Constraint: Danger is clearly telegraphed

--- Output 8 ---

Grammar: loop (Looping space with repeated traversal)

Risk: low | Density: medium

Zones: central area, loop path, unsafe shortcut

Constraint: Danger is clearly telegraphed

Design Prompt: How does repetition change player behavior? Constraint: Danger is clearly telegraphed

--- Output 9 ---

Grammar: loop (Looping space with repeated traversal)

Risk: low | Density: medium

Zones: central area, loop path, obscured vantage point

Constraint: Danger is clearly telegraphed

Design Prompt: How does repetition change player behavior? Constraint: Danger is clearly telegraphed

--- Output 10 ---

Grammar: linear (Linear space with forward pressure)

Risk: low | Density: medium

Zones: entry, choke point, terminal space, hazard pocket

Constraint: Safe fallback zone exists

Design Prompt: How does forward progress increase tension? Constraint: Safe fallback zone exists

--- Output 11 ---

Grammar: loop (Looping space with repeated traversal)

Risk: low | Density: medium

Zones: central area, loop path, hidden cave

Constraint: Safe fallback zone exists

Design Prompt: How does repetition change player behavior? Constraint: Safe fallback zone exists

--- Output 12 ---

Grammar: branch (Hub with short branching paths)

Risk: low | Density: medium

Zones: hub, branch A, branch B, hazard pocket

Constraint: Danger is clearly telegraphed

Design Prompt: How does partial information affect choice? Constraint: Danger is clearly telegraphed

--- Output 13 ---

Grammar: linear (Linear space with forward pressure)

Risk: low | Density: medium

Zones: entry, choke point, terminal space, timing gate

Constraint: Danger is clearly telegraphed

Design Prompt: How does forward progress increase tension? Constraint: Danger is clearly telegraphed

--- Output 14 ---

Grammar: branch (Hub with short branching paths)

Risk: low | Density: medium

Zones: hub, branch A, branch B, timing gate

Constraint: Danger is clearly telegraphed

Design Prompt: How does partial information affect choice? Constraint: Danger is clearly telegraphed

--- Output 15 ---

Grammar: branch (Hub with short branching paths)

Risk: low | Density: medium

Zones: hub, branch A, branch B, unsafe shortcut

Constraint: Mistakes are recoverable

Design Prompt: How does partial information affect choice? Constraint: Mistakes are recoverable

--- Output 16 ---

Grammar: branch (Hub with short branching paths)

Risk: low | Density: medium

Zones: hub, branch A, branch B, unsafe shortcut

Constraint: Safe fallback zone exists

Design Prompt: How does partial information affect choice? Constraint: Safe fallback zone exists

--- Output 17 ---

Grammar: loop (Looping space with repeated traversal)

Risk: low | Density: medium

Zones: central area, loop path, hidden cave

Constraint: Danger is clearly telegraphed

Design Prompt: How does repetition change player behavior? Constraint: Danger is clearly telegraphed

--- Output 18 ---

Grammar: loop (Looping space with repeated traversal)

Risk: low | Density: medium

Zones: central area, loop path, timing gate

Constraint: Danger is clearly telegraphed

Design Prompt: How does repetition change player behavior? Constraint: Danger is clearly telegraphed

--- Output 19 ---

Grammar: loop (Looping space with repeated traversal)

Risk: low | Density: medium

Zones: central area, loop path, hazard pocket

Constraint: Mistakes are recoverable

Design Prompt: How does repetition change player behavior? Constraint: Mistakes are recoverable

--- Output 20 ---

Grammar: loop (Looping space with repeated traversal)

Risk: low | Density: medium

Zones: central area, loop path, hazard pocket

Constraint: Mistakes are recoverable

Design Prompt: How does repetition change player behavior? Constraint: Mistakes are recoverable


# Known Limitations

The Procedural Sketch Generator intentionally does not support:

Full dungeons or multi-room maps
Narrative or story generation on top of the thought provoking prompt
Genre-specific mechanics such as combat system, certain types of puzzles, etc.
A native visual layout or asset placement (the user has to sketch the room themselves)
