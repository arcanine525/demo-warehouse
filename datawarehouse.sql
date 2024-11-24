-- Dimension Tables

CREATE TABLE DimCity (
    CityID VARCHAR(2) PRIMARY KEY,
    CityName VARCHAR(10) NOT NULL,
    PostalCode VARCHAR(10) NOT NULL
);

CREATE TABLE DimDistrict (
    DistrictID VARCHAR(2) PRIMARY KEY,
    DistrictName VARCHAR(10) NOT NULL,
    CityID VARCHAR(2) NOT NULL,
    FOREIGN KEY (CityID) REFERENCES DimCity(CityID)
);

CREATE TABLE DimCustomer (
    CustID VARCHAR(10) PRIMARY KEY,
    DistrictID VARCHAR(2) NOT NULL,
    CityID VARCHAR(2) NOT NULL, -- Added CityID (based on your diagram)
    CustName VARCHAR(10) NOT NULL,
    CustEmail VARCHAR(50),
    CustAddress VARCHAR(50),
    CustGender CHAR(1) NOT NULL,
    CustDOB DATE NOT NULL,
    CustBio VARCHAR(50),
    FOREIGN KEY (DistrictID) REFERENCES DimDistrict(DistrictID),
    FOREIGN KEY (CityID) REFERENCES DimCity(CityID)
);

CREATE TABLE DimStore (
    StoreID VARCHAR(4) PRIMARY KEY,
    DistrictID VARCHAR(2) NOT NULL,
    StoreName VARCHAR(50) NOT NULL,
    StoreAddress VARCHAR(10) NOT NULL,
    StoreArea VARCHAR(1) NOT NULL, -- Assuming this is a store area code or identifier
    FOREIGN KEY (DistrictID) REFERENCES DimDistrict(DistrictID)
);

CREATE TABLE DimCategory (
    CategoryID VARCHAR(10) PRIMARY KEY,
    CategoryName VARCHAR(50) NOT NULL
);

CREATE TABLE DimProduct (
    ProductID VARCHAR(10) PRIMARY KEY,
    CategoryID VARCHAR(10) NOT NULL,
    ProductDesc VARCHAR(50) NOT NULL,
    FOREIGN KEY (CategoryID) REFERENCES DimCategory(CategoryID)
);

CREATE TABLE DimPayment (
    PaymentID VARCHAR(2) PRIMARY KEY,
    PaymentName VARCHAR(10) NOT NULL
);

-- Fact Tables

CREATE TABLE FactTransactionHeader (
    TransID VARCHAR(10) PRIMARY KEY,
    StoreID VARCHAR(4) NOT NULL,
    CustID VARCHAR(10) NOT NULL,
    PaymentID VARCHAR(2) NOT NULL, -- Assuming this is PaymentID
    TransDate DATE NOT NULL,
    TotalCost INT NOT NULL, -- Consider using DECIMAL for currency
    FOREIGN KEY (StoreID) REFERENCES DimStore(StoreID),
    FOREIGN KEY (CustID) REFERENCES DimCustomer(CustID),
    FOREIGN KEY (PaymentID) REFERENCES DimPayment(PaymentID)
);

CREATE TABLE FactTransactionItem (
    TransRecordID VARCHAR(10) PRIMARY KEY,
    TransID VARCHAR(10) NOT NULL,
    -- ItemNo VARCHAR(2) NOT NULL, -- Assuming this is an item number within the transaction
    ProductID VARCHAR(10) NOT NULL,
    ProductDesc VARCHAR(50) NOT NULL, -- Consider removing if redundant with DimProduct
    Quantity INT NOT NULL,
    Cost INT NOT NULL,
    TransDate DATE NOT NULL,
    FOREIGN KEY (TransID) REFERENCES FactTransactionHeader(TransID),
    FOREIGN KEY (ProductID) REFERENCES DimProduct(ProductID)
);

CREATE TABLE Product_Unit_Price (
    RecordID INT PRIMARY KEY,
    ProductID VARCHAR(10) NOT NULL,
    UnitPrice INT NOT NULL, -- Consider using DECIMAL for currency
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    FOREIGN KEY (ProductID) REFERENCES DimProduct(ProductID)
);
