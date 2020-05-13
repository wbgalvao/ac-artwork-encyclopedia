DROP TABLE IF EXISTS artwork;

CREATE TABLE artwork (
    id SERIAL PRIMARY KEY,
    animal_crossing_name TEXT UNIQUE NOT NULL,
    real_life_name TEXT NOT NULL,
    real_life_author TEXT NOT NULL,
    authenticity_helper_info TEXT NOT NULL,
    polygon_image_url TEXT NOT NULL
);