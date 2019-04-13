pragma solidity ^0.5.0;

contract PropertySale {
    
    event Sale(
        address _from,
        string _houseAddress,
        string _buyerName,
        string _sellerName,
        string _date,
        string _transactionType,
        uint _price
    );

    function emitSale(string memory houseAddress, string memory buyerName, string memory sellerName, 
    string memory date, string memory transactionType, uint price) public{
        emit Sale(msg.sender,houseAddress,buyerName,sellerName,date,transactionType,price);
    }
}

contract PropertyTax {
    
    event Tax(
        address _from,
        string _houseAddress,
        string _owner,
        uint _taxYear,
        bool _taxesRecieved
    );
    
    function emitTax(string memory houseAddress, string memory owner, uint taxYear, bool taxesRecieved) public {
        emit Tax(msg.sender, houseAddress, owner, taxYear, taxesRecieved);
    }
}

contract PropertyMortgage {
    
    event Mortgage(
        address _from,
        string _houseAddress,
        string _owner,
        uint _mortgageAmount,
        uint _currentBalance,
        string _status
    );
    
    function emitMortgage(string memory houseAddress, string memory owner, uint mortgageAmount, 
    uint currentBalance, string memory status) public{
        emit Mortgage(msg.sender, houseAddress, owner, mortgageAmount, currentBalance, status);
    }
}

contract PropertyJudgement {
    
    event Judgement(
        address _from,
        string _houseAddress,
        string _owner,
        uint caseNumber,
        string description,
        string fileDate,
        uint amount
    );
    
    function emitJudgement(string memory houseAddress, string memory owner, uint caseNumber,
    string memory description, string memory fileDate, uint amount) public {
        emit Judgement(msg.sender, houseAddress, owner, caseNumber, description, fileDate, amount);
    }
}

