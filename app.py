import generate
import send
import gradeTable
from flask import Flask, request
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)
CORS(app)
text1 = "亲爱的"
text2 = "同学:\n祝贺您顺利完成本学期的学习！教务处在此向您发送最新的成绩单。\n"
text3 = """希望您能够对自己的成绩感到满意，并继续保持努力和积极的学习态度。如果您在某些科目上没有达到预期的成绩，不要灰心，\
这也是学习过程中的一部分。我们鼓励您与您的任课教师或辅导员进行交流，他们将很乐意为您解答任何疑问并提供帮助。\n\
请记住，学习是一个持续不断的过程，我们相信您有能力克服困难并取得更大的进步。\n\
再次恭喜您，祝您学习进步、事业成功！\n\
教务处
"""
path = "./score.xlsx"

my_t = """亲爱的XXX同学:\
祝贺您顺利完成本学期的学习！教务处在此向您发送最新的成绩单。\n\
XXX\
希望您能够对自己的成绩感到满意，并继续保持努力和积极的学习态度。如果您在某些科目上没有达到预期的成绩，不要灰心，\
这也是学习过程中的一部分。我们鼓励您与您的任课教师或辅导员进行交流，他们将很乐意为您解答任何疑问并提供帮助。\n\
请记住，学习是一个持续不断的过程，我们相信您有能力克服困难并取得更大的进步。\n\
再次恭喜您，祝您学习进步、事业成功！\n\
教务处\n\
"""

def op_text(t):
    text1 = ""
    text2 = ""
    text3 = ""
    f = 1
    cnt = 0
    for i in range(len(t)):
        if t[i] == 'X':
            cnt += 1
            if cnt == 3:
                cnt = 0
                f += 1
            # print("i = ", i)
            # print("f = ", f)
        else:
            if f == 1:
                text1 += t[i]
            elif f == 2:
                text2 += t[i]
            else:
                text3 += t[i]
    return text1, text2, text3


@app.route('/send')
def send_mail():
    text = request.args.get('text')
    global text1, text2, text3, path
    data = gradeTable.getDataTable(path)
    report, name = generate.generate_g(data, text1, text2, text3)
    send.Send_Email(name, report)
    return jsonify("send success!")

@app.route('/modify')
def modify_tem():
    text = request.args.get('text')
    global text1, text2, text3
    text1, text2, text3 = op_text(text)
    return jsonify("modify success!")


if __name__ == '__main__':
    # app.run()
    data = gradeTable.getDataTable(path)
    x1, x2, x3 = op_text(my_t)
    # report, name = generate.generate_g(data, text1, text2, text3)
    report, name = generate.generate_g(data, x1, x2, x3)
    for i in report:
        print(i)
    print("name = ", name)
    # send.Send_Email(report, name)