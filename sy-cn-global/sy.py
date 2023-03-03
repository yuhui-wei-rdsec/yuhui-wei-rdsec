import json

import os


# dataset_path = '/mnt/c/Users/ext_bc_rdsec_yuhuiw/Desktop/New folder/a-pipeline/yuhui-wei-rdsec/sy-cn-global/china.json'
def china_json():
    china_path = os.path.dirname(__file__)

    with open(os.path.join(china_path, 'china.json')) as cn:
        data = json.load(cn)
    china_mail = []
    for mail in data["china"]:
        china_mail.append(mail["mail"])
    return china_mail

def global_json():
    global_path = os.path.dirname(__file__)
    with open(os.path.join(global_path, 'global.json')) as gl:
        data = json.load(gl)
    global_mail = []
    for mail in data["global"]:
        global_mail.append(mail["Email"])
    return global_mail

if __name__ == '__main__':
    cns= china_json()
    gls = global_json()
    
    ret = []
    for i in cns:
        if i not in gls:
            ret.append(i)
    print(ret)
    
    
    ret1 = []
    for i in gls:
        if i not in cns:
            ret1.append(i)
    print(ret1)
    

