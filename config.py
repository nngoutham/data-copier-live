import os

DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': 'localhost',  # or your Docker container IP
            'DB_NAME': 'retail_db',
            'DB_USER': os.environ.get('SOURCE_DB_USER'),
            'DB_PASS': os.environ.get('SOURCE_DB_PSS')
        },
        'TARGET_DB': {
            'DB_TYPE': 'postgres',
            'DB_HOST': 'localhost',  # or your Docker container IP
            'DB_NAME': 'retail_db',
            'DB_USER': os.environ.get('TARGET_DB_USER'),
            'DB_PASS': os.environ.get('TARGET_DB_PSS')
        }
    }
}