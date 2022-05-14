pragma solidity ^0.4.23;

contract ERC721 {

event Transfer(address indexed _from, address indexed _to, uint256[] tokenIndices);
event Approval(address indexed _owner,address indexed _approved, uint256 _tokenID);

function balanceOf(address _owner) public view returns (uint256[] _balances);
function ownerOf(uint256 _tokenId) public view returns (address _owner);
function transfer(address _to, uint256[] _tokens) public;
function approve(address _to, uint256[] _tokens) public;

}