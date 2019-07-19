# -*- coding: utf-8 -*-

from qiniu import Auth, put_file, etag

from common import config

def upload(file_name,file_path):

    qn_auth = Auth(config.QN_Access_Key, config.QN_Secret_Key)

    # 生成上传 Token，可以指定过期时间等
    token = qn_auth.upload_token(config.QN_BUCKET_NAME, file_name, 3600)
    # 要上传文件的本地路径
    ret, info = put_file(token, file_name, file_path)

    return ret, info

