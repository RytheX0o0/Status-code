# Status-code

Status Code Checker

This tool is designed to test a list of URLs and print the HTTP status code for each URL. It's a simple and easy-to-use command-line interface that's perfect for website developers, administrators, and anyone who wants to ensure that their website is running smoothly.
Prerequisites

To use this tool, you'll need Python 3 and the requests module installed on your machine. You can install the requests module using pip:

pip install requests

Getting Started

To get started with this tool, follow these simple steps:

Clone this repository to your local machine.
Open a command prompt or terminal window.
Navigate to the directory where you cloned the repository.
Type the following command to see the available options:


python3 status.py -help

Type the following command to test a list of URLs:

python3 status.py input_file.txt

Replace "input_file.txt" with the name of your input file that contains a list of URLs you want to test. By default, the tool will test the first 200 URLs in the input file.

If you want to save the results to a file, use the "-o" or "--output" option followed by the name of your output file:

python status.py input_file.txt -o output_file.txt

If you encounter any issues or errors, please let us know by opening an issue on this repository.
