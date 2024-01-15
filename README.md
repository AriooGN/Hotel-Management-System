<h1>HotelDatabase: Hotel Management System</h1>

<p>Welcome to the HotelDatabase project, a robust application designed to streamline hotel management operations. This project is my initial venture into using Python's Tkinter library for GUI development, focusing on integrating backend processes with an interactive frontend.</p>

<h2>Introduction</h2>

<p>The HotelDatabase system is tailored for managing various hotel operations. As my first experience with Tkinter, the frontend design was a learning curve, leading to valuable insights into GUI development, although the code organization could have been more streamlined.</p>

<h2>Features</h2>

<ul>
    <li><b>Database Management:</b> Implements SQL scripts for managing hotel operations data, such as guest and staff information, room bookings, and financial transactions.</li>
    <li><b>User Interface:</b> Features a user-friendly interface developed using Tkinter, allowing easy interaction with the application.</li>
    <li><b>Data Entry and Validation:</b> Includes forms for entering and validating new data, ensuring accuracy and consistency.</li>
    <li><b>Reporting and Analytics:</b> Supports generating detailed reports and insights for efficient hotel management.</li>
</ul>

<h2>Technical Stack</h2>
<p>Frontend: Tkinter (Python), Backend: Python, Database: Oracle SQL</p>

<h2>Detailed Code Review</h2>

<p>The HotelDataBase project showcases a combination of frontend GUI development using Tkinter and backend processing in Python:</p>

<ul>
    <li><b>main.py:</b> Central script integrating GUI with backend logic. Handles user interaction, form submission, and database operations.</li>
    <li><b>TableView.py:</b> Responsible for displaying data in a table format using customtkinter widgets.</li>
    <li><b>oracleDB.py:</b> Manages database connections and executes SQL operations, ensuring data integrity.</li>
    <li><b>utils.py:</b> Contains utility functions for form creation and input validation.</li>
    <li><b>SQL Scripts:</b> Define the database schema and include queries for data management and reporting.</li>
    <li><b>GUI Screenshots:</b> Provide a visual representation of the application's interface.</li>
</ul>

<p>While the project is functional, the frontend code in <code>main.py</code> could benefit from greater modularity and separation of concerns for enhanced maintainability.</p>

<hr style="width:80%" color="black">

<h3>Login Screens</h3>
<div style="display: flex; justify-content: center; gap: 20px;">
  <img src="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/LoginFilled.png" alt="Login Screen">
  <img src="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/LoginFilledShowPass.png" alt="Login Screen (Show Password)">
</div>

<h3>Login Successful</h3>
<div align="center">
  <img src="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/LoginSuccesful.png" alt="Login Successful">
</div>

<h3>Main Menu</h3>
<div align="center"> <img src="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/MainMenu.png"> </a> </div>

<h3>Insert Menu</h3>
<div align="center"> <img src="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/InsertMenu.png"> </a> </div>

<h3>Queries Menu</h3>
<div align="center"> <img src="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/QueriesMenu.png"> </a> </div>

<h3>Query Results Presented Through TableView</h3>
<a href="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/Queries1.png" target="_blank">
    <img src="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/Queries1.png" alt="Queries 1" style="max-width: 100%; height: auto;">
</a>
<a href="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/Queries2.png" target="_blank">
    <img src="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/Queries2.png" alt="Queries 2" style="max-width: 100%; height: auto;">
</a>



<h3>Data Insert Forms</h3>
<div style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap; gap: 10px;">
    <a href="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/Passenger_Info.png" target="_blank">
        <img src="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/Passenger_Info.png" alt="Passenger Info Form" style="max-width: 100%; height: auto;">
    </a>
    <a href="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/PersonnelForm.png" target="_blank">
        <img src="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/PersonnelForm.png" alt="Personnel Form" style="max-width: 100%; height: auto;">
    </a>
    <a href="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/Personnel_Info.png" target="_blank">
        <img src="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/Personnel_Info.png" alt="Personnel Info" style="max-width: 100%; height: auto;">
    </a>
    <a href="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/ResInfoForm.png" target="_blank">
        <img src="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/ResInfoForm.png" alt="Reservation Info Form" style="max-width: 100%; height: auto;">
    </a>
    <a href="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/RoomForm.png" target="_blank">
        <img src="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/RoomForm.png" alt="Room Form" style="max-width: 100%; height: auto;">
    </a>
    <a href="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/RoomFormDropDown.png" target="_blank">
        <img src="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/RoomFormDropDown.png" alt="Room Form with Dropdown" style="max-width: 100%; height: auto;">
    </a>
    <a href="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/PaymentForm.png" target="_blank">
        <img src="https://github.com/AriooGN/HotelDataBase/blob/main/Screenshots/PaymentForm.png" alt="Payment Form" style="max-width: 100%; height: auto;">
    </a>
</div>



<h2>Project Reflection</h2>
<p>This project was an enlightening journey into the world of GUI development with Tkinter and also marked my first foray into SQL project development. It taught me about the importance of code organization and the intricacies involved in creating a functional and user-friendly interface. Additionally, this project allowed me to apply the principles of database normalization, which I learned throughout my database management class. The experience of organizing and structuring the tables in the database to achieve normalization was both challenging and rewarding, providing a strong foundation in database design.</p>

<h2>Contributions</h2>
<p>Feedback and contributions are welcomed to enhance the application's functionality and code quality.</p>
