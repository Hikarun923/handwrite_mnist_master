from typing import Any, Union

import numpy as np
import scipy.misc
from keras.models import load_model
from keras import backend as K
import os
from PIL import Image




def format_data(X_train):
    img_rows, img_cols = 32, 32
    X_train = X_train.reshape(1, img_rows, img_cols, 1)
    return X_train


def convert_result(r):
    hiragana_list = ['あ', 'い', 'う', 'え', 'お',
                     'か', '平', 'が', 'き', 'ぎ', 'く', 'ぐ', 'け', 'げ', 'こ', 'ご',
                     'さ', 'ざ', 'し', 'じ', 'す', 'ず', 'せ', 'ぜ', 'そ', 'ぞ',
                     'た', 'だ', 'ち', 'ぢ', 'つ', 'づ', 'て', 'で', 'と', 'ど',
                     'な', 'に', 'ぬ', 'ね', 'の',
                     'は', 'ば', 'ぱ', 'ひ', 'び', 'ぴ', 'ふ', 'ぶ', 'ぷ', 'へ', 'べ', 'ぺ', 'ほ', 'ぼ', 'ぽ',
                     'ま', 'み', 'む', 'め', 'も',
                     'や', 'ゆ', 'よ',
                     'ら', '開', 'り', 'る', 'れ', 'ろ',
                     'わ', 'ん'
                     ]
    return hiragana_list[r]



def result(x):
    '''
    model_hiragana.h5  ひらがなm6_1
    model_hiragana_v2.h5  ひらがなclassic_neural
    model_hiragana_v3.h5　　ひらがなCNN
    '''
    np.set_printoptions(threshold=np.inf)

    K.clear_session()
    model = load_model(os.path.abspath(os.path.dirname(__file__)) + '/model_hiragana_v3.h5')
    x = np.expand_dims(x, axis=0)
    x = x[0]

    x_train = scipy.misc.imresize(x, (32, 32), mode='F')
    x_answer = format_data(x_train)
    r = np.argmax(model.predict(x_answer))
    r = convert_result(int(r))
    return r



def kuzushiji_picture(r):

    pic = Image.open("img0.png")

    r = convert_result(int(r))

    if r == 0:
        pic = Image.open("img0.png")

    if r == 1:
        pic = Image.open("img1.png")

    if r == 2:
        pic = Image.open("img2.png")

    if r == 3:
        pic = Image.open("img3.png")

    if r == 4:
        pic = Image.open("img4.png")

    if r == 5:
        pic = Image.open("img5.png")

    if r == 6:
        pic = Image.open("img6.png")

    if r == 7:
        pic = Image.open("img7.png")

    if r == 8:
        pic = Image.open("img8.png")

    if r == 9:
        pic = Image.open("img9.png")

    if r == 10:
        pic = Image.open("img10.png")

    if r == 11:
        pic = Image.open("img11.png")

    if r == 12:
        pic = Image.open("img12.png")

    if r == 13:
        pic = Image.open("img13.png")

    if r == 14:
        pic = Image.open("img14.png")

    if r == 15:
        pic = Image.open("img15.png")

    if r == 16:
        pic = Image.open("img16.png")

    if r == 17:
        pic = Image.open("img17.png")

    if r == 18:
        pic = Image.open("img18.png")

    if r == 19:
        pic = Image.open("img19.png")

    if r == 20:
        pic = Image.open("img20.png")

    if r == 21:
        pic = Image.open("img21.png")

    if r == 22:
        pic = Image.open("img22.png")

    if r == 23:
        pic = Image.open("img23.png")

    if r == 24:
        pic = Image.open("img24.png")

    if r == 25:
        pic = Image.open("img25.png")

    if r == 26:
        pic = Image.open("img26.png")

    if r == 27:
        pic = Image.open("img27.png")

    if r == 28:
        pic = Image.open("img28.png")

    if r == 29:
        pic = Image.open("img29.png")

    if r == 30:
        pic = Image.open("img30.png")

    if r == 31:
        pic = Image.open("img31.png")

    if r == 32:
        pic = Image.open("img32.png")

    if r == 33:
        pic = Image.open("img33.png")

    if r == 34:
        pic = Image.open("img34.png")

    if r == 35:
        pic = Image.open("img35.png")

    if r == 36:
        pic = Image.open("img36.png")

    if r == 37:
        pic = Image.open("img37.png")

    if r == 38:
        pic = Image.open("img38.png")

    if r == 39:
        pic = Image.open("img39.png")

    if r == 40:
        pic = Image.open("img40.png")

    if r == 41:
        pic = Image.open("img41.png")

    if r == 42:
        pic = Image.open("img42.png")

    if r == 43:
        pic = Image.open("img43.png")

    if r == 44:
        pic = Image.open("img44.png")

    if r == 45:
        pic = Image.open("img45.png")

    if r == 46:
        pic = Image.open("img46.png")

    if r == 47:
        pic = Image.open("img47.png")

    if r == 48:
        pic = Image.open("img48.png")

    if r == 49:
        pic = Image.open("img49.png")

    if r == 50:
        pic = Image.open("img50.png")

    if r == 51:
        pic = Image.open("img51.png")

    if r == 52:
        pic = Image.open("img52.png")

    if r == 53:
        pic = Image.open("img53.png")

    if r == 54:
        pic = Image.open("img54.png")

    if r == 55:
        pic = Image.open("img55.png")

    if r == 56:
        pic = Image.open("img56.png")

    if r == 57:
        pic = Image.open("img57.png")

    if r == 58:
        pic = Image.open("img58.png")

    if r == 59:
        pic = Image.open("img59.png")

    if r == 60:
        pic = Image.open("img60.png")

    if r == 61:
        pic = Image.open("img61.png")

    if r == 62:
        pic = Image.open("img62.png")

    if r == 63:
        pic = Image.open("img63.png")

    if r == 64:
        pic = Image.open("img64.png")

    if r == 65:
        pic = Image.open("img65.png")

    if r == 66:
        pic = Image.open("img66.png")

    if r == 67:
        pic = Image.open("img67.png")

    if r == 68:
        pic = Image.open("img68.png")

    if r == 69:
        pic = Image.open("img69.png")

    if r == 70:
        pic = Image.open("img70.png")

    if r == 71:
        pic = Image.open("img71.png")

    pic.show()






