# Pokemon API Data Engineering Project

## Introduction
This project is a data engineering pipeline built using Python to extract, transform, and organize data from the [PokéAPI](https://pokeapi.co/). It focuses on retrieving and structuring data about Pokémon, their species, and abilities, storing it in a clean and relational format suitable for further analysis or integration into downstream systems.

The main goal is to demonstrate how to:
 - Build and manage data pipelines using real-world APIs.
 - Clean, transform, and merge multiple datasets.
 - Apply efficient data structuring practices for analytics and visualization.

 ## Objective
 - Collect and store data from multiple API endpoints:
    - /pokemon → core Pokémon attributes (stats, types, height, weight, etc.)
    - /pokemon-species → species-related info (color, habitat, generation, etc.)
    - /ability → ability details including effects and descriptions
- Process and join datasets to create structured DataFrames.
- Handle missing or multilingual data (e.g., English-only effect text for abilities).
- Build a base dataset ready for analytical or ML use.

## Tools and Technology Used
| Category                   | Tools / Libraries                                                        |
| -------------------------- | ------------------------------------------------------------------------ |
| **Language**               | Python 3.x                                                               |
| **IDE**                    | Visual Studio Code                                                       |
| **API Source**             | [PokéAPI](https://pokeapi.co/)                                           |
| **Core Libraries**         | `requests`, `pandas`, `json`                                             |
| **Version Control**        | Git + GitHub                                                             |