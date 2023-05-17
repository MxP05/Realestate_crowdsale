import streamlit as st
import pandas as pd
import numpy as np
import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv



st.set_page_config(page_title="Real Estate Tokenization", layout='wide')


# create tab as container
tab = st.container()
#create tabs for display in steamlit
tab1, tab2, tab3,tab5 = st.tabs(['Project','ICO Platform','Wallet Balance','Property NFTs'])

with tab1:

    st.title('Tokenization of Real Estate Properties')

    st.header('Project Objective:')

    st.text('The goal of this project is to connect owners of real estate properties with a community of')
    
    st.text('real estate micro-investors in an effort to make real estate investment accessible through') 
            
    st.text('a fractional ownership (FO) tokenized system. Tokenizing the real estate investment process') 
    
    st.text('is mutually beneficial for property owners and investors as it eliminates middle-man') 
    
    st.text('expenses such as brokers. In addition to expanding investment opportunities and eliminating') 
    
    st.text('real estate middle-men, this system would allow for expanded democratization of real estate') 
    
    st.text('prices.')
    
    st.text('We elected to pursue a FO tokenization because creating and entire asset (EA) ownership token')
    
    st.text(' would require turning a property deed into its own NFT, which is an undeveloped asset class.')
    
    st.text('However, in this application we do store property info metadata and ownership deeds within')
    
    st.text('an IPFS. Verification of NFT contracts and metadata was completed with Etherscan. Including')
    
    st.text(' these verified NFTs allows investors to confirm that the tokens they are purchasing are') 
    
    st.text('representative of fractional ownership of a specificproperty. While the real estate tokens')
    
    st.text('can be transferred, the property-specific NFTs cannot, preventingcomplications that may')
    
    st.text('arise with an EA ownership token.')

with tab2:
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
        'Akasaka': 'Resources/Akasaka.jpg',
        'Chiyoda': 'Resources/Chiyoda.jpg',
        'Niijuku': 'Resources/Niijuku.jpg',
    }

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
        





    
#dropdown for property NFT selection and links to allow users to verify NFTs, properties, deployed contracts, metadata, deeds. deeds are for NY and are blank, but included for proof of concept. pinata ipfs used to store metadata. contract verification completed with etherscan.
with tab5:
    st.title('Property NFTs')            
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
            st.write('View Chiyoda PoC deed [Deeds PDF](https://gateway.pinata.cloud/ipfs/QmQfAHuLV9ptSwxSShdQmkLYA4aoMUeJVesKXVepjVztvH/)')
            

with tab3:
    st.title('Wallet Balance')
    with st.form('Balance'):
    # Cache the contract on load
# Define the load_contract function
        def load_contract():

    # Load Art Gallery ABI
         with open(Path('akasakacoin_abi.json')) as f:
          certificate_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
         contract_address = "0x796339Bb6051dd930F0d29DcA09CBEFb9Cd434E9"

    # Get the contract
         contract = w3.eth.contract(
         address=contract_address,
         abi=certificate_abi
         )
    # Return the contract from the function
         return contract

# Load the contract
    contract = load_contract()


################################################################################
# Award Certificate
################################################################################
    accounts = w3.eth.accounts
    account = accounts[0]
    wallet_t = st.selectbox("Select Account", options=accounts) # Student's wallet.
    if st.button("Display Wallet Balance"):
            Balance_of=contract.functions.balanceOf(wallet_t).call()
            st.write(f"balance is {Balance_of}")
    else:
            st.write("no balance")
    # Make sure that only Rice could mint. That is not built in here yet.

################################################################################
# Display Certificate
########################################################