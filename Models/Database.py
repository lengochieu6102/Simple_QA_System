class Database:
    def __init__(self, raw_db_path):
        self.trains = []
        self.atimes = []
        self.dtimes = []
        self.runtimes = []
        # Read each line in raw_db
        with open(raw_db_path, 'r') as f:
            rows = f.readlines()
            for row in rows:
                row = ' '.join(row.strip().replace('(', ' ').replace(')', ' ').split())
                if 'TRAIN' in row:
                    self.trains.append(row)
                elif 'ATIME' in row:
                    self.atimes.append(row)
                elif 'DTIME' in row:
                    self.dtimes.append(row)
                elif 'RUN-TIME' in row:
                    self.runtimes.append(row)
              
    def __str__(self):
        return '\n'.join(self.trains + self.atimes + self.dtimes + self.runtimes)