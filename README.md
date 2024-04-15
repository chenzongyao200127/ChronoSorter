# Exam Time Sorting Script

## Overview

This Python script is designed to read exam date information from a text file, parse the dates in various formats, and then sort the exams by date and time. The sorted exam data is then written back to a file. This utility is particularly useful for organizing exam schedules that are listed in non-standard or mixed date formats.

## Features

- **Date Parsing**: Supports a wide range of date formats including YYYY-MM-DD, DD/MM/YYYY, and formats with time stamps.
- **Sorting**: Exams are sorted chronologically based on their start times.
- **Flexibility**: The script can handle different year assumptions for dates that only include month and day.

## Requirements

- Python 3.6 or higher
- `python-dateutil` package

To install the required package, run:
```bash
pip install python-dateutil
```

## Files

- **script.py**: Contains the main script to parse, sort, and write the exam data.
- **ori_exam_data.txt**: Example input file containing unsorted exam dates.
- **exam_data.txt**: Output file with sorted exam dates.

## Usage

1. Ensure that the source file (`ori_exam_data.txt`) is in the same directory as the script, or provide the path to the source file.
2. Run the script using the following command:
   ```bash
   python script.py
   ```
3. Check the output in the `exam_data.txt` file.

## Functions

### `parse_exam_data(line, default_year=datetime.now().year)`

Parses a line of text to extract the date and time of the exam.

**Parameters:**
- `line`: A string containing a line from the input file.
- `default_year`: The default year to assume for dates that do not include a year.

**Returns:**
- A tuple containing the parsed `datetime` object and the revised line with the formatted date prepended.

### `read_and_sort_exams(filename)`

Reads the exam data from a file, parses it, and sorts it by date.

**Parameters:**
- `filename`: The name of the file to read from.

**Returns:**
- A list of strings, each containing a sorted line from the input file.

### `write_sorted_exams(filename, sorted_exams)`

Writes the sorted exam data back to a file.

**Parameters:**
- `filename`: The output file name.
- `sorted_exams`: A list of sorted exam strings to be written to the file.

## Example

Given a file named `ori_exam_data.txt` with the following contents:

```
2023-04-15 09:00 Exam A
15/04/2023 Exam B
April 13, 2023, 14:00 Exam C
```

After running the script, the `exam_data.txt` will contain:

```
2023-04-13 14:00:00 April 13, 2023, 14:00 Exam C
2023-04-15 09:00:00 2023-04-15 09:00 Exam A
2023-04-15 00:00:00 15/04/2023 Exam B
```

## Note

This script assumes that the input dates are valid and in a recognizable format based on the defined patterns. In case of unrecognized formats, the original line is returned with no date sorting applied.