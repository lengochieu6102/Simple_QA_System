map_city = {
    'Huế':'HUE',
    'Hồ Chí Minh': 'HCMC',
    'Đà Nẵng':'DANANG',
    'Nha Trang': 'NTrang',
    'Hà Nội': 'HN'
}

class ProcedureSemantic:
    def __init__(self, logical_form):
        logical_form_query = logical_form.logical_form_query
        logical_form_partern = logical_form.logical_form_partern
        self.request = {
            'name':'',
            'var':[]
        }
        self.var_train = '?t'
        self.var_depart = '?d'
        self.var_depart_time = '?dt'
        self.var_arrival = '?a'
        self.var_arrival_time = '?at'
        self.var_run_time = '?rt'

        for wh in logical_form_query:
            if wh['name']=='WH-TRAIN':
                self.request['name'] = 'PRINT-ALL'
                self.request['var'].append('?t')
            elif wh['name']=='WH-ATIME':
                self.request['name'] = 'PRINT-ALL'
                self.request['var'].append('?at')
            elif wh['name']=='WH-DTIME':
                self.request['name'] = 'PRINT-ALL'
                self.request['var'].append('?dt')
            elif wh['name']=='WH-RUNTIME':
                self.request['name'] = 'PRINT-ALL'
                self.request['var'].append('?rt')
            elif wh['name']=='WH-DET':
                self.request['name'] = 'CHECK-ALL-TRUE'
                self.request['var'].append('yn')
            
        for pat in logical_form_partern:
            if pat.objname=='TO-LOC':
                self.var_arrival = map_city[pat.value.value]
            elif pat.objname == 'FROM-LOC':
                self.var_depart = map_city[pat.value.value]
            elif pat.objname=='ARRIVAL-TIME':
                self.var_arrival_time = pat.value.value
            elif pat.objname == 'THEME':
                self.var_train = pat.value.value
        
        self.dbTrain = {'var_train':self.var_train}
        self.dbDtime = {
            'var_train':self.var_train,
            'var_depart':self.var_depart,
            'var_depart_time':self.var_depart_time
        }
        self.dbAtime = {
            'var_train':self.var_train,
            'var_arrival':self.var_arrival,
            'var_arrival_time':self.var_arrival_time
        }
        self.dbRuntime ={
            'var_train':self.var_train,
            'var_depart':self.var_depart,
            'var_arrival':self.var_arrival,
            'var_run_time': self.var_run_time
        }
        

    def __str__(self):
        wh = self.request['name'] +' '+' '.join([var for var in self.request['var']])
        train_param = f'(TRAIN {self.var_train})'
        dtime_param = f'(DTIME {self.var_train} {self.var_depart} {self.var_depart_time})'
        atime_param = f'(ATIME {self.var_train} {self.var_arrival} {self.var_arrival_time})'
        rtime_param = f'(RUN-TIME {self.var_train} {self.var_depart} {self.var_arrival} {self.var_run_time})'
        return f'({wh} {train_param} {dtime_param} {atime_param} {rtime_param})'
    
    def __repr__(self):
        return self.__str__()