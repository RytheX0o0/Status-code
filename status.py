import argparse
import requests
import termcolor

# Initialize the argument parser
parser = argparse.ArgumentParser(description="Test a list of URLs and print the HTTP status code for each URL.")

# Add the input file argument
parser.add_argument("input_file", help="the file containing the URLs to test")

# Add the output file argument
parser.add_argument("-o", "--output", help="the file to save the results to")

# Add the help option
parser.add_argument("-help", "--show_help", action="store_true", help="show this help message and exit")

# Parse the command-line arguments
args = parser.parse_args()

# Show the help message and exit, if specified
if args.show_help:
    parser.print_help()
    exit()

# Open the file containing the URLs
with open(args.input_file, "r") as f:
    # Read the URLs into a list
    url_list = f.read().splitlines()

# Test each URL and print the HTTP status code
results = []
for url in url_list[:200]:
    try:
        response = requests.get(url)
        result = "[" + termcolor.colored("+", "green") + "] URL: {} | Status Code: {}".format(url, response.status_code)
        results.append(result)
    except requests.exceptions.RequestException as e:
        result = "[" + termcolor.colored("-", "red") + "] URL: {} | Error: {}".format(url, e)
        results.append(result)

# Print the results to the console
for result in results:
    print(result)

# Save the results to a file, if specified
if args.output:
    with open(args.output, "w") as f:
        f.write("\n".join(results))
