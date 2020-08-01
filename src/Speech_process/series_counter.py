import results_checker as rc
import filepath as f_p
#This will extract the first word from a line
class Counter:
    def __init__(self, check, loc):
        self.check = check
        self.loc = loc
    
    # this will get the last line
    def last_line(self):
        with open(self.loc, 'r') as f:
            lines = f.read().splitlines()
            self.last_line = lines[-1]

    # Extracting first word from the line
    def extract_first_word(self):
        fst_word = self.last_line
        self.first_word = fst_word.split()[0]

    # removing last character or dot from the word, i.e string = "1." ---> string = "1"
    def dotremover(self):
        ord = self.first_word
        self.word = ord
        self.word = self.word[:-1]

    # add one to the last count
    def add_one(self):
        int_word = self.word
        int_word = int(int_word)
        self.added_word = (int_word + 1)

    # Add dot to the current count i.e 2 ---> "2.""
    def dotadder(self):
        str_word = str(self.added_word)
        self.final_word = str_word + "."

    # return the final word
    def count(self):
        final = self.final_word
        if not self.check:
            count = final
            return count
        else:
            count = "1. "
            return count

# this run all the functions in the class Counter
def runall(check,results_loc):
    counter = Counter(check, results_loc)
    counter.last_line()
    counter.extract_first_word()
    counter.dotremover()
    counter.add_one()
    counter.dotadder()
    counter = counter.count()
    return counter

# finally run the script
def run():
    check = rc.run()
    results_loc = f_p.run("results")
    run = runall(check, results_loc)
    return run




