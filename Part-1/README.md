# TOPSIS CLI: Multi-Criteria Decision Analysis Tool

This project provides a robust **Python-based command-line interface (CLI)** for executing the **TOPSIS** method. It is designed to assist in Multi-Criteria Decision Making (MCDM) by ranking alternatives based on their proximity to an "ideal" solution.

## Core Functionality
- **Data Ingestion**: Imports alternatives and criteria from CSV files.
- **Normalization**: Standardizes criteria values for comparability.
- **Weighting**: Applies user-defined importance to each criterion.
- **Ideal Solutions**: Calculates the "best" and "worst" possible outcomes.
- **Ranking**: Assigns a performance score and rank to each alternative.

## Requirements
- Python 3.x
- pandas
- numpy

Install dependencies:
`pip install pandas numpy`

## Usage
Run the script using the following command:
```bash
python topsis.py <InputDataFile> <Weights> <Impacts> <ResultFileName>

Example:
python topsis.py data.csv "1,1,1,2,1" "+,+,+,-,+" result.csv
