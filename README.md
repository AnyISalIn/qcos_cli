# qcos_cli

> 腾讯云对象存储命令行工具

## 安装

### 源码安装

```shell
$ git clone https://github.com/AnyISalIn/qcos_cli.git

$ cd qcos_cli

$ pip install .

$ python setup.py install
```

### PyPI

```shell
$ pip install qcos_cli
```

### usage

```shell
$ qcos_cli

Type:        Pipeline
String form: <qcos_cli.cli.Pipeline object at 0x22876d0>
File:        /usr/lib/python2.7/site-packages/qcos_cli/cli.py

Usage:       /usr/bin/qcos_cli
             /usr/bin/qcos_cli file
             /usr/bin/qcos_cli folder
```

```shell
$ qcos_cli file

Type:        FileOps
String form: <qcos_cli.cli.FileOps object at 0x3b37710>
File:        /usr/lib/python2.7/site-packages/qcos_cli/cli.py

Usage:       /usr/bin/qcos_cli file
             /usr/bin/qcos_cli file delete
             /usr/bin/qcos_cli file stat
             /usr/bin/qcos_cli file update
             /usr/bin/qcos_cli file upload
```

```shell
$ qcos_cli folder

Type:        FolderOps
String form: <qcos_cli.cli.FolderOps object at 0x2a8c750>
File:        /usr/lib/python2.7/site-packages/qcos_cli/cli.py

Usage:       /usr/bin/qcos_cli folder
             /usr/bin/qcos_cli folder create
             /usr/bin/qcos_cli folder delete
             /usr/bin/qcos_cli folder list
             /usr/bin/qcos_cli folder update
```

## 配置

```python
config = {
    'appid': int(os.getenv('QCOS_APPID', 0)),
    'secret_id': os.getenv('QCOS_SECRET_ID', '').decode('utf-8'),
    'secret_key': os.getenv('QCOS_SECRET_KEY', '').decode('utf-8'),
    'region': os.getenv('QCOS_REGION', '').decode('utf-8'),
    'bucket_name': os.getenv('QCOS_BUCKET_NAME', '').decode('utf-8')
}
```

通过环境变量设置认证信息

```shell
$ export QCOS_BUCKET_NAME=xxxxx
$ export QCOS_REGION=xxxx
$ export QCOS_SECRET_KEY=xxxx
$ export QCOS_SECRET_ID=xxxxxxxxxxxx
$ export QCOS_APPID=xxxxxxxxxxxxxx
$ export QCOS_BUCKET_NAME=xxxxxxxx
```

## 上传文件

```shell
$ qcos_cli file upload run.py '/run.py' --overwrite
  {
      "message": "SUCCESS",
      "code": 0,
      "data": {
          "url": "http://xxxxxxxxx/files/v2/1251720225/anyisalin1/run.py",
          "access_url": "http://xxxxxxxxx.file.myqcloud.com/run.py",
          "resource_path": "/1251720225/anyisalin1/run.py",
          "vid": "000235515c0xxxxxxxxx5dcbe80f51493887255",
          "source_url": "http://anyisaxxxxxx0225.cossh.myqcloud.com/run.py"
      },
      "request_id": "NTkwYWU5MxxxxxxxxNzhfNGYzYmM="
  }
```

### 查看文件状态

```shell
$ qcos_cli file stat '/run.py'
{
    "message": "SUCCESS",
    "code": 0,
    "data": {
        "slicesize": 768,
        "ctime": 1493887255,
        "biz_attr": "",
        "filelen": 768,
        "authority": "eInvalid",
        "source_url": "http://xxxxx.cossh.myqcloud.com/run.py",
        "forbid": 0,
        "sha": "4ac277xxxxxxxx091d5f057a13faff373",
        "custom_headers": {},
        "filesize": 768,
        "mtime": 1493887255,
        "access_url": "http://anyisaxxxxxle.myqcloud.com/run.py"
    },
    "request_id": "NTkwYxxxxxxzMV8yM2Y2ZWY="
}
```

### 更新文件

```shell
$ qcos_cli file update /run.py --content_type=text/html

{
   "message": "SUCCESS",
   "code": 0,
   "request_id": "NTkwYWVjMjhfNWJiODQzXzlmMzNfNjBmZmM="
}
```

### 删除文件

```shell
$ qcos_cli file delete '/run.py'

{
   "message": "SUCCESS",
   "code": 0,
   "request_id": "NTkwYWVjYjRfNTlhODQzXzgxYWFfNTdmYzg="
}
```

### 创建文件夹

```shell
$ qcos_cli folder create '/cccc/'

{
    "message": "SUCCESS",
    "code": 0,
    "data": {
        "ctime": 1493888203
    },
    "request_id": "NTkwYWVjY2JfNThhMDY4XzI0ZGVfNWIyNTE="
}
```

### 查看文件夹状态

```shell
$ qcos_cli folder stat '/cccc/'

{
   "message": "SUCCESS",
   "code": 0,
   "data": {
       "mtime": 1493888203,
       "ctime": 1493888203,
       "biz_attr": ""
   },
   "request_id": "NTkwYWVjZGVfZjM0NDNfMTE4OV8xZjk3Njc="
}
```

### 列出所有文件

```shell
$ qcos_cli folder list '/cccc/'
{
    "message": "SUCCESS",
    "code": 0,
    "data": {
        "infos": [
            {
                "ctime": 1493888266,
                "biz_attr": "",
                "filelen": 768,
                "authority": "eInvalid",
                "source_url": "http://xxxxx25.cossh.myqcloud.com/cccc/run.py",
                "sha": "4ac2778f74eeaaxxxxx5f057a13faff373",
                "filesize": 768,
                "mtime": 1493888266,
                "access_url": "http://anyisxxxxxe.myqcloud.com/cccc/run.py",
                "name": "run.py"
            }
        ],
        "listover": true,
        "context": ""
    },
    "request_id": "NTkwYWVkMxxxx2FhMWNfNTczNjU="
}
```

### 删除文件夹

```shell
$ qcos_cli folder delete '/cccc/'

{
    "message": "SUCCESS",
    "code": 0,
    "request_id": "NTkwYWVkNDJfMmIzOTQzXzgxNTZfNTJjODE="
}
```
