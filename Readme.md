# India Historical Events Analyzer

A command-line tool for analyzing historical events in India from 1970-1999. The tool allows filtering and analysis of events based on various criteria such as year properties (prime numbers, divisibility), event categories, impact scores, and international significance.

## Project Structure
```
india_events_analyzer/
├── data/
│   └── india_events.csv
├── src/
│   └── event_analyzer/
│       ├── __init__.py
│       ├── utils.py
│       ├── data_handler.py
│       └── india_events_analyzer.py
├── tests/
│   ├── __init__.py
│   └── test_india_events.py
├── logs/
│   └── test_execution.log
└── README.md
```

## Features

- Read and parse CSV data of historical events
- Filter events by:
  - Prime numbered years
  - Years divisible by a specific number
  - Event category
  - Impact score
  - International significance
- Detailed or concise output formats
- Comprehensive logging of operations
- Unit tests with detailed test coverage

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd india_events_analyzer
```

2. Ensure you have Python 3.9 or higher installed:
```bash
python --version
```

3. Set up your data file in the `data/` directory:
- Create a CSV file named `india_events.csv`
- Format: Year,Event,Category,Impact_Score,International_Significance
- Example:
  ```csv
  Year,Event,Category,Impact_Score,International_Significance
  1971,Indo-Pakistani War,Military,10,True
  1975,Emergency Declaration,Political,9,True
  ```

## Usage

### Basic Commands

Show all events:
```bash
python src/event_analyzer/india_events_analyzer.py data/india_events.csv
```

Show help and available options:
```bash
python src/event_analyzer/india_events_analyzer.py --help
```

### Filtering Options

1. **Prime Year Events**
```bash
python src/event_analyzer/india_events_analyzer.py data/india_events.csv -p
```

2. **Events in Years Divisible by N**
```bash
python src/event_analyzer/india_events_analyzer.py data/india_events.csv -a 5
```

3. **Filter by Category**
```bash
python src/event_analyzer/india_events_analyzer.py data/india_events.csv -c Military
```

4. **Filter by Minimum Impact Score**
```bash
python src/event_analyzer/india_events_analyzer.py data/india_events.csv -m 8
```

5. **Show Only International Events**
```bash
python src/event_analyzer/india_events_analyzer.py data/india_events.csv -i
```

6. **Verbose Output**
```bash
python src/event_analyzer/india_events_analyzer.py data/india_events.csv -v
```

### Combining Filters

You can combine multiple filters:
```bash
python src/event_analyzer/india_events_analyzer.py data/india_events.csv -c Military -m 8 -i -v
```

## Running Tests

Run all tests:
```bash
python -m unittest tests/test_india_events.py
```

Run tests with verbose output:
```bash
python -m unittest tests/test_india_events.py -v
```

Run specific test:
```bash
python -m unittest tests.test_india_events.TestIndiaEventsAnalyzer.test_is_prime
```

## Logs

Test execution logs are stored in the `logs/` directory with timestamps:
```bash
logs/test_execution_YYYYMMDD_HHMMSS.log
```

## Data Format

The CSV file should contain the following columns:
- Year: Integer (1970-1999)
- Event: String (Description of the event)
- Category: String (e.g., Military, Political, Economic)
- Impact_Score: Integer (1-10)
- International_Significance: Boolean (True/False)

Example:
```csv
Year,Event,Category,Impact_Score,International_Significance
1971,Indo-Pakistani War,Military,10,True
1975,Emergency Declaration,Political,9,True
1983,World Cup Victory,Sports,8,True
```

## Project Components

- `utils.py`: Mathematical utility functions
- `data_handler.py`: Data processing and filtering functions
- `india_events_analyzer.py`: Main script with CLI interface
- `test_india_events.py`: Comprehensive test suite

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request


## Author

Saurabh Srivastava

srivastava.sau@northeastern.edu

## Acknowledgments

- Software Velocity Corp for the project requirements
