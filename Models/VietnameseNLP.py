from .DependencyGrammar import DependencyGrammar
from .GrammarRelation import GrammarRelation
from .LogicalForm import LogicalForm
from .ProcedureSemantic import ProcedureSemantic
from .Retrieval import Retrieval

class Token:
    def __init__(self, name, typ):
        self.name = name
        self.typ = typ
    def __str__(self):
        return f'({self.name}, {self.typ})'
    def __repr__(self):
        return f'({self.name}, {self.typ})'

class VietnameseNLP:
    def __init__(self, lexicon_file):
        self.lstToken = self.__extract_lexicon(lexicon_file)

    def __extract_lexicon(self, lexicon_file):
        lstToken = {} 
        f = open(lexicon_file, 'r', encoding="utf8")
        lines = f.readlines()
        
        for line in lines:
            parts = line.split(';')
            name = parts[0]
            typ = parts[1]
            lstToken[name]=typ
        f.close()
        return lstToken
    
    def handle_compound_tokenization(self, input):
        lstTokenName = self.lstToken.keys()
        result= []
        #define limit compound_word length
        compound_word=""
        limit = 5
        for token in input:
            if compound_word=="":
                compound_word=token
            else:
                compound_word+= " "+token
            limit-=1
      
            if compound_word in lstTokenName:
                result.append(compound_word)
                compound_word=""
                limit = 5
            elif limit<0 or token==input[-1]:
                print(f"Warning: may be hasn't '{compound_word}' in corpus, pls add lexicon or review input again")
                result.append(compound_word)
                compound_word=""
                limit = 5
        return result

    #mysterious function 
    def handle_special(self, lst_token_sentence):
        flag = False
        i=0
        for token in lst_token_sentence:
            if token[0]!='đến' and token[1]=='V':
                flag=True
            elif token[0]=='đến' and flag:
                lst_token_sentence[i]=('đến','TO')
            i+=1
        return lst_token_sentence

    def dependency_grammar(self, questionStr):
        # f = open(filename, 'r', encoding="utf8")
        # input = self.__extract_query(f.readline())
        #Create list of token
        questionStr=questionStr.replace(',','')
        input = questionStr.split(' ')
        #Handle compound phrase
        list_word = self.handle_compound_tokenization(input)
        lst_token_sentence = [(word,self.lstToken[word]) for word in list_word if word in self.lstToken.keys()]
        #1chutmadao
        lst_token_sentence = self.handle_special(lst_token_sentence)
        print_token = ' '.join(['('+str(i[0])+','+str(i[1])+')' for i in lst_token_sentence])
        dependency_grammar = DependencyGrammar(lst_token_sentence)
        return print_token,dependency_grammar

    def grammar_relations(self, dependency_grammar):
        grammar_relation = GrammarRelation(dependency_grammar.get_dependency())
        return grammar_relation
        
    def logical_form(self, grammar_relation):
        logical_form = LogicalForm(grammar_relation.get_grammar_relation())
        return logical_form

    def procedure_semantic(self, logical_form):
        procedure_semantic = ProcedureSemantic(logical_form)
        return procedure_semantic
    
    def retrieval(self, procedure_semantic, db):
        retrieval = Retrieval(procedure_semantic, db)
        return retrieval
