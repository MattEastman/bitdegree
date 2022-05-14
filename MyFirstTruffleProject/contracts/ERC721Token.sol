pragma solidity ^0.4.23;


import "./ERC721.sol";
import "./SafeMath.sol";

contract ERC721Token is ERC721 {

    using SafeMath for unit256;

    mapping (uint256=> address) private tokenOwner;
    mapping (address => uint256[]) private ownerTokens;

    function _mint(address _to,uint256 _tokenId) public{
        require(_to ! = address(0));  
        require(tokenOwner[_tokenID] == address(0));

        tokenOwner[_tokenId] = _to;

        ownedTokens[_to].push(_tokenId);

        emit Transfer(0x0,_to,_tokenId);
    }

    function ownerOf(uint256 tokenId) public view returns (address){
            address owner = tokenOwner[_tokenID];
            require(owner != address(0));
            return owner;
    }

    function balanceOf(address _owner) public view returns(uint256){
        return ownedTokens[_owner].length;
    }

    functiontokensof(address _owner) public view returns(uint256[]){
          return ownedTokens[_owner];
    }
  

}