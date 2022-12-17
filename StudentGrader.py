class StudentGrader:
    '''
        Class that can be used as a basic grader for students
        on various assignment types.
        Joe Kennedy
        11/29/2022
    '''
    def __init__(self, name = '', assignment = '', score = 0.0):
        self.__name = name
        self.__assignment = assignment
        self.__score = score
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def assignment(self):
        return self.__assignment
    @assignment.setter
    def assignment(self, assignment):
        self.__assignment = assignment
        
    @property
    def score(self):
        return float(self.__score)
    @score.setter
    def score(self, score):
        self.__score = score
        
    
    def __str__(self):
        ''' string representation of the student grader '''
        displayString = str('{:10} {:15}\n'.format('Student name:', self.__name) + 
                            '{:10} {:1}\n'.format('Assignment:', (self.__assignment)) + 
                            '{:10} {:<15.2f}\n'.format('Score:', self.__score))
        return displayString
    
if __name__ == '__main__':
    i1 = StudentGrader()
    print(i1)
    
    i2 = StudentGrader()
    i2.name = 'Joe K'
    i2.assignment = 'Quiz'
    i2.score = 99
    print(i2)