import json

class Wom:
    def __init__(self, filepath):
        self.json_data = json.load(open(filepath))
        self.useranswers = []
        self.raw_results = {}
        self.similarity_results = {}
        self.max_disparity = len(self.json_data['questions']) * 2
        for party in self.json_data['answers']:
            self.raw_results.update({party : 0})
            self.similarity_results.update({party : 0.0})

    def get_answers (self):
        allowed_chars = ['J', 'N', '-']
        for question in self.json_data['questions']:
            print(question)
            inpt = 'X'
            while inpt not in allowed_chars:
                inpt = input("[J / N / -]: ")
            self.useranswers.append(inpt)

    def calculate (self):
        # for each party, calculate the overall distance between the user's and
        # the party's answers. lowest distance wins!
        for party in self.raw_results:
            answers = self.json_data['answers'][party]
            for i in range(len(answers)):
                if answers[i] == self.useranswers[i]:
                    pass
                elif answers[i] == '-':
                    self.raw_results[party] += 1
                elif self.useranswers[i] == '-':
                    self.raw_results[party] += 1
                else:
                    self.raw_results[party] += 2

            self.similarity_results[party] = ((self.max_disparity -
                self.raw_results[party]) / self.max_disparity) * 100

    def print_results (self):
        for party in sorted(self.similarity_results,
            key=self.similarity_results.get, reverse=True):
            print("{}: {:.2f}%".format(party, self.similarity_results[party]))

if __name__ == "__main__":
    wom = Wom("wom_ltw_by_2018.json")
    wom.get_answers()
    wom.calculate()
    wom.print_results()
