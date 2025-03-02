import json
import sys
import os


def main():
#
    # Validate if we have any arguments
    #
    if len(sys.argv) < 2:
        #
        # No template on comand line, quit
        #
        print(f"Usage: {sys.argv[0]} file(s)")
        sys.exit(1)
    
    for x in range(1,len(sys.argv)):
        print(f"printing {sys.argv[x]}")
        
        with open(sys.argv[x], 'r') as handle:
            parsed = json.load(handle)
            print(json.dumps(parsed, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
    
