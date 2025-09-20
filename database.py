import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('analysis_results.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS results (
            task_id TEXT PRIMARY_KEY,
            query TEXT,
            analysis TEXT,
            file_processed TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_result(task_id: str, query: str, analysis: str, file_processed: str):
    conn = sqlite3.connect('analysis_results.db')
    c = conn.cursor()
    c.execute('INSERT INTO results (task_id, query, analysis, file_processed, timestamp) VALUES (?, ?, ?, ?, ?)',
              (task_id, query, analysis, file_processed, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    conn.commit()
    conn.close()

def get_result(task_id: str):
    conn = sqlite3.connect('analysis_results.db')
    c = conn.cursor()
    c.execute('SELECT * FROM results WHERE task_id = ?', (task_id,))
    result = c.fetchone()
    conn.close()
    return result