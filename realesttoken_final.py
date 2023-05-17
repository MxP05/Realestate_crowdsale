#Import the required libraries 
import streamlit as st
from web3 import Web3
import json
import pandas as pd
import plotly.graph_objects as go


# Create vertical tabs using st.sidebar
tab_selection = st.sidebar.radio("Select Tab", ("IcoPlatform", "PropertyNFT"))



# Connect to the local blockchain
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Define contract ABI for each crowdsale contract
crowdsale_abi_1 = [{"constant":False,"inputs":[{"name":"beneficiary","type":"address"}],"name":"buyTokens","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"inputs":[{"name":"rate","type":"uint256"},{"name":"wallet","type":"address"},{"name":"token","type":"address"},{"name":"goal","type":"uint256"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"payable":True,"stateMutability":"payable","type":"fallback"},{"anonymous":False,"inputs":[{"indexed":True,"name":"purchaser","type":"address"},{"indexed":True,"name":"beneficiary","type":"address"},{"indexed":False,"name":"value","type":"uint256"},{"indexed":False,"name":"amount","type":"uint256"}],"name":"TokensPurchased","type":"event"},{"constant":True,"inputs":[],"name":"cap","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"capReached","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"rate","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"token","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"wallet","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"weiRaised","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"}]
crowdsale_abi_2 = [{"constant":False,"inputs":[{"name":"beneficiary","type":"address"}],"name":"buyTokens","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"inputs":[{"name":"rate","type":"uint256"},{"name":"wallet","type":"address"},{"name":"token","type":"address"},{"name":"goal","type":"uint256"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"payable":True,"stateMutability":"payable","type":"fallback"},{"anonymous":False,"inputs":[{"indexed":True,"name":"purchaser","type":"address"},{"indexed":True,"name":"beneficiary","type":"address"},{"indexed":False,"name":"value","type":"uint256"},{"indexed":False,"name":"amount","type":"uint256"}],"name":"TokensPurchased","type":"event"},{"constant":True,"inputs":[],"name":"cap","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"capReached","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"rate","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"token","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"wallet","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"weiRaised","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"}]
crowdsale_abi_3 = [{"constant":False,"inputs":[{"name":"beneficiary","type":"address"}],"name":"buyTokens","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"inputs":[{"name":"rate","type":"uint256"},{"name":"wallet","type":"address"},{"name":"token","type":"address"},{"name":"goal","type":"uint256"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"payable":True,"stateMutability":"payable","type":"fallback"},{"anonymous":False,"inputs":[{"indexed":True,"name":"purchaser","type":"address"},{"indexed":True,"name":"beneficiary","type":"address"},{"indexed":False,"name":"value","type":"uint256"},{"indexed":False,"name":"amount","type":"uint256"}],"name":"TokensPurchased","type":"event"},{"constant":True,"inputs":[],"name":"cap","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"capReached","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"rate","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"token","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"wallet","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"weiRaised","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"}]

# Define contract addresses for each crowdsale contract
crowdsale_address_1 = '0x4B0d8ae41E418c1927cbeDDf8956435cb652953A'  # Address for the first crowdsale contract
crowdsale_address_2 = '0x1bdb220538172c89d9d20dab0934A2cf7f9b973c'  # Address for the second crowdsale contract
crowdsale_address_3 = '0xaeE67a9C1ba268E83Aee3aCC4dA7550c5cDfa46b'  # Address for the third crowdsale contract

# Create instances of each crowdsale contract
crowdsale_contract_1 = w3.eth.contract(abi=crowdsale_abi_1, address=crowdsale_address_1)
crowdsale_contract_2 = w3.eth.contract(abi=crowdsale_abi_2, address=crowdsale_address_2)
crowdsale_contract_3 = w3.eth.contract(abi=crowdsale_abi_3, address=crowdsale_address_3)


