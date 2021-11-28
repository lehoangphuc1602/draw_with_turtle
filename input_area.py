class Input():

    #選択の範囲
    def choose():

        num_side = int(input("どんな図形を描きたいですか？番号を選んでください。\n0: 円\n1: 三角形\n2: 正方形\n3: 長方形\n 番号： "))
        return num_side
    
    #角度の値を入力
    def inp_angle():

        angle = input("角度の値を入力してください：").split()
        return angle
    
    
    #サイド(辺)の値を入力
    def inp_side():

        side = input("辺の値を入力してください：").split()
        len_side = len( side )
        
        #len_sideのところで一つ値を代入して、円の半径として代入する
        if len_side == 1:

            from math import pi

            p_cir = float( side[0] ) * 2 * pi
            cir_area = float( side[0] ) ** 2 *pi

            #円の周囲値、面積の計算
            print("円周値は {} mです。".format( round ( p_cir , 3)))
            print("円の面積は {} ㎡です。".format( round(  cir_area , 3 )))

        #三つ以上場合、正方形また長方形の周囲値、面積の計算
        elif len_side ==3:

            def p_triangle():

                result = 0

                for i in range( len_side ):
                
                    value = float( side[i] )
                    result += value
                        #周囲値の半分
                return result

            #変数で関数を定義する、グローバル化
            global p_tri
            p_tri = p_triangle()

            #三角形の面積
            def area_triangle():

                import math

                a, b , c = float( side[0] ), float( side[1] ), float( side[2] )

                #三角形の計算公式から面積を計算する
                s =  ( p_tri / 2 ) * (( p_tri / 2 ) - a ) * (( p_tri / 2 ) - b ) * (( p_tri / 2 ) - c )
                #ルート
                total = math.sqrt( s )
                #桁捨て 
                total = round( total, 3 ) #小数点以下切り捨て

                return total

            x = area_triangle()

            print("この三角形の周囲値は {} mです".format( p_tri ))
            print("この三角形の面積は {} ㎡です。".format( x ))

        #４辺同じ場合正方形として計算する
        elif len_side == 4:

            a, b , c, d = float( side[0] ), float( side[1] ), float( side[2] ), float( side[3] )

            if a == c == b == d:

                print("これは正方形です。")
                p_squa = a + b + c + d

                def square():

                    total = a * c
                    return total

                print("正方形の周囲値は {} mです".format( p_squa ))
                print("正方形の面積は {} ㎡です".format( square() ))
            
            #長方形の一辺目と三辺目同じ　!=　二辺目と四辺目同じ
            elif a == c != b == d:

                print("これは長方形です。")
                p_rec = a + b + c + d

                def rectangal():

                    total = a * b
                    return total

                print("長方形の周囲値は {} mです".format( p_rec ))
                print("長方形の面積は {} ㎡です".format( rectangal() ))

        return side