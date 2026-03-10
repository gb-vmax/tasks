Hey, I need some help processing a product data file for our e-commerce website. We have a CSV export from our inventory system at `/home/user/store/products.csv` and I need to convert a filtered subset of it into a JSON file that our frontend API can consume.

Here's what I need:

1. Filter the CSV to only include rows where the `status` column is `active`.
2. Convert those rows to a JSON array, but with these field transformations:
   - Rename `product_id` → `id`
   - Rename `product_name` → `name`
   - Keep `price` as-is, but make sure it's a **number** (float), not a string
   - Keep `category` as-is (string)
   - Drop the `status` column entirely (it shouldn't appear in the output)
3. Write the result to `/home/user/store/active_products.json`.

The output JSON file must be an array of objects, one object per active product. The keys in each object must be in this order: `id`, `name`, `price`, `category`. The file should be pretty-printed with 2-space indentation. There should be no trailing newline after the closing `]`.

For example, a valid entry would look like:
```json
  {
    "id": "P001",
    "name": "Widget A",
    "price": 9.99,
    "category": "widgets"
  }
```

Please process the file and write the result to `/home/user/store/active_products.json`.
</think>
