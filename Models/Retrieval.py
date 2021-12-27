class Retrieval:
    def __init__(self, procedure, db):
        self.train = [train.split()[1] for train in db.trains]
        self.dtime = [train.split()[1:] for train in db.dtimes]
        self.atime = [train.split()[1:] for train in db.atimes]
        self.runtime =  [train.split()[1:] for train in db.runtimes]
        self.retrieval =[]
        for var in procedure.request['var']:
            if var == '?t':
                self.retrieval.append(self.find_train(procedure))
            elif var == '?rt':
                self.retrieval.append(self.find_runtime(procedure))
            elif var == '?dt':
                self.retrieval.append(self.find_dtime(procedure))
            elif var == 'yn':
                self.retrieval.append(['Có'] if self.find_train(procedure) else ['Không'])


    def find_train(self,procedure):
        if procedure.var_train == '?t':
            result = self.train
        else:
            result = procedure.var_train
        if procedure.var_depart != '?d':
            retrieval = [d[0] for d in self.dtime if d[1]== procedure.var_depart ]
            result = list(set(result).intersection(set(retrieval)))
        if procedure.var_depart_time != '?dt':
            retrieval = [d[0] for d in self.dtime if d[2]== procedure.var_depart_time ]
            result = list(set(result).intersection(set(retrieval)))
        if procedure.var_arrival != '?a':
            retrieval = [a[0] for a in self.atime if a[1]== procedure.var_arrival ]
            result = list(set(result).intersection(set(retrieval)))
        if procedure.var_arrival_time != '?at':
            retrieval = [a[0] for a in self.atime if a[2]== procedure.var_arrival_time ]
            result = list(set(result).intersection(set(retrieval)))
        if procedure.var_run_time != '?rt':
            retrieval = [r[0] for r in self.runtime if r[3]== procedure.var_run_time ]
            result = list(set(result).intersection(set(retrieval)))
        return result
    
    def find_runtime(self, procedure):
        result = [d[3] for d in self.runtime]
        if procedure.var_depart != '?d':
            retrieval = [d[3] for d in self.runtime if d[1]== procedure.var_depart]
            result = list(set(result).intersection(set(retrieval)))
        if procedure.var_train != '?t':
            retrieval = [d[3] for d in self.runtime if d[0]== procedure.var_train ]
            result = list(set(result).intersection(set(retrieval)))
        if procedure.var_arrival != '?a':
            retrieval = [d[3] for d in self.runtime if d[2]== procedure.var_arrival ]
            result = list(set(result).intersection(set(retrieval)))
        return result
    
    def find_dtime(self, procedure):
        result = [d[2] for d in self.dtime]
        if procedure.var_depart != '?d':
            retrieval = [d[2] for d in self.dtime if d[1]== procedure.var_depart]
            result = list(set(result).intersection(set(retrieval)))
        if procedure.var_train != '?t':
            retrieval = [d[2] for d in self.dtime if d[0]== procedure.var_train ]
            result = list(set(result).intersection(set(retrieval)))
        return result

    def __str__(self):
        temp = ''
        for res in self.retrieval:
            if len(res)>0:
                temp += ' '.join([i for i in res])
            else:
                temp += 'Không tìm thấy kết quả'
            temp += '\n'
        return f'{temp}'