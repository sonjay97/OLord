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
        try:
            
        except IOError as e:
            print(f"IO Error, please enter valid input: {e}")

    def runPrompt():
        pass