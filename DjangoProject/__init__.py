import pymysql

pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'NAME': 'django',  # 数据库名
        'USER': 'user',  # 用户名
        'PASSWORD': 'password!',  # 密码
        'HOST': 'localhost',  # 数据库主机，默认为localhost
        'PORT': '3306',  # 数据库端口，MySQL默认为3306
        'OPTIONS': {
            'autocommit': True,
        },
    }
}
