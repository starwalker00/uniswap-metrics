#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from web3 import Web3

def main():
    print("main()")
    load_dotenv()
    alchemy_url = os.environ['HTTP_PROVIDER_URL']
    w3 = Web3(Web3.HTTPProvider(alchemy_url))
    print(w3.isConnected())

if __name__ == "__main__":   
    main()