
import mysql.connector
import pytest

@pytest.fixture
def db():
    connection = mysql.connector.connect(
        host="localhost",
        port=3307,
        user="root",
        password="root",
        database="IT_Servicedesk"
    )
    yield connection
    connection.close()

def test_database_connection(db):
    assert db.is_connected()


def test_department_table(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Department")
    results = cursor.fetchall()
    assert results is not None
    cursor.close()


def test_employee_table(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Employee")
    assert cursor.fetchall() is not None
    cursor.close()


def test_ticket_table(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Tickets")
    assert cursor.fetchall() is not None
    cursor.close()


def test_retrieve_tickets(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Tickets")
    assert len(cursor.fetchall()) >= 0
    cursor.close()


def test_filter_open_tickets(db):
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM Tickets WHERE status='Open'"
    )
    results = cursor.fetchall()
    assert all(row[2] == 'Open' for row in results)
    cursor.close()


def test_join_query(db):
    cursor = db.cursor()
    cursor.execute("""
        SELECT Tickets.ticket_id, Employee.emp_name
        FROM Tickets
        INNER JOIN Employee
        ON Tickets.emp_id = Employee.emp_id
    """)
    assert cursor.fetchall() is not None
    cursor.close()


def test_aggregate_query(db):
    cursor = db.cursor()
    cursor.execute("""
        SELECT status, COUNT(*)
        FROM Tickets
        GROUP BY status
    """)
    assert cursor.fetchall() is not None
    cursor.close()


def test_duplicate_employee_id(db):
    cursor = db.cursor()
    cursor.execute("SELECT emp_id FROM Employee LIMIT 1")
    emp_id = cursor.fetchone()[0]

    with pytest.raises(mysql.connector.IntegrityError):
        cursor.execute(
            "INSERT INTO Employee VALUES (%s, %s, %s, %s)",
            (emp_id, 'Test', 'test@gmail.com', 1)
        )
    db.rollback()
    cursor.close()


def test_invalid_ticket_search(db):
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM Tickets WHERE ticket_id = -999"
    )
    assert cursor.fetchall() == []
    cursor.close()


def test_update_invalid_ticket(db):
    cursor = db.cursor()
    cursor.execute("""
        UPDATE Tickets SET status='Closed'
        WHERE ticket_id=-999
    """)
    assert cursor.rowcount == 0
    db.rollback()
    cursor.close()


def test_total_ticket_count(db):
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM Tickets")
    count = cursor.fetchone()[0]
    assert count >= 0
    cursor.close()
