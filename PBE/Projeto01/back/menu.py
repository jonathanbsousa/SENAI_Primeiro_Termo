import pandas as pd
import sqlite3

class ProdutoCRUD:
    def __init__(self, db_name = 'db.sqlite3'):
        self.conn = sqlite3.connect(db_name)