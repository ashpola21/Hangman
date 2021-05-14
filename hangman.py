Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from sys import argvdef debug_print(s):
if len(argv) > 4:
print(s)
def dash(word,letters):
 """
 Given a word and list of letters, returns the word with "_", except the mentioned in
the list
 """
 dash_letters=list(set(word)-set(letters))
 for i in dash_letters:
   word=word.replace(i,"_")
 return(word)
def words_list(filename):
 """
 Given a file name, returns the words in the file as a list
 """
 words = []
 with open(filename) as fin:
   for line in fin:
     words.append(line.strip())
 return words
def word(lists,n):
"""
 Given a list of word and a number, returns a list containing words with length equal
to the give number
 """
 word_list=[]
 for q in lists:
   if len(q)==n:
     word_list.append(q)
 return word_list
def dic(letters,words):
 """
 Given a list of words and a list of letters, returns a dictionary with dashed word
as the key and its corresponding list of words as list
 """
 word_dict={}
 for i in words:
   dash_word=dash(i,letters)
   if dash_word in word_dict:
     word_dict[dash_word].append(i)
   else:
      word_dict[dash_word]=[]
     word_dict[dash_word].append(i)
 return(word_dict)
def hangman(word,chances,miss,word_dash):
 """
 Given a word, number of chances, missed letters,word with dashes runs the  phase 1
hagman game.
 """
 count=chances
 while (count<=chances):
   if word_dash==word:
    print(f"You guessed the word: {word}")
    break;
   debug_print(f"1 words left.")
   print(word_dash)
   print(f"missed letters: {miss.strip()} ({count} chances left)")
   guess=(input("Enter your guess: ")).lower()
   if guess in word:
     same=[]
     lists=list(word)
     for g in range(len(lists)):
       if lists[g]==guess:
         same.append(g)
     dash_list=list(word_dash)
     for r in same:
       dash_list[r]=guess
     word_dash="".join(dash_list)
   if (guess not in word) :
     miss=miss+" "+guess
     count=count-1
   debug_print(f"{word_dash}:1")
   print()
   if (count==0) and (word_dash != word):
     print(f"You lost after {argv[3]} wrong guesses.")
     break;
 return
def wicked(word_list,chances):
 """
 given a list of words and number of chances, it will execute the phase 2 of hangman.
This code tries to reduce the list of words into 1 word then it would continue in the
phase 1 hangman.
 """
 x=word_list
 miss=""
 cha=chances
 
  word="_"*int(argv[2])
 letters=[]
 while (len(x)>=1):
   debug_print(f"{len(x)} words left.")
   print(word)
   print(f"missed letters: {miss.strip()} ({cha} chances left)")
   guess=(input("Enter your guess: ")).lower()
   letters.append(guess)
   word_dict= dic(letters,x)
   keys=sorted(list(word_dict.keys()),key=lambda h:
(len(word_dict[h]),h.count("_"),h))
   if (word in keys) and len(word_dict[word])==len(word_dict[keys[-1]]):
     keys.remove(word)
     keys.append(word)
   for t in keys:
     debug_print(f"{t}:{len(word_dict[t])}")
   x=word_dict[keys[-1]]
   word=keys[-1]
   if len(x)==1:
     print()
     hangman(x[0],cha,miss,word)
     break;
   if guess not in word:
     cha=cha-1
     miss=miss+" "+guess
     letters.remove(guess)
   print()
   if cha==0:
     print(f"You lost after {chances} wrong guesses.")
     break;
 return()
def run():
 """
 this function executes the hangman program and if there is 1 single word, it will
execute phase 1, if not phase2
 """
 a=words_list(argv[1])
 b=word(a,int(argv[2]))
 if len(b)==1:
   word_dashed="_"*(int(argv[2]))
   miss=""
   hangman(b[0],int(argv[3]),miss,word_dashed)
 else:
   wicked(b,int(argv[3]))
return()
 
if __name__ == '__main__':
 run()