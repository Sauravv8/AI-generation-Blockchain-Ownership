async function main() {
    const AIArtNFT = await ethers.getContractFactory("AIArtNFT");
    const contract = await AIArtNFT.deploy();
    await contract.deployed();
    console.log("Deployed to:", contract.address);
  }
  main().catch(console.error);
  