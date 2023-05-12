# Status-code
This script uses the argparse module to create a command-line interface for testing a list of URLs and printing the HTTP status code for each URL. The script takes an input file containing the URLs to test and an optional output file to save the results to. It also provides a help message that can be accessed with the 
"-help" or "--show_help" option.

The script reads the input file, tests each URL using the requests module, and prints the results to the console. If an output file is specified, the results are also saved to the file. If the URL test encounters an error, the script catches the exception and includes the error message in the results.
