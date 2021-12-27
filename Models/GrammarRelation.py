class Pattern:
    def __init__(self, var, relation, value):
        self.var = var
        self.relation = relation
        self.value = value

    def __str__(self):
        return f'({self.var} {self.relation} {self.value})'
    
    def __repr__(self):
        return f'({self.var} {self.relation} {self.value})'

class Literal:
    def __init__(self, type, var, value):
        self.type = type
        self.var = var
        self.value = value
    
    def __str__(self):
        return f'({self.type} {self.var} {self.value})'
    
    def __repr__(self):
        return f'({self.type} {self.var} {self.value})'

class GrammarRelation:
    def __init__(self,dependency_grammar):
        self.dependency_grammar = dependency_grammar
        self.grammar_relation_set=[]
        for grammar in self.dependency_grammar:
            if grammar.relation == 'root':
                self.grammar_relation_set.append(Pattern('s1','PRED',grammar.depend[0]))
        
        for grammar in self.dependency_grammar:
            if grammar.relation == 'wh-train':
                self.grammar_relation_set.append(Pattern('s1','LSUBJ', 'WH-TRAIN'))
            
            elif grammar.relation == 'wh-time':
                if 'from-loc' in [x.relation for x in self.dependency_grammar] and 'to-loc' in [x.relation for x in self.dependency_grammar]:
                    self.grammar_relation_set.append(Pattern('s1','LSUBJ', 'WH-RUNTIME'))
                elif 'from-loc' in [x.relation for x in self.dependency_grammar]:
                    self.grammar_relation_set.append(Pattern('s1','LSUBJ', 'WH-DTIME'))
                elif 'to-loc' in [x.relation for x in self.dependency_grammar]:
                    self.grammar_relation_set.append(Pattern('s1','LSUBJ', 'WH-ATIME'))
            
            elif grammar.relation == 'wh-det':
                self.grammar_relation_set.append(Pattern('s1', 'LSUBJ', 'WH-DET'))
            
            elif grammar.relation == 'train-name':
                train = Literal('TRAIN-NAME', 't1', grammar.depend[0])
                self.grammar_relation_set.append(Pattern('s1','LOBJ', train))

            elif grammar.relation == 'dobj':
                if grammar.head[0] == 'đến':
                    loc = Literal('CITY-NAME', 'c2', grammar.depend[0])
                    self.grammar_relation_set.append(Pattern('s1','TO-LOC',loc))

            elif grammar.relation == 'pobj':
                if grammar.head[0] == 'đến':
                    time = Literal('TIMEMOD', 'a1', grammar.depend[0])
                    self.grammar_relation_set.append(Pattern('s1','ARRIVAL-TIME',time))
            
            elif grammar.relation == 'from-loc':
                loc = Literal('CITY-NAME', 'c1', grammar.head[0])
                self.grammar_relation_set.append(Pattern('s1','FROM-LOC',loc))
            
            elif grammar.relation == 'to-loc':
                loc = Literal('CITY-NAME', 'c2', grammar.head[0])
                self.grammar_relation_set.append(Pattern('s1','TO-LOC',loc))
        
    def get_grammar_relation(self):
        return self.grammar_relation_set

    def __str__(self):
        return ' '.join(str(i) for i in self.grammar_relation_set) 
    
    def __repr__(self):
        return self.__str__()
                



