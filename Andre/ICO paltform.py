import streamlit as st
from web3 import Web3
import json
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Connect to Ethereum network using Infura API
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))


crowdsale_abi_1 = [{"constant":False,"inputs":[{"name":"beneficiary","type":"address"}],"name":"buyTokens","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"inputs":[{"name":"rate","type":"uint256"},{"name":"wallet","type":"address"},{"name":"token","type":"address"},{"name":"goal","type":"uint256"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"payable":True,"stateMutability":"payable","type":"fallback"},{"anonymous":False,"inputs":[{"indexed":True,"name":"purchaser","type":"address"},{"indexed":True,"name":"beneficiary","type":"address"},{"indexed":False,"name":"value","type":"uint256"},{"indexed":False,"name":"amount","type":"uint256"}],"name":"TokensPurchased","type":"event"},{"constant":True,"inputs":[],"name":"cap","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"capReached","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"rate","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"token","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"wallet","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"weiRaised","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"}]
crowdsale_abi_2 = [{"constant":False,"inputs":[{"name":"beneficiary","type":"address"}],"name":"buyTokens","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"inputs":[{"name":"rate","type":"uint256"},{"name":"wallet","type":"address"},{"name":"token","type":"address"},{"name":"goal","type":"uint256"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"payable":True,"stateMutability":"payable","type":"fallback"},{"anonymous":False,"inputs":[{"indexed":True,"name":"purchaser","type":"address"},{"indexed":True,"name":"beneficiary","type":"address"},{"indexed":False,"name":"value","type":"uint256"},{"indexed":False,"name":"amount","type":"uint256"}],"name":"TokensPurchased","type":"event"},{"constant":True,"inputs":[],"name":"cap","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"capReached","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"rate","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"token","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"wallet","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"weiRaised","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"}]
crowdsale_abi_3 = [{"constant":False,"inputs":[{"name":"beneficiary","type":"address"}],"name":"buyTokens","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"inputs":[{"name":"rate","type":"uint256"},{"name":"wallet","type":"address"},{"name":"token","type":"address"},{"name":"goal","type":"uint256"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"payable":True,"stateMutability":"payable","type":"fallback"},{"anonymous":False,"inputs":[{"indexed":True,"name":"purchaser","type":"address"},{"indexed":True,"name":"beneficiary","type":"address"},{"indexed":False,"name":"value","type":"uint256"},{"indexed":False,"name":"amount","type":"uint256"}],"name":"TokensPurchased","type":"event"},{"constant":True,"inputs":[],"name":"cap","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"capReached","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"rate","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"token","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"wallet","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"weiRaised","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"}]

# Define contract addresses for each crowdsale contract
crowdsale_address_1 = '0x2b17cac53Fd363CA45A7A9cDFF9b37e170d5Fc72'  # Address for the first crowdsale contract
crowdsale_address_2 = '0x7Af49E33bb28dE836881B665C46f5129Dd1cDFe1'  # Address for the second crowdsale contract
crowdsale_address_3 = '0x186aA20196ec1E41090047995b98441c1d9f0469'  # Address for the third crowdsale contract

# Create instances of each crowdsale contract
crowdsale_contract_1 = w3.eth.contract(abi=crowdsale_abi_1, address=crowdsale_address_1)
crowdsale_contract_2 = w3.eth.contract(abi=crowdsale_abi_2, address=crowdsale_address_2)
crowdsale_contract_3 = w3.eth.contract(abi=crowdsale_abi_3, address=crowdsale_address_3)


st.title("Real Estate Token ICO Platform")



property_images = {
    'Property 1': 'Resources/Akasaka.jpg',
    'Property 2': 'Resources/Chiyoda.jpg',
    'Property 3': 'Resources/Niijuku.jpg',
}

property_info = {
    'Property 1': 'Property 1 description and details...',
    'Property 2': 'Property 2 description and details...',
    'Property 3': 'Property 3 description and details...',
}

property_options = ['Property 1', 'Property 2', 'Property 3']
selected_property = st.selectbox("Select Property", property_options)

