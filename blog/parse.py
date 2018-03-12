def parse_message(xml):
    tousername = xml.find('ToUserName').text
    fromusername = xml.find('FromUserName').text
    createtime = xml.find('CreateTime').text
    msgtype = xml.find('MsgType').text
    content = xml.find('Content').text
    msgid = xml.find('MsgId').text
    ToUserName=fromusername
    FromUserName=tousername
    CreateTime=createtime
    MsgType=msgtype
    Content=content
    MsgId=fromusername
    dic ={'ToUserName':ToUserName,'FromUserName':FromUserName,'CreateTime':CreateTime,'MsgType':MsgType,'MsgId':MsgId,'Content':Content}
    return dic

def parse_image(xml):
    tousername = xml.find('ToUserName').text
    fromusername = xml.find('FromUserName').text
    createtime = xml.find('CreateTime').text
    msgtype = xml.find('MsgType').text
    picurl = xml.find('PicUrl').text
    mediaid = xml.find('MediaId').text
    msgid = xml.find('MsgId').text
    ToUserName=fromusername
    FromUserName=tousername
    CreateTime=createtime
    MsgType=msgtype
    PicUrl=picurl
    MediaId=mediaid
    dic ={'ToUserName':ToUserName,'FromUserName':FromUserName,'CreateTime':CreateTime,'MsgType':MsgType,'PicUrl':PicUrl,'MediaId':MediaId}
    return dic
def parse_link(xml):
    tousername = xml.find('ToUserName').text
    fromusername = xml.find('FromUserName').text
    createtime = xml.find('CreateTime').text
    msgtype = xml.find('MsgType').text
    title = xml.find('PicUrl').text
    mediaid = xml.find('MediaId').text
    msgid = xml.find('MsgId').text
    ToUserName=fromusername
    FromUserName=tousername
    CreateTime=createtime
    MsgType=msgtype
    PicUrl=picurl
    MediaId=mediaid
    dic ={'ToUserName':ToUserName,'FromUserName':FromUserName,'CreateTime':CreateTime,'MsgType':MsgType,'PicUrl':PicUrl,'MediaId':MediaId}
    return dic

def parse_voice(xml):
    tousername = xml.find('ToUserName').text
    fromusername = xml.find('FromUserName').text
    createtime = xml.find('CreateTime').text
    msgtype = xml.find('MsgType').text
    mediaid = xml.find('MediaId').text
    aformat = xml.find('Format').text
    msgid = xml.find('MsgId').text
    ToUserName=fromusername
    FromUserName=tousername
    CreateTime=createtime
    MsgType=msgtype
    Format=aformat
    MediaId=mediaid
    dic ={'ToUserName':ToUserName,'FromUserName':FromUserName,'CreateTime':CreateTime,'MsgType':MsgType,'Format':Format,'MediaId':MediaId}
    return dic

