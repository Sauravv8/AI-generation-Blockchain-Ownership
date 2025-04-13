// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract AIArtNFT is ERC721URIStorage, Ownable {
    uint256 public tokenCounter;

    constructor() ERC721("AIArtNFT", "AINFT") {
        tokenCounter = 0;
    }

    function mintNFT(address recipient, string memory tokenURI) public returns (uint256) {
        tokenCounter += 1;
        _safeMint(recipient, tokenCounter);
        _setTokenURI(tokenCounter, tokenURI);
        return tokenCounter;
    }
}
