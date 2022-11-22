import yfinance as yf
import pandas as pd
eth_usd = yf.download("ETH-USD", interval = "1d", start = '2022-10-01', end = '2022-10-01')['Close']
eth_usd_user = yf.download("ETH-USD", interval = "1d", start = '2022-05-25', end = '2022-09-15')['Close']
usdc_usd = yf.download("USDC-USD", interval = "1d", start = '2022-10-01', end = '2022-10-01')['Close']
weth_usd = yf.download("WETH-USD", interval = "1d", start = '2022-10-01', end = '2022-10-01')['Close']
wbtc_usd = yf.download("WBTC-USD", interval = "1d", start = '2022-10-01', end = '2022-10-01')['Close']
dai_usd = yf.download("DAI-USD", interval = "1d", start = '2022-10-01', end = '2022-10-01')['Close']
uma_usd = yf.download("UMA-USD", interval = "1d", start = '2022-10-01', end = '2022-10-01')['Close']
boba_usd = yf.download("BOBA-USD", interval = "1d", start = '2022-10-01', end = '2022-10-01')['Close']
bal_usd = yf.download("BAL-USD", interval = "1d", start = '2022-10-01', end = '2022-10-01')['Close']
usdt_usd = yf.download("USDT-USD", interval = "1d", start = '2022-10-01', end = '2022-10-01')['Close']
badger_usd = yf.download("BADGER-USD", interval = "1d", start = '2022-10-01', end = '2022-10-01')['Close']
Ether = 2.701*eth_usd
USDC = 23990801.603918 *usdc_usd
WETH = 7653.997751791189275806*weth_usd 
WBTC = 66.71671988*wbtc_usd
DAI = 865704.90222842684822576*dai_usd 
UMA = 35675.634676572623219231*uma_usd
BOBA = 242194.871260699784675188 *boba_usd
BAL = 38152.834072344697504092 *bal_usd
USDT = 200.038793*usdt_usd

df = pd.DataFrame(eth_usd_user*0.5)
df['ETH']=0.5
df['d_in_pool'] = df['ETH']*df['Close']

BADGER = 1.75104362218004139*badger_usd
eth_usd2 = yf.download("ETH-USD", interval = "1d", start = '2022-11-20', end = '2022-11-21')['Close']
usdc_usd2 = yf.download("USDC-USD", interval = "1d", start = '2022-11-20', end = '2022-11-21')['Close']
weth_usd2 = yf.download("WETH-USD", interval = "1d", start = '2022-11-20', end = '2022-11-21')['Close']
wbtc_usd2 = yf.download("WBTC-USD", interval = "1d", start = '2022-11-20', end = '2022-11-21')['Close']
dai_usd2 = yf.download("DAI-USD", interval = "1d", start = '2022-11-20', end = '2022-11-21')['Close']
uma_usd2 = yf.download("UMA-USD", interval = "1d", start = '2022-11-20', end = '2022-11-21')['Close']
boba_usd2 = yf.download("BOBA-USD", interval = "1d", start = '2022-11-20', end = '2022-11-21')['Close']
bal_usd2 = yf.download("BAL-USD", interval = "1d", start = '2022-11-20', end = '2022-11-21')['Close']
usdt_usd2 = yf.download("USDT-USD", interval = "1d", start = '2022-11-20', end = '2022-11-21')['Close']
badger_usd2 = yf.download("BADGER-USD", interval = "1d", start = '2022-11-20', end = '2022-11-21')['Close']
Ether2 = 3.361*eth_usd2
USDC2 = 4845523.720962*usdc_usd2
WETH2 = 1486.39878789458164*weth_usd2
WBTC2 = 91.49373871*wbtc_usd2
DAI2 = 265879.011154039058*dai_usd2
UMA2 = 36632.7487563794700*uma_usd2
BOBA2 = 269520.57453216511*boba_usd2
BAL2 = 7958.54619479602*bal_usd2
USDT2 = 200.038793*usdt_usd2
BADGER2 = 1.75104362218004139*badger_usd2
blockDiff=113
amount_in_d = df.d_in_pool[0]
sum_size_reward = Ether+USDC+WETH+WBTC+DAI+UMA+BOBA+BAL+USDT+BADGER
df = pd.DataFrame(eth_usd_user*0.5)
df['ETH']=0.5
df['d_in_pool'] = df['ETH']*df['Close']
reward = 345.3146370854914
reward_per_block = 29.664649611753303688460154654532
blockDiff=113
amount_in_d = df.d_in_pool[0]
k = (reward/(blockDiff*reward_per_block*amount_in_d))*sum_size_reward[0]
amount = Ether2+USDC2+WETH2+WBTC2+DAI2+UMA2+BOBA2+BAL2+USDT2+BADGER2
def get_acx(days, amount, pool_size):
    reward_per_block_ = 70000000/2359783
    reward_ = k*days*reward_per_block_*amount*(1/pool_size[0])
    return f'{reward_}ACX'
print("К-во дней:")
days=float(input())
print("К-во токенов в $:")
amount=float(input())
print(get_acx(days,amount,sum_size_reward))