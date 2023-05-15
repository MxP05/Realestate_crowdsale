import "./customtoken.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";


// Bootstrap the KaseiCoinCrowdsale contract by inheriting the following OpenZeppelin:
// * Crowdsale
// * MintedCrowdsale
contract CustomCoinCrowdsale is Crowdsale, MintedCrowdsale {
    
    // Provide parameters for all of the features of your crowdsale, such as the `rate`, `wallet` for fundraising, and `token`.
    constructor(
        uint256 rate, // rate in TKNbits
        address payable wallet, // sale beneficiary
        customtoken token // the KaseiCoin itself that the KaseiCoinCrowdsale will work with
    ) public Crowdsale(rate, wallet, token) {
        // constructor can stay empty
    }
}


contract CustomCoinCrowdsaleDeployer {
    // Create an `address public` variable called `kasei_token_address`.
    address public custom_token_address;
    // Create an `address public` variable called `kasei_crowdsale_address`.
    address public custom_crowdsale_address;

    // Add the constructor.
    constructor(
        string memory name,
        string memory symbol,
        address payable wallet // this address will receive all Ether raised by the crowdsale
    ) public {
        // Create a new instance of the KaseiCoin contract.
        customtoken token = new customtoken(name, symbol, 0);
        
        // Assign the token contract’s address to the `kasei_token_address` variable.
        custom_token_address = address(token);

        // Create a new instance of the `KaseiCoinCrowdsale` contract
        CustomCoinCrowdsale custom_crowdsale =
            new CustomCoinCrowdsale(1, wallet, token);
            
        // Aassign the `KaseiCoinCrowdsale` contract’s address to the `kasei_crowdsale_address` variable.
        custom_crowdsale_address = address(custom_crowdsale);

        // Set the `KaseiCoinCrowdsale` contract as a minter
        token.addMinter(custom_crowdsale_address);
        
        // Have the `KaseiCoinCrowdsaleDeployer` renounce its minter role.
        token.renounceMinter();
    }
}