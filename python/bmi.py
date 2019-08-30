# -*- coding: utf-8 -*-
weight = input('体重を入力してください')
weight = float(weight)
height = input('身長を入力してください')
height = float(height)
bmi = weight/(height ** 2)
if bmi < 18.5:
    print('やせてる')
elif bmi < 25:
    print('普通')
elif bmi < 35:
    print('ちょっと太ってる')
else:
    print('だいぶ太ってる')
