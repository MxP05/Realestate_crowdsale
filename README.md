# **Real Estate Tokenization Project**

### The goal of this project is to connect owners of real estate properties with a community of real estate micro-investors in an effort to make real estate investment accessible through a fractional ownership (FO) tokenized system. Tokenizing the real estate investment process is mutually beneficial for property owners and investors as it eliminates middle-man expenses such as brokers. In addition to expanding investment opportunities and eliminating real estate middle-men, this system would allow for expanded democratization of real estate prices. Theoretically, the minted tokens could also serve as a fiat currency backed by the value of the property they represent. 
### We elected to pursue a FO tokenization because creating and entire asset (EA) ownership token would require turning a property deed into its own NFT, which is an undeveloped asset class. However, in this application we do store property info metadata and ownership deeds within an IPFS. The deployed contracts have been verified through Etherscan. Including these verified NFTs allows investors to confirm that the tokens they are purchasing are representative of fractional ownership of a specific property.  While the real estate tokens can be transferred, the property-specific NFTs cannot, preventing complications that may arise with an EA ownership token.
### [Source](https://www.fool.com/investing/stock-market/market-sectors/financials/non-fungible-tokens/nft-real-estate/).
---
# **Review of Literature:**

### At this time, a review of literature determined that there are no identical projects, though some companies are making efforts to tokenize real estate and provide micro-finance investment opportunities:

## **DigiShares:**

### Though not yet fully functional, Digishares addresses some of the problems we are attempting to solve. Their platform allows real estate owners to tokenize their property and create a crowdfunding platform. The minted tokens are “compatible with exchanges” and use “audited smart contracts” and electronic signatures to make exchanges. They also claim to have shareholder meetings and votes, but refrain from expanding on the functional process. A future version of our application would try to incorporate this functionality as well. Where our idea differs from DigiShares is with an incorporated lending market, which allows users to acquire loans to purchase tokens, provided the borrower meets loan criteria. We also have a primary focus on tokenizing rental properties. Thus, our application creates two additional means of passive income for users: lenders make money by loaning Eth and borrowers make money by retaining a portion of the rent paid to their property. 
### [For more on DigiShares:](https://digishares.io/real-estate-tokenization?utm_feeditemid=&utm_device=c&utm_term=how%20to%20tokenize%20property&utm_source=google&utm_medium=ppc&utm_campaign=USA+%2B+Canada+-+v3&hsa_cam=17322637350&hsa_grp=142284528212&hsa_mt=b&hsa_src=g&hsa_ad=599963647351&hsa_acc=3998698433&hsa_net=adwords&hsa_kw=how%20to%20tokenize%20property&hsa_tgt=kwd-1187718903723&hsa_ver=3&gad=1&gclid=Cj0KCQjwu-KiBhCsARIsAPztUF2g2h5j501tbDSomwqYZwEzQ1cokxyvhjV5rlsQ3jVTHpUoA2Z5UBYaAhkxEALw_wcB)

## **Yieldstreet:**

