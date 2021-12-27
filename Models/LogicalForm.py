map_var = {
    'WH-TRAIN': 't1',
    'WH-ATIME': 'at1',
    'WH-DTIME': 'dt1',
    'WH-RUNTIME': 'rt1',
    'WH-DET':'d1'
}

class LogicalPartern:
    def __init__(self, objname, variable, literal):
        self.objname = objname
        self.variable = variable
        self.value = literal

    def __str__(self):
        if self.value is None:
            return f'({self.objname} {self.variable})'
        else:
            return f'({self.objname} {self.variable} {self.value})'
    
    def __repr__(self):
        if self.value is None:
            return f'({self.objname} {self.variable})'
        else:
            return f'({self.objname} {self.variable} {self.value})'

class LogicalForm:
    def __init__(self, grammar_relation):
        self.grammar_relation = grammar_relation
        self.logical_form_query =[]
        self.logical_form_partern = []

        for grammar in self.grammar_relation:
            if grammar.relation == 'LSUBJ':
                self.logical_form_query.append({
                    'name': grammar.value,
                    'var': map_var[grammar.value]
                })
            elif grammar.relation == 'PRED':
                self.logical_form_partern.append(LogicalPartern(grammar.value.upper(), 'v1', None))
            elif grammar.relation == 'TO-LOC':
                self.logical_form_partern.append(LogicalPartern(grammar.relation, 'v1',grammar.value))
            elif grammar.relation == 'FROM-LOC':
                self.logical_form_partern.append(LogicalPartern(grammar.relation, 'v1',grammar.value))
            elif grammar.relation == 'ARRIVAL-TIME':
                self.logical_form_partern.append(LogicalPartern(grammar.relation, 'v1', grammar.value))
            elif grammar.relation == 'LOBJ':
                self.logical_form_partern.append(LogicalPartern('THEME', 'v1', grammar.value))

    def get_logical_form(self):
        return (self.logical_form_query,self.logical_form_partern)
    
    def __str__(self):
        temp =''
        end =''
        temp2=''
        for i in self.logical_form_query:
            end +=')'
        for query in self.logical_form_query:
            temp += query['name'] + ' ' + query['var']+ ': (' 

        for partern in self.logical_form_partern:
            temp2 += str(partern) +''
        return f'({temp}{temp2}{end})'
    
    def __repr__(self):
        temp =''
        end =''
        temp2=''
        for i in self.logical_form_query:
            end +=')'
        for query in self.logical_form_query:
            temp += query['name'] + ' ' + query['var']+ ': (' 

        for partern in self.logical_form_partern:
            temp2 += str(partern) +''
        return f'({temp}{temp2}{end})'
