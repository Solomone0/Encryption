import os

os.system("clear")

from termcolor import *

p=("""_;~)                  (~;_

(   |                  |   )

 ~', ',    ,''~'',   ,' ,'~

     ', ','       ',' ,'

       ',: {'} {'} :,'

         ;   /^\   ;

          ~\  ~  /~

        ,' ,~~~~~, ',

      ,' ,' ;~~~; ', ',

    ,' ,'           ', ',

  (~  ;               ;  ~)

   -;_)               (_;-""")

print(colored(p,"red"))

print("  ")

print("  ")

print(colored("1= Encryption \n2= Decryption\n{Out of loop {1}=0}\n{Out of loop {2}= done } \n{Out of loop {3}=0}","green"))

print("  ")

print("  ")
a44=int(input(colored("Enter Your Encryption or Decryption >! ","yellow")))


while True: 
	if a44==0:

		break

	if a44==1:

		while True:

			if a44==1:

				stri=input(colored("Enter Your String >! ",'cyan'))

				if stri=='done':

					break

			p2=''

			for i in stri:

					if i==' ':

						p=11000011

						p2=p2+str(p)

					elif i=='W'or i=='w':

						p=10010100

						p2=p2+str(p)

					elif i=='E'or i=='e':

						p=10010001

						p2=p2+str(p)

					elif i=='R'or i=='r':

						p=10010000

						p2=p2+str(p)

					elif i=='T'or i=='t':

						p=10001101

						p2=p2+str(p)

					elif i=='Y'or i=='y':

						p=10001100

						p2=p2+str(p)

					elif i=='U'or i== 'u':

						p=10001011

						p2=p2+str(p)

					elif i=='I'or i=='i':

						p=101010

						p2=p2+str(p)

					elif i=='O'or i=='o':

						p=10000101

						p2=p2+str(p)

					elif i=='P'or i=='p':

						p=10000100

						p2=p2+str(p)

					elif i=='A'or i=='a':

						p=10000011

						p2=p2+str(p)

					elif i=='S'or i=='s':

						p=10000001

						p2=p2+str(p)

					elif i=='D'or i=='d':

						p=10000110

						p2=p2+str(p)

					elif i=='F'or i=='f':

						p=10000111

						p2=p2+str(p)

					elif i=='G'or i=='g':

						p=10011010

						p2=p2+str(p)

					elif i=='H'or i=='h':

						p=10001000

						p2=p2+str(p)

					elif i=='J'or i=='j':

						p=10001001

						p2=p2+str(p)

					elif i=='K' or i=='k':

						p=10001110

						p2=p2+str(p)

					elif i=='L'or i=='l':

						p=10011000

						p2=p2+str(p)

					elif i=='Z'or i=='z':

						p=10001112

						p2=p2+str(p)

					elif i=='X'or i=='x':

						p=10010010

						p2=p2+str(p)

					elif i=='C'or i=='c':

						p=10000010

						p2=p2+str(p)

					elif i=='V'or i=='v':

						p=10010011

						p2=p2+str(p)

					elif i=='B'or i=='b':

						p=10010110

						p2=p2+str(p)

					elif i=='N'or i=='n':

						p=10010111

						p2=p2+str(p)

					elif i=='M'or i=='m':

						p=10011001

						p2=p2+str(p)

					elif i=='Q' or i=='q':

						p=10010101

						p2=p2+str(p)	

					elif i== 'ج' :

						p=10011011

						p2=p2+str(p)	

					elif i==  'ح':

						p=10011100

						p2=p2+str(p)	

					elif i=='خ' :

						p=10011101

						p2=p2+str(p)	

					elif i== 'ه' :

						p=10011110

						p2=p2+str(p)	

					elif i== 'ع':

						p=10011111

						p2=p2+str(p)	

					elif i==  "غ":

						p=10100101

						p2=p2+str(p)	

					elif i== "ف" :

						p=10100110

						p2=p2+str(p)	

					elif i== "ق":

						p=10100111

						p2=p2+str(p)	

					elif i== "ث" :

						p=10101000

						p2=p2+str(p)	

					elif i== "ص" :

						p=10101001

						p2=p2+str(p)	

					elif i== "ض" :

						p=10101111

						p2=p2+str(p)	

					elif i== "ط" :

						p=10101110

						p2=p2+str(p)	

					elif i== "ك" :

						p=10101101

						p2=p2+str(p)	

					elif i== "م" :

						p=10101100

						p2=p2+str(p)	

					elif i== "ن" :

						p=10101011

						p2=p2+str(p)	

					elif i== "ت" :

						p=10101010

						p2=p2+str(p)

					elif i== "ا"or i=='أ'or i=='آ'or i== 'إ'or i=='ٱ':

						p=10100100

						p2=p2+str(p)	

					elif i== "ل" :

						p=10100011

						p2=p2+str(p)	

					elif i== "ب" :

						p=10100010

						p2=p2+str(p)	

					elif i== "ي" :

						p=10100001

						p2=p2+str(p)

					elif i== "س" :

						p=10100000

						p2=p2+str(p)	

					elif i== "ش" :

						p=10110101

						p2=p2+str(p)	

					elif i== "د" :

						p=10110110

						p2=p2+str(p)	

					elif i== "ظ" :

						p=10110111

						p2=p2+str(p)

					elif i== "ز" :

						p=10111000

						p2=p2+str(p)	

					elif i== "و" :

						p=10111001

						p2=p2+str(p)	

					elif i== "ة" :

						p=10111101

						p2=p2+str(p)	

					elif i== "ى" :

						p=10111110

						p2=p2+str(p)

					elif i== "ر" :

						p=10111111

						p2=p2+str(p)	

					elif i== "ؤ" :

						p=10111100

						p2=p2+str(p)	

					elif i== "ء" :

						p=10111011

						p2=p2+str(p)	

					elif i== "ذ" :

						p=10111010

						p2=p2+str(p)

					elif i== "1" :

						p=10110100

						p2=p2+str(p)	

					elif i== "2" :

						p=10110011

						p2=p2+str(p)	

					elif i== "3" :

						p=10110010

						p2=p2+str(p)	

					elif i== "4" :

						p=10110001

						p2=p2+str(p)

					elif i== "5" :

						p=10110000

						p2=p2+str(p)	

					elif i== "6" :

						p=11000100

						p2=p2+str(p)	

					elif i== "7" :

						p=11000101

						p2=p2+str(p)	

					elif i== "8" :

						p=11000010

						p2=p2+str(p)

					elif i== "9" :

						p=11000001

						p2=p2+str(p)	

					elif i== "0" :

						p=11000000

						p2=p2+str(p)	

			print(colored(p2,'red'))

