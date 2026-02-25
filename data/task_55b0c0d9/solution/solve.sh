#!/bin/bash
set -e
cd /home/user

sqlite3 /home/user/ml_data/new_training_data.db 'CREATE TABLE IF NOT EXISTS train_samples (id INTEGER, sentence TEXT, label INTEGER); INSERT INTO train_samples SELECT * FROM "/home/user/ml_data/old_training_data.db".train_samples;' ".mode insert" ".import /home/user/ml_data/old_training_data.db train_samples"
sqlite3 /home/user/ml_data/new_training_data.db "ATTACH '/home/user/ml_data/old_training_data.db' AS old; CREATE TABLE IF NOT EXISTS train_samples (id INTEGER, sentence TEXT, label INTEGER); INSERT INTO train_samples SELECT * FROM old.train_samples; DETACH old;"
old_count=$(sqlite3 /home/user/ml_data/old_training_data.db "SELECT COUNT(*) FROM train_samples;"); new_count=$(sqlite3 /home/user/ml_data/new_training_data.db "SELECT COUNT(*) FROM train_samples;"); echo -e "Record count in old_training_data.db: $old_count\nRecord count in new_training_data.db: $new_count\nMigration successful: $( [ "$old_count" = "$new_count" ] && echo yes || echo no )" > /home/user/ml_data/migration_validation.log
cat /home/user/ml_data/migration_validation.log
