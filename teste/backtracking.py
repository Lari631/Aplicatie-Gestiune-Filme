
valori = [1,'X',2]

def first_element(a):
    return 1

def next_element(a):
    if a == 1:
        return 'X'
    if a == 'X':
        return 2
    if a == 2:
        return 1

def consistent(x,dim):
    # if dim==3 and x[2]=='X':
          #return False
     count = 0 # to count how many are equal to 1
     for i in range (len(x)-1):
          if x[i]==1:
               count = count+1
     if count>2:
          return False
     return True

def solution(x,dim):
     return len(x)==dim

def solutionFound(x,dim):
     print(x)

def backIter(dim):
      x=[1] #candidate solution
      while len(x)>0:
          choosed = False
          while not choosed and x[-1]<dim-1:
               x[-1] = x[-1]+1 #increase the last component
               #x[-1]=next_element(x[-1])
               choosed = consistent(x, dim)
          if choosed:
               if solution(x, dim):
                    solutionFound(x, dim)
               x.append(-1) # expand candidate solution
          else:
               x = x[:-1] #go back one component

backIter(7)
