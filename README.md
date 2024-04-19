
# PDF Table Parser

PDF Table Parser is a Python tool for extracting tables from PDF documents and converting them into CSV files.


## Installation

### Prerequisites

• If Python 3.x is not installed on your system ([Python](https://www.python.org/downloads/))

• Virtual environment set up (optional but recommended)

### Creating Virtual Environment

#### On Linux

Open a terminal.
Navigate to your project directory.
Run the following command to create a virtual environment named venv:

```bash
python3 -m venv venv
```

#### On Windows

Open Command Prompt.
Navigate to your project directory.
Run the following command to create a virtual environment named venv:

```bash
python -m venv venv
```

### Activating Virtual Environment

#### On Linux

Open a terminal.
Navigate to your project directory.
Run the following command to activate the virtual environment:

```bash
source venv/bin/activate
```

#### On Windows

Open power shell.
Navigate to your project directory.
Run the following command to activate the virtual environment:

```bash
venv\Scripts\activate.ps1
```

### Deactivating Virtual Environment

To deactivate the virtual environment, simply run the following command in your terminal or Power Shell:

```bash
deactivate
```


### Installing Dependencies

Before running the PDF Table Parser, make sure to install the required dependencies listed in requirements.txt.

```bash
pip install -r requirements.txt
```

This will install the following packages:

• [camelot-py](https://pypi.org/project/camelot-py/): A Python library to extract tables from PDFs into pandas DataFrames.

• [ghostscript](https://pypi.org/project/ghostscript/): A Python interface to the Ghostscript C-API.

• [opencv-python](https://pypi.org/project/opencv-python/): A Python binding for OpenCV, a computer vision library.

## Usage/Examples

### Executing the PDF Table Parser

To run the PDF Table Parser, follow these steps:

- Navigate to the src directory.
```bash
cd src
```

- Run the main.py script.

```bash
python main.py
```
This will generate a CSV file from the PDF files located in the test_files directory. Make sure to adjust the filename in the main.py file as needed.





## Running Tests

To run all tests, run the following command

```bash
python -m unittest discover -s tests
```


## File Structure

```
pdf-table-parser/
├── src/
│   ├── main.py
│   ├── csv_writer.py
│   ├── pdf_parser.py
│   ├── utils.py
│
├── test_files/
│   ├── pdf1.pdf
│   ├── pdf2.pdf
│   ├── pdf3.pdf
│   ├── pdf4.pdf
│
├── tests/
│   ├── test_csv_writer.py
│   ├── test_pdf_parser.py
│  
├── readme.md
├── requirements.txt
├── .gitignore

```
