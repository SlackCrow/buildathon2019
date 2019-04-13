pragma solidity ^0.5.0;

contract PropertySale {

    string public houseAddress;
    string public buyerName;
    string public sellerName;
    string public date;
    string public transactionType;
    uint public price;

    event Sale(
        address _from,
        string _houseAddress,
        string _buyerName,
        string _sellerName,
        string _date,
        string _transactionType,
        uint _price
    );

    function emitSale() public{
        emit Sale(msg.sender,houseAddress,buyerName,sellerName,date,transactionType,price);
    }

    function setBuyer(string memory nm) public {
        buyerName = nm;
    }
    function setSeller(string memory nm) public {
        sellerName = nm;
    }

    function setPrice(uint x) public {
       price  = x;
    }
}

contract PropertyTax {

    string public houseAddress;
    string public owner;
    uint public taxYear;
    bool public taxesRecieved;

    event Tax(
        address _from,
        string _houseAddress,
        string _owner,
        uint _taxYear,
        bool _taxesRecieved
    );

    function emitTax() public {
        emit Tax(msg.sender, houseAddress, owner, taxYear, taxesRecieved);
    }

    function setOwner(string memory _owner) public {
        owner = _owner;
    }

    function setTaxYear(uint _taxYear) public {
        taxYear = _taxYear;
    }

    function setTaxesRecieved(bool _taxesRecieved) public {
        taxesRecieved = _taxesRecieved;
    }
}

contract PropertyMortgage {

    string public houseAddress;
    string public owner;
    uint public mortgageAmount;
    uint public currentBalance;
    string public status;

    event Mortgage(
        address _from,
        string _houseAddress,
        string _owner,
        uint _mortgageAmount,
        uint _currentBalance,
        string _status
    );

    function emitMortgage() public{
        emit Mortgage(msg.sender, houseAddress, owner, mortgageAmount, currentBalance, status);
    }

    function setOwner(string memory _owner) public {
        owner = _owner;
    }

    function setMortgageAmount(uint _mortgageAmount) public {
        mortgageAmount = _mortgageAmount;
    }

    function setCurrentBalance(uint _currentBalance) public {
        currentBalance = _currentBalance;
    }

    function setStatus(string memory _status) public {
        status = _status;
    }

}

contract PropertyJudgement {

    string public houseAddress;
    string public owner;
    uint public caseNumber;
    string public description;
    string public fileDate;
    uint public amount;

    event Judgement(
        address _from,
        string _houseAddress,
        string _owner,
        uint caseNumber,
        string description,
        string fileDate,
        uint amount
    );

    function emitJudgement() public {
        emit Judgement(msg.sender, houseAddress, owner, caseNumber, description, fileDate, amount);
    }

    function setOwner(string memory _owner) public {
        owner = _owner;
    }

    function setCaseNumber(uint _caseNumber) public {
        caseNumber = _caseNumber;
    }

    function setDescription(string memory _description) public {
        description = _description;
    }

    function setFileDate(string memory _fileDate) public {
        fileDate = _fileDate;
    }

    function setAmount(uint _amount) public {
        amount = _amount;
    }

}