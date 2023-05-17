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
# **Incorporated Technologies and Libraries**

## **NFT Development:** NFTs developed using the ethereum.org developer tutorial and ERC721 protocols. 

### [Ethereum NFT Dev Tutorial:](https://ethereum.org/ca/developers/tutorials/how-to-write-and-deploy-an-nft/)

### **OpenZeppelin:** Contracts for ERC721 implementation in NFT development.
### *openzeppelin/contracts/token/ERC721/ERC721.sol
### *openzeppelin/contracts/utils/Counters.sol
### *openzeppelin/contracts/access/Ownable.sol
### *openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol

### **Alchemy:** Used to create real estate NFTs. Connected to Sepliola test net. Alchemy used to create project and associated API key used in .env file.
![Alchemy Project Creation on Sepiola Test Network](https://github.com/MxP05/Realestate_crowdsale/blob/main/Jason/alchemy.jpg)

### **Sepiola Test Network:** Test network for execution of transactions related to NFT development. Connected to Metamask to present Sepiola Eth and NFTs in wallet and allow for minting of NFTs on test network. Sepiola also provided the eth faucet for the project development. 

### **Node.js:** Used for running javascript programs.

### **Hardhat:** Tells project about dependencies and plug-ins. 

### **Ethers:** Library for making Eth requests. Ethers plugin used for contract deployment.

### **Etherscan:** View and verify smart contract deployment, NFT minting, transaction details. 

### **Metamask:** For storing eth, NFTs, and creating private key to sign transactions in NFT minting.
![Metamask screenshot](

### **Pinata:** Used to store configured metadata of NFTs in IPFS. Stores property deed pdfs, building images, property-specific info. Provided hashed CIDs of metadata in IPFS included in NFT minting. Investors can view metadata stored with Pinata. It should be noted that while the NFT properties are in Tokyo, the deeds in the NFT metadata are for New York. Japan does not have detailed legal requirements for transfer of property ownership. These deeds are included for application proof of concept.

### [Japan Real Estate Law:](https://www.dlapiperrealworld.com/law/index.html?t=sale-and-purchase&s=contents-of-a-contract&c=JP)
---

# **Next Steps:** 

### Address SEC regulations for ICO

### Develop automated process to get real estate token owners portion of rent to provide stream of passive income in addition to investment income.

### Create lender/borrower platform to permit loans for coin purchase with APR and APY determined by machine learning programs.

### Complete vested smart contract for real estate tokens.

### Include NFT gallery in app instead of using links to NFTs, metadata, etc

