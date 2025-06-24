CREATE TABLE users (
  user_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(40),
  email VARCHAR(100),
  phone VARCHAR(15),
  created_at TIMESTAMP DEFAULT current_timestamp
);
insert into users(name, email, phone)
values ('Adelard Dcunha', 'adelard@gmail.com', '8390190605')

select * from users;



CREATE TABLE expenses (
  expense_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(user_id),
  amount FLOAT,
  category VARCHAR(20),
  description VARCHAR(100),
  date TIMESTAMP DEFAULT current_timestamp,
  payment_mode VARCHAR(20)
);

insert into expenses(amount, user_id, category, description, payment_mode)
values (250, '8303c197-2587-4b36-a531-4f1bfdac7704', 'Food', 'Lunch at KFC', 'UPI')

select * from expenses;


create table bills(
  bill_id uuid primary key default gen_random_uuid(),
  user_id uuid references users(user_id),
  title varchar(20),
  due_date date,
  amount float,
  paid_status boolean default false,
  category varchar(20)
)
insert into bills (user_id, title, due_date, amount, paid_status, category)
values (
  '8303c197-2587-4b36-a531-4f1bfdac7704', 
  'Metro Tain pass',
  '2025-05-16',
  1200,
  false,
  'Travel'
  )

select * from bills


create table budgets (
  budget_id uuid primary key default gen_random_uuid(),
  user_id uuid references users(user_id),
  title varchar(40),
  amount float,
  start_date date,
  end_date date
)

insert into budgets (user_id, title, amount, start_date, end_date)
values (
  '8303c197-2587-4b36-a531-4f1bfdac7704', 
  'Software Engineer at EduvanceAI', 
  33000, 
  '2025-05-06', 
  '2025-06-06'
  )

select * from budgets

create table debts(
  debts_id uuid primary key default gen_random_uuid(),
  user_id uuid references users(user_id),
  lender_name varchar(100),
  amount float,
  due_date date,
  is_paid boolean default false
)
insert into debts(user_id, lender_name, amount, due_date, is_paid)
values (
  '8303c197-2587-4b36-a531-4f1bfdac7704', 
  'Axis Bank of India',
  2500000,
  '2035-05-06',
  false
  ) 

select * from debts

create table investments(
  investment_id uuid primary key default gen_random_uuid(),
  user_id uuid references users(user_id),
  type varchar(100),
  name varchar(100),
  amount float,
  purchase_date date,
)
insert into investments(user_id, type, name, amount, purchase_date)
values (
  '8303c197-2587-4b36-a531-4f1bfdac7704',
  'Stock Market',
  'Tata Consultancy',
  5000,
  '2025-05-05'
)

select * from investments