# Token 1 contract address and ABI
token1_address = "0xd7b8856E3F85befAA40d55713D3c5726b62DBa5B"
token1_abi = [{"inputs": [{"internalType": "string", "name": "name", "type": "string"}, {"internalType": "string", "name": "symbol", "type": "string"}, {"internalType": "uint256", "name": "initial_supply", "type": "uint256"}], "payable": False, "stateMutability": "nonpayable", "type": "constructor"}, {"anonymous": False, "inputs": [{"indexed": True, "internalType": "address", "name": "owner", "type": "address"}, {"indexed": True, "internalType": "address", "name": "spender", "type": "address"}, {"indexed": False, "internalType": "uint256", "name": "value", "type": "uint256"}], "name": "Approval", "type": "event"}, {"anonymous": False, "inputs": [{"indexed": True, "internalType": "address", "name": "account", "type": "address"}], "name": "MinterAdded", "type": "event"}, {"anonymous": False, "inputs": [{"indexed": True, "internalType": "address", "name": "account", "type": "address"}], "name": "MinterRemoved", "type": "event"}, {"anonymous": False, "inputs": [{"indexed": True, "internalType": "address", "name": "from", "type": "address"}, {"indexed": True, "internalType": "address", "name": "to", "type": "address"}, {"indexed": False, "internalType": "uint256", "name": "value", "type": "uint256"}], "name": "Transfer", "type": "event"}, {"constant": False, "inputs": [{"internalType": "address", "name": "account", "type": "address"}], "name": "addMinter", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [{"internalType": "address", "name": "owner", "type": "address"}, {"internalType": "address", "name": "spender", "type": "address"}], "name": "allowance", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [{"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "approve", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [{"internalType": "address", "name": "account", "type": "address"}], "name": "balanceOf", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": True, "inputs": [], "name": "decimals", "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}], "payable": False, ",stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [{"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "subtractedValue", "type": "uint256"}], "name": "decreaseAllowance", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": False, "inputs": [{"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "addedValue", "type": "uint256"}], "name": "increaseAllowance", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [{"internalType": "address", "name": "account", "type": "address"}], "name": "isMinter", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [{"internalType": "address", "name": "account", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "mint", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [], "name": "name", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [], "name": "renounceMinter", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [], "name": "symbol", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": True, "inputs": [], "name": "totalSupply", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [{"internalType": "address", "name": "recipient", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "transfer", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": False, "inputs": [{"internalType": "address", "name": "sender", "type": "address"}, {"internalType": "address", "name": "recipient", "type": "address"}, {"internalType": "uint256", "name": "amount", "type":"uint256"}], "name": "transferFrom", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}]

# Token 2 contract address and ABI
token2_address = "0x2764BE37413B1A154deEF95633f8048213Be0a0b"
token2_abi = [{"inputs": [{"internalType": "string", "name": "name", "type": "string"}, {"internalType": "string", "name": "symbol", "type": "string"}, {"internalType": "uint256", "name": "initial_supply", "type": "uint256"}], "payable": False, "stateMutability": "nonpayable", "type": "constructor"}, {"anonymous": False, "inputs": [{"indexed": True, "internalType": "address", "name": "owner", "type": "address"}, {"indexed": True, "internalType": "address", "name": "spender", "type": "address"}, {"indexed": False, "internalType": "uint256", "name": "value", "type": "uint256"}], "name": "Approval", "type": "event"}, {"anonymous": False, "inputs": [{"indexed": True, "internalType": "address", "name": "account", "type": "address"}], "name": "MinterAdded", "type": "event"}, {"anonymous": False, "inputs": [{"indexed": True, "internalType": "address", "name": "account", "type": "address"}], "name": "MinterRemoved", "type": "event"}, {"anonymous": False, "inputs": [{"indexed": True, "internalType": "address", "name": "from", "type": "address"}, {"indexed": True, "internalType": "address", "name": "to", "type": "address"}, {"indexed": False, "internalType": "uint256", "name": "value", "type": "uint256"}], "name": "Transfer", "type": "event"}, {"constant": False, "inputs": [{"internalType": "address", "name": "account", "type": "address"}], "name": "addMinter", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [{"internalType": "address", "name": "owner", "type": "address"}, {"internalType": "address", "name": "spender", "type": "address"}], "name": "allowance", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [{"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "approve", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [{"internalType": "address", "name": "account", "type": "address"}], "name": "balanceOf", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": True, "inputs": [], "name": "decimals", "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}], "payable": False, ",stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [{"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "subtractedValue", "type": "uint256"}], "name": "decreaseAllowance", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": False, "inputs": [{"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "addedValue", "type": "uint256"}], "name": "increaseAllowance", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [{"internalType": "address", "name": "account", "type": "address"}], "name": "isMinter", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [{"internalType": "address", "name": "account", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "mint", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [], "name": "name", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [], "name": "renounceMinter", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [], "name": "symbol", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": True, "inputs": [], "name": "totalSupply", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [{"internalType": "address", "name": "recipient", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "transfer", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": False, "inputs": [{"internalType": "address", "name": "sender", "type": "address"}, {"internalType": "address", "name": "recipient", "type": "address"}, {"internalType": "uint256", "name": "amount", "type":"uint256"}], "name": "transferFrom", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}]

# Token 3 contract address and ABI
token3_address = "0x30f29609023fEbee9908EAF27A64Ef3a00235c50"
token3_abi = [{"inputs": [{"internalType": "string", "name": "name", "type": "string"}, {"internalType": "string", "name": "symbol", "type": "string"}, {"internalType": "uint256", "name": "initial_supply", "type": "uint256"}], "payable": False, "stateMutability": "nonpayable", "type": "constructor"}, {"anonymous": False, "inputs": [{"indexed": True, "internalType": "address", "name": "owner", "type": "address"}, {"indexed": True, "internalType": "address", "name": "spender", "type": "address"}, {"indexed": False, "internalType": "uint256", "name": "value", "type": "uint256"}], "name": "Approval", "type": "event"}, {"anonymous": False, "inputs": [{"indexed": True, "internalType": "address", "name": "account", "type": "address"}], "name": "MinterAdded", "type": "event"}, {"anonymous": False, "inputs": [{"indexed": True, "internalType": "address", "name": "account", "type": "address"}], "name": "MinterRemoved", "type": "event"}, {"anonymous": False, "inputs": [{"indexed": True, "internalType": "address", "name": "from", "type": "address"}, {"indexed": True, "internalType": "address", "name": "to", "type": "address"}, {"indexed": False, "internalType": "uint256", "name": "value", "type": "uint256"}], "name": "Transfer", "type": "event"}, {"constant": False, "inputs": [{"internalType": "address", "name": "account", "type": "address"}], "name": "addMinter", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [{"internalType": "address", "name": "owner", "type": "address"}, {"internalType": "address", "name": "spender", "type": "address"}], "name": "allowance", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [{"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "approve", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [{"internalType": "address", "name": "account", "type": "address"}], "name": "balanceOf", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": True, "inputs": [], "name": "decimals", "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}], "payable": False, ",stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [{"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "subtractedValue", "type": "uint256"}], "name": "decreaseAllowance", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": False, "inputs": [{"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "addedValue", "type": "uint256"}], "name": "increaseAllowance", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [{"internalType": "address", "name": "account", "type": "address"}], "name": "isMinter", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [{"internalType": "address", "name": "account", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "mint", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [], "name": "name", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [], "name": "renounceMinter", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [], "name": "symbol", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": True, "inputs": [], "name": "totalSupply", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [{"internalType": "address", "name": "recipient", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "transfer", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": False, "inputs": [{"internalType": "address", "name": "sender", "type": "address"}, {"internalType": "address", "name": "recipient", "type": "address"}, {"internalType": "uint256", "name": "amount", "type":"uint256"}], "name": "transferFrom", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}]

token1_contract = w3.eth.contract(abi=token1_abi, address=token1_address)
token2_contract = w3.eth.contract(abi=token2_abi, address=token2_address)
token3_contract = w3.eth.contract(abi=token3_abi, address=token3_address)


if tab_selection == "IcoPlatform":
     
 st.title("Real Estate Token ICO Platform")


# Map the name of property to the it's image path
property_images = {
        'Akasaka': 'Resources/Akasaka.jpg',
        'Chiyoda': 'Resources/Chiyoda.jpg',
        'Niijuku': 'Resources/Niijuku.jpg',
    }

# Create a dictionary for the property information 
property_info = {
        'Akasaka': 'Location: Tokyo, Akasaka district in Minato Ward. 4 minutes from Akasaka train station. Property includes land and building. Commercial zone. Est building price: $555,100,000',
        'Chiyoda': 'Location: Tokyo, Yombancho district in Chiyoda Ward.4 minutes from Ichigaya train station. Propperty includes land and building. Commercial zone. Est building price: $345,800,000',
        'Niijuku': 'Location: Tokyo, Niijuku district in Katsushika Ward. 9 minutes from Kanamachi train station. Property includes only land. Industrial zone. Est building price: $409,500,000',
    }

property_options = ['Akasaka', 'Chiyoda', 'Niijuku']
selected_property = st.selectbox("Select Property", property_options)

# Display the selected property's image
st.image(property_images[selected_property], caption=selected_property, use_column_width=True)

# Display the selected property's information
st.write(property_info[selected_property])

# Create a dictionary for token details 
token_details = {
        'Akasaka': {'name': 'AkasakaCoin', 'symbol': 'AKC', 'price': 0.3},
        'Chiyoda': {'name': 'ChiyodaCoin', 'symbol': 'CYC', 'price': 0.3},
        'Niijuku': {'name': 'NiijukuCoin', 'symbol': 'NJC', 'price': 0.3},
    }



# Token distribution data
token_distributions = {
        'Akasaka': {
            "Investors": 500000,
            "Founders": 300000,
            "Team Members": 150000,
            "Advisors": 50000
        },
        'Chiyoda': {
            "Investors": 600000,
            "Founders": 250000,
            "Team Members": 100000,
            "Advisors": 50000
        },
        'Niijuku': {
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

# Token balances
                if token1_contract:
                    token1_balance = token1_contract.functions.balanceOf(user_address).call()
                    st.write(f"AkasakaCoin balance: {token1_balance} tokens")

                if token2_contract:
                    token2_balance = token2_contract.functions.balanceOf(user_address).call()
                    st.write(f"ChiyodaCoin balance: {token2_balance} tokens")

                if token3_contract:
                    token3_balance = token3_contract.functions.balanceOf(user_address).call()
                    st.write(f"NiijukuCoin balance: {token3_balance} tokens")

# Token Details
st.subheader("Token Details")
selected_token = token_details[selected_property]
st.write(f"Token name: {selected_token['name']}")
st.write(f"Token symbol: {selected_token['symbol']}")
st.write(f"Token price: {selected_token['price']} ETH")


# Define a function to buy tokens based on the selected property
def buy_tokens_for_selected_property(selected_property, user_address, amount_to_invest):
        if selected_property == 'Akasaka':
            crowdsale_contract = crowdsale_contract_1
        elif selected_property == 'Chiyoda':
            crowdsale_contract = crowdsale_contract_2
        elif selected_property == 'Niijuku':
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

# dropdown for property NFT selection and links to allow users to verify NFTs, properties, deployed contracts, metadata, deeds. deeds are for NY and are blank, but included for proof of concept. pinata ipfs used to store metadata. contract verification completed with etherscan.
elif tab_selection == "PropertyNFT":
        
 with st.form('Select Property for Verification'):
        property_nft=st.selectbox('Which property would you like to verify?',('Niijuku', 'Akasaka', 'Chiyoda'))
        submitted8 = float(st.form_submit_button('Submit'))
        if property_nft=='Niijuku':
            st.write('View link to NiijukuNFT in Etherscan to verify property information [NiijukuNFT](https://sepolia.etherscan.io/token/0xf5921ea1515f57f41ec5dc072f0a04d583567f8a)')
            st.write('View Niijuku metadata [Niijuku Metadata](https://gateway.pinata.cloud/ipfs/QmeG9UaWgNein2XMax7KSsBoxx2Q2mNqQh6qPKLK9VttsG)')
            st.write('View Niijuku PoC deed [Deeds PDF](https://gateway.pinata.cloud/ipfs/QmQfAHuLV9ptSwxSShdQmkLYA4aoMUeJVesKXVepjVztvH/)')
        elif property_nft=='Akasaka':
            st.write('View link to AkasakaNFT in Etherscan to verify property information [AkasakaNFT](https://sepolia.etherscan.io/token/0x7d9e54d03214f81a44767510ef46e0a2d84e6b47)')
            st.write('View Akasaka metadata [Akasaka Metadata](https://gateway.pinata.cloud/ipfs/QmQLZ75xSL9EvdMGkesuNSebMmFXEzpxLK4nLFooqvhNTz)')
            st.write('View Akasaka PoC deed [Deeds PDF](https://gateway.pinata.cloud/ipfs/QmQfAHuLV9ptSwxSShdQmkLYA4aoMUeJVesKXVepjVztvH/)')
        else:
            st.write('View link to ChiyodaNFT in Etherscan to verify property information [ChiyodaNFT](https://sepolia.etherscan.io/token/0xFb9eF17F2245d877B5E526537437fE8939a04C47)')
            st.write('View Chiyoda metadata [Chiyoda Metadata](https://gateway.pinata.cloud/ipfs/QmZwrrtL9aG17gect2mv13NAZhQUj2dPRCrhCpi6Xp4Y8K)')
            st.write('View Chiyoda PoC deed [Deeds PDF](https://gateway.pinata.cloud/ipfs/QmQfArHuLV9ptSwxSShdQmkLYA4aoMUeJVesKXVepjVztvH/)')
            