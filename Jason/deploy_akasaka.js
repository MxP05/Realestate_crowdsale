async function main() {
    //contract factory to deploy smart contracts. contract instances connected to first signer by default
      const MyNFT = await ethers.getContractFactory("contracts/AkasakaNFT.sol:MyNFT")
    
      // Start deployment, returning a promise that resolves to a contract object
      const myNFT = await MyNFT.deploy()
      await myNFT.deployed()
      //where contract deployed to. can check on etherscan
      console.log("Contract deployed to address:", myNFT.address)
    }
    //do not deploy nft with an error
    main()
      .then(() => process.exit(0))
      .catch((error) => {
        console.error(error)
        process.exit(1)
      })