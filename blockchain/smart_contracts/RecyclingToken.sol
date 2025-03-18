// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract RecyclingToken {
    string public name = "PlasticRecyclingToken";
    string public symbol = "PRT";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1000000 * 10**uint256(decimals);
    
    mapping(address => uint256) public balanceOf;
    address public owner;

    event Transfer(address indexed from, address indexed to, uint256 value);

    constructor() {
        owner = msg.sender;
        balanceOf[owner] = totalSupply;
    }

    function transfer(address to, uint256 value) public returns (bool) {
        require(balanceOf[msg.sender] >= value, "Insufficient balance");
        balanceOf[msg.sender] -= value;
        balanceOf[to] += value;
        emit Transfer(msg.sender, to, value);
        return true;
    }

    function mint(address recipient, uint256 amount) public {
        require(msg.sender == owner, "Only owner can mint");
        totalSupply += amount;
        balanceOf[recipient] += amount;
        emit Transfer(address(0), recipient, amount);
    }
}