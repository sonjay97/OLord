import sys
import fileinput


class OLord():
    """Class for OLord Scanner"""

    def main(self, args):
        """Main function for OLord Scanner"""

        try:
            if len(args) > 1:
                print("Usage: OLord [script]")
                exit
            elif len(args) == 1:
                self.runFile(args[0])
            else:
                self.runPrompt()
        except IOError as e:
            print(f"IO Error, please enter valid input: {e}")
            exit

    def runFile(path: str):
        """Run files from command line"""
        try:
            with open(path, 'r', encoding='utf-8') as file:
                source = file.read()
            run(source)
        except IOError as e:
            print(f"Error reading file '{path}': {e}")
            sys.exit(1)

    def runPrompt():
        "REPL prompt for OLord"
        try:
             while True:
                line = input("> ") # Read input
                if not line.strip():
                    continue
                run(line)
        except KeyboardInterrupt as e:
            print(f"\nExiting: {e}")
            sys.exit(0)
        except EOFError as e:
            print(f"\nExiting: {e}")
            sys.exit(0)

    def run(source: str):
        
