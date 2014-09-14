import logging, csv, argparse, sys

# Set the log output file, and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

def put(name, snippet, update, filename):
    """ Store a snippet with an associated name in the CSV file """
    logging.info("Writing {}:{} to {}".format(name, snippet, filename))
    logging.debug("Opening file")
    if update:
        logging.debug("Updating snippet to file".format(name, snippet))
        row_store = []
        # Get all rows except for the one we're updating
        with open(filename, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] != name:
                    row_store.append(row)
        # Add the row we're updating
        row_store.append([name, snippet])
        # Erase the file and write all rows back
        with open(filename, "w") as f:
            writer = csv.writer(f)
            for row in row_store:
                writer.writerow(row)
        logging.debug("Update successful")
    else:
        with open(filename, "a") as f:
            writer = csv.writer(f)
            logging.debug("Writing snippet to file".format(name, snippet))
            writer.writerow([name, snippet])
        logging.debug("Write successful")
    return name, snippet, update, filename

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
        print "I couldn't find the snippet for that name."
        logging.debug("Read unsuccessful. No snippet for name provided.")
    else:
        logging.debug("Read successful")
    return name, snippet, filename

def search(string, filename):
    """ Search for a snippet string and return the full string and associated name in the CSV file """
    snippet = None
    name = None
    logging.info("Searching for {} from {}".format(string, filename))
    logging.debug("Opening file")
    with open(filename, "r") as f:
        reader = csv.reader(f)
        logging.debug("Searching for string from file".format(string))
        for row in reader:
            if string in row[1]:
                snippet = row[1]
                name = row[0]
    if snippet is None:
        print "I couldn't find the snippet for that string."
        logging.debug("Search unsuccessful. No snippet for search string provided.")
    else:
        logging.debug("Search successful")
    return name, string, snippet, filename

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
    put_parser.add_argument("-u", "--update", action='store_true', default=False,
                    dest='update', help="Update an existing entry instead of create a new one")

    # Subparser for the get command
    logging.debug("Constructing get subparser")
    get_parser = subparsers.add_parser("get", help="Retrieve a snippet")
    get_parser.add_argument("name", help="The name of the snippet to get")
    get_parser.add_argument("filename", default="snippets.csv", nargs="?", help="The snippet filename to get from")

    # Subparser for the search command
    logging.debug("Constructing search subparser")
    search_parser = subparsers.add_parser("search", help="Search for a snippet from a given string")
    search_parser.add_argument("string", help="The name of the snippet to get")
    search_parser.add_argument("filename", default="snippets.csv", nargs="?", help="The snippet filename to search")

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
        name, snippet, update, filename = put(**arguments)
        if update:
            print "Updated '{}' as '{}' into {}".format(snippet, name, filename)
        else:
            print "Stored '{}' as '{}' into {}".format(snippet, name, filename)
    elif command == "get":
        name, snippet, filename = get(**arguments)
        print "Retrieved '{}' from {}, which is '{}'".format(name, filename, snippet)
    elif command == "search":
        name, string, snippet, filename = search(**arguments)
        print "Found '{}' in '{}', with name '{}' in file {}".format(string, snippet, name, filename)

if __name__ == "__main__":
    main()