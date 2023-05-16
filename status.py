import argparse
import termcolor
import requests

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
results_200 = ["Status code 200"]
results_500 = ["\nStatus code 500"]
errorlist = ["\nErrors found"]
print("\n---------------Checking link status----------------")

for url in url_list[:10]:
    try:
        response = requests.get(url)
        if (response.status_code == 200):
            result = "[" + termcolor.colored("+", "green") + "] URL: {} | Status Code: {}".format(url, response.status_code)
            # result = "URL: {} | Status Code {}".format(url, response.status_code)
            print(result)
            results_200.append(url)
        if (response.status_code == 500):
            result = "[" + termcolor.colored("+", "green") + "] URL: {} | Status Code: {}".format(url, response.status_code)
            # result = "URL: {} | Status Code {}".format(url, response.status_code)
            print(result)
            results_500.append(url)
    except requests.exceptions.RequestException as e:
        result = "[" + termcolor.colored("-", "red") + "] URL: {} | Error: {}".format(url, e)
        # result = "URL: {} | Error: {}".format(url, e)
        print(result)
        error = "{} | Error: {}".format(url, e) 
        errorlist.append(error)
print("\n---------------Analysis Complete----------------")
print("\n")
print("---------------Displaying results---------------\n")


# # Print the results to the console
print("\n-------------------Status 200-------------------")
if len(results_200) > 1:
    for result in results_200[1: ]:
        print(result)
else:
    print("0 links found")


print("\n-------------------Status 500-------------------")
if len(results_500) > 1:
    for result in results_500[1: ]:
        print(result)
else:
    print("0 links found")

print("\n-------------------Erros found-------------------")
if len(errorlist) > 1:
    for result in errorlist[1: ]:
        print(result)
else:
    print("0 errors found")

final_result = results_200 + results_500 + errorlist

# Save the results to a file, if specified
if args.output:
    with open(args.output, "w") as f:
        f.write("\n".join(final_result))
