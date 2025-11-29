import sqlite3

def create_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professions (
            profession TEXT,
            much INTEGER
        )
    ''')

    cursor.execute('''
        INSERT INTO professions VALUES
            ('doctor', 0),
            ('architect', 0),
            ('programmer', 0),
            ('teacher', 0),
            ('designer', 0),
            ('engineer', 0),
            ('journalist', 0),
            ('lawyer', 0),
            ('entrepreneur', 0),
            ('biotechnologist', 0),
            ('jeweler', 0)
    ''')

    conn.commit()
    conn.close()

def plus_doctor(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE professions
        SET much = much + 1
        WHERE profession = 'doctor'
    ''')

    conn.commit()
    conn.close()
def plus_architect(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE professions
        SET much = much + 1
        WHERE profession = 'architect'
    ''')

    conn.commit()
    conn.close()

def plus_programmer(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE professions
        SET much = much + 1
        WHERE profession = 'programmer'
    ''')

    conn.commit()
    conn.close()

def plus_teacher(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE professions
        SET much = much + 1
        WHERE profession = 'teacher'
    ''')

    conn.commit()
    conn.close()

def plus_designer(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE professions
        SET much = much + 1
        WHERE profession = 'designer'
    ''')

    conn.commit()
    conn.close()

def plus_engineer(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE profession
        SET much = much + 1
        WHERE profession = 'engineer'
    ''')

    conn.commit()
    conn.close()

def plus_journalist(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE professions
        SET much = much + 1
        WHERE profession = 'journalist'
    ''')

    conn.commit()
    conn.close()

def plus_lawyer(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE professions
        SET much = much + 1
        WHERE profession = 'lawyer'
    ''')

    conn.commit()
    conn.close()

def plus_entrepreneur(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE professions
        SET much = much + 1
        WHERE profession = 'entrepreneur'
    ''')

    conn.commit()
    conn.close()

def plus_biotechnologist(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE professions
        SET much = much + 1
        WHERE profession = 'biotechnologist'
    ''')

    conn.commit()
    conn.close()

def plus_jeweler(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE professions
        SET much = much + 1
        WHERE profession = 'jeweler'
    ''')

    conn.commit()
    conn.close()
def top_professions(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT profession, much
        FROM professions
        ORDER BY much DESC
        LIMIT 3
    ''')

    results = cursor.fetchall()
    conn.close()
    return results

