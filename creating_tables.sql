CREATE TABLE IF NOT EXISTS
    Movies( movie_id INTEGER PRIMARY KEY,
            movie_name TEXT,
            movie_rating REAL );

CREATE TABLE IF NOT EXISTS
    Projection( id INTEGER PRIMARY KEY,
                movie_id INTEGER,
                projection_type TEXT,
                data Date,
                time TEXT
                FOREIGN KEY (movie_id) REFERENCES (Movies.movie_id)7
                );

CREATE TABLE IF NOT EXISTS
    Reservation( id INTEGER PRIMARY KEY,
                 username TEXT,
                 projection_id INTEGER,
                 row INTEGER,
                 collumn INTEGER,
                 FOREIGN KEY (projection_id) REFERENCES (Projection.id)
                 );

