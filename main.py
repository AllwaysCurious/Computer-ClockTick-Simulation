# Created By Bit Curious Creations

from random import randint
import time
CIR = "" # Current Instruction Register
ACC = "" # Accumulator
MAR = "" # Memory Address Register
MDR = "" # Memory Data Register
PC = 0 # Programme Counter
ProgressNum = 0
OPCODE = ""
OPERAND = ""
Memory = [[],[]] # 1-InstructionData 2-NumberData
while True:
    Quest = input("How many ticks do you want the system to do? (Type = 'inf' for infinite ticks): ")
    if Quest.lower() == "inf":
        Quest = float("inf")
        break
    else:
        try:
            Quest = int(Quest)
            break
        except:
            print("Type only numbers!")

Instructions = ["STO","ADD","SUB","DEV","MUL"]

def OutputRegisters(Progress,Num):
    if Progress == True:
        print(f'++ Clock Tick #{ProgressNum} Progress #{Num} ++')
    else:
        print(f'++ Finished Clock Tick #{ProgressNum} ++')
    print(f'CIR[{CIR}]')
    print(f'ACC[{ACC}]')
    print(f'MAR[{MAR}]')
    print(f'MDR[{MDR}]')
    print(f'PC[{PC}]')
    print("")
    time.sleep(0.05)

def RandomizeInstruction():
    Memory[1].append(f'{randint(0,999)}')
    if PC == 0:
        Memory[0].append(f'STO#{randint(0,len(Memory[1])-1)}')
    elif ProgressNum == Quest:
        Memory[0].append("HALT")
        return "HALT"
    else:
        if randint(1,2) == 1:
            Memory[0].append(Instructions[randint(0,len(Instructions)-1)] + f'#{randint(0,len(Memory[1])-1)}')
        else:
            Memory[0].append(Instructions[randint(0,len(Instructions)-1)] + f'{randint(0,len(Memory[1])-1)}')

while True:
    RandomizeInstruction()
    ProgressNum = ProgressNum + 1

    # Fetch #
    MAR = PC
    OutputRegisters(True,1)
    MDR = Memory[0][MAR]
    OutputRegisters(True,2)
    CIR = MDR
    OutputRegisters(True,3)
    PC = PC + 1
    OutputRegisters(True,4)

    # Decode #
    OPCODE = CIR[0:3] # "STO #4536"
    if OPCODE == "HAL":
        OPCODE = "HALT"
    OPERAND = CIR[3:]
    #print(OPCODE)
    #print(OPERAND)

    # Execute #
    if OPCODE == "HALT":
        break
    elif OPCODE == "STO":
        #print(OPERAND[0])
        if OPERAND[0] == "#":
            ACC = int(int(OPERAND[1:]))
        else:
            ACC = int(Memory[1][int(OPERAND[0:])])
    elif OPCODE == "ADD":
        if OPERAND[0] == "#":
            ACC = ACC + int(int(OPERAND[1:]))
        else:
            ACC = ACC + int(Memory[1][int(OPERAND[0:])])
    elif OPCODE == "SUB":
        if OPERAND[0] == "#":
            ACC = ACC - int(int(OPERAND[1:]))
        else:
            ACC = ACC - int(Memory[1][int(OPERAND[0:])])
    elif OPCODE == "DEV":
        try:
            if OPERAND[0] == "#":
                ACC = ACC / int(int(OPERAND[1:]))
            else:
                ACC = ACC / int(Memory[1][int(OPERAND[0:])])
        except:
            print("Cannot Divide by 0, Skipping Arithlogic Logic Unit Calculation...")
    elif OPCODE == "MUL":
        if OPERAND[0] == "#":
            ACC = ACC * int(OPERAND[1:])
        else:
            ACC = ACC * int(Memory[1][int(OPERAND[0:])])
    OutputRegisters(False,0)
