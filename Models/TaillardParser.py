class TaillardParser:

    def __init__(self, filename):
        self.filename = filename
        self.file_size = self.init_size()
        r = self.init_reader()
        if not r:
            raise Exception('FileError')

    def get_connexion_matrix(self):
        return self.readmatrix(self.file_size + 1)

    def get_distance_matrix(self):
        return self.readmatrix(0)

    def readmatrix(self, index):
        file_reader = self.init_reader()
        next(file_reader)  # skip du header

        for _ in range(index):  # skip des premières lignes
            next(file_reader)

        j = 0
        strbuf = ''
        connexion_matrix = []
        matrix_line = []

        line = file_reader.readline()

        while j < self.file_size and line != '':
            for i in line:
                if (i == ' ' or i == '\n') and strbuf != '':
                    matrix_line.append(int(strbuf))
                    strbuf = ''
                elif i != ' ' and i != '\n':
                    strbuf += i
            connexion_matrix.append(matrix_line)
            matrix_line = []
            line = file_reader.readline()
            j += 1

        file_reader.close()
        return connexion_matrix

    def init_size(self):
        file_reader = self.init_reader()

        file_size = file_reader.readline()

        file_reader.close()
        return int(file_size.strip())

    def init_reader(self):
        try:
            file_reader = open('data/' + self.filename, 'r')
        except NameError:
            print('Something went wrong')
            file_reader = False
        return file_reader





