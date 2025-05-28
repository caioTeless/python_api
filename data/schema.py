TABLE_SCHEMA = [
    {
        'name': 'users',
        'query': '''
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            password_confirmation TEXT NOT NULL,
            birthdate TEXT NOT NULL,
            active INTEGER default 0,
            created_at TEXT,
            updated_at TEXT
            )
        '''
    },
    {
        'name': 'transactions',
        'query': '''
            CREATE TABLE IF NOT EXISTS transactions(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            date TEXT NOT NULL, 
            value REAL, 
            description TEXT, 
            type INTEGER,
            user_id INTEGER,
            responsible TEXT,
            category_id INTEGER,
            created_at TEXT,
            updated_at TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
            )
        '''
    },
    {
        'name': 'configurations',
        'query': '''
            CREATE TABLE IF NOT EXISTS configurations(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            description TEXT NOT NULL,
            active INTEGER default 0,
            user_id INTEGER,
            created_at TEXT,
            updated_at TEXT,
            UNIQUE(type, user_id) ON CONFLICT REPLACE,
            FOREIGN KEY(user_id) REFERENCES users(id)
            )
        '''
    },
    {
        'name': 'automations',
        'query': '''
            CREATE TABLE IF NOT EXISTS automations(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            generation_date TEXT NOT NULL,
            user_id INTEGER,
            created_at TEXT,
            updated_at TEXT,
            FOREIGN KEY(transaction_id) REFERENCES transactions(id),
            FOREIGN KEY(user_id) REFERENCES users(id)
            )
        '''
    },
    {
        'name': 'products',
        'query': '''
            CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            value TEXT NOT NULL,
            user_id INTEGER,
            created_at TEXT,
            updated_at TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
            )
        '''
    }
]
