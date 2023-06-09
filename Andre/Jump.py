import streamlit as st
from web3 import Web3
import json
import pandas as pd
import plotly.graph_objects as go


## Create vertical tabs using st.sidebar
tab_selection = st.sidebar.radio("Select Tab", ("IcoPlatform", "PropertyNFT"))



# Connect to the local blockchain
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))


crowdsale_abi_1 = [{"constant":False,"inputs":[{"name":"beneficiary","type":"address"}],"name":"buyTokens","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"inputs":[{"name":"rate","type":"uint256"},{"name":"wallet","type":"address"},{"name":"token","type":"address"},{"name":"goal","type":"uint256"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"payable":True,"stateMutability":"payable","type":"fallback"},{"anonymous":False,"inputs":[{"indexed":True,"name":"purchaser","type":"address"},{"indexed":True,"name":"beneficiary","type":"address"},{"indexed":False,"name":"value","type":"uint256"},{"indexed":False,"name":"amount","type":"uint256"}],"name":"TokensPurchased","type":"event"},{"constant":True,"inputs":[],"name":"cap","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"capReached","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"rate","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"token","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"wallet","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"weiRaised","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"}]
crowdsale_abi_2 = [{"constant":False,"inputs":[{"name":"beneficiary","type":"address"}],"name":"buyTokens","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"inputs":[{"name":"rate","type":"uint256"},{"name":"wallet","type":"address"},{"name":"token","type":"address"},{"name":"goal","type":"uint256"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"payable":True,"stateMutability":"payable","type":"fallback"},{"anonymous":False,"inputs":[{"indexed":True,"name":"purchaser","type":"address"},{"indexed":True,"name":"beneficiary","type":"address"},{"indexed":False,"name":"value","type":"uint256"},{"indexed":False,"name":"amount","type":"uint256"}],"name":"TokensPurchased","type":"event"},{"constant":True,"inputs":[],"name":"cap","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"capReached","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"rate","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"token","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"wallet","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"weiRaised","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"}]
crowdsale_abi_3 = [{"constant":False,"inputs":[{"name":"beneficiary","type":"address"}],"name":"buyTokens","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"inputs":[{"name":"rate","type":"uint256"},{"name":"wallet","type":"address"},{"name":"token","type":"address"},{"name":"goal","type":"uint256"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"payable":True,"stateMutability":"payable","type":"fallback"},{"anonymous":False,"inputs":[{"indexed":True,"name":"purchaser","type":"address"},{"indexed":True,"name":"beneficiary","type":"address"},{"indexed":False,"name":"value","type":"uint256"},{"indexed":False,"name":"amount","type":"uint256"}],"name":"TokensPurchased","type":"event"},{"constant":True,"inputs":[],"name":"cap","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"capReached","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"rate","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"token","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"wallet","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"weiRaised","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"}]

# Define contract addresses for each crowdsale contract
crowdsale_address_1 = '0x72f1A88042931820b233eB425e2e46f4B6F3834b'  # Address for the first crowdsale contract
crowdsale_address_2 = '0x3e520f68196Fcd5A7A66d01b3dcB942ca0389969'  # Address for the second crowdsale contract
crowdsale_address_3 = '0x6095a9C66BCB17DB6cAd0a6fe29Cd0fFeaa5eAfB'  # Address for the third crowdsale contract

# Create instances of each crowdsale contract
crowdsale_contract_1 = w3.eth.contract(abi=crowdsale_abi_1, address=crowdsale_address_1)
crowdsale_contract_2 = w3.eth.contract(abi=crowdsale_abi_2, address=crowdsale_address_2)
crowdsale_contract_3 = w3.eth.contract(abi=crowdsale_abi_3, address=crowdsale_address_3)


if tab_selection == "IcoPlatform":
     
 st.title("Real Estate Token ICO Platform")



property_images = {
        'Akasaka': 'Resources/Akasaka.jpg',
        'Chiyoda': 'Resources/Chiyoda.jpg',
        'Niijuku': 'Resources/Niijuku.jpg',
    }

property_info = {
        'Akasaka': 'Akasaka description and details...',
        'Chiyoda': 'Chiyoda description and details...',
        'Niijuku': 'Niijuku description and details...',
    }

property_options = ['Akasaka', 'Chiyoda', 'Niijuku']
selected_property = st.selectbox("Select Property", property_options)

# Display the selected property's image
st.image(property_images[selected_property], caption=selected_property, use_column_width=True)

# Display the selected property's information
st.write(property_info[selected_property])


token_details = {
        'Akasaka': {'name': 'AkasakaCoin', 'symbol': 'AKC', 'price': 0.3},
        'Chiyoda': {'name': 'ChiyodaCoin', 'symbol': 'CYC', 'price': 0.3},
        'Niijuku': {'name': 'NiijukuCoin', 'symbol': 'NJC', 'price': 0.3},
    }

contract_addresses = {
        'Akasaka': '0x123...',
        'Chiyoda': '0x456...',
        'Niijuku': '0x789...',
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
            
 