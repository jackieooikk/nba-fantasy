
def find_attempt(fgperc):
    fgstring = ""
    state = 0
    for char in fgperc:
        if (char == '/'):
            state = 1
        elif (char == ')'):
            state = 0
        elif (state == 1):
            fgstring += char
    return float(fgstring)

class Stars:
    name = ""
    team = ""
    position = ""
    gp = 0
    
    points = 0.0
    rebounds = 0.0
    assists = 0.0
    steals = 0.0
    blocks = 0.0
    threes = 0.0

    fgm = 0.0
    fga = 0.0
    ftm = 0.0
    fta = 0.0
    fg = 0.0
    ft = 0.0
    to = 0.0


    

    def __init__(self, row):
        self.name = row[2]
        self.team = row[4]
        self.position = row[3]
        self.gp = row[5]

        self.fgm = row[7]
        self.ftm = row[9]
        self.fga = find_attempt(row[8])
        self.fta = find_attempt(row[10])

        self.fg = self.fgm/self.fga
        self.ft = self.ftm/self.fta
        self.threes = row[11]
        self.points = row[12]
        self.rebounds = row[13]
        self.assists = row[14]
        self.steals = row[15]
        self.blocks = row[16]
        self.to = row[17]

        

    def __repr__(self):
        return f"{self.name} {self.team}"