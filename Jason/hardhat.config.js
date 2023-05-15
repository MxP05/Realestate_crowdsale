/**
* @type import('hardhat/config').HardhatUserConfig
*/
//include dependencies and pull info from .env
require('dotenv').config({path:__dirname+'/nft.env'});
//install ethers to interact and make requests to eth. will use eithers plug in from hardhat to deploy contract
require("@nomiclabs/hardhat-ethers");
const {API_URL, PRIVATE_KEY} = process.env;
module.exports = {
   solidity: "0.8.1",
   //use alchemy sepiola as test network. hardhat network knows which contracts are being run, what they do and why they fail (taken from hardhat documentation)
   defaultNetwork: "sepiola",
   networks: {
      hardhat: {},
      sepiola: {
         url: API_URL,
         accounts: [`0x${PRIVATE_KEY}`]
      }
   },
}