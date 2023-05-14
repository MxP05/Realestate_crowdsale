pragma solidity ^0.8.0;

// Create a contract named lending platform 
contract LendingPlatform {
    uint256 public lenderInterestRate; 
    uint256 public borrowerInterestRate; 

    mapping(address => uint256) public deposits; // Implement mapping for each user's deposited ether
    mapping(address => uint256) public borrowedAmount; // Implement mapping for each user's borrowed amount

    // Add these variables
    uint256 public totalDeposits; // Stores the total amount deposited by all users.
    uint256 public totalInterestPaid; // Stores the total amount of interest paid by borrowers.
    uint256 public platformSharePercentage = 35; // The percentage of interest that the platform will keep.
    address payable public platformAddress; // The address of the platform that receives the percentage share of the interest.

// Set the interest rates for lenders and borrowers and specify the platform address for your lending platform.
    constructor(uint256 _lenderInterestRate, uint256 _borrowerInterestRate, address payable _platformAddress) {
        lenderInterestRate = _lenderInterestRate;
        borrowerInterestRate = _borrowerInterestRate;
        platformAddress = _platformAddress; // Initialize the platform address
    }


// Add a Function to allow users to deposit ether into the platform
 function deposit() public payable {
        require(msg.value > 0, "Deposit amount must be greater than zero.");
        deposits[msg.sender] += msg.value;
        totalDeposits += msg.value; // Update the total deposits
    }

 