#===============

	elif a44==2:

			while True:

						num=int(input(colored("Enter Your Number >! ",'blue')))

						p3=str(num)

						p1=len(p3)

						p2=''

						if num==0:

							break

						while p1!=0:

							i=num%100000000

							num=num//100000000

							if i==11000011:

								p=' '

								p2=p2+str(p)

								p1-=8

							elif i==10010100:

								p='w'

								p2=p2+str(p)

								p1-=8

							elif i==10010001:

								p='e'

								p2=p2+str(p)

								p1-=8

							elif i==10010000:

								p='r'

								p2=p2+str(p)

								p1-=8

							elif i==10001101:

								p='t'

								p2=p2+str(p)

								p1-=8

							elif i==10001100:

								p='y'

								p2=p2+str(p)

								p1-=8

							elif i==10001011:

								p='u'

								p2=p2+str(p)

								p1-=8

							elif i==10001010:

								p='i'

								p2=p2+str(p)

								p1-=8

							elif i==10000101:

								p='o'

								p2=p2+str(p)

								p1-=8

							elif i==10000100:

								p='p'

								p2=p2+str(p)

								p1-=8

							elif i==10000011:

								p='a'

								p2=p2+str(p)

								p1-=8

							elif i==10000001:

								p='s'

								p2=p2+str(p)

								p1-=8

							elif i==10000110:

								p='d'

								p2=p2+str(p)

								p1-=8

							elif i==10000111:

								p='f'

								p2=p2+str(p)

								p1-=8	

							elif i==10011010:

								p='g'

								p2=p2+str(p)

								p1-=8

							elif i==10001000:

								p='h'

								p2=p2+str(p)

								p1-=8

							elif i==10001001:

								p='j'

								p2=p2+str(p)

								p1-=8

							elif i==10001110:

								p='k'

								p2=p2+str(p)

								p1-=8

							elif i==10011000:

								p='l'

								p2=p2+str(p)

								p1-=8	

							elif i==10001112:

								p='z'

								p2=p2+str(p)

								p1-=8

							elif i==10010010:

								p='x'

								p2=p2+str(p)

								p1-=8

							elif i==10000010:

								p='c'

								p2=p2+str(p)

								p1-=8

							elif i==10010011:

								p='v'

								p2=p2+str(p)

								p1-=8

							elif i==10010110:

								p='b'

								p2=p2+str(p)

								p1-=8

							elif i==10010111:

								p='n'

								p2=p2+str(p)

								p1-=8

							elif i==10011001:

								p='m'

								p2=p2+str(p)

								p1-=8

							elif i==10010101:

								p='q'

								p2=p2+str(p)

								p1-=8

							elif i== 10011011:

							    p=" ج"

							    p2=p2+str(p)

							    p1-=8

							elif i== 10011100:

							    p="ح "

							    p2=p2+str(p)

							    p1-=8

							elif i==10011100 :

							    p="خ "

							    p2=p2+str(p)

							    p1-=8

							elif i== 10011110:

							    p="ه "

							    p2=p2+str(p)

							    p1-=8

							elif i== 10011111:

							    p="ع "

							    p2=p2+str(p)

							    p1-=8

							elif i== 10100101:

							    p="غ "

							    p2=p2+str(p)

							    p1-=8

							elif i== 10100110:

							    p="ف "

							    p2=p2+str(p)

							    p1-=8

							elif i==10100111 :

							    p="ق "

							    p2=p2+str(p)

							    p1-=8

							elif i==10101000 :

							    p=" ث"

							    p2=p2+str(p)

							    p1-=8

							elif i== 10101001:

							    p="ص "

							    p2=p2+str(p)

							    p1-=8

							elif i== 10101111:

							    p="ض "

							    p2=p2+str(p)

							    p1-=8

							elif i==10101110 :

							    p=" ط"

							    p2=p2+str(p)

							    p1-=8

							elif i== 10101101:

							    p="ك "

							    p2=p2+str(p)

							    p1-=8

							elif i==10101100 :

							    p="م "

							    p2=p2+str(p)

							    p1-=8

							elif i== 10101011:

							    p="ن "

							    p2=p2+str(p)

							    p1-=8

							elif i== 10101010:

							    p="ت "

							    p2=p2+str(p)

							    p1-=8

							elif i== 10100100:

							    p="ا "

							    p2=p2+str(p)

							    p1-=8

							elif i== 10100011:

							    p="ل "

							    p2=p2+str(p)

							    p1-=8

							elif i== 10100010:

							    p="ب "

							    p2=p2+str(p)

							    p1-=8

							elif i== 10100001:

							    p="ي "

							    p2=p2+str(p)

							    p1-=8

							elif i== 10100000:

							    p="س "

							    p2=p2+str(p)

							    p1-=8

							elif i==10110101 :

							    p="ش "

							    p2=p2+str(p)

							    p1-=8

							elif i== 10110110:

							    p="د "

							    p2=p2+str(p)

							    p1-=8

							elif i== 10110111:

							    p="ظ "

							    p2=p2+str(p)

							    p1-=8

							elif i==10111000 :

							    p="ز "

							    p2=p2+str(p)

							    p1-=8

							elif i== 10111001:

							    p="و "

							    p2=p2+str(p)

							    p1-=8

							elif i== 10111101:

							    p="ة "

							    p2=p2+str(p)

							    p1-=8

							elif i==10111110 :

							    p="ى "

							    p2=p2+str(p)

							    p1-=8

							elif i==10111111 :

							    p="ر "

							    p2=p2+str(p)

							    p1-=8

							elif i==10111100 :

							    p="ؤ "

							    p2=p2+str(p)

							    p1-=8

							elif i==10111011 :

							    p=" ء"

							    p2=p2+str(p)

							    p1-=8

							elif i== 10111010:

							    p="ذ "

							    p2=p2+str(p)

							    p1-=8

							elif i== 10110100:

							    p=" 1"

							    p2=p2+str(p)

							    p1-=8

							elif i== 10110011:

							    p="2 "

							    p2=p2+str(p)

							    p1-=8

							elif i== 10110010:

							    p=" 3"

							    p2=p2+str(p)

							    p1-=8

							elif i== 10110001:

							    p="4 "

							    p2=p2+str(p)

							    p1-=8

							elif i==10110000 :

							    p="5 "

							    p2=p2+str(p)

							    p1-=8

							elif i== 11000100:

							    p="6 "

							    p2=p2+str(p)

							    p1-=8

							elif i== 11000101:

							    p=" 7"

							    p2=p2+str(p)

							    p1-=8

							elif i== 11000010:

							    p="8 "

							    p2=p2+str(p)

							    p1-=8

							elif i==11000001 :

							    p="9 "

							    p2=p2+str(p)

							    p1-=8

							elif i== 11000000:

							    p="0 "

							    p2=p2+str(p)

							    p1-=8

							

						m=p2[::-1]

						print(colored(m,'cyan'))

						

						
