import streamlit as st
import base64

def bar_bg(img):
    last = 'png'
    st.markdown(
        f"""
        <style>
        [data-testid='stSidebar'] > div:first-child {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

def page_bg(img):
    last = 'png'
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )
bar_bg('bj2.png')
page_bg('bj1.jpg')
bar_list = ['我的简介', '我的音乐', '聊天区', '留言区','留言聊天区发送后未显示点这里','作者荣誉','打赏作者','词典','《三体》人物介绍','阅读区']
page = st.sidebar.radio('沣沣的网站', bar_list)

def page_1():
    st.image('logo.png')
    st.write('沣沣的网站 ')
    st.write('作者信息')
    st.write('现就读于深圳市光明区南科大凤凰')
    st.write('光明区小院士，明日科创之星，nct scratch3级，python1级 详细可到作者荣誉一栏')
    st.write('爱看三体')
    kw = 114514
    kw1 = 777888
    n_keyword = st.text_input('密码')
    with open('gg.txt', 'r', encoding='utf-8') as f:
        gg = f.read()
    with open('gly.txt', 'r', encoding='utf-8') as f:
        gg1 = f.read()
    if n_keyword != '':
        if int(n_keyword) == kw:
            k = st.text_area('公告牌')
            with open('gg.txt', 'w', encoding='utf-8') as f:
                f.write(k)
        elif int(n_keyword) == kw1:
            k1 = st.text_area('管理员公告牌')
            with open('gly.txt', 'w', encoding='utf-8') as f:
                f.write(k1)
    st.code('公告牌'+'\n'+gg)
    st.code('管理员公告牌'+'\n'+gg1)
    
def song(a):

    st.write(a[:-4])
    with open(a, 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='a', start_time=0)

def page_2():

    song_list = ['暮色回响_吉星出租.mp3','年轮央视2015全球中文音乐榜上榜_汪苏泷.mp3','蒲公英的约定_周杰伦.mp3','青花瓷_周杰伦.mp3','晴天_周杰伦.mp3',
                '如果爱忘了_汪苏泷单依纯.mp3','心如止水_IcePaper.mp3','夜航星NightVoyager_不才三体宇宙.mp3','盗墓笔记十年人间.mp3','JarOfLove_曲婉婷.mp3',
                '指纹_杜宣达.mp3','追梦赤子心_GALA.mp3','最后一页_江语晨.mp3','黑暗森林.mp3','精卫_30年前50年后.mp3','兰亭序_周杰伦.mp3','虚拟_陈粒.mp3']
    go = st.selectbox('选择想要听的歌',song_list)
    song(go)
    
def page_3():
    st.image('logo.png')
    st.write('聊天区')
    with open('leave_messages-副本.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        st.write(i[1],':',i[2])
    with open('zh.txt', 'r', encoding='utf-8') as f:
        zh_list = f.read().split('\n')
        for i in range(len(zh_list)):
            zh_list[i] = zh_list[i].split('#')
        zh_dict={}
        for i in  zh_list:
            zh_dict[i[0]] = i[1]
        name = st.text_input('我是谁')
        kw = st.text_input('密码')
        
        if name != '' and kw !="":
            if name in zh_dict: 
                if kw == zh_dict[name]:
                    new_message = st.text_input('想要说的话……')
                    if new_message != '':
                        if st.button('发送'):
                            messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
    
                            with open('leave_messages-副本.txt', 'w', encoding='utf-8') as t:
                                message = ''
                                for i in messages_list:
                                    message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
                                message = message[:-1]
                                t.write(message)
                else:
                    st.write("密码错误") 
            else:
                st.write('请检查是否输入正确或是否注册')
    if st.checkbox('注册'):
        zczh = st.text_input('注册账号')
        zcmm = st.text_input('账号密码')
        if zcmm != '' and zczh != '':
            if '#' not in zcmm and '#' not in zczh:
                # zh_list.append(zczh+'#'+zcmm+"\n")
                # zh_list = zh_list[:-1]
                
                with open("zh.txt","a",encoding="utf-8") as f:
                    f.write('\n'+zczh+'#'+zcmm)
                st.write("成功")
            else:
                st.write('账号密码中不允许出现违规字符！')
                        

   
def page_4():
    st.image('logo.png')
    st.write('给沣沣留言')
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        st.write(i[1],':',i[2])
    name = st.text_input('我是谁')
    
    if name == '作者':
        kw = st.text_input('密码')
        kwn = '182507'
        if kw == kwn:
            new_message = st.text_input('想要说的话……')
    elif name == '茗茗管理员':
        kw1 = st.text_input('密码')
        kwn1 = '777888'
        if kw1 == kwn1:
            new_message = st.text_input('想要说的话……')
    else:
        new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])

        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
    
def page_5():
    kw = 182507
    n_keyword = st.text_input('密码')
    if n_keyword != '':
        if int(n_keyword) == kw:
            for i in range(20):
                st.image(str(i+1)+'.jpg')
def page_6():
    st.write('打赏一下吧')
    st.image('fkm.jpg')
def page_7():
    with open('words_space.txt','r',encoding='utf-8') as f:
        wl = f.read().split('\n')
    for i in range(len(wl)):
        wl[i] = wl[i].split('#')
    wd = {}
    for i in wl:
        wd[i[1]] = [int(i[0]),i[2]]
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    w = st.text_input('输入查询的单词')
    
    if w in wd:
        st.write(wd[w])
        n =  wd[w][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        st.write('共查询',times_dict[n],'次')
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k,v in times_dict.items():
                message = str(k) + '#' + str(v) + '\n'
                
            message = message[:-1]
            f.write(message)
                
        if w == 'code':
            st.code('''
                    #彩蛋
                    print('我最爱编程了！！！')
                    ''')
            
    else:
        st.write('您查询的单词不存在！')
def page_9():
    books = ['st.txt','三体1地球往事1.txt','三体2黑暗森林.txt','三体3死神永生.txt','球状闪电.txt','超新星纪元.txt']
    with open('st.txt','r',encoding='utf-8') as f:
        tb = f.read()
    st.code('''
            #名场面：罗辑对三体人谈判
            ''')
    st.image('lg.jpg')
    st.write(tb)
def page_8():
    books = ['st.txt','三体1地球往事1.txt','三体2黑暗森林.txt','三体3死神永生.txt','球状闪电.txt','超新星纪元.txt']
    go = st.selectbox('选择想要看的书',books)
    with open(go,'r',encoding='utf-8') as f:
        tb1 = f.read()
    st.write(tb1)    
if page == '我的简介':
    page_1()
elif page == '我的音乐':
    page_2()
elif page == '聊天区':
    page_3()
elif page == '留言区':
    page_4()
elif page == '作者荣誉':
    page_5()
elif page == '打赏作者':
    page_6()
elif page == '词典':
    page_7()
elif page == '阅读区':
    page_8()
elif page == '《三体》人物介绍':
    page_9()
         

