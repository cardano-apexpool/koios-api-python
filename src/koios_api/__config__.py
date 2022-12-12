import os
env = dict(os.environ)
SLEEP_TIME = 1
if 'CARDANO_NET' not in env:
    CARDANO_NET = 'mainnet'
    if 'API_BASE_URL' not in env:
        API_BASE_URL = 'https://api.koios.rest/api/v0'
    else:
        API_BASE_URL = env['API_BASE_URL']
else:
    if env['CARDANO_NET'] == 'mainnet' or env['CARDANO_NET'] == '--mainnet':
        CARDANO_NET = 'mainnet'
        if 'API_BASE_URL' not in env:
            API_BASE_URL = 'https://api.koios.rest/api/v0'
        else:
            API_BASE_URL = env['API_BASE_URL']
    elif env['CARDANO_NET'] == 'preprod' or env['CARDANO_NET'] == '--testnet-magic 1':
        CARDANO_NET = env['CARDANO_NET']
        if 'API_BASE_URL' not in env:
            API_BASE_URL = 'https://preprod.koios.rest/api/v0'
        else:
            API_BASE_URL = env['API_BASE_URL']
    elif env['CARDANO_NET'] == 'preview' or env['CARDANO_NET'] == '--testnet-magic 2':
        CARDANO_NET = env['CARDANO_NET']
        if 'API_BASE_URL' not in env:
            API_BASE_URL = 'https://preview.koios.rest/api/v0'
        else:
            API_BASE_URL = env['API_BASE_URL']
    else:
        CARDANO_NET = env['CARDANO_NET']
        API_BASE_URL = env['API_BASE_URL']
