kr = open("kr.txt", "r");
eng = open("eng.txt", "r");

f = open("../_new.json", "w")
f.write("{ \"\": {")
while True:
    kr_word = kr.readline()
    eng_word = eng.readline()

    if not kr_word or not eng_word:
        break
    f.write("\"{}\": \"{}\",".format(kr_word.strip(), eng_word.strip()))
f.write("}}")

kr.close()
eng.close()
f.close()