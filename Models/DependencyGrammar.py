
rule_left_arc = {
    ('N','V'):'nsubj',
    ('ADJ','CITY-NAME'):'amod',
    ('P','PRO_TIME'):'at-time',
    ('N','N'):'nmod',
    ('FROM','CITY-NAME'):'from-loc',
    ('TO','CITY-NAME'):'to-loc',
    ('BE','WH-TIME'):'be',
    ('P','WH-TIME'):'time-at',
    ('BE','V'): 'vmod',
}

rule_right_arc = {
    ('N','DET'):'wh-train',
    ('ROOT','V'):'root',
    ('V','N'):'dobj',
    ('V','CITY-NAME'):'dobj',
    ('V','PRO_TIME'):'pobj',
    ('PRO_TIME','AUX_TIME'):'timemod',
    ('V','PUNCH'):'punch',
    ('V','WH-TIME'):'wh-time',
    ('N','TRAIN-NAME'):'train-name',
    ('V','AUX'):'wh-det',
}

rule_shift = {
    ('V','ADJ'):None,
    ('V','P'):None,
    ('V','FROM'):None,
    ('V','TO'):None,
    ('TO','ADJ'):None,
    ('V','BE'):None,
    ('FROM','ADJ'):None,
    ('N','BE'):None,
}

class Relation:
    def __init__(self, relation, head, depend):
        self.relation = relation
        self.head = head
        self.depend = depend
    def __str__(self):
        return (f'{self.relation} ({self.head[0]},{self.depend[0]})')
    def __repr__(self):
        return (f'{self.relation} ({self.head[0]},{self.depend[0]})')

class DependencyGrammar:
    def __init__(self, lstToken):
        self.lstToken = lstToken
        self.stack = [('ROOT','ROOT')]
        self.buffer = lstToken
        self.set_dependency = []

        while self.buffer:
            ele_type1= self.stack[-1][1]
            ele_type2 = self.buffer[0][1]
            if (ele_type1, ele_type2) in rule_left_arc.keys():
                self.__leftArc(rule_left_arc[(ele_type1, ele_type2)])
            elif (ele_type1, ele_type2) in rule_right_arc.keys():
                self.__rightArc(rule_right_arc[(ele_type1, ele_type2)])
            elif len(self.stack) == 1 or (ele_type1, ele_type2) in rule_shift.keys():
                self.__shift()
            else:
                self.__reduce()

    def __leftArc(self, relation):
        head = self.buffer[0]
        depend = self.stack.pop()
        temp = Relation(relation, head, depend)
        self.set_dependency.append(temp)

    def __rightArc(self, relation):
        head = self.stack[-1]
        depend = self.buffer.pop(0)
        self.stack.append(depend)
        temp = Relation(relation, head, depend)
        self.set_dependency.append(temp)

    def __shift(self):
        self.stack.append(self.buffer.pop(0))

    def __reduce(self):
        self.stack.pop()

    def get_dependency(self):
        return self.set_dependency

    def __str__(self):
        return '\n'.join(str(i) for i in self.set_dependency)

    def __repr__(self):
        return self.__str__()
# a = DependencyGrammar([('Tàu hỏa', 'N'), ('B5', 'TRAIN-NAME'), ('có', 'BE'), ('chạy', 'V'), ('từ', 'FROM'), ('Đà Nẵng', 'CITY-NAME'), ('không', 'AUX'), ('?', 'PUNCH')])