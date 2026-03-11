Hey, I just started a new machine learning research project and I need help setting up my dataset directory structure. I have a bunch of datasets I'll be working with and I want everything organized properly from the start.

Can you set up the following directory structure under `/home/user/research/datasets`?

```
/home/user/research/datasets/
├── raw/
│   ├── images/
│   └── tabular/
├── processed/
│   ├── train/
│   ├── val/
│   └── test/
└── archive/
```

All of those should be actual directories (not files).

Once the directories are created, please create an index file at `/home/user/research/datasets/INDEX.txt` with exactly this content (including the blank lines and spacing as shown):

```
DATASET REGISTRY
================

raw/images       - unprocessed image files
raw/tabular      - unprocessed CSV and tabular data
processed/train  - training split
processed/val    - validation split
processed/test   - test split
archive          - deprecated or backed-up datasets
```

Finally, I want to make sure the `archive/` directory is protected from accidental writes. Please set its permissions to read and execute only for the owner (no write permission for anyone), i.e., `dr-x------` (octal `500`).

Everything else can keep the default permissions from when the directories were created.

To confirm everything looks right, could you also verify that running `ls -ld /home/user/research/datasets/archive` shows permissions starting with `dr-x------`?
