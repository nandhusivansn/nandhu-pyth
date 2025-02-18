കൂradius=int(input("enter the radius of the circle"))
area=3.14*radius*radius
perimeter=2*3.14*radius
print(f"area of a circle is:{area}")
print(f"perimeter is :{perimeter}")
Data for locations:-

INSERT INTO locations (location_id,street_address,postal_code,city, state_province,country_id) VALUES ('1400', '2014 Jabberwocky Rd','26192', 'Southlake', 'Texas', 'US'), ('1500', '2011 Interiors Blvd', '99236', 'South San Francisco', 'California', 'US'), ('1700', '2004 Charade Rd', '98199',' Seattle', 'Washington', 'US'), ('1800','147 Spadina Ave','M5V 2L7', 'Toronto', 'Ontario', 'CA'), ('2400','8204 Arthur St', NULL, 'London', NULL, 'UK'), ('2500', 'Magdalen Centre, The Oxford Science Park', 'OX99ZB', 'Oxford', 'Oxford','UK'), ('2700', 'Schwanthalerstr. 7031', '80925', 'Munich', 'Bavaria', 'DE');

Data for jobs:-

INSERT INTO jobs(job_id,job_title,min_salary,max_salary) VALUES ('1', 'Public Accountant', 4200.00,9000.00), ('2', 'Accounting Manager', 8200.00,16000.00), ('3', 'Administration Assistant', 3000.00,6000.00), ('4', 'President', 20000.00,40000.00), ('5', 'Administration Vice President', 15000.00,30000.00), ('6', 'Accountant', 4200.00,9000.00), ('7', 'Finance Manager', 8200.00,16000.00), ('8', 'Human Resources Representative', 4000.00,9000.00), ('9', 'Programmer', 4000.00,10000.00), ('10', 'Marketing Manager', 9000.00,15000.00), ('11', 'Marketing Representative', 4000.00,9000.00), ('12', 'Public Relations Representative', 4500.00,10500.00), ('13', 'Purchasing Clerk', 2500.00,5500.00), ('14', 'Purchasing Manager', 8000.00,15000.00), ('15', 'Sales Manager', 10000.00,20000.00), ('16','Sales Representative', 6000.00,12000.00), ('17', 'Shipping Clerk', 2500.00,5500.00), ('18', 'Stock Clerk', 2000.00,5000.00), ('19', 'Stock Manager', 5500.00,8500.00);
Department of Computer Applications

INSERT INTO departments (department_id, department_name, location_id) VALUES

('1','Administration', '1700'), ('2', 'Marketing', '1800'), ('3', 'Purchasing', '1700'), ('4', 'Human Resources', '2400'), ('5', 'Shipping', '1500'), ('6', 'IT', '1400'), ('7', 'Public Relations', '2700'), ('8', 'Sales', '2500'), ('9', 'Executive', '1700'), ('10', 'Finance', '1700'), (11,' Accounting', 1700);

Data for employees:-

INSERT INTO employees(employee_id,first_name,last_name,email,phone_number,hire_date,

job_id, salary, manager_id,department_id) VALUES (100, 'Steven', 'King',

steven.king@sqltutorial.org', '515.123.4567', '1987-06-17',4,24000.00, NULL, 9),

(101, 'Neena', 'Kochhar', 'neena.kochhar@sqltutorial.org', '515.123.4568','1989-09-21', 5,17000.00, 100,9), (102, 'Lex', 'DeHaan', 'lex.de haan@sqltutorial.org', '515.123.4569', '1993-01-13',5,17000.00, 100,9), (103, 'Alexander', 'Hunold', 'alexander.hunold@sqltutorial.org', '590.423.4567', '1990-01-03',9,9000.00,102,6), (104, 'Bruce', 'Ernst', 'bruce.ernst@sqltutorial.org', '590.423.4568','1991-05-21',9,6000.00,103,6), (105, 'David', 'Austin','david.austin@sqltutorial.org','590.423.4569', '1997-06-25,9,4800.00,103,6), (106, 'Valli', 'Pataballa', 'valli.pataballa@sqltutorial.org', '590.423.4560','1998-02-05',9,4800.00,103,6), (107, 'Diana', 'Lorentz','diana.lorentz@sqltutorial.org', '590.423.5567', '1999-02-07,9,4200.00,103,6), (108, 'Nancy', 'Greenberg', 'nancy.greenberg@sqltutorial.org', '515.124.4569','1994-08-17',7,12000.00,101,10), (109, 'Daniel', 'Faviet',

'daniel.faviet@sqltutorial.org', '515.124.4169', '1994-08-16',6,9000.00,108,10), (110,'John', 'Chen','john.chen@sqltutorial.org', '515.124.4269','1997-09-28',6,8200.00,108,10), (111, 'Ismael', 'Sciarra', ismael.sciarra@sqitutorial.org', '515.124.4369','1997-09-30',6,7700.00, 108,10), (112, 'Jose Manuel', 'Urman', 'josemanuel.urman@sqltutorial.org', '515.124.4469','1998-03-07',6,7800.00,108,10), (113,'Luis', 'Popp', 'luis.popp@sqltutorial.org','515.124.4567', '1999-12-07',6,6900.00,108,10), (114,'Den', 'Raphaely','den.raphaely@sqltutorial.org', '515.127.4561','1994-12-07,14,11000.00,100,3), (115, Alexander', 'Khoo','alexander.khoo@sqltutorial.org', '515.127.4562', '1995-05-18',13,3100.00,114,3), (116, 'Shelli', 'Baida', 'shelli.baida@sqltutorial.org','515.127.4563', '1997-12-24',13,2900.00,114,3), (117, 'Sigal', Tobias', 'sigal.tobias@sqltutorial.org','515.127.4564', '1997-07-24',13,2800.00,114,3), (118, 'Guy', 'Himuro', 'guy.himuro@sqltutorial.org', '515.127.4565', '1998-11-15',13,2600.00,114,3), (119, 'Karen', 'Colmenares', 'karen.colmenares@sqitutorial.org', '515.127.4566',' 1999-08-10',13,2500.00,114,3), (120, 'Matthew', 'Weiss',

'matthew.weiss@sqltutorial.org','650.123.1234', '1996-07-18′,19,8000.00,100,5), (121, 'Adam', 'Fripp', adam.fripp@sqltutorial.org', '650.123.2234', '1997-04-10',19,8200.00,100,5), (122, 'Payam', 'Kaufling', 'payam.kaufling@sqltutorial.org', '650.123.3234', '1995-05-01',19,7900.00,100,5), (123, 'Shanta', 'Vollman', 'shanta.vollman@sqltutorial.org', '650.123.4234','1997-10-10',19,6500.00,