### While Yieldstreet does not present opportunities for tokenization of real estate, they do provide users with the opportunity for real estate micro-investments with an investment minimum of $5,000.00. Yieldstreet is a private real estate investment fund, but it does provide an opportunity for users to obtain partial ownership of a specific property. However, Yieldsreet serves as strictly an investment platform, and does not create alternative income streams or allow for easy transition between ownership of properties. As a more conventional real estate investment fund, they are also subject to conventional real estate fees for purchase of properties. Their site includes the useful insight that real estate ownership is an excellent hedge against inflation as “US property prices and income have historically outpaced inflation.”
### [For more on Yieldstreet:](https://www.yieldstreet.com/real-estate-investing/?ad_id=652726043019&adset_id=145388436923&campaign_id=19643999464&campaign_type=search&g_acctid=323-576-2402&g_adgroupid=145388436923&g_adid=652726043019&g_adtype=search&g_campaign=S+-+NonBrand_Real+Estate_tCPA-Tier+1_EPB&g_campaignid=19643999464&g_keyword=realty%20investment&g_keywordid=kwd-308775751137&g_network=g&hdlt_campaign=S+-+NonBrand_Real+Estate_tCPA-Tier+1_EPB&hdlt_source=google&keyword=realty%20investment&matchtype=p&medium=cpc&placement=g&utm_campaign=NonBrand_Real%20Estate_Realty_Tier%201_PM&utm_content=responsivead&utm_medium=cpc&utm_source=Google_Search&utm_term=realty%20investment&gad=1&gclid=Cj0KCQjwu-KiBhCsARIsAPztUF16Ra0yrt51x4GW-9h2oZ6pL9mKx9prUyMxvFeaSKr1FFqX5FgYOzAaAoCMEALw_wcB)
---
# **Tokenization and Smartcontracts
RealEstate token is a fungible token that is ERC-20 compliant. This contract launches a crowdsale and token that will allow people who are interested in investing in to realestate at a fractional level.
## Installation Guide
Technologies
[pragma solidity ^0.5.0;
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/IERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/CappedCrowdsale.sol";]

Step 1 run/deploy program using Solidity for the smart contract

step 2 take/use Realestatetoken.sol file in main folder.

step 3 compile, in the deployment panel connect your Ganache to ur remix IDE

step 4: deploy the realestatecrowdsale deployer

step5: connect the token address to realestatetoken, and the crowdsale address to realestatecrowdsale

congratulations u have deployed the smart contracts!

![Ganache select](https://github.com/MxP05/Realestate_crowdsale/blob/main/Screenshots/ganacheselect.png?raw=true)
![Kaseiaddress](https://github.com/MxP05/Realestate_crowdsale/blob/main/Screenshots/gotodeployer.png?raw=true)
![Token,crowdsaleaddress](https://github.com/MxP05/Realestate_crowdsale/blob/main/Screenshots/tokenadresscrowdsale%20address.png?raw=true)

# **When u run the streamlit make sure you paste the deployed token , and crowdsale adress!!!

![Crowdsaleaddress](https://github.com/MxP05/Realestate_crowdsale/blob/main/Screenshots/crowdsaleaddress.png?raw=true)
![Tokenaddress](https://github.com/MxP05/Realestate_crowdsale/blob/main/Screenshots/token%20address.png?raw=true)

# Streamlit 
 Wallet connection: Click on the connect wallet button and enter your wallet address in the input field
 
 Buy tokens= Enter the amount you want to invest and click on the buy token button
 
 ![streamlit-buy-connect](https://github.com/MxP05/Realestate_crowdsale/assets/118853744/b1545014-b514-4d2b-ab98-e9dd60dbff6a)
 
 
 Balanceofbutton: select the wallet you use to purchase the token and click the display wallet balance 
 
 ![balanceofbutton](https://github.com/MxP05/Realestate_crowdsale/assets/118853744/e0803e4e-bee1-4565-b826-0d435323dc42)

# Using the NFT portion of Streamlit: Select property to verify from dropdown in Property NFT tab
![Property NFT Example Streamlit](https://github.com/MxP05/Realestate_crowdsale/blob/main/Jason/nft%20links.jpg)
# NFT contract and transaction verified on Etherscan and available in application:
![NFT contract etherscan](https://github.com/MxP05/Realestate_crowdsale/blob/main/Jason/nft_etherscan_contract.jpg)
# Metadata Pinata IPFS for NFT contracts available as link in app:
![NFT metadata](https://github.com/MxP05/Realestate_crowdsale/blob/main/Jason/nft_etherscan_metadata.jpg)
# Blank PoC property deeds Pinata IPFS:
![Deeds screenshot](https://github.com/MxP05/Realestate_crowdsale/blob/main/Jason/nft_blank_deeds.jpg)


# **Incorporated Technologies and Libraries**

## **NFT Development:** NFTs developed using the ethereum.org developer tutorial and ERC721 protocols. 

### [Ethereum NFT Dev Tutorial:](https://ethereum.org/ca/developers/tutorials/how-to-write-and-deploy-an-nft/)

### **OpenZeppelin:** Contracts for ERC721 implementation in NFT development.
*openzeppelin/contracts/token/ERC721/ERC721.sol
*openzeppelin/contracts/utils/Counters.sol
*openzeppelin/contracts/access/Ownable.sol
*openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol

### **Alchemy:** Used to create real estate NFTs. Connected to Sepliola test net. Alchemy used to create project and associated API key used in .env file.
![Alchemy Project Creation on Sepiola Test Network](https://github.com/MxP05/Realestate_crowdsale/blob/main/Jason/alchemy.jpg)
### **Sepiola Test Network:** Test network for execution of transactions related to NFT development. Connected to Metamask to present Sepiola Eth and NFTs in wallet and allow for minting of NFTs on test network. Sepiola also provided the eth faucet for the project development. 

### **Node.js:** Used for running javascript programs.

### **Hardhat:** Tells project about dependencies and plug-ins. 

### **Ethers:** Library for making Eth requests. Ethers plugin used for contract deployment.

### **Etherscan:** View and verify smart contract deployment, NFT minting, transaction details. 
![Etherscan screenshot](https://github.com/MxP05/Realestate_crowdsale/blob/main/Jason/etherscan.jpg)
### **Metamask:** For storing eth, NFTs, and creating private key to sign transactions in NFT minting.
![Metamask screenshot](https://github.com/MxP05/Realestate_crowdsale/blob/main/Jason/metamask2.jpg)
### **Pinata:** Used to store configured metadata of NFTs in IPFS. Stores property deed pdfs, building images, property-specific info. Provided hashed CIDs of metadata in IPFS included in NFT minting. Investors can view metadata stored with Pinata. It should be noted that while the NFT properties are in Tokyo, the deeds in the NFT metadata are for New York. Japan does not have detailed legal requirements for transfer of property ownership. These deeds are included for application proof of concept.
![Pinata screenshot](https://github.com/MxP05/Realestate_crowdsale/blob/main/Jason/pinata.jpg)

### [Japan Real Estate Law:](https://www.dlapiperrealworld.com/law/index.html?t=sale-and-purchase&s=contents-of-a-contract&c=JP)
---
# **Real Estate Property NFTs Development and Functionality:**

### The purpose of minting property-specific NFTs is to allow the real estate investors and microinvestors using our application to verify that the property-specific ERC20 tokens they are purchasing represent ownership in a real property. Each NFT was created by following the Ethereum ERC721 protocol for minting NFTs. A link to the basic tutorial is available as a link above. We used Alchemy to create our NFT project and deployed it on the Sepiola Testnet. Using Sepiola also permitted us to use the Sepiola Eth faucet. The Sepiola Eth faucet provided the test Eth used to deploy each of our NFT contracts to the Sepiola Testnet. After the initial creation of our project, we developed ERC721 contracts for each property's NFT. These contracts were created under the MIT license and permitted only a single minter. Each contract was then deployed to the Sepiola Testnet using the ethers library. The address of the deployed contract was then incorporated into its corresponding minting script. The contract deployment was verified using Etherscan. The minting of each NFT used: the API from our Alchemy project, a public key (wallet address where test Eth was deposited and origin of transaction), a private key obtained with Metamask to sign the transaction, the NFT contract, the address of the contract deployment, and a transaction construction for minting property-specific NFTs. However, the NFTs still required property metadata in their minting for this circumstantial application. The metadata (building type, municipality, building value, building image, property deed, etc.) was stored in an IPFS using Pinata. With all necessary prerequisites, the property NFTs were minted. Each transaction was verified with the corresponding transaction hash on Etherscan. The NFTs were then deposited in a wallet, which can be seen above in the Metamask display.  The final step was to verify the deployer each of the NFT contracts/minter of the NFTs, which was done by flattening each NFT contract script and matching the source code in Etherscan. With our NFTs minted with the necessary metadata and corresponding contracts verified, we created links in our application to allow investors to view ownership and property data and feel more at ease with their purchase of the ERC20 property tokens.

# **Next Steps:** 

### Address SEC regulations for ICO

### Develop automated process to get real estate token owners portion of rent to provide stream of passive income in addition to investment income.

### Create lender/borrower platform to permit loans for coin purchase with APR and APY determined by machine learning programs.

### Complete vested smart contract for real estate tokens.

### Include NFT gallery in app instead of using links to NFTs, metadata, etc

## License Back-end front-end Dapp, used to ICO fragmental realestate tokens, ownership gets verified by NFT's ,deeds,ethscan.
## Contributors Andre Johnson,Marc Pocorni,Jason Steiner, Bria
