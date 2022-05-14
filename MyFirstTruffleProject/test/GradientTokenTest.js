//import assertRevert from "./assertRevert.js";


const GradientToken = artifacts.require("GradientToken");

contract ("Gradient Token", accounts => {

    it("should make first account an owner" , async ()=> {
       let instance = await GradientToken.deployed();
       let owner = await instance.owner();
       assert.equal(owner,accounts[0]);
    });

    describe("mint",()=> {
        it("Creates a token with specified outer and inner colours", async ()=> {
            let instance = await GradientToken.deployed();
            let owner = await instance.owner();

                    await instance.mint("#ffoodd#", "#dddfff");

            let token = await instance.tokenOf(owner);
            let gradients = await instance.getGradient(tokens[0]);
            assert.deepEqual(gradients,["#ffoodd#", "#dddfff"]);

        });

        it("test ", ()=>)

    });

});