-- Dimension Tables

CREATE TABLE DimCity (
    CityID INT PRIMARY KEY,
    CityName VARCHAR(50) NOT NULL
);

CREATE TABLE DimDistrict (
    DistrictID INT PRIMARY KEY,
    DistrictName VARCHAR(100) NOT NULL,
    CityID INT NOT NULL,
    FOREIGN KEY (CityID) REFERENCES DimCity(CityID)
);

CREATE TABLE DimCustomer (
    CustID INT PRIMARY KEY,
    DistrictID INT NOT NULL,
    CustName VARCHAR(50) NOT NULL,
    CustEmail VARCHAR(50) NOT,
    CustAddress VARCHAR(50) NOT NULL,
    CustGender CHAR(1) NOT NULL,
    CustDOB DATE NOT NULL,
    CustBio VARCHAR(50) NOT NULL,
    FOREIGN KEY (DistrictID) REFERENCES DimDistrict(DistrictID)
);

CREATE TABLE DimStore (
    StoreID INT PRIMARY KEY,
    DistrictID INT NOT NULL,
    StoreName VARCHAR(50) NOT NULL,
    StoreAddress VARCHAR(100) NOT NULL,
    StoreArea VARCHAR(1) NOT NULL, -- Assuming this is a store area code or identifier
    FOREIGN KEY (DistrictID) REFERENCES DimDistrict(DistrictID)
);

CREATE TABLE DimCategory (
    CategoryID INT PRIMARY KEY,
    CategoryName VARCHAR(50) NOT NULL
);

CREATE TABLE DimProduct (
    ProductID INT PRIMARY KEY,
    CategoryID INT NOT NULL,
    ProductDesc VARCHAR(50) NOT NULL,
    FOREIGN KEY (CategoryID) REFERENCES DimCategory(CategoryID)
);

CREATE TABLE DimPayment (
    PaymentID INT PRIMARY KEY,
    PaymentName VARCHAR(10) NOT NULL
);

-- Fact Tables

CREATE TABLE FactTransactionHeader (
    TransHeaderID BIGINT PRIMARY KEY,
    StoreID INT NOT NULL,
    CustID INT NOT NULL,
    PaymentID INT NOT NULL, -- Assuming this is PaymentID
    TransDate DATE NOT NULL,
    TotalCost INT NOT NULL, -- Consider using DECIMAL for currency
    FOREIGN KEY (StoreID) REFERENCES DimStore(StoreID),
    FOREIGN KEY (CustID) REFERENCES DimCustomer(CustID),
    FOREIGN KEY (PaymentID) REFERENCES DimPayment(PaymentID)
);

CREATE TABLE FactTransactionItem (
    TransRecordID BIGINT PRIMARY KEY,
    TransHeaderID BIGINT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    Cost INT NOT NULL,
    TransDate DATE NOT NULL,
    FOREIGN KEY (TransHeaderID) REFERENCES FactTransactionHeader(TransHeaderID),
    FOREIGN KEY (ProductID) REFERENCES DimProduct(ProductID)
);

CREATE TABLE Product_Unit_Price (
    RecordID INT PRIMARY KEY,
    ProductID INT NOT NULL,
    UnitPrice INT NOT NULL, -- Consider using DECIMAL for currency
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    FOREIGN KEY (ProductID) REFERENCES DimProduct(ProductID)
);
