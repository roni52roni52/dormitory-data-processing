USE dormitory;

-- Optimizes queries that join students with rooms and calculate student age using birthday
CREATE INDEX idx_students_room_birthday
    ON students (room_id, birthday);

-- Optimizes queries that join students with rooms and check different sexes within each room
CREATE INDEX idx_students_room_sex
    ON students (room_id, sex);