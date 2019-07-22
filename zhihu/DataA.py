from zhihu.PutMongo import putMongo

import pyhanlp as ph
from collections import Counter
import matplotlib.pyplot as plt

from pylab import mpl 
mpl.rcParams['font.sans-serif'] = ['SimHei']

def getContents():
    '''
    从mongoDB中找到回答正文内容
    '''
    mongo = putMongo()
    contents = mongo.findData(items = ['content'])
    return contents

def chooseName(contents):
    segment = ph.HanLP.newSegment().enableNameRecognize(True)
    i = 0
    actors = []
    while i >= 0:
        try:
            content = contents[i]
            items = segment.seg(content['content'])
            names = []
            for j in range(items.size()):
                if items.get(j).nature.toString() == 'nr':
                    names.append(items.get(j).word)

            if names != []:        
                counter_names = Counter(names)
                actors.append(counter_names.most_common(1)[0][0])

            if i % 50 == 0:
                print('{}ok！'.format(i))

        except IndexError as e:
            print('已完成')
            break
        i += 1
    return actors

if __name__ == "__main__":
    contents = getContents()
    actors = chooseName(contents)
    actors_conuter = Counter(actors)
    max_actor = actors_conuter.most_common(10)
    names = [i[0] for i in max_actor]
    nums = [i[1] for i in max_actor]
    plt.bar(names, nums)
    plt.show()

    


