import pandas as pd

def clear(st):
    st.replace("\n","").replace(u'\u3000',u"").replace('\r', '')
    return st

def type_detect(st):
    if (('《'in st) and ('》' in st)):
        return 3
    elif (("大学" in st) or ("学院" in st)):
        return 1
    elif ("等奖作品" in st):
        return 2
    else:
        return -1

file = open("Raw_Data/15/raw_15.txt",encoding='utf-8')
file_text = file.readlines()
df = pd.DataFrame(columns=['Name','Prize','Uni'])
for lines in file_text:
    line = clear(lines)
    type = type_detect(line) # 1:uni;2:Prize;3:Name;-1:Undetectable(Province,Empty)
    if (type > 0):
        if (type == 1):
            uni = line
        elif (type == 2):
            pri = line
        elif (type == 3):
            df.loc[len(df.index)] = [line.replace('》','').replace('《','').replace('\n',''),pri.replace("特等奖作品","0").replace("一等奖作品","1").replace("二等奖作品","2").replace("三等奖作品","3").replace('\n',''),uni.replace('\n','')]
df.to_csv("Dataset/15.csv",index=False,encoding='utf_8_sig')