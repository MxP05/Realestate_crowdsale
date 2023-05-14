import streamlit as st
from web3 import Web3
from pathlib import Path
import os
import json
from wallet_connect import wallet_connect
from dotenv import load_dotenv

load_dotenv()
# Connect to Ethereum
connect_button = wallet_connect(label="wallet", key="wallet")
web3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

# User Inputs
st.title('RealEstate Token Crowdsale')

# Crowdsale Contract Details
#crowdsale_address = '0x051D61C263f3dd2e5E592FE471A974e422fb96eb'
buyer_address = st.text_input("Your Ethereum Address")
eth_to_send = st.number_input("Amount of RET to buy")

# Button to buy tokens
if st.button('Buy Tokens'):
    # Connect to the contract
    with open(Path('./contracts/compiled/crowdsale_abi.json')) as f:
        crowdsale_abi = json.load(f)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")
    crowdsale_contract = web3.eth.contract(
        address=contract_address, abi=crowdsale_abi)

    # Define the transaction
    transaction = {
        'from': buyer_address,
        'value': web3.toWei(eth_to_send, 'ether'),
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei'),
    }

    # Estimate the gas cost
    gas_estimate = crowdsale_contract.functions.buyTokens(
        buyer_address).estimateGas(transaction)

    # Update the transaction with the gas estimate
    transaction['gas'] = gas_estimate

    # Send the transaction
    tx_hash = crowdsale_contract.functions.buyTokens(
        buyer_address).transact(transaction)

    st.write(f'Transaction Hash: {tx_hash.hex()}')
