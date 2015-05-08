DROP TABLE IF EXISTS Movies;
DROP TABLE IF EXISTS Projection;
DROP TABLE IF EXISTS Reservation;

CREATE TABLE
    Movies( movie_id INTEGER PRIMARY KEY,
            movie_name TEXT,
            movie_rating REAL );

CREATE TABLE
    Projection( id INTEGER PRIMARY KEY,
                movie_id INTEGER,
                projection_type TEXT,
                data Date,
                time TEXT,
                FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
                UNIQUE(data, time, movie_id, projection_type)
                );

CREATE TABLE
    Reservation( id INTEGER PRIMARY KEY,
                 username TEXT UNIQUE,
                 projection_id INTEGER,
                 row INTEGER,
                 column INTEGER,
                 FOREIGN KEY (projection_id) REFERENCES Projection(id),
                 UNIQUE(row, column)
                 );

