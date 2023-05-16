//Minting NFT
//use alchemy web3 library for creating requests eth blockchain


//get public and private keys from .env for sending and signing transxns
require("dotenv").config({path:__dirname+'/nft.env'});
const API_URL= process.env.API_URL;
const PUBLIC_KEY = process.env.PUBLIC_KEY;
const PRIVATE_KEY = process.env.PRIVATE_KEY;
//alchemy web3 installation to make eth bchain requests
const {createAlchemyWeb3} = require("@alch/alchemy-web3");
const web3 = createAlchemyWeb3(API_URL);
//grab contract abi. hardhat automatically generates abi and saves in MyNft.json file
const contract = require("../artifacts/contracts/NiijukuNFT.sol/MyNFT.json");
//add recipient contract address
const contractAddress = "0xf5921EA1515f57F41EC5dc072f0A04d583567F8A";
//use web3 contract method to create contract w/ abi and address
const nftContract = new web3.eth.Contract(contract.abi, contractAddress);
//view contract abi
console.log(JSON.stringify(contract.abi));

//track number of transactions for security and prevening replay attacks
async function mintNFT(tokenURI) {
    const nonce = await web3.eth.getTransactionCount(PUBLIC_KEY, 'latest'); //get latest nonce

  //create transaction.
    const tx = {
      'from': PUBLIC_KEY,
      'to': contractAddress,
      'nonce': nonce, //acct nonce with # transxns sent from address
      'gas': 500000,
      'data': nftContract.methods.mintNFT(PUBLIC_KEY, tokenURI).encodeABI() //minting nft
    };
//sign transxn with private key
  const signPromise = web3.eth.accounts.signTransaction(tx, PRIVATE_KEY);
  signPromise
    .then((signedTx) => {
        //gives transxn hash to make sure transxn mined. error checking from eth development tutorial included to make sure transxn successful
      web3.eth.sendSignedTransaction(
        signedTx.rawTransaction,
        function (err, hash) {
          if (!err) {
            console.log(
              "The hash of your transaction is: ",
              hash,
              "\nCheck Alchemy's Mempool to view the status of your transaction!"
            )
          } else {
            console.log(
              "Something went wrong when submitting your transaction:",
              err
            )
          }
        }
      )
    })
    .catch((err) => {
      console.log(" Promise failed:", err);
    })
}

//mint nft with metadata from pinata
mintNFT("ipfs://QmeG9UaWgNein2XMax7KSsBoxx2Q2mNqQh6qPKLK9VttsG")

//NFT deployed and minted on eth bchain!!