# Display the selected property's image
st.image(property_images[selected_property], caption=selected_property, use_column_width=True)

# Display the selected property's information
st.write(property_info[selected_property])



token_details = {
    'Property 1': {'name': 'Token 1', 'symbol': 'TK1', 'price': 1.0},
    'Property 2': {'name': 'Token 2', 'symbol': 'TK2', 'price': 1.5},
    'Property 3': {'name': 'Token 3', 'symbol': 'TK3', 'price': 2.0},
}

contract_addresses = {
    'Property 1': '0x123...',
    'Property 2': '0x456...',
    'Property 3': '0x789...',
}

# Token distribution data
token_distributions = {
    'Property 1': {
        "Investors": 500000,
        "Founders": 300000,
        "Team Members": 150000,
        "Advisors": 50000
    },
    'Property 2': {
        "Investors": 600000,
        "Founders": 250000,
        "Team Members": 100000,
        "Advisors": 50000
    },
    'Property 3': {
        "Investors": 550000,
        "Founders": 200000,
        "Team Members": 200000,
        "Advisors": 50000
    }
}






# Pie chart (Token distribution)
allocations = token_distributions[selected_property]
fig = go.Figure(data=[go.Pie(labels=list(allocations.keys()), values=list(allocations.values()))])
fig.update_layout(title_text=f"Token Distribution for {selected_property}")
st.plotly_chart(fig)



# Initialize user session state
if "user_address" not in st.session_state:
    st.session_state.user_address = None
if "user_balance" not in st.session_state:
    st.session_state.user_balance = 0

# Create a button to connect to wallet
connect_button = st.button("Connect to Wallet")

if connect_button:
    # Check if Web3 is connected to a provider
    if not w3.isConnected():
        st.error("Web3 is not connected to a provider.")
    else:
        # Get the user's Ethereum address
        user_address = st.text_input("Enter your Ethereum address")
        if not user_address:
            st.warning("Please enter your Ethereum address.")
        else:
            # Check if the address is valid
            if not w3.isAddress(user_address):
                st.error("Invalid Ethereum address.")
            else:
                st.session_state.user_address = user_address
                st.session_state.user_balance = w3.eth.getBalance(user_address)
                st.success(f"Connected to wallet. Your Ethereum address: {user_address}")
                st.write(f"Your balance: {w3.fromWei(st.session_state.user_balance, 'ether')} ETH")

# Token Details
st.subheader("Token Details")
selected_token = token_details[selected_property]
st.write(f"Token name: {selected_token['name']}")
st.write(f"Token symbol: {selected_token['symbol']}")
st.write(f"Token price: {selected_token['price']} ETH")


# Define a function to buy tokens based on the selected property
def buy_tokens_for_selected_property(selected_property, user_address, amount_to_invest):
    if selected_property == 'Property 1':
        crowdsale_contract = crowdsale_contract_1
    elif selected_property == 'Property 2':
        crowdsale_contract = crowdsale_contract_2
    elif selected_property == 'Property 3':
        crowdsale_contract = crowdsale_contract_3
    else:
        st.error("Invalid property selected")
        return

    # Call the buyTokens function for the selected crowdsale contract
    txn_hash = crowdsale_contract.functions.buyTokens(user_address).transact({'from': user_address, 'value': amount_to_invest})
    st.write(f"Transaction hash: {txn_hash.hex()}")
    st.write("Waiting for the transaction to be mined...")
    txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)
    st.write(f"Transaction mined. Block number: {txn_receipt['blockNumber']}")

# Get the investment amount from the user
investment_amount = st.text_input("Enter the amount of Ether you want to invest:")

# Create a "Buy Tokens" button
buy_tokens_button = st.button("Buy Tokens")

# Call the buy_tokens_for_selected_property() function when the user clicks the "Buy Tokens" button
if buy_tokens_button:
    amount_to_invest = w3.toWei(float(investment_amount), 'ether')
    buy_tokens_for_selected_property(selected_property, st.session_state.user_address, amount_to_invest)




