# qcos_cli

> 腾讯云对象存储命令行工具

```shell
$ python run.py --help
usage: python run.py [-h]
                     {upload_file,stat_file,update_file,del_file,create_folder,update_folder,stat_folder,del_folder,list_folder}
                     ...

positional arguments:
  {upload_file,stat_file,update_file,del_file,create_folder,update_folder,stat_folder,del_folder,list_folder}
    upload_file         upload local file
    stat_file           show remote file status
    update_file         update file
    del_file            del file
    create_folder       create folder
    update_folder       update folder
    stat_folder         show remote folder status
    del_folder          del folder
    list_folder         list folder

optional arguments:
  -h, --help            show this help message and exit
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
$ python run.py upload_file --help

usage: python run.py upload_file [-h] [--overwrite] local_file remote_file

positional arguments:
  local_file   local file path
  remote_file  remote file path, start with /, end not /

optional arguments:
  -h, --help   show this help message and exit
  --overwrite  overwrite remote file

  $ python run.py upload_file --overwrite run.py '/run.py'
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
$ python run.py stat_file '/run.py'
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

### 删除文件

### 创建文件夹

### 查看文件夹状态

### 删除文件夹

### 列出所有文件
