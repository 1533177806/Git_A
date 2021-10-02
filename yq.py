Pro_1=['浙江省\n']
Pro_2=['江西省\n']
Pro_3=['广东省\n']
Pro_4=['江西省\n']
Pro_5=['湖南省\n']
Pro_6=['安徽省\n']
Pro_7=['陕西省\n']
Pro_8=['安徽省\n']
Pro_9=['贵州省\n']
#定义不同省的变量
out_file=[]
def input_file(out_file):
    filename_out='yq_out.txt'
    fileopen=open(filename_out,"w")#写
    fileopen.writelines(out_file)
    fileopen.close()
#打开文件
def Sifting(filename):
    file=open(filename,"r")#只读
    for eachline in file.readlines():
        prlist=eachline.split('\t',1) #将格式为：省  市  数字的每一行分为两段“省” “市  数字”
        if prlist[0] =='浙江省' :
            if prlist[1] == '待明确地区	0':
                continue                   #筛选掉待明确地区
            else:
                global Pro_1
                Pro_1.append(prlist[1])    #将非待明确地区加入list
        if prlist[0] =='江西省' :
            global Pro_2
            Pro_2.append(prlist[1])
        if prlist[0] =='广东省' :
            if prlist[1] == '待明确地区	0':
                continue
            else:
                global Pro_3
                Pro_3.append(prlist[1])
        if prlist[0] =='江苏省'  :
            if prlist[1] == '待明确地区	0':
                continue
            else:
                global Pro_4
                Pro_4.append(prlist[1])
        if prlist[0] == '湖南省' and prlist[1] != '待明确地区	0':
            if prlist[1] == '待明确地区	0':
                continue
            else:
                global Pro_5
                Pro_5.append(prlist[1])
        if prlist[0] == '安徽省' and prlist[1] != '待明确地区	0':
            if prlist[1] == '待明确地区	0':
                continue
            else:
                global Pro_6
                Pro_6.append(prlist[1])
        if prlist[0] == '陕西省' and prlist[1] != '待明确地区	0':
            if prlist[1] == '待明确地区	0':
                continue
            else:
                global Pro_7
                Pro_7.append(prlist[1])
        if prlist[0] == '河南省' and prlist[1] != '待明确地区	0':
            if prlist[1] == '待明确地区	0':
                continue
            else:
                global Pro_8
                Pro_8.append(prlist[1])
        if prlist[0] == '贵州省' and prlist[1] != '待明确地区	0':
            if prlist[1] == '待明确地区	0':
                continue
            else:
                global Pro_9
                Pro_9.append(prlist[1])
    Pro_1.append('\n')
    Pro_2.append('\n')
    Pro_3.append('\n')
    Pro_4.append('\n')
    Pro_5.append('\n')
    Pro_6.append('\n')
    Pro_7.append('\n')
    Pro_8.append('\n')
    Pro_9.append('\n')
    yp_out=Pro_1+Pro_2+Pro_3+Pro_4+Pro_5+Pro_6+Pro_7+Pro_8+Pro_9
    input_file(yp_out)


if __name__ == '__main__':
    openfile="yq_in.txt"
    Sifting(openfile)
