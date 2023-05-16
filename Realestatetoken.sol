pragma solidity ^0.5.0;

//imports for ERC20 and ERC20Detailed contracts for crowdsale
//contract owns # of tokens and transfers ownership as users purchase them

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";

//import mint contract from openzepplin to be able to mint tokens for crowdsale

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";

//create token contract with inherited code from ERC20, etc
contract RealEstateToken is ERC20, ERC20Detailed, ERC20Mintable{
    //ERC20Mintable constructor includes MinterRole function allowing only account deploying contract to be minter
    //onlyMinter modifier can only be called by MinterRole acct
    constructor(
        string memory name,
        string memory symbol,
        uint initial_supply
    )
    //call ERC20Detailed constructor. 18 used for decimal to allow conversion tokens to eth
    //call mint function from ERC20Mintable to allow token contract to call mint function
    ERC20Detailed(name, symbol, 18) public{}
}
//create smart contract that can mint tokens itself when sent eth


//import crowdsale and mintedcrowdsale contracts from openzeppelin
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/CappedCrowdsale.sol";
//create crowdsale contract
contract RealEstateTokenCrowdsale is Crowdsale, MintedCrowdsale, CappedCrowdsale {
    //call crowdsale constructor (set parameter values in contract deployment)
    constructor(
        uint rate,
        address payable wallet,
        RealEstateToken token,
        uint goal)
        public

        Crowdsale(rate, wallet, token)
        CappedCrowdsale(goal)
        {}

}

//use deployer contract to configure and deploy token and crowdsale contracts. deployer contract will create token and crowdsale contracts. 
//after deployer has set up crowdsale, owner and minter roles transfered to crowdsale contract
//create public address variables to keep track of contract addresses for minting and crowdsale (addresses to be assigned later)
contract RealEstateTokenCrowdsaleDeployer {
    address public realestate_token_address;
    address public realestate_token_crowdsale_address;
    constructor(string memory name, string memory symbol, address payable wallet, uint goal)
    //create token within constructor. store token as variable. initial supply 0 because crowdsale contract will take over minting and mints new tokens on command.
    //keywork 'new' allows contract to create another contract (ie deployer contract creates token contract)
    public
    {RealEstateToken token = new RealEstateToken(name, symbol, 0);
    //store token's address in public variable
    realestate_token_address = address(token);
    //create token crowdsale and include token
    RealEstateTokenCrowdsale realestate_token_crowdsale = new RealEstateTokenCrowdsale(300000000000000000, wallet, token, goal);
    realestate_token_crowdsale_address = address(realestate_token_crowdsale);
    // make the crowdsale contract minter, then deployer contract renounces minter role
    token.addMinter(realestate_token_crowdsale_address);
    token.renounceMinter();
    }
}