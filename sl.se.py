def fares (age,student=false,senior=false):
    print age, student,senior if age <=18:
    return 'halv' elif age >=66:
    return 'halv'
else:
    return 'hel'





    print 'barn 10',fares(10)
    print 'pension 66',fares(66)
    print 'student 24',fares(24,student=true)
    print 'vuxen 46',fares(46)