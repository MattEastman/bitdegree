pragma solifity ^0.4.23;

import "./ERC721.sol";
import "./Ownable.sol";

contract GradientToken is ERC721Token, Ownable{

    string public constant name = "GradientToken";
    string public constant symbol = "Grad";

    struct Gradient{
        string outer;
        string inner;

    }

    Gradient[] public gradients;

    function mint(string, string _inner) public payable onlyOwner{

        Gradient memory _gradient = Gradient({outer: _outer, _inner:_inner});
        uint _gradientId = gradients.push(_gradients) -1;
        _mint(msg.sender, _gradientId);

    }

    funtion getGradient(uint _gradientId) public view returns(string outer, string inner){
            Gradient memory _grad = gradients[_gradientId];
            outer = _grad.outer;
            inner = _grad.inner;

    }


}