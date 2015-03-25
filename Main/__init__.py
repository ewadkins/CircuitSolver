from le import solveEquations

'''
eq1 = [(1, 'e1'), (-1, 'e0'), (-15, None)]
eq2 = [(1, 'e1'), (-1, 'e2'), (-3, 'i2')]
eq3 = [(1, 'e2'), (-1, 'e0'), (-2, 'i3')]
eq4 = [(1, 'i4'), (10, None)]

eq5 = [(1, 'i1'), (1, 'i2'), (0, None)]
eq6 = [(1, 'i3'), (1, 'i4'), (-1, 'i2'), (0, None)]

eq7 = [(1, 'e0'), (0, None)]

equationList = [eq1, eq2, eq3, eq4, eq5, eq6, eq7]
'''

class OnePort:
    def __init__(self, e1, e2, i):
        self.e1 = e1
        self.e2 = e2
        self.i = i
class VSrc(OnePort):
    def __init__(self, v0, e1, e2, i):
        OnePort.__init__(self,e1,e2,i)
        self.equation = [(1, e1), (-1, e2), (-v0, None)]

class ISrc(OnePort):
    def __init__(self, i0, e1, e2, i):
        OnePort.__init__(self,e1,e2,i)
        self.equation = [(i0, None), (-1, i)]

class Resistor(OnePort):
    def __init__(self, r, e1, e2, i):
        OnePort.__init__(self,e1,e2,i)
        self.equation = [(1, e1), (-1, e2), (-r, i)]


def flatten_list(l):
    out = []
    for i in l:
        if type(i) == list:
            out.extend(flatten_list(i))
        else:
            out.append(i)
    return out


def solveCircuit(componentList, GND):
    # flatten_list is necessary for lists that contain two-ports.
    # It has no effect on lists that contain just one-ports.
    # Do not remove the following line.
    componentList = flatten_list(componentList)

    equationList = [[(1, GND)]]

    for component in componentList:
        equationList.append(component.equation)
    
    nodeList = []
    for component in componentList:
        if(component.e1 == GND or component.e2 == GND):
            continue
        if (not component.e1 in nodeList):
            nodeList.append(component.e1)
        if (not component.e2 in nodeList):
            nodeList.append(component.e2)
    for node in nodeList:
        equation = []
        for component in componentList:
            if(component.e1 == node):
                equation.append((1, component.i))
            if(component.e2 == node):
                equation.append((-1, component.i))
            
        equationList.append(equation)
    
    
    return solveEquations(equationList,verbose=False)


ans = {}

'''
v1 = VSrc(15, 'e1', 'e0', 'i1')
r1 = Resistor(3, 'e1','e2','i2')
r2 = Resistor(2, 'e2', 'e0', 'i3')
i1 = ISrc(-10, 'e2','e0','i4')
ans = solveCircuit([v1,r1,r2,i1],'e0')
'''
'''
v1 = VSrc(90, 'e1', 'e0', 'i1')
r1 = Resistor(3, 'e1','e2','i2')
r2 = Resistor(6, 'e2', 'e0', 'i3')
r3 = Resistor(20, 'e2', 'e0', 'i0')
ans = solveCircuit([v1, r1, r2, r3],'e0')
'''

v1 = VSrc(6, 'e2', 'e0', 'i1')
v2 = VSrc(5, 'e3', 'e0', 'i5')
r1 = Resistor(3, 'e2','e1','i2')
r2 = Resistor(1, 'e1', 'e3', 'i4')
r3 = Resistor(1, 'e1', 'e0', 'i3')
ans = solveCircuit([v1, v2, r1, r2, r3],'e0')

'''
val1 = 0
val2 = 0
for i in range(100):
    for j in range(100):
        v1 = VSrc(i*0.5, 'e1', 'e0', 'i1')
        v2 = VSrc(j*0.5, 'e4', 'e0', 'i5')
        r1 = Resistor(2, 'e1','e2','i2')
        r2 = Resistor(1, 'e2', 'e3', 'i3')
        r3 = Resistor(4, 'e3', 'e4', 'i4')
        r4 = Resistor(2, 'e2', 'e0', 'ia')
        r5 = Resistor(5, 'e3', 'e0', 'ib')
        ans = solveCircuit([v1, v2, r1, r2, r3, r4, r5],'e0')
        #print ans['ia'], ans['ib']
        if(ans['ia']>=6.99 and ans['ia']<=7.01 and ans['ib']>=2.99 and ans['ib']<=3.01):
            val1 = i
            val2 = j
            break

print "V1:", val1
print "V2:", val2
'''

for key in ans.keys():
    print "%s:" % key,  ans[key]

