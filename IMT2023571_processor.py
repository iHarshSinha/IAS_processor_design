import time
ACCUMULATOR = ""
MAR = ""
MBR = ""
IR = "" 
IBR = ""
MEM = ""
MQ = ""
PC = "200"
c = 1
LIR = 1
jump_flag_all=0
dic = {}
file1 = open("binary.txt", "r")

def printer():
  global ACCUMULATOR
  global MAR
  global MBR
  global IR
  global IBR
  global MQ
  global PC
  # print("value of accumulator in binary and decimal is")
  # print (ACCUMULATOR)
  # print(int(binary_to_decimal(ACCUMULATOR)))
  # print("value of mar in binary and decimal is")
  # print (MAR)
  # print(int(binary_to_decimal((MAR))))
  # print("value of mbr in binary and decimal is")
  # print (MBR)
  # print(int(binary_to_decimal(MBR)))
  # print("value of ir in binary and decimal is")
  # print (IR)
  # print(int(binary_to_decimal(IR)))
  # print("value of ibr in binary and decimal is")
  # print (IBR)
  # print(int(binary_to_decimal(IBR)))
  # print("value of mq in binary and decimal is")
  # print (MQ)
  # print(int(binary_to_decimal(MQ)))

def decimal_to_binary(n):
  n=int(n)
  if (n >= 0):
    b = ""
    while n > 0:
      r = n % 2
      b = str(r) + b
      n //= 2
    a = len(b)
    if (a == 39):
      return ('0' + b)
    elif (a < 39):
      return ((40 - a) * '0' + b)
  else:
    n1 = -n
    i = 1
    while (n1 // (2**(i)) != 0):
      i += 1
    #print(i)
    i += 1  # value=5
    a = 2**(i - 1) - n1
    b = decimal_to_binary(a)
    b = b[-(i - 1):]
    b = ((40 - len(b)) * '1') + b
    return b

def binary_to_decimal(b_string):
  ret =0
  b_string=b_string[::-1]
  count=0
  for i in range(len(b_string)):
    if(i<len(b_string)-1):
      ret+=(2**count)*int(b_string[i])
    else:
      ret-=(2**count)*int(b_string[i])
    count+=1
  if(ret>=0):
    return (3-len(str(ret)))*'0'+str(ret)
  else:
    return '-'+(3-len(str(-ret)))*'0'+str(-ret)

def load(ad):
  global dic
  global ACCUMULATOR
  global MBR
  ad=binary_to_decimal(ad)
  value=dic[ad]
  MBR=value
  ACCUMULATOR=MBR
  global jump_flag_all
  jump_flag_all=0

def add(ad):
  global dic
  global ACCUMULATOR
  global MBR
  ad=binary_to_decimal(ad)
  value=dic[ad]
  MBR=value
  ac_value=int(binary_to_decimal(ACCUMULATOR))
  mbr_value=int(binary_to_decimal(MBR))
  sum=ac_value+mbr_value
  ACCUMULATOR=decimal_to_binary(sum)
  global jump_flag_all
  jump_flag_all=0

def sub(ad):
  global ACCUMULATOR
  global dic
  global MBR
  ad=binary_to_decimal(ad)
  value=dic[ad]
  MBR=value
  ac_value=int(binary_to_decimal(ACCUMULATOR))
  mbr_value=int(binary_to_decimal(MBR))
  dif=ac_value-mbr_value
  ACCUMULATOR=decimal_to_binary(dif)
  global jump_flag_all
  jump_flag_all=0

def stor(ad):
  global ACCUMULATOR
  global dic
  global MBR
  MBR=ACCUMULATOR
  ad=binary_to_decimal(ad)
  dic[ad]=MBR
  global jump_flag_all
  jump_flag_all=0

def load_MQ(ad):
  global ACCUMULATOR
  global MQ
  ACCUMULATOR = MQ
  global jump_flag_all
  jump_flag_all=0

def div(ad):
  global ACCUMULATOR
  global dic
  global MQ
  global MBR
  ad=binary_to_decimal(ad)
  MBR=dic[ad]
  value_ac=int(binary_to_decimal(ACCUMULATOR))
  value_mbr=int(binary_to_decimal(MBR))
  quo=value_ac//value_mbr
  rem=value_ac%value_mbr
  ACCUMULATOR=decimal_to_binary(rem)
  MQ=decimal_to_binary(quo)
  global jump_flag_all
  jump_flag_all=0
  
def storl(ad):
  global ACCUMULATOR
  global dic
  global MBR
  MBR='0'*28+ACCUMULATOR[28:]
  ad=binary_to_decimal(ad)
  dic[ad]=((dic[ad])[:8])+MBR[28:]+dic[ad][20:]
  #(dic[ad])[8:20]=MBR[28:]
  global jump_flag_all
  jump_flag_all=0

def storr(ad):
  global dic
  global ACCUMULATOR
  global MBR
  MBR='0'*28+ACCUMULATOR[28:]
  ad=binary_to_decimal(ad)
  dic[ad]=((dic[ad])[:28])+MBR[28:]
  #(dic[ad])[28:]=MBR[28:]

def jumpl(ad):
  global PC
  global dic
  global jump_flag_all
  
  PC = binary_to_decimal(ad)
  jump_flag_all=1
  printer()


def jumpr(ad):
  global PC
  global dic
  global jump_flag_all
  
  global LIR
  PC = binary_to_decimal(ad)
  LIR = 0
  jump_flag_all=1

def jumpal(ad):
  global PC
  global dic
  global jump_flag_all
  global ACCUMULATOR
  if (int(binary_to_decimal(ACCUMULATOR)) == 1):
    PC = binary_to_decimal(ad)
    jump_flag_all=1

    


def jumpar(ad):
  global PC
  global dic
  global LIR
  global jump_flag_all
  
  if (int(binary_to_decimal(ACCUMULATOR)) == 1):
    PC = binary_to_decimal(ad)
    LIR = 0
    jump_flag_all=1

def lt(ad):
  global ACCUMULATOR
  global dic
  global PC
  ad= binary_to_decimal(ad)
  value_ac = int(binary_to_decimal(ACCUMULATOR))
  value_loc=int(binary_to_decimal(dic[ad]))
  if(value_ac<value_loc):
    ACCUMULATOR=('0'*39) +'1'
  else:
    ACCUMULATOR='1'*40

def gt(ad):
  global dic
  global ACCUMULATOR
  ad= binary_to_decimal(ad)
  value_ac=int(binary_to_decimal(ACCUMULATOR))
  value_loc=int(binary_to_decimal(dic[ad]))
  if(value_loc<value_ac):
    ACCUMULATOR=('0'*39) +'1'
  else:
    ACCUMULATOR='1'*40

def returnval(ad):
  global dic
  if(PC=="804"):
    print("Max value: ",int(binary_to_decimal(dic[binary_to_decimal(ad)])))
  if(PC=="805"):
    print("Min value: ",int(binary_to_decimal(dic[binary_to_decimal(ad)])))
  if(PC=="807"):
    print("Sum of all elements: ",int(binary_to_decimal(dic[binary_to_decimal(ad)])))
  if(PC=="806"):
    print("Range value: ",int(binary_to_decimal(dic[binary_to_decimal(ad)])))
  if(PC=="808"):
    print("COD value: ",int(binary_to_decimal(dic[binary_to_decimal(ad)])))
  if(PC=="809"):
    print("Mean value: ",int(binary_to_decimal(dic[binary_to_decimal(ad)])))
  
  

def nop():
  pass

def execute_cycle(opcode):
  global dic
  if (opcode == "load"):
    load(MAR)
  if (opcode == "load MQ"):
    load_MQ(MAR)
  if (opcode == "add"):
    add(MAR)
  if (opcode == "sub"):
    sub(MAR)
  if (opcode == "div"):
    div(MAR)
  if (opcode == "stor"):
    stor(MAR)
  if (opcode == "storl"):
    storl(MAR)
  if (opcode == "storr"):
    storr(MAR)
  if (opcode == "jumpl"):
    jumpl(MAR)
  if (opcode == "jumpr"):
    jumpr(MAR)
  if (opcode == "jumpal"):
    jumpal(MAR)
  if (opcode == "jumpar"):
    jumpar(MAR)
  if (opcode == "lt"):
    lt(MAR)
  if (opcode == "gt"):
    gt(MAR)
  if (opcode == "returnval"):
    returnval(MAR)
  if (opcode == "nop"):
    nop()


def decodecycle(opcode):
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
  if (opcode == dict["load"]):
    execute_cycle("load")
  if (opcode == dict["load MQ"]):
    execute_cycle("load MQ")
  if (opcode == dict["add"]):
    execute_cycle("add")
  if (opcode == dict["sub"]):
    execute_cycle("sub")
  if (opcode == dict["div"]):
    execute_cycle("div")
  if (opcode == dict["stor"]):
    execute_cycle("stor")
  if (opcode == dict["storl"]):
    execute_cycle("storl")
  if (opcode == dict["storr"]):
    execute_cycle("storr")
  if (opcode == dict["jumpl"]):
    execute_cycle("jumpl")
  if (opcode == dict["jumpr"]):
    execute_cycle("jumpr")
  if (opcode == dict["jump+l"]):
    execute_cycle("jumpal")
  if (opcode == dict["jump+r"]):
    execute_cycle("jumpar")
  if (opcode == dict["lt"]):
    execute_cycle("lt")
  if (opcode == dict["gt"]):
    execute_cycle("gt")
  if (opcode == dict["return"]):
    execute_cycle("returnval")
  if (opcode == dict["nop"]):
    execute_cycle("nop")


def fetch(dic):
  global c
  global PC
  global jump_flag_all
  global IR
  global IBR
  global MAR
  global MBR
  global LIR
 
  if(LIR==1):
    if(len(IBR)==0):
        if (len(PC) < 3):
            PC = "0" * (3 - len(PC)) + PC
        MAR = PC
        MBR = dic[MAR]

        IR = MBR[0:8]
        MAR = MBR[8:20]
        IBR=MBR[20:]
        decodecycle(IR)
    if(jump_flag_all==1):
        jump_flag_all=0
        IBR=""
        return 
    if(len(IBR)>0):
        IR = IBR[0:8]
        MAR = IBR[8:20]
        decodecycle(IR)
        if(jump_flag_all==1):
         jump_flag_all=0
         IBR=""
         return 
  else:
     MBR=dic[PC]
     IBR=MBR[20:40]
     IR=IBR[0:8]
     MAR=IBR[8:20]
     decodecycle(IR)
     LIR=1

  k = int(PC)
  k = k + 1
  PC = str(k)
  IBR=""



def Meml(dic):
  global c
  for line in file1:
    if (c < 24):
      #print(line[:3],end =" ")

      dic[line[:3]] = (line[4:-1])
      c += 1
      #print(binary_to_decimal(dic[line[:3]]))
    else:
      dic[line[:3]] = line[4:-1]


Meml(dic)
while (PC != "810"):
  if(int(PC)<499):
    print(PC," current value of PC")
    print(int(binary_to_decimal(dic['021']))," current value of max stored at '21' in my loop")
    print()
    time.sleep(.5)
  if(int(PC)>499 and int(PC)<599):
    print(PC," current value of PC")
    print(int(binary_to_decimal(dic['026']))," current value of min stored at '26'")
    print()
    time.sleep(.5)
  if(int(PC)>749 and int(PC)<804):
    print(PC," current value of PC")
    print(int(binary_to_decimal(dic['030']))," current value of sum stored at '30'")
    print()
    time.sleep(.5)
  fetch(dic)
  # if(int(PC)==804):
  #   print("- "*200)
# print("value of mean of all terms stored at '32' is ",int(binary_to_decimal(dic['032'])))
# print("value of range stored at '27' is ",int(binary_to_decimal(dic['027'])))
# print("value of coeff of disperson stored at '29' is ",int(binary_to_decimal(dic['029'])))
# print("final value of max stored at '21' is ",int(binary_to_decimal(dic['021'])))
# print("final value of min stored at '26' is ",int(binary_to_decimal(dic['026'])))



