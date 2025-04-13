import { useState } from "react";
import { ethers } from "ethers";
import ABI from "./abi/AIArtNFT.json";

const CONTRACT_ADDRESS = "YOUR_CONTRACT_ADDRESS";

export default function MintNFT() {
  const [uri, setUri] = useState("");

  const mint = async () => {
    const provider = new ethers.BrowserProvider(window.ethereum);
    const signer = await provider.getSigner();
    const contract = new ethers.Contract(CONTRACT_ADDRESS, ABI, signer);
    const tx = await contract.mintNFT(await signer.getAddress(), uri);
    await tx.wait();
    alert("NFT Minted!");
  };

  return (
    <div>
      <input placeholder="Enter IPFS URI" onChange={(e) => setUri(e.target.value)} />
      <button onClick={mint}>Mint NFT</button>
    </div>
  );
}
