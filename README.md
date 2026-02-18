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
With the default settings, the tool will generate a batch of room prompts and print them to the terminal.

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



# Known Limitations

The Procedural Sketch Generator intentionally does not support:

Full dungeons or multi-room maps
Narrative or story generation on top of the thought provoking prompt
Genre-specific mechanics such as combat system, certain types of puzzles, etc.
A native visual layout or asset placement (the user has to sketch the room themselves)
