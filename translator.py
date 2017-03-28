#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a translator module'

__author__ = 'Andy Xu'

import sys, os, time

#LHTranslator:
#input:ShopNumber
def LHtranslator(NewJob):
	SONum = NewJob[:6]
	PartCode = NewJob[-5:-4]
	LHPath = "S:/LiftingHoles/" + SONum + ".txt"	#Liftinghole numbers and angles information
	LHPositionPath = "S:/holelocation/" + SONum + PartCode + ".txt"	#Liftinghole distance and diameter information
	LHTool = "S:/Development/Gary/test/DieRingTranslatorTest/LiftingHoleToolID.txt"
	if not os.path.exists(LHPath):
	 print("=======================================")
	 print(LHPath, "not exist, can't do liftinghole!")
	 print("=======================================")
	 return
	if not os.path.exists(LHPositionPath):
	 print("=======================================")
	 print(LHPositionPath, "not exist, can't do liftinghole!")
	 print("=======================================")
	 return	
	Size = ""
	file = open(LHPath)
	AngleList_M = []
	AngleList_P = []
	AngleList_B = []
	AngleList_F = []
	while 1:				#Here we get size and liftinghole numbers and angles
	 line = file.readline()
	 if not line:
	  break
	 lineLen = len(line)
	 if line == "3/4-10\n":
	  Size = "3_4-10"
	 if line == "3/4-10x47\n":
	  Size = "3_4-10x47"
	 if line == "3/4-10x47-CBORE\n":
	  Size = "3_4-10x47-CBORE"
	 if line == "1in-8\n":
	  Size = "1in-8"
	 if "MANDREL" in line:
	  pos = 1
	  CommaList = []
	  while line.find(',',pos + 1) != -1:
	   pos = line.find(',', pos + 1)
	   CommaList.append(pos)
	  AngleNums = int(line[CommaList[0] + 1: CommaList[0] + 2])
	  if(AngleNums == 1):
	   AngleList_M.append('90')
	  elif(AngleNums == 2):
	   AngleList_M.append(line[CommaList[1] + 1: CommaList[2]])
	   AngleList_M.append(line[CommaList[2] + 1: lineLen - 1])
	  elif(AngleNums == 3):
	   AngleList_M.append(line[CommaList[1] + 1: CommaList[2]])
	   AngleList_M.append(line[CommaList[2] + 1: CommaList[3]])
	   AngleList_M.append(line[CommaList[3] + 1: lineLen - 1])
	  elif(AngleNums == 4):
	   AngleList_M.append(line[CommaList[1] + 1: CommaList[2]])
	   AngleList_M.append(line[CommaList[2] + 1: CommaList[3]])
	   AngleList_M.append(line[CommaList[3] + 1: CommaList[4]])
	   AngleList_M.append(line[CommaList[4] + 1: lineLen - 1])
	 if "PLATE" in line:
	  pos = 1
	  CommaList = []
	  while line.find(',',pos + 1) != -1:
	   pos = line.find(',', pos + 1)
	   CommaList.append(pos)
	  AngleNums = int(line[CommaList[0] + 1: CommaList[0] + 2])
	  if(AngleNums == 1):
	   AngleList_P.append('90')
	  elif(AngleNums == 2):
	   AngleList_P.append(line[CommaList[1] + 1: CommaList[2]])
	   AngleList_P.append(line[CommaList[2] + 1: lineLen - 1])
	  elif(AngleNums == 3):
	   AngleList_P.append(line[CommaList[1] + 1: CommaList[2]])
	   AngleList_P.append(line[CommaList[2] + 1: CommaList[3]])
	   AngleList_P.append(line[CommaList[3] + 1: lineLen - 1])
	  elif(AngleNums == 4):
	   AngleList_P.append(line[CommaList[1] + 1: CommaList[2]])
	   AngleList_P.append(line[CommaList[2] + 1: CommaList[3]])
	   AngleList_P.append(line[CommaList[3] + 1: CommaList[4]])
	   AngleList_P.append(line[CommaList[4] + 1: lineLen - 1])
	 if "BACKER" in line:
	  pos = 1
	  CommaList = []
	  while line.find(',',pos + 1) != -1:
	   pos = line.find(',', pos + 1)
	   CommaList.append(pos)
	  AngleNums = int(line[CommaList[0] + 1: CommaList[0] + 2])
	  if(AngleNums == 1):
	   AngleList_B.append('90')
	  elif(AngleNums == 2):
	   AngleList_B.append(line[CommaList[1] + 1: CommaList[2]])
	   AngleList_B.append(line[CommaList[2] + 1: lineLen - 1])
	  elif(AngleNums == 3):
	   AngleList_B.append(line[CommaList[1] + 1: CommaList[2]])
	   AngleList_B.append(line[CommaList[2] + 1: CommaList[3]])
	   AngleList_B.append(line[CommaList[3] + 1: lineLen - 1])
	  elif(AngleNums == 4):
	   AngleList_B.append(line[CommaList[1] + 1: CommaList[2]])
	   AngleList_B.append(line[CommaList[2] + 1: CommaList[3]])
	   AngleList_B.append(line[CommaList[3] + 1: CommaList[4]])
	   AngleList_B.append(line[CommaList[4] + 1: lineLen - 1])
	 if "FEEDER" in line:
	  pos = 1
	  CommaList = []
	  while line.find(',',pos + 1) != -1:
	   pos = line.find(',', pos + 1)
	   CommaList.append(pos)
	  AngleNums = int(line[CommaList[0] + 1: CommaList[0] + 2])
	  if(AngleNums == 1):
	   AngleList_F.append('90')
	  elif(AngleNums == 2):
	   AngleList_F.append(line[CommaList[1] + 1: CommaList[2]])
	   AngleList_F.append(line[CommaList[2] + 1: lineLen - 1])
	  elif(AngleNums == 3):
	   AngleList_F.append(line[CommaList[1] + 1: CommaList[2]])
	   AngleList_F.append(line[CommaList[2] + 1: CommaList[3]])
	   AngleList_F.append(line[CommaList[3] + 1: lineLen - 1])
	  elif(AngleNums == 4):
	   AngleList_F.append(line[CommaList[1] + 1: CommaList[2]])
	   AngleList_F.append(line[CommaList[2] + 1: CommaList[3]])
	   AngleList_F.append(line[CommaList[3] + 1: CommaList[4]])
	   AngleList_F.append(line[CommaList[4] + 1: lineLen - 1])
	file.close()
	
	file = open(LHTool)
	while 1:				#Here we get tool numbers
	 line = file.readline()
	 lineLen = len(line)
	 if not line:
	  break
	 if Size in line:
	  pos = 1
	  ToolNums = 0
	  ColonList = []
	  ToolList = []
	  ToolNameList = []
	  CommaList = []
	  while line.find(':', pos + 1) != -1:
	   pos = line.find(':', pos + 1)
	   ColonList.append(pos)
	   ToolNums += 1
	  i = 0
	  while i < ToolNums:
	   ToolList.append(line[ColonList[i] + 1: ColonList[i] + 3])
	   i += 1
	  pos = 1
	  while line.find('|', pos + 1) != -1:
	   pos = line.find('|', pos + 1)
	   CommaList.append(pos)
	  i = 1
	  while i <= ToolNums:
	   ToolNameList.append(line[CommaList[i] + 1: ColonList[i - 1]])
	   i += 1
	  break
	
	file = open(LHPositionPath)
	while 1:				#Here we get Distance and Diameter
	 line = file.readline()
	 lineLen = len(line)
	 if not line:
	  break
	 DisPos = line.find('LOC', 0)
	 DiaPos = line.find('LOCDIA', 0)
	 LHDis = line[DisPos + 4: DisPos + 9]
	 LHDia = float(line[DiaPos + 7: lineLen])
	 LHDia *= 2
	 LHDia = str(LHDia)
	file.close()
	
	file = open('S:/Development/Gary/test/DieRingTranslatorTest/MachSetup.txt')
	while 1:				#Here we get V3001, V3002 and V3003
	 line = file.readline()
	 if not line:
	  break
	 lineLen = len(line)
	 if "MC1" in line:
	  pos = 2
	  VerticalList = []
	  while line.find('|',pos + 1) != -1:
	   pos = line.find('|', pos + 1)
	   VerticalList.append(pos)
	  MC1_V3001 = line[VerticalList[0] + 1: VerticalList[1]]
	  MC1_V3002 = line[VerticalList[1] + 1: VerticalList[2]]
	  MC1_V3003 = line[VerticalList[2] + 1: VerticalList[3]]
	 if "MCNP" in line:
	  pos = 2
	  VerticalList = []
	  while line.find('|',pos + 1) != -1:
	   pos = line.find('|', pos + 1)
	   VerticalList.append(pos)
	  MCNP_V3001 = line[VerticalList[0] + 1: VerticalList[1]]
	  MCNP_V3002 = line[VerticalList[1] + 1: VerticalList[2]]
	  MCNP_V3003 = line[VerticalList[2] + 1: VerticalList[3]]
	 if "MC21" in line:
	  pos = 2
	  VerticalList = []
	  while line.find('|',pos + 1) != -1:
	   pos = line.find('|', pos + 1)
	   VerticalList.append(pos)
	  MC21_V3001 = line[VerticalList[0] + 1: VerticalList[1]]
	  MC21_V3002 = line[VerticalList[1] + 1: VerticalList[2]]
	  MC21_V3003 = line[VerticalList[2] + 1: VerticalList[3]]
	file.close()
	
	#Start translate
	MC1File = "S:/Development/Andy/LiftingHoleTest/result/" + SONum + PartCode + ".txt"
	file = open(MC1File,"w")
	file.write('%\n')
	file.write('N0 (SONUM: ' + SONum + ')\n')
	file.write('N1 (Do Lifting Holes #1)\n')
	file.write('N2 [SV,V23=' + LHDia + ',V24=' + LHDis + ']\n')
	file.write('N3 [V3001=' + MC1_V3001 + ']\n')
	file.write('N4 [V3002=V24+' + MC1_V3002 + ']\n')
	file.write('N5 [V3003=V23/2' + MC1_V3003 + ']\n')
	file.write('N6 G53\n')
	file.write('N7 G73Z900\n')
	file.write('N8 G57H901\n')
	lineNum = 9
	ToolNum = 0
	RunningToolNameNum = 0
	HoldToolNameNum = 1
	RunningToolNum = 0
	HoldToolNum = 1
	NoMoreTool = False
	InitialRound = True
	
	cur_angleNum = 0
	if PartCode == 'M':
	 file.write('N' + str(lineNum) + ' G00 B' + AngleList_M[cur_angleNum] + '\n')
	elif PartCode == 'P':
	 file.write('N' + str(lineNum) + ' G00 B' + AngleList_P[cur_angleNum] + '\n')
	elif PartCode == 'B':
	 file.write('N' + str(lineNum) + ' G00 B' + AngleList_B[cur_angleNum] + '\n')
	elif PartCode == 'F':
	 file.write('N' + str(lineNum) + ' G00 B' + AngleList_F[cur_angleNum] + '\n')
	cur_angleNum += 1
	lineNum += 1
	file.write('N' + str(lineNum) + ' T' + ToolList[RunningToolNum] + '\n')
	lineNum += 1
	file.write('N' + str(lineNum) + ' M06\n')
	lineNum += 1
	file.write('N' + str(lineNum) + ' G551H' + ToolList[RunningToolNum] + '\n')
	lineNum += 1
	file.write('N' + str(lineNum) + ' G73Z900\n')
	lineNum += 1
	file.write('N' + str(lineNum) + ' G90G00X0.0Y0.0\n')
	lineNum += 1
	file.write('N' + str(lineNum) + ' G43Z101.6H' + ToolList[RunningToolNum] + '\n')
	lineNum += 1
	file.write('N' + str(lineNum) + ' T' + ToolList[HoldToolNum] + '\n')
	lineNum += 1
	file.write('N' + str(lineNum) + ' (MSG,' + ToolNameList[RunningToolNameNum] + ')\n')
	lineNum += 1
	
	#Read all files in tool folder
	SizeFolder = "S:/Development/Gary/test/DieRingTranslatorTest/LiftingHole/" + Size
	list = os.listdir(SizeFolder)
	
	for i in range(0, len(list)):
	 path = os.path.join(SizeFolder, list[i])
	 if InitialRound == True:
	  cur_angleNum = 1
	 else:
	  cur_angleNum = 1
	 while cur_angleNum <= AngleNums:
	  inputFile = open(path, errors="ignore")
	  while 1:
	   inputline = inputFile.readline()
	   if not inputline:
	    break
	   file.write('N' + str(lineNum) + ' ' + inputline)
	   lineNum += 1
	  file.write('\n')
	  #file.write('Here just finish read!!!!!!!!!!!!!!!!!!!!\n')
	  #file.write('cur_angleNum is ' + str(cur_angleNum) + ', AngleNums is ' + str(AngleNums) + '\n')
	  if cur_angleNum == AngleNums:
	   inputFile.close()
	   break
	  else:
	   if PartCode == 'M':
	    file.write('N' + str(lineNum) + ' G00 B' + AngleList_M[cur_angleNum] + '\n')
	   elif PartCode == 'P':
	    file.write('N' + str(lineNum) + ' G00 B' + AngleList_P[cur_angleNum] + '\n')
	   elif PartCode == 'B':
	    file.write('N' + str(lineNum) + ' G00 B' + AngleList_B[cur_angleNum] + '\n')
	   elif PartCode == 'F':
	    file.write('N' + str(lineNum) + ' G00 B' + AngleList_F[cur_angleNum] + '\n')  
	   lineNum += 1
	   #file.write('cur_angleNum in line 298 add 1\n')
	   cur_angleNum += 1
	  inputFile.close()
	 file.write('N' + str(lineNum) + ' S100\n')
	 lineNum += 1
	 file.write('N' + str(lineNum) + ' M03\n')
	 lineNum += 1
	 file.write('N' + str(lineNum) + ' M19\n')
	 lineNum += 1
	 file.write('N' + str(lineNum) + ' G551c' + ToolList[RunningToolNum] + '\n')
	 lineNum += 1
	 file.write('N' + str(lineNum) + ' G73Z900M01\n')
	 lineNum += 1
	 RunningToolNum = HoldToolNum
	 RunningToolNameNum = HoldToolNameNum
	 if NoMoreTool == True:
	  break
	 if HoldToolNum < len(ToolList) - 1:
	  HoldToolNum += 1
	  HoldToolNameNum += 1
	 else:
	  NoMoreTool = True
	 file.write('N' + str(lineNum) + ' (MSG,Shift Tool T' + ToolList[RunningToolNum] + ')\n')
	 lineNum += 1
	 file.write('N' + str(lineNum) + ' M06\n')
	 lineNum += 1
	 file.write('N' + str(lineNum) + ' G551H' + ToolList[RunningToolNum] + '\n')
	 lineNum += 1
	 file.write('N' + str(lineNum) + ' G73Z900\n')
	 lineNum += 1
	 file.write('N' + str(lineNum) + ' G90G00X0.0Y0.0\n')
	 lineNum += 1
	 file.write('N' + str(lineNum) + ' G43Z101.6H' + ToolList[RunningToolNum] + '\n')
	 lineNum += 1
	 #file.write("Enter here!!!!!!!!!!!!")
	 cur_angleNum = 0
	 #print(cur_angleNum)
	 #print(AngleList_B)
	 if NoMoreTool:
	  file.write('N' + str(lineNum) + ' (MSG,' + ToolNameList[HoldToolNameNum] + ')\n')
	  lineNum += 1
	  if PartCode == 'M':
	   file.write('N' + str(lineNum) + ' G00 B' + AngleList_M[cur_angleNum] + '\n')
	  elif PartCode == 'P':
	   file.write('N' + str(lineNum) + ' G00 B' + AngleList_P[cur_angleNum] + '\n')
	  elif PartCode == 'B':
	   file.write('N' + str(lineNum) + ' G00 B' + AngleList_B[cur_angleNum] + '\n')
	  elif PartCode == 'F':
	   file.write('N' + str(lineNum) + ' G00 B' + AngleList_F[cur_angleNum] + '\n')
	  cur_angleNum += 1
	  lineNum += 1
	 else:
	  #file.write('Here made some mistakes!,cur_angleNum is ' + str(cur_angleNum) + '\n')
	  file.write('N' + str(lineNum) + ' T' + ToolList[HoldToolNum] + '\n')
	  lineNum += 1
	  file.write('N' + str(lineNum) + ' (MSG,' + ToolNameList[HoldToolNameNum - 1] + ')\n')
	  lineNum += 1
	  if PartCode == 'M':
	   file.write('N' + str(lineNum) + ' G00 B' + AngleList_M[cur_angleNum] + '\n')
	  elif PartCode == 'P':
	   file.write('N' + str(lineNum) + ' G00 B' + AngleList_P[cur_angleNum] + '\n')
	  elif PartCode == 'B':
	   file.write('N' + str(lineNum) + ' G00 B' + AngleList_B[cur_angleNum] + '\n')
	  elif PartCode == 'F':
	   file.write('N' + str(lineNum) + ' G00 B' + AngleList_F[cur_angleNum] + '\n')
	  #file.write('cur_angleNum in line 363 add 1\n')
	  cur_angleNum += 1
	  lineNum += 1
	  InitialRound = False
	file.write('N' + str(lineNum) + ' (End Lifting Holes #1)\n')
	file.write('%')
	file.close() 
	return

