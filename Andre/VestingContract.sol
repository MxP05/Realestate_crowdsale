pragma solidity ^0.5.0;

//Import the following library from openzeppelin 
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/IERC20.sol";

// Create a contract Call LargeInvestorVesting
contract LargeInvestorVesting {
    IERC20 private _token;
    
    struct VestingSchedule {
        uint256 amount;
        uint256 start;
        uint256 end;
        uint256 released;
    }
    
    mapping(address => VestingSchedule) public vestingSchedules;
    
//Create a contructor the LargeInvestorVesting contract 
    constructor(IERC20 token) public {
        _token = token;
    }
    
    //Add a function to depositTokens 
    function depositTokens(address beneficiary, uint256 amount, uint256 start, uint256 end) public {
        require(beneficiary != address(0), "Invalid beneficiary address");
        require(amount > 0, "Invalid amount");
        require(end > start, "Invalid vesting period");
        
        VestingSchedule storage schedule = vestingSchedules[beneficiary];
        require(schedule.amount == 0, "Vesting schedule already exists");
        
        schedule.amount = amount;
        schedule.start = start;
        schedule.end = end;
        schedule.released = 0;
        
        _token.transferFrom(msg.sender, address(this), amount);
    }
