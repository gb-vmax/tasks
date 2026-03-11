FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

DATASETS_DIR="/home/user/datasets"

mkdir -p "$DATASETS_DIR/genomics"
mkdir -p "$DATASETS_DIR/climate"
mkdir -p "$DATASETS_DIR/imaging"
mkdir -p "$DATASETS_DIR/text_corpus"

# genomics
python3 -c "print('A' * 3500, end='')" > "$DATASETS_DIR/genomics/reference.bin"
python3 -c "print('B' * 1800, end='')" > "$DATASETS_DIR/genomics/samples.csv"
python3 -c "print('C' * 400, end='')" > "$DATASETS_DIR/genomics/notes.txt"

# climate
python3 -c "print('D' * 2500, end='')" > "$DATASETS_DIR/climate/temperatures.csv"
python3 -c "print('E' * 900, end='')" > "$DATASETS_DIR/climate/metadata.json"
python3 -c "print('F' * 600, end='')" > "$DATASETS_DIR/climate/errors.log"

# imaging
python3 -c "print('G' * 4100, end='')" > "$DATASETS_DIR/imaging/scan001.bin"
python3 -c "print('H' * 3200, end='')" > "$DATASETS_DIR/imaging/scan002.bin"
python3 -c "print('I' * 750, end='')" > "$DATASETS_DIR/imaging/labels.csv"
python3 -c "print('J' * 120, end='')" > "$DATASETS_DIR/imaging/readme.txt"

# text_corpus
python3 -c "print('K' * 1500, end='')" > "$DATASETS_DIR/text_corpus/articles.txt"
python3 -c "print('L' * 300, end='')" > "$DATASETS_DIR/text_corpus/stopwords.txt"

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
