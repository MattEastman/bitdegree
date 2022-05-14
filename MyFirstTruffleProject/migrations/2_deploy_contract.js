const Migrations = artifacts.require("./GradientToken.sol");

module.exports = function (deployer) {
  deployer.deploy(GradientToken);
};
