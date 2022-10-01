#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from web3 import Web3
from uniswap import Uniswap

address = None          # or None if you're not going to make transactions
private_key = None  # or None if you're not going to make transactions
version = 3                       # specify which version of Uniswap to use
#provider = "WEB3 PROVIDER URL"    # can also be set through the environment variable `PROVIDER`

eth = "0x0000000000000000000000000000000000000000"
bat = "0x0D8775F648430679A709E98d2b0Cb6250d2887EF"
dai = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
safe = "0x5aFE3855358E112B5647B952709E6165e1c1eEEe"
usdc = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
weth = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
safeEthPoolAddress = "0xBB0ecCb680FF8b2cbBB239b200cC6f9927b4aacB"

def main():
    print("main()")
    load_dotenv()
    uniswap = Uniswap(address=address, private_key=private_key, version=version, provider=os.environ['PROVIDER'])
    # Returns the amount of DAI you get for 1 ETH (10^18 wei)
    oneEthInUsdc = uniswap.get_price_input(eth, usdc, 1*10**18)*1e-6
    print(oneEthInUsdc)
    oneSafeInUsdc = uniswap.get_price_input(safe, eth, 1*10**18) # fails, does not find pool, uniswap ui does
    print(oneSafeInUsdc)

    safeEthPool = uniswap.get_pool_instance(weth,safe) # pool not found ?
    print(safeEthPool)

if __name__ == "__main__":   
    main()