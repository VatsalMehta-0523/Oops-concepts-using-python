class student:                          # class named student
    
    def __init__(self , m1,m2,m3):      # instance method

        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        tot = self.m1 + self.m2 + self.m3
        print("total = " , tot)
        print("average = " , tot/3 )

# student() --> is constructer which can constructs multiple objects
s1 = student(99, 89, 93)        # s1 is object