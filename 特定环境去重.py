import json
import math
import os
import shutil
import time
while True:
    是否重命名 = input("Y：重命名，N：筛选,请输入你的指示：")
    # 要求路径
    路径 = input("输入路径:")
    # 计时
    筛选数 = 0
    # 算距离
    def 计算距离(x1, x2, y1, y2):
        """
        :param x1: 第一个json文件的x值
        :param x2: 第二个json文件的x值
        :param y1: 第一个json文件的y值
        :param y2: 第二个json文件的y值
        """
        差x = x1 - x2
        差y = y1 - y2
        距离的平方 = pow(差x, 2) + pow(差y, 2)
        距离 = math.sqrt(距离的平方)
        return 距离
    # 重命名函数
    def rename(path114514, oldname, newname):
        shutil.copyfile(fr"{path114514}\{oldname}", fr"{path114514}\{newname}")
        os.remove(fr"{path114514}\{oldname}")
    # 检查是否有为“筛选出来的文件”的文件夹
    if not os.path.exists(fr"{路径}\筛选出来的文件"):
        pass
    else:
        try:
            os.remove(fr"{路径}\筛选出来的文件")
        except:
            print("删除文件夹失败，请手动删除")
    # 算大致时间
    文件树 = os.listdir(路径)
    文件数量 = len(文件树)
    大致时间 = 0.0011064728141934 * 文件数量
    print(f"大致需要时间{大致时间}秒")
    time.sleep(3)
    # 筛选
    if 是否重命名 == "N" or 'n':
        筛选距离 = input("请输入筛选的距离(请不要输入其他字符）：")
        开始计时 = time.time()
        for i in range(0, 文件数量):
            当前文件 = 文件树[i]
            if str(文件树[i]).count(".json") == 1:
                try:
                    with open(fr"{路径}\{当前文件}", encoding="UTF-8", mode="r") as f:
                        json内容 = json.load(f)
                        坐标1 = json内容["position"]
                        x1 = 坐标1[0]
                        y1 = 坐标1[2]
                    for x in range(1, 文件数量):
                        下一个文件 = 文件树[x]
                        try:
                            with open(fr"{路径}\{下一个文件}", encoding="UTF-8", mode="r") as f:
                                json内容 = json.load(f)
                                坐标2 = json内容["position"]
                                x2 = 坐标2[0]
                                y2 = 坐标2[2]
                            if 计算距离(x1, x2, y1, y2) <= float(筛选距离):
                                if not os.path.exists(fr"{路径}\筛选出来的文件"):
                                    os.mkdir(fr"{路径}\筛选出来的文件")
                                    shutil.copyfile(fr"{路径}\{下一个文件}", fr"{路径}\筛选出来的文件\{下一个文件}")
                                    os.remove(fr"{路径}\{下一个文件}")
                                    print(fr"筛选出{下一个文件}距离:[{int(计算距离(x1, x2, y1, y2))}M]")
                                    筛选数 += 1
                                else:
                                    shutil.copyfile(fr"{路径}\{下一个文件}", fr"{路径}\筛选出来的文件\{下一个文件}")
                                    os.remove(fr"{路径}\{下一个文件}")
                                    print(fr"筛选出{下一个文件}距离:[{int(计算距离(x1, x2, y1, y2))}M]")
                                    筛选数 += 1
                        finally:
                            pass
                except:
                    pass
            else:
                print("不要把不是json放进当前目录（")
                break
        print(f"筛选出{筛选数}个文件")
    # 重命名
    if 是否重命名 == "Y" or 'y':
        文件名 = input("输入要替换的名称:")
        开始计时 = time.time()
        遍历文件 = os.walk(路径)
        for i in range(0, 文件数量):
            当前文件 = 文件树[i]
            if str(文件树[i]).count(".json") == 1:
                try:
                    with open(fr"{路径}\{当前文件}", encoding="UTF-8", mode="r") as f:
                        try:
                            json内容 = json.load(f)
                        except:
                            print(fr"疑似损坏json文件：{当前文件}")
                        json内容处理过 = str(json内容).replace("'", '"')
                        name = json内容["name"]
                    with open(fr"{路径}\{当前文件}", encoding="UTF-8", mode="w") as f:
                        f.write(json内容处理过.replace(f'"name": "{name}"', f'"name": "{文件名}{i + 1}"'))
                    with open(fr"{路径}\{当前文件}", encoding="UTF-8", mode="r") as f:
                        json内容 = json.load(f)
                        json内容处理过 = str(json内容).replace("'", '"')
                        name = json内容["name"]
                    shutil.copyfile(fr"{路径}\{当前文件}",fr"{路径}\{文件名}{i+1}.json")
                    os.remove(fr"{路径}\{当前文件}")
                except:
                    pass
            else:
                print("不要把不是json放进当前目录（")
                break
    结束计时 = time.time()
    try:
        print(f"耗时：{结束计时 - 开始计时}秒")
    except:
        print("你好好想想你选对了吗（")
    time.sleep(3)
