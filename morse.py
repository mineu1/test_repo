import streamlit as st

morsea = ['`ㅊㅁ`ㅍㄴ`ㅈ', '`ㅇ`ㄹㅇ`ㅇ`ㅌㄴ', '`ㅂㄴ`ㅁㄴ`ㅅㄴ', '`ㅁ`ㅊㄴ`ㅅ`ㄲ', '`ㅁㄴ`ㅅㄴ', '`ㅈㅇ`ㅇ`ㅇㄴ', '`ㄱ`ㅇ`ㄱㄴ', '`ㄱ`ㄱㄴ', '`ㄱㅁ`ㅈ`ㅎㄴ', '`ㄱㅁ`ㅉ', '`ㄱㅁ`ㅁㄴ`ㄱㄹ', '`ㅁㄴ`ㄱㅇ`ㅎㄴ', '`ㄱㅁ`ㅅ`ㅎㄴ', '`ㄸㅇ`ㄱ`ㅁㅇ', '`ㅆ`ㄹ`ㅇ`ㅅ', '`ㅅ`ㄲ`ㄷㄹ', '`ㅇㅁ`ㅈ`ㅇ`ㅅ`ㅈ', '`ㄹㄹ`ㄹ`ㅆ`ㄹ', '`ㅇ`ㅊ`ㅅㄴ`ㄱ', '`ㅅㄴ`ㅅㄴ`ㄱ`ㄹ`ㄱ', '`ㄴㅇ`ㄴ', '`ㄷㄹ', '`ㅈㅇ']
morsaa = ['침팬지', '오랑우탄', '변민선', '미친새끼', '민선', '장애인', '그건', '그건', '김지훈', '김지훈', '김민결', '민경현', '김서현', '똥구멍', '시리어스(serious)', '새끼들', '매장당하니까 사리자', '진짜 미안한데', '그건 선기야', '이선기', '농노', '장애인새끼들', '장애']
morseb = ['우이', '너사즐', '마그네슘', '시보귬', 'mgsg', 'Mgsg', 'MGSG', 'Rasa', '안디여', 'axa', 'Axa', 'AXA']
morsab = ['워', '너도 사실 즐기고 있잖아', '매장당하니까', '사리자', '매장당하니까 사리자', '매장당하니까 사리자', '매장당하니까 사리자', '진짜 미안한데', '안돼', '임사현', '임사현', '임사현']


BASE_CODE, CHO_CODE, JUNG_CODE, MAX_CODE = 44032, 588, 28, 55203
CHO_LIST = list('ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ')
JUNG_LIST = list('ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ')
JONG_LIST = list(' ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ')

KORS = list('ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ')
ENGS = ['r', 'R', 'rt', 's', 'sw', 'sg', 'e', 'f', 'fr', 'fa', 'fq', 'ft', 'fx', 'fv', 'fg', 'a', 'q', 'qt', 't',
        'T', 'd', 'w', 'c', 'z', 'x', 'v', 'g',
        'k', 'o', 'i', 'O', 'j', 'p', 'u', 'P', 'h', 'hk', 'ho', 'hl', 'y', 'n', 'nj', 'np', 'nl', 'b', 'm', 'ml', 'l']
KOR_ENG_TABLE = dict(zip(KORS, ENGS))

def kor2eng(text):
    res = ''
    for ch in text:
        spl = split(ch)
        if spl is None:
            res += ch
        else:
            res += ''.join([v for v in spl if v != ' '])
    return res

def split(kor):
    code = ord(kor) - BASE_CODE
    if code < 0 or code > MAX_CODE - BASE_CODE:
        if kor == ' ': return None
        if kor in CHO_LIST: return kor, ' ', ' '
        if kor in JUNG_LIST: return ' ', kor, ' '
        if kor in JONG_LIST: return ' ', ' ', kor
        return None
    return CHO_LIST[code // CHO_CODE], JUNG_LIST[(code % CHO_CODE) // JUNG_CODE], JONG_LIST[(code % CHO_CODE) % JUNG_CODE]


def translate(text):
    cho = []
    x = text + '`'
    y = []

    for i in range(len(x)):
        y.append(x[i])

    chox = "`".join(y)
    x = x.replace(' ', '@')

    for i in range(len(x)):
        a = kor2eng(x[i])

        cho.append('`' + a[0])
        try:
            cho.append(a[2])
        except:
            pass

    string = ("".join(cho)).replace('`@', '@')
    result = '`' + chox.replace('` ', "**")

    for i in range(len(morsea)):
        for j in range(string.count(morsea[i])):
            loc = string.rfind(morsea[i])
            part = string[0:loc+1]
            partb = result
            strg = string
            locpartb = 0
            locstrg = 0

            for k in range(part.count("`")):
                locpartb += partb.find('`') + 1
                locstrg += strg.find('`') + 1
                partb = partb[partb.find("`") + 1:]
                strg = strg[strg.find("`") + 1:]

            locpartbb = 0
            locstrgb = 0
            for k in range(morsea[i].count("`")):
                locpartbb += partb.find("`") + 1
                locstrgb += strg.find('`') + 1
                partb = partb[partb.find("`") + 1:]
                strg = strg[strg.find('`') + 1:]

            add = ""
            if (result[locpartb + locpartbb-3:locpartb + locpartbb-1]) == "**":
                add = " "
            result = result[:locpartb] + morsaa[i] + add + result[locpartb + locpartbb-1:]
            string = string[:locstrg] + morsaa[i] + add + string[locstrg + locstrgb-1:]

    result = result.replace("**", " ")
    result = result.replace("`", "")

    for i in range(len(morseb)):
        result = result.replace(morseb[i], morsab[i])

    return result



box = st.text_input(label="번역할 텍스트를 입력하시오 :")
st.caption(translate(box))
