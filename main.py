from Models.VietnameseNLP import VietnameseNLP
from Models.Database import Database
import optparse
import sys

def readInput(path):
    f = open(path, 'r', encoding="utf8")
    input = f.readline()
    f.close()
    return input

def writeOutput(path, content):
    f = open(path, 'w', encoding="utf8")
    f.write(content)
    f.close()

def parse_args(args):
    parser = optparse.OptionParser(description='Run QA Train System')
    parser.add_option('--input-directory',
                      dest='inputRoot',
                      default='Input',
                      help='Root input directory which contains query')
    parser.add_option('--input-file',
                      dest='inputFile',
                      default='input_1.txt',
                      help='Root input directory which contains query')
    options, _ = parser.parse_args(args)
    return options
if __name__=='__main__':
    options = parse_args(sys.argv)
    input = readInput(f'{options.inputRoot}/{options.inputFile}')
    db = Database('Input/db.txt')
    model = VietnameseNLP('Models/lexicon.txt')
    
    token,lstDependency = model.dependency_grammar(input)
    writeOutput('Output/output_a.txt', token)
    print(f'>>> Tokenization:\n{token}')
    writeOutput('Output/output_b.txt', str(lstDependency))
    print(f'\n>>> Dependence Grammar:\n{lstDependency}')
    
    lstGrammarRelation = model.grammar_relations(lstDependency)
    writeOutput('Output/output_c.txt', str(lstGrammarRelation))
    print(f'\n>>> Grammar Relation:\n{lstGrammarRelation}')

    logical_form = model.logical_form(lstGrammarRelation)
    writeOutput('Output/output_d.txt', str(logical_form))
    print(f'\n>>> Logical Form:\n{logical_form}')

    procedure_semantic = model.procedure_semantic(logical_form)
    writeOutput('Output/output_e.txt', str(procedure_semantic))
    print(f'\n>>> Procedure Semantic:\n{procedure_semantic}')

    retrieval = model.retrieval(procedure_semantic, db)
    writeOutput('Output/output_f.txt', str(retrieval))
    print(f'\n>>> Query Output:\n{retrieval}')
    
    

    

