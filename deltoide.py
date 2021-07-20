def deltoid(h):

  if h%2 == 0:
    h = h+1
    
  if h > 43:
    print("The number is bigger than 43")
  elif h < 3:
    print("The number is shorter than 3")
  else:  
    j = int(h / 2 - 0.5)

    m = []
    for x in range(1, h+1, 2):
        print(" " * j + "*" * x)
        j = j - 1
        m.append(x)

    j = 1

    n = m[::-1]
    del n[0]

    for x in n:
        print(" " * j + "*" * x)
        j = j + 1

deltoid(int(input("Give me a number between 3 and 43 ")))

def curry_border(h):
  if h%2 == 0:
    h = h+1
    
  if h > 43:
    print("The number is bigger than 43")
  elif h < 3:
    print("The number is shorter than 3")
  else:
    j = int(h / 2 + 0.5)

    s = []

    i = 1

    print(" " * j + "*")
    for x in range(1, j):
        
        s.append([j-1, i])

        if i >= 1: i = i + 2
        else: i = i + 1

        j = j - 1

        print(" " * s[x-1][0] + "*" + " " * s[x-1][1] + "*")

    f = s[::-1]
    del f[0]

    j = int(h / 2 + 0.5)

    for u in range(1, j-1):
        print(" " * f[u-1][0] + "*" + " " * f[u-1][1] + "*")
        j = j - 1

    j = int(h / 2 + 0.5)

    print(" " * j + "*")

curry_border(int(input("Give me a number between 3 and 43 ")))

def dragon(h):
  if h%2 == 0:
    h = h+1
    
  if h > 43:
    print("The number is bigger than 43")
  elif h < 3:
    print("The number is shorter than 3")
  else:
    j = int(h / 2 + 0.5)
    #k =  int((h / 2 + 0.5)/2-0.5)
    k = 0

    s = []

    i = 1

    print(" " * j + "*")
    for x in range(1, j):
        
        s.append([j-1, i])

        if i >= 1: i = i + 2
        else: i = i + 1

        j = j - 1

        if j == 1:
            print(" " * s[x-1][0] + "*" * h)
        else:
            print(" " * s[x-1][0] + "*" + " " * k + "*" + " " * k + "*")
            k += 1
        
    k -= 1

    f = s[::-1]
    del f[0]

    j = int(h / 2 + 0.5)

    for u in range(1, j-1):
        print(" " * f[u-1][0] + "*" + " " * k + "*" + " " * k + "*")
        k -= 1
        j = j - 1

    j = int(h / 2 + 0.5)

    print(" " * j + "*")

dragon(int(input("Give me a number between 3 and 43 ")))
