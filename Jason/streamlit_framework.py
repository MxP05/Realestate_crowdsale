import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Real Estate Tokenization", layout='wide')


# create tab as container
tab = st.container()

#create tabs for display in steamlit
tab1, tab2, tab3, tab4, tab5 = st.tabs(['Project','Crowdsale','something','something','Property NFTs'])

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
            