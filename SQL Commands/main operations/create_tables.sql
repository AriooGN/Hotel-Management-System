-- Hotel Managment Database

-- Passenger_ID table
CREATE TABLE Passenger_ID (
    Customer_Id INT NOT NULL,
    Phone VARCHAR2 (10) NOT NULL,
    Email VARCHAR2 (100) NOT NULL,
    PRIMARY KEY (Customer_Id),
    UNIQUE (Phone),
    UNIQUE (Email)
);
          
CREATE TABLE Passenger_INFO (
    Email VARCHAR2(100) NOT NULL,
    Phone VARCHAR2(10) NOT NULL,
    FirstN VARCHAR2(50),
    MiddleN VARCHAR2(50),
    LastN VARCHAR2(50),
    city VARCHAR2(25),
    postalCode VARCHAR2(10),
    street VARCHAR2(50),
    province VARCHAR2(25),
    PRIMARY KEY (Email, Phone),
    FOREIGN KEY (Email) REFERENCES Passenger_ID(Email),
    FOREIGN KEY (Phone) REFERENCES Passenger_ID(Phone)
);

-- Personnel_ID table      
CREATE TABLE Personnel_ID (
    NIN INT NOT NULL,
    FirstN VARCHAR2 (50) NOT NULL,
    MiddleN VARCHAR2 (50),
    LastN VARCHAR2 (50) NOT NULL,
    PRIMARY KEY (NIN)
);

-- Personnel_info table          
CREATE TABLE Personnel_INFO (
    NIN INT,
    Salary DECIMAL (10,2),
    Date_of_Birth DATE,
    Street VARCHAR2 (255),
    home_number VARCHAR2 (50),
    City VARCHAR2 (100),
    province VARCHAR2 (100),
    postalcode VARCHAR2 (10),
    FOREIGN KEY (NIN) REFERENCES Personnel_ID(NIN)
);

-- Payment table
CREATE TABLE Payment (
    Payment_ID INT NOT NULL,
    PaymentAmount NUMBER(10,2),
    TransactionType VARCHAR2 (50),
    PRIMARY KEY (Payment_ID)
);

-- Reservation table
CREATE TABLE Reservation (
    Reservation_ID INT NOT NULL,
    CheckInDate DATE NOT NULL,
    CheckOutDate DATE NOT NULL,
    PRIMARY KEY (Reservation_ID)
);

-- Room table
CREATE TABLE Room (
    RoomNumber INT NOT NULL,
    NumberOfBed INT,
    PricePerNight NUMBER (10,2),
    PRIMARY KEY (RoomNumber)
);

-- SingleRoom table
CREATE TABLE SingleRoom (
    RoomNumber INT NOT NULL,
    SizeOfBed VARCHAR2(10),
    FOREIGN KEY (RoomNumber) REFERENCES Room(RoomNumber)
);
         
-- TwinRoom table
CREATE TABLE TwinRoom (
    RoomNumber INT NOT NULL,
    SizeOfBed VARCHAR2 (10),
    FOREIGN KEY (RoomNumber) REFERENCES Room(RoomNumber)
);
            
-- KingRoom table
CREATE TABLE KingRoom (
    RoomNumber INT NOT NULL,
    SizeOfBed VARCHAR2 (10),
    FOREIGN KEY (RoomNumber) REFERENCES Room(RoomNumber)
);

-- RoomState table
CREATE TABLE RoomState (
    Reservation_ID INT NOT NULL,
    RoomNumber INT NOT NULL,
    RoomStatus CHAR(1) CHECK (RoomStatus IN ('O', 'A')), -- 'O' Occupy and 'A' Available 
    PRIMARY KEY (Reservation_ID, RoomNumber),
    FOREIGN KEY (RoomNumber) REFERENCES Room(RoomNumber)
);

-- Balance table
CREATE TABLE Balance (
    Reservation_ID INT NOT NULL,
    Payment_ID INT NOT NULL,
    Customer_Id INT NOT NULL,
    Account_Balance NUMBER(10,2),
    FOREIGN KEY (Payment_ID) REFERENCES Payment(Payment_ID),
    FOREIGN KEY (Customer_Id) REFERENCES Passenger_ID(Customer_Id),
    FOREIGN KEY (Reservation_ID) REFERENCES Reservation(Reservation_ID)
);