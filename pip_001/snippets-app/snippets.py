import logging, csv, argparse, sys

# Set the log output file, and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

def put(name, snippet, filename):
    """ Store a snippet with an associated name in the CSV file """
    logging.info("Writing {}:{} to {}".format(name, snippet, filename))
    logging.debug("Opening file")
    with open(filename, "a") as f:
        writer = csv.writer(f)
        logging.debug("Writing snippet to file".format(name, snippet))
        writer.writerow([name, snippet])
    logging.debug("Write successful")
    return name, snippet, filename

def get(name, filename):
    """ Retrieve a snippet using an associated name in the CSV file """
    snippet = None
    logging.info("Retrieving {} from {}".format(name, filename))
    logging.debug("Opening file")
    with open(filename, "r") as f:
        reader = csv.reader(f)
        logging.debug("Retrieving snippet from file".format(name))
        for row in reader:
            if row[0] == name:
                snippet = row[1]
    if snippet is None:
        print "I couldn't find the snippet for that name"
        logging.debug("Read unsuccessful. No snippet for name provided.")
    else:
        logging.debug("Read successful")
    return name, snippet, filename

def make_parser():
    """ Construct the command line parser """
    logging.info("Constructing parser")
    description = "Store and retrieve snippets of text"
    parser = argparse.ArgumentParser(description=description)

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="The name of the snippet to put")
    put_parser.add_argument("snippet", help="The snippet text to put")
    put_parser.add_argument("filename", default="snippets.csv", nargs="?", help="The snippet filename to put into")

    # Subparser for the get command
    logging.debug("Constructing get subparser")
    get_parser = subparsers.add_parser("get", help="Retrieve a snippet")
    get_parser.add_argument("name", help="The name of the snippet to get")
    get_parser.add_argument("filename", default="snippets.csv", nargs="?", help="The snippet filename to get from")

    return parser

def main():
    """ Main function """
    logging.info("Starting snippets")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "put":
        name, snippet, filename = put(**arguments)
        print "Stored '{}' as '{}' into {}".format(snippet, name, filename)
    elif command == "get":
        name, snippet, filename = get(**arguments)
        print "Retrieved '{}' from {}, which is '{}'".format(name, filename, snippet)

if __name__ == "__main__":
    main()