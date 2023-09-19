# RANDOM WALLETS MODE
RANDOM_WALLET = False  # True or False

# SLEEP MODE
IS_SLEEP = True  # True or False

SLEEP_FROM = 21  # Second
SLEEP_TO = 38  # Second

# PROXY MODE
USE_PROXY = True

# GWEI CONTROL MODE
CHECK_GWEI = True  # True or False
MAX_GWEI = 20

def value_okx():

    '''
    OKX
    BSC
    ERC20
    TRC20
    Polygon
    Avalanche C-Chain
    Avalanche X-Chain
    Arbitrum One
    Optimism
    Fantom
    zkSync Era
    StarkNet
    '''

    chain       = 'StarkNet'
    symbol      = ''

    amount_from = 0.0091
    amount_to   = 0.0091

    account = 'player'

    FEE         = 0.0001 # комса на вывод
    SUB_ACC     = False # True / False. True если хочешь проверять субаккаунты и сначала делать с них перевод на основной счет

    is_private_key = False # True если в wallets.txt вставил evm приватники. False если адреса (evm / не evm)

    return chain, symbol, amount_from, amount_to, account, FEE, SUB_ACC, is_private_key