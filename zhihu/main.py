from zhihu.GetAnswers import getZhihuAnswers
from zhihu.PutMongo import putMongo



if __name__ == "__main__":
    
    questionID = 263570848  #问题ID
    page = 0
    col = putMongo('localhost','zhihu','actors')
    data = {'data':range(10)}
    while page  == 0:  #最大页数  
        answers = getZhihuAnswers(questionID, page)
        data = answers.getPages()
        if data != None :
            col.insertData(data, page)
        page += 1
