from qcos_cli.config import config


def check_config(config):
    for key, val in config.items():
        if not val:
            if key == 'appid':
                export_key = 'QCOS_APPID'
            elif key == 'secret_id':
                export_key = 'QCOS_SECRET_ID'
            elif key == 'secret_key':
                export_key = 'QCOS_SECRET_KEY'
            elif key == 'region':
                export_key = 'QCOS_REGION'
            elif key == 'bucket_name':
                export_key = 'QCOS_BUCKET_NAME'
            raise AttributeError(
                '{key} is not set, should export {export_key}=xxxxxx'.format(key=key, export_key=export_key))


if __name__ == '__main__':
    check_config(config)
    from qcos_cli.cli import main

    main()
