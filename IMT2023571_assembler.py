def identifier(s):
  s = s[4:]
  l = []
  if (';' in s):
    s1 = ""
    for i in s:
      if (i != ';'):
        s1 = s1 + i
      else:
        break

    if (s1 == 'nop'):
      l.append('nop')
    else:
      w = ''
      for i in s1:
        if (i != ' '):
          w += i
        else:
          break
      if (w == 'load'):
        if ('(' in s1):
          a = s1[7:10]
          l.append(w)
          l.append(a)
        else:
          l.append(w+" "+"MQ")
      elif (w == 'stor'):
        if (',' in s1):
          if (s1[11] == '8'):
            l.append("storl")
            l.append(s1[7:10])
          else:
            l.append('storr')
            l.append(s1[7:10])
        else:
          l.append(w)
          l.append(s1[7:10])
      elif (w == "add"):
        l.append(w)
        l.append(s1[6:9])
      elif (w == "sub"):
        l.append(w)
        l.append(s1[6:9])
      elif (w == "div"):
        l.append(w)
        l.append(s1[6:9])
      elif (w == "jump"):
        if (s1[11] == '2'):
          l.append("jumpr")
          l.append(s1[7:10])
        else:
          l.append("jumpl")
          l.append(s1[7:10])
      elif (w == "jump+"):
        if (s1[12] == '2'):
          l.append("jump+r")
          l.append(s1[8:11])
        else:
          l.append("jump+l")
          l.append(s1[8:11])
      elif (w == "return"):
        l.append(w)
        l.append(s1[9:12])
      elif (w == "lt"):
        l.append(w)
        l.append(s1[5:8])
      elif (w == "gt"):
        l.append(w)
        l.append(s1[5:8])

    j = 0
    for i in range(len(s)):
      if (s[i] == ';'):
        j = i
        break
    s2 = s[j + 1:]
    if (s2 == 'nop'):
      l.append('nop')
    else:
      w = ''
      for i in s2:
        if (i != ' '):
          w += i
        else:
          break
      if (w == 'load'):
        if ('(' in s2):
          a = s2[7:10]
          l.append(w)
          l.append(a)
        else:
          l.append(w + " " + "MQ")

      elif (w == 'stor'):
        if (',' in s2):
          if (s2[11] == '8'):
            l.append("storl")
            l.append(s2[7:10])
          else:
            l.append('storr')
            l.append(s2[7:10])
        else:
          l.append(w)
          l.append(s2[7:10])
      elif (w == "add"):
        l.append(w)
        l.append(s2[6:9])
      elif (w == "sub"):
        l.append(w)
        l.append(s2[6:9])
      elif (w == "div"):
        l.append(w)
        l.append(s2[6:9])
      elif (w == "jump"):
        if (s2[11] == '2'):
          l.append("jumpr")
          l.append(s2[7:10])
        else:
          l.append("jumpl")
          l.append(s2[7:10])
      elif (w == "jump+"):
        if (s2[12] == '2'):
          l.append("jump+r")
          l.append(s2[8:11])
        else:
          l.append("jump+l")
          l.append(s2[8:11])
      elif (w == "return"):
        l.append(w)
        l.append(s2[9:12])
      elif (w == "lt"):
        l.append(w)
        l.append(s2[5:8])
      elif (w == "gt"):
        l.append(w)
        l.append(s2[5:8])
  else:
    l.append(s)
  #print(l)
  return l


#function to convert decimal to binary
def dtob(decimal_number):
  binary = ""
  #decimal_number = int(decimal_number)
  while decimal_number > 0:
    remainder = decimal_number % 2
    binary = str(remainder) + binary
    decimal_number //= 2

  if (len(binary) <= 12):
    k = ""
    k = k + ("0") * (12 - len(binary))
    k = k + binary
    binary = k
  return binary

dict = {}
dict["load"] = "00000001"
dict["load MQ"] = "00001010"
dict["add"] = "00000101"
dict["sub"] = "00000110"
dict["div"] = "00001100"
dict["stor"] = "00100001"
dict["storl"] = "00010010"
dict["storr"] = "00010011"
dict["jumpl"] = "00001101"
dict["jumpr"] = "00001110"
dict["jump+l"] = "00001111"
dict["jump+r"] = "00010000"
dict["lt"] = "11110000"
dict["gt"] = "11111000"
dict["return"] = "11111100"
dict["nop"] = "11111110"

file2 = open('binary.txt', 'w')
with open('IMT2023571_assembly.txt', 'r') as file1:
  for line in file1:
    s = ""
    s = s + line[:3] + " "
    #print(s)
    #print(line)
    l = identifier(line[:-1])
    if (len(l) == 4):
      lefti = dict[l[0]]
      lefta = str(dtob(int(l[1])))
      righti = dict[l[2]]
      righta = str(dtob(int(l[3])))
      s = s + lefti + lefta + righti + righta

    elif (len(l) == 3):
      if (l[0] == "load MQ"):
        lefti = dict[l[0]]
        lefta = "000000000000"
        righti = dict[l[1]]
        righta = str(dtob(int(l[2])))
        s = s + lefti + lefta + righti + righta

      elif (l[2] == "load MQ"):
        lefti = dict[l[0]]
        lefta = str(dtob(int(l[1])))
        righti = dict[l[2]]
        righta = "000000000000"
        s = s + lefti + lefta + righti + righta

      elif (l[2] == "nop"):
        lefti = dict[l[0]]
        lefta = str(dtob(int(l[1])))
        righti = dict[l[2]]
        righta = "000000000000"
        s = s + lefti + lefta + righti + righta

    elif (len(l) == 2):
      lefti = dict[l[0]]
      lefta = "000000000000"
      print(l)
      righti = dict[l[1]]
      righta = "000000000000"
      s = s + lefti + lefta + righti + righta

    elif (len(l) == 1):
      #print(l[0])
      x = dtob(int(l[0]))
      s = s + "0" * 28 + x

    file2.write(s)
    file2.write("\n")
file1.close()
file2.close()