#LocateEngraving:
def LocateEngraving(LinesFile, GrooveFile, Type):
	if not os.path.exists(LinesFile):
	 print("=======================================")
	 print(LinesFile, "not exist, can't do engraving!")
	 print("=======================================")
	 return -1, -1
	if not os.path.exists(GrooveFile):
	 print("=======================================")
	 print(GrooveFile, "not exist, can't do engraving!")
	 print("=======================================")
	 return -1, -1
	
	NoGroove = False
	file = open(GrooveFile)
	while 1:				#Here we get groove information
	 line = file.readline()
	 if not line:
	  break
	 if "GRVCFF" in line:
	  pos = line.find("=", 1)
	  GrooveCenter = float(line[pos + 1: len(line) - 1])
	  if GrooveCenter == 0:
	   NoGroove = True
	 if "GRVWIDTOP" in line:
	  pos = line.find("=", 1)
	  GrooveWidth = float(line[pos + 1: len(line) - 1])
	  if GrooveWidth == 0:
	   NoGroove = True
	  else:
	   GrooveLside = GrooveCenter + GrooveWidth / 2
	   GrooveRside = GrooveCenter - GrooveWidth / 2
	 if "GRVDIAT" in line:
	  pos = line.find("=", 1)
	  GrooveZPos = float(line[pos + 1: len(line) - 1]) / 2
	  if GrooveZPos == 0:
	   NoGroove = True  
	file.close()
	
	MNDList = []
	PLTList = []
	BKRList = []
	FDRList = []
	file = open(LinesFile)
	while 1:				#Here we get lines and types
	 line = file.readline()
	 if not line:
	  break
	 if "ARC" in line:
	  continue
	 if "MNDCRV" in line:
	  cur_part = "MND"
	 if "PLTCRV" in line:
	  cur_part = "PLT"
	 if "BKRCRV" in line:
	  cur_part = "BKR"
	 if "FDRCRV" in line:
	  cur_part = "FDR"
	 if "BOLCRV" in line:
	  cur_part = "BOL"
	 if "RNGCRV" in line:
	  cur_part = "RNG"
	  
	#Get lines:
	 pos = 1
	 SpaceList = []
	 TwoPoints = []
	 if "LINE" in line:
	  while 1:
	   if line.find(" ", pos + 1) == -1:
	    break
	   pos = line.find(" ", pos + 1)
	   SpaceList.append(pos)
	  TwoPoints.append(float(line[SpaceList[0] + 1: SpaceList[1]]))
	  TwoPoints.append(float(line[SpaceList[1] + 1: SpaceList[2]]))
	  TwoPoints.append(float(line[SpaceList[2] + 1: SpaceList[3]]))
	  TwoPoints.append(float(line[SpaceList[4] + 1: SpaceList[5]]))
	  if len(SpaceList) != 7:
	   TwoPoints.append(float(line[SpaceList[6] + 1: SpaceList[7]]))
	   TwoPoints.append(float(line[SpaceList[7] + 1: len(line) - 1]))
	  else:
	   TwoPoints.append(float(line[SpaceList[5] + 1: SpaceList[6]]))
	   TwoPoints.append(float(line[SpaceList[6] + 1: len(line) - 1]))
	  if cur_part == "MND":
	   MNDList.append(TwoPoints)
	  elif cur_part == "PLT":
	   PLTList.append(TwoPoints)
	  elif cur_part == "BKR":
	   BKRList.append(TwoPoints)
	  elif cur_part == "FDR":
	   FDRList.append(TwoPoints)
	file.close()
	
	RightSide_M = -1000.0
	RightSide_P = -1000.0
	RightSide_B = -1000.0
	RightSide_F = -1000.0
	#Engraving can only do on flat line, delete other lines here
	#Then sort
	if Type == "C":
	 i = 0
	 while i < len(MNDList):
	  if MNDList[i][0] > RightSide_M:
	   RightSide_M = MNDList[i][0]
	  if MNDList[i][1] != MNDList[i][4] or MNDList[i][0] <= MNDList[i][3]:
	   MNDList.pop(i)
	   i -= 1
	  i += 1
	 MNDList = sorted(MNDList, key=lambda Z: Z[1])
	 MNDList.reverse()
	if Type == "P":
	 i = 0
	 while i < len(PLTList):
	  if PLTList[i][0] > RightSide_P:
	   RightSide_P = PLTList[i][0]
	  if PLTList[i][1] != PLTList[i][4] or PLTList[i][0] <= PLTList[i][3]:
	   PLTList.pop(i)
	   i -= 1
	  i += 1
	 PLTList = sorted(PLTList, key=lambda Z: Z[1])
	 PLTList.reverse()
	if Type == "B":
	 i = 0
	 while i < len(BKRList):
	  if BKRList[i][0] > RightSide_B:
	   RightSide_B = BKRList[i][0]
	  if BKRList[i][1] != BKRList[i][4] or BKRList[i][0] <= BKRList[i][3]:
	   BKRList.pop(i)
	   i -= 1
	  i += 1
	 BKRList = sorted(BKRList, key=lambda Z: Z[1])
	 BKRList.reverse()
	if Type == "F":
	 i = 0
	 while i < len(FDRList):
	  if BKRList[i][0] > RightSide_F:
	   RightSide_F = BKRList[i][0]
	  if FDRList[i][1] != FDRList[i][4] or FDRList[i][0] <= FDRList[i][3]:
	   FDRList.pop(i)
	   i -= 1
	  i += 1
	 FDRList = sorted(FDRList, key=lambda Z: Z[1])
	 FDRList.reverse()
	
	#Check: if distance enough for engraving with groove
	if NoGroove == False:
	 if Type == "C":
	  i = 0
	  NeedDistance = 8
	  while i < len(MNDList):
	   if i != 0:
	    NeedDistance = 17
	   if GrooveZPos == MNDList[i][1]:
	    distance1 = RightSide_M - MNDList[i][0]
	    distance2 = GrooveRside
	    if distance2 - distance1 >= NeedDistance:
	     return -MNDList[i][0], MNDList[i][1]
	    distance3 = RightSide_M - MNDList[i][3]
	    distance4 = GrooveLside
	    if distance3 - distance4 >= NeedDistance:
	     return GrooveLside - RightSide_M, MNDList[i][1]
	   else:
	    if MNDList[i][0] - MNDList[i][3] >= NeedDistance:
	     return -MNDList[i][0], MNDList[i][1]
	   i += 1
	  return -1, -1
	 if Type == "P":
	  i = 0
	  NeedDistance = 8
	  while i < len(PLTList):
	   if i != 0:
	    NeedDistance = 17
	   if GrooveZPos == PLTList[i][1]:
	    distance1 = RightSide_P - PLTList[i][3]
	    distance2 = GrooveLside
	    if distance1 - distance2 >= NeedDistance:
	     return GrooveLside - RightSide_P, PLTList[i][1]
	    distance3 = RightSide_P - PLTList[i][0]
	    distance4 = GrooveRside
	    if distance3 - distance4 >= NeedDistance:
	     return -PLTList[i][0], PLTList[i][1]
	   else:
	    if PLTList[i][0] - PLTList[i][3] >= NeedDistance:
	     return -PLTList[i][0], PLTList[i][1]
	   i += 1
	  return -1, -1
	 if Type == "B":
	  i = 0
	  NeedDistance = 8
	  while i < len(BKRList):
	   if i != 0:
	    NeedDistance = 17
	   if GrooveZPos == BKRList[i][1]:
	    distance1 = RightSide_B - BKRList[i][3]
	    distance2 = GrooveLside
	    if distance1 - distance2 >= NeedDistance:
	     return GrooveLside - RightSide_B, BKRList[i][1]
	    distance3 = RightSide_B - BKRList[i][0]
	    distance4 = GrooveRside
	    if distance3 - distance4 >= NeedDistance:
	     return -BKRList[i][0], BKRList[i][1]
	   else:
	    if BKRList[i][0] - BKRList[i][3] >= NeedDistance:
	     return -BKRList[i][0], BKRList[i][1]
	   i += 1
	  return -1, -1
	 if Type == "F":
	  i = 0
	  NeedDistance = 8
	  while i < len(PLTList):
	   if i != 0:
	    NeedDistance = 17
	   if GrooveZPos == FDRList[i][1]:
	    distance1 = RightSide_F - FDRList[i][3]
	    distance2 = GrooveLside
	    if distance1 - distance2 >= NeedDistance:
	     return GrooveLside - RightSide_F, FDRList[i][1]
	    distance3 = RightSide_F - FDRList[i][0]
	    distance4 = GrooveRside
	    if distance3 - distance4 >= NeedDistance:
	     return -FDRList[i][0], FDRList[i][1]
	   else:
	    if FDRList[i][0] - FDRList[i][3] >= NeedDistance:
	     return -FDRList[i][0], FDRList[i][1]
	   i += 1
	  return -1, -1
	else:
	 if Type == "C":
	  i = 0
	  NeedDistance = 8
	  while i < len(MNDList):
	   if i != 0:
	    NeedDistance = 17
	   if MNDList[i][0] - MNDList[i][3] >= NeedDistance:
	    return MNDList[i][0], MNDList[i][1]
	   i += 1
	 return -1, -1
	 if Type == "P":
	  i = 0
	  NeedDistance = 8
	  while i < len(PLTList):
	   if i != 0:
	    NeedDistance = 17
	   if PLTList[i][0] - PLTList[i][3] >= NeedDistance:
	    return PLTList[i][0], PLTList[i][1]
	   i += 1
	 return -1, -1
	 if Type == "B":
	  i = 0
	  NeedDistance = 8
	  while i < len(BKRList):
	   if i != 0:
	    NeedDistance = 17
	   if BKRList[i][0] - BKRList[i][3] >= NeedDistance:
	    return BKRList[i][0], BKRList[i][1]
	   i += 1
	 return -1, -1
	 if Type == "F":
	  i = 0
	  NeedDistance = 8
	  while i < len(FDRList):
	   if i != 0:
	    NeedDistance = 17
	   if FDRList[i][0] - FDRList[i][3] >= NeedDistance:
	    return FDRList[i][0], FDRList[i][1]
	   i += 1
	 return -1, -1
	return -1, -1

