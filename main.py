#繰り返し処理
import math

def conf():

        while True:

            print("もう一度やりますか？")
            n = int(input("<1:Yes／0:No>:"))

            if n == 0 or n==1:
                return n

while True:

    try:

        import input_area

        num_side = input_area.Input.choose()

                        
        if num_side >= 0 and num_side <= 3:
            #円を描き
            if num_side == 0:

                print("円の半径として一つの辺の値を代入する")
                side_lenght = input_area.Input.inp_side()

                if len(side_lenght) == 1:
                    print("描き終わるまでにしばらくお待ちください。")

                    def circal():

                        import turtle
                        from random import choice

                        cir = turtle.Turtle()
                        col = ["red","yellow","blue","green","pink","orange"]

                        cir.fillcolor( choice( col ) )
                        cir.begin_fill()
                        cir.circle( float( side_lenght[0] ))
                        cir.end_fill()

                        turtle.done()
                        turtle.TurtleScreen._RUNNING = True

                    circal()
                    
                else:
                    print("円の半径として一つだけの値を代入してください")

            else:

                #複数データを入力し、一辺ずつをリストに追加する
                side_lenght = input_area.Input.inp_side()

                #複数データを入力し、角度ずつをリストに追加する
                angle_value = input_area.Input.inp_angle()


                len_side = len( side_lenght )         #辺のリスト
                len_angle = len( angle_value )        #角度のリスト

                #三角形、正方形、長方形が合計の各角度180また360度未満場合は実行させない
                def angle():

                    result = 0

                    for i in range( len_angle ):
                        s = float( angle_value[i] )
                        result += s

                    return result

                #変数を定義する(変わらない値)
                angle_result = angle()

                # start
                def start():

                    import turtle
                    from random import choice

                    board = turtle.Turtle()

                    lst = side_lenght + angle_value     #リスト合体
                    
                    col = ["red","yellow","blue","green","pink","orange"]


                    board.fillcolor( choice(col) )#color
                    board.begin_fill()

                    for i in range(len( side_lenght)):

                        board.forward(float(lst[i]))  #辺を描く
                        #60度入力するとturtleは60度だけ回りますので三角形の60度場合は (180-60)=120度回ります。
                        board.left( 180 - float( lst [ len( side_lenght ) + int( i ) ]))

                    board.end_fill()#color

                    turtle.done()
                    turtle.TurtleScreen._RUNNING = True


                #角度の数と辺の数比較すると
                #合わない場合

                if len_side > 4 and len_angle > 4:
                    print("この図形は存在しないです")

                #合う場合
                else:
                    
                    while True:

                        #三角形
                        if num_side == 1:

                            #三角形は３辺ある
                            if len_side != 3:
                                print("入力値は三角形値ではありません")
                                break

                            else:

                                #三角形合計の各角度は180です。
                                if angle_result != 180:
                                    print("#三角形合計の各角度は180です。")
                                    break

                                else:
                                    print("描き終わるまでにしばらくお待ちください。")
                                    start()
                                    break

                        #正方形
                        elif num_side == 2:

                            #正方形は4辺がある
                            if len_side != 4:
                                print("入力値は正方形値ではありません")
                                break

                            else:

                                #正方形合計の各角度は360です。
                                if angle_result != 360:
                                    print("正方形合計の各角度は360です。")
                                    break

                                else:

                                    s_1, s_2, s_3, s_4 = side_lenght[0], side_lenght[1], side_lenght[2], side_lenght[3] #辺の値
                                    a_1, a_2, a_3, a_4 = angle_value[0], angle_value[1], angle_value[2], angle_value[3] #角度の値

                                    #４辺すべて同じ、各角度は90
                                    if s_1 == s_2 == s_3 == s_4:

                                        if float(a_1) == float(a_2) == float(a_3) == float(a_4) == 90:
                                            print("描き終わるまでにしばらくお待ちください。")
                                            print(start())
                                            break

                                        else:
                                            print("正方形の各角度は90度です。")  
                                            break

                                    print("各辺は同じ値必要です。")
                                    break
                                  
                        #長方形
                        elif num_side == 3:
                            if len_side == 4:
                                #値を定義する: side, angle in list
                                s_1, s_2, s_3, s_4 = side_lenght[0], side_lenght[1], side_lenght[2], side_lenght[3] #辺の値
                                a_1, a_2, a_3, a_4 = angle_value[0], angle_value[1], angle_value[2], angle_value[3] #角度の値
                            #長方形は4辺がある

                                
                                #1辺目and3辺目 ちがう 2辺目and4辺目、また各角度は90度
                                if s_1 == s_3 != s_2 == s_4:
                                    
                                    #各角度は90合う
                                    if float(a_1) == float(a_2) == float(a_3) == float(a_4) == 90:
                                        print("描き終わるまでにしばらくお待ちください。")
                                        start()
                                        break
                                    
                                    #各角度は90合わない
                                    else:
                                        print("正方形の各角度は90度です。")  
                                        break

                                #すべて辺が同じ場合
                                elif s_1 == s_2 == s_3 == s_4:
                                    print("これは正方形の値です。")
                                    break
                                
                                #残り場合
                                else:
                                    print("入力値は長方形値ではありません")
                                    break
                            #辺が足りない、また余る
                            else:
                                print("４つ辺は値必要です。")
                                break
                                
        else:
            print("0~3まで入力してください")
    #例外処理
    except (ValueError):
        print("整数を入力し、もしくは半角を確認してください\n認識できません。")

    finally:
        print("お疲れ様です。")
    #繰り返し処理
    if not conf():
        break

