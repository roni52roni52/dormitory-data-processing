# Dormitory Data Processing Application

A Python application that loads rooms and students data from JSON files,
stores the data in a MySQL database, executes analytical SQL queries,
and exports the results to JSON or XML.

## Features

- Load rooms and students from JSON files
- Store data in a MySQL relational database
- Many-to-one relationship between students and rooms
- Execute analytical queries using SQL
- Export query results to JSON or XML
- Command-line interface for input files and output format
- Query optimization using database indexes
- Object-oriented architecture
- No ORM - database operations are implemented using SQL

## Database Queries

The application executes the following queries:

1. List of rooms and the number of students in each room
2. Five rooms with the smallest average student age
3. Five rooms with the largest difference in student ages
4. List of rooms where students of different sexes live

## Project Structure

```text
Dormitory/
├── database/
│   ├── connection.py
│   ├── query_repository.py
│   ├── room_repository.py
│   └── student_repository.py
├── exporters/
│   ├── exporter.py
│   ├── json_exporter.py
│   └── xml_exporter.py
├── loaders/
│   └── json_loader.py
├── sql/
│   ├── schema.sql
│   └── indexes.sql
├── config.py
├── main.py
├── requirements.txt
└── README.md

### Responsibilities

- `DatabaseConnection` - manages the MySQL database connection.
- `JsonLoader` - loads input data from JSON files.
- `RoomRepository` - handles database operations for rooms.
- `StudentRepository` - handles database operations for students.
- `QueryRepository` - executes analytical SQL queries.
- `JsonExporter` - exports query results to JSON.
- `XmlExporter` - exports query results to XML.
- `Exporter` - defines the common interface for result exporters.
- `main.py` - handles command-line arguments and coordinates the application.

## Requirements

- Python 3
- MySQL Server
- `mysql-connector-python`

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Database Setup

Create the database and tables using:

```text
sql/schema.sql
```

The database contains two tables:

- `rooms`
- `students`

A room can contain multiple students, while each student belongs to one room.

The relationship is implemented using:

```text
students.room_id -> rooms.id
```

## Database Configuration

Database connection settings are read from environment variables.

Example for Windows PowerShell:

```powershell
$env:DB_PASSWORD="your_mysql_password"
```

Optional environment variables:

```text
DB_HOST
DB_PORT
DB_USER
DB_PASSWORD
DB_NAME
```

Default configuration uses:

```text
host: localhost
port: 3306
user: root
database: dormitory
```

## Usage

The application requires three command-line arguments:

- `--students` - path to the students JSON file
- `--rooms` - path to the rooms JSON file
- `--format` - output format (`json` or `xml`)

Example with JSON output:

```bash
python main.py --students data/students.json --rooms data/rooms.json --format json
```

Example with XML output:

```bash
python main.py --students data/students.json --rooms data/rooms.json --format xml
```

Depending on the selected format, the application generates:

```text
results.json
```

or:

```text
results.xml
```

## Query Optimization

The application includes SQL indexes designed for the analytical queries.

The indexes are defined in:

```text
sql/indexes.sql
```

The following composite indexes are used:

```sql
CREATE INDEX idx_students_room_birthday
    ON students (room_id, birthday);

CREATE INDEX idx_students_room_sex
    ON students (room_id, sex);
```

The `(room_id, birthday)` index supports queries that group students by room and calculate age-related statistics.

The `(room_id, sex)` index supports queries that group students by room and determine whether students of different sexes live in the same room.

The primary key on `rooms.id` is already indexed, and MySQL also requires an appropriate index for the foreign key relationship involving `students.room_id`.

## OOP and SOLID

The application separates responsibilities between database connection management, data loading, repositories, analytical queries, and result exporters.

The exporter implementations share a common `Exporter` abstraction, allowing JSON and XML output implementations to follow the same interface.

This structure keeps individual classes focused on a single responsibility and makes the application easier to extend and maintain.

## Technologies

- Python
- MySQL
- mysql-connector-python
- JSON
- XML