I'm building an ETL pipeline and need to verify data integrity for a batch of incoming CSV files before processing them. I have three raw data files sitting in `/home/user/etl/incoming/` — `customers.csv`, `orders.csv`, and `products.csv` — and I need to generate a checksum manifest so downstream pipeline steps can verify nothing got corrupted in transit.

Can you help me generate a SHA-256 checksum manifest file at `/home/user/etl/checksums.sha256`?

The file should contain exactly three lines, one per CSV file, in this format (which is the standard `sha256sum` output format):

```
<64-char hex hash>  <filename>
```

Note: there are **two spaces** between the hash and the filename, which is the standard `sha256sum` format. The filename should be just the bare filename (e.g., `customers.csv`), **not** a full or relative path like `./customers.csv` or `/home/user/etl/incoming/customers.csv`.

The lines must be sorted **alphabetically by filename**, so the order should be:
1. `customers.csv`
2. `orders.csv`
3. `products.csv`

After creating the manifest, verify it passes the `sha256sum --check` validation (run from the `/home/user/etl/incoming/` directory so the bare filenames resolve correctly). The check should report all three files as `OK` with no failures.

The final manifest file should be at `/home/user/etl/checksums.sha256` and must be ready for use by downstream pipeline consumers.
</think>
