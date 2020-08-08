class Counter:
    def __init__(self, results_loc):
        self.loc = results_loc
    # this will get the last line
    def last_line(self):
        with open(self.loc, 'r') as f:
            lines = f.read().splitlines()
            self.last_line = lines[-1]

    # Extracting first word from the line
    def extract_first_word(self):
        last_line = self.last_line
        self.first_word = last_line.split()[0]
    def delete_first_word(self):
        fst_word = self.first_word
        del_first_word = self.last_line.strip(fst_word+" ")
        final_recent_conv = del_first_word
        self.final_recent_conv =  final_recent_conv
    def result(self):
        return self.final_recent_conv
def run(results_loc):
    count = Counter(results_loc)
    count.last_line()
    count.extract_first_word()
    return count.result()