#Engravingtranslator:
#input:ShopNumber
def Engravingtranslator(NewJob):
	SONum = NewJob[:6]
	PartCode = NewJob[-5:-4]
	if PartCode == "M":
	 PartCode = "C"
	DCRVPath = "S:/LDATA/ModelData/" + SONum + "DCRV.TXT"	#Liftinghole numbers and angles information
	TURNPath = "S:/LDATA/Turn/" + SONum + PartCode			#Liftinghole distance and diameter information
	if not os.path.exists(DCRVPath):
	 print("=======================================")
	 print(DCRVPath, "not exist, can't do engraving!")
	 print("=======================================")
	 return
	if not os.path.exists(TURNPath):
	 print("=======================================")
	 print(TURNPath, "not exist, can't do engraving!")
	 print("=======================================")
	 return
	
	#Xcoordinate, Ycoordinate = LocateEngraving(DCRVPath, TURNPath, PartCode)
	#print(LocateEngraving(DCRVPath, TURNPath, PartCode))
	EngFile = "S:/Development/Andy/LiftingHoleTest/Engresult/" + SONum + PartCode + ".txt"
	file = open(EngFile,"w")
	Xcoordinate, Ycoordinate = LocateEngraving(DCRVPath, TURNPath, PartCode)
	file.write(str(Xcoordinate) + ' ' + str(Ycoordinate))
	file.close()
	return


#main function
path_to_watch = "S:/Development/Andy/LiftingHoleTest"

before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
  time.sleep (3)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  removed = [f for f in before if not f in after]
  if added:
   print("Added: ", ", ".join (added))
   added = added[-1]
   LHtranslator(added)
   Engravingtranslator(added)
  if removed: print("Removed: ", ", ".join (removed))
  before = after