import voter

d = input("Enter your id :")
b = False
propositionA = input("Enter you are in favor of PropositionA(True/False) :")
if propositionA == "True":
      b = True
type = input("Enter I-Independent, R-Republiocan, D-Democrat :")
if type == "I":
   a = Voter("firstname1","lastname1",id,b)
   print(a)
if type == "D":
   b = False
   c = False
   candidateB = input("Enter you are in favor of candidateB(True/False) :")
   if candidateB == "True":
      b = True
   candidateC = input("Enter you are in favor of candidateC(True/False) :")
   if candidateC == "True":
      b = True
  
   while b is True and c is True:
       print("You can not vote for both the candidates.Please change your inputs")
       candidateB = bool(input("Enter you are in favor of candidateB(True/False) :"))
       candidateC = bool(input("Enter you are in favor of candidateC(True/False) :"))
      
   a = Democrat("firstname1","lastname1",id,propositionA,b,c)
   print(a)
if type == "R":
   candidateC = input("Enter you are in favor of candidateD(True/False) :")
   b = False
   if candidateD == "True":
      b = True
   a = Republican("firstname1","lastname1",id,propositionA,b)
   print(a)
