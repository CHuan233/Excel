def generate_g(g_list, text1, text2, text3):
    name = []
    report = []
    # 收集所有学生的名字
    for info in g_list:
        if info['name'] not in name:
            name.append(info['name'])
    # 生成每个学生的成绩单
    for sname in name:
        gol = ""
        for info in g_list:
            if info['name'] == sname:
                gol += str(info['course']) + ": " + str(info['grade1']) + " " + str(info['grade2']) + "（绩点）\n"
        report.append(text1 + str(sname) + text2 + gol + text3)

    return report, name

if __name__ == '__main__':
    text1 = "亲爱的"
    text2 = "同学:\n祝贺您顺利完成本学期的学习！教务处在此向您发送最新的成绩单。\n"
    text3 = """希望您能够对自己的成绩感到满意，并继续保持努力和积极的学习态度。如果您在某些科目上没有达到预期的成绩，不要灰心，\
这也是学习过程中的一部分。我们鼓励您与您的任课教师或辅导员进行交流，他们将很乐意为您解答任何疑问并提供帮助。\n\
请记住，学习是一个持续不断的过程，我们相信您有能力克服困难并取得更大的进步。\n\
再次恭喜您，祝您学习进步、事业成功！\n\
教务处
"""
    g_list = []
    g_list.append({'name': "jack", 'course': "爱课程", 'grade1': "98",'grade2': "4.0"})
    g_list.append({'name': "jack", 'course': "超星", 'grade1': "95", 'grade2': "3.0"})
    g_list.append({'name': "Tom", 'course': "智慧树", 'grade1': "81", 'grade2': "2.0"})
    g_list.append({'name': "Tom", 'course': "强国", 'grade1': "40", 'grade2': "1.0"})
    res, na = generate_g(g_list, text1, text2, text3)
    for i in na:
        print(i)
    for i in res:
        print(i)