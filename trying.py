import os
for i in range(0, 2691):
    f = open("Congressional_App_Challenge_AI/articleBiases/article%dBias.txt" % i, 'r', encoding="utf-8")
    contents = f.read()
    f.close()
    if(contents=='-1'):
        print(contents)
        g = open("Congressional_App_Challenge_AI/articleBiases/article%dBias.txt" % i, 'w+', encoding="utf-8")
        g.write('0')
        g.close()

    