import json

import os


# dataset_path = '/mnt/c/Users/ext_bc_rdsec_yuhuiw/Desktop/New folder/a-pipeline/yuhui-wei-rdsec/sy-cn-global/china.json'
def match():
    china_path = os.path.dirname(__file__)
    with open(os.path.join(china_path, 'china.json')) as cn:
        datacn = json.load(cn)
    
    global_path = os.path.dirname(__file__)
    with open(os.path.join(global_path, 'global.json')) as gl:
        datagl = json.load(gl)
    # print(datacn)
    ret = []
    for cnuser in datacn["china"]:
        flag = False
        for gluser in datagl["global"]:
            if cnuser["userPrincipalName"].split('@')[0] == gluser["Member"].split('\\')[1]:
                flag = True
        if(flag == False):
            print(cnuser["id"])
                   
                
                # ret.append(i)
            # print(gluser)
    # print(ret)
                    
                

if __name__ == '__main__':
    match()

    
    # ret = []
    # for i in cns:
    #     if i not in gls:
    #         ret.append(i)
    # print(ret)
    
    
 

