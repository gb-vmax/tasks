Hey, I'm testing an integration with a third-party user management API and I need your help transforming the response into a flat CSV format that our internal system expects.

I've already captured an API response and saved it to `/home/user/api_response.json`. The file contains a JSON object with a top-level key `"users"`, which is an array of user objects. Each user object has the following structure:

```json
{
  "id": 42,
  "username": "jdoe",
  "email": "jdoe@example.com",
  "status": "active",
  "profile": {
    "first_name": "John",
    "last_name": "Doe",
    "department": "Engineering"
  },
  "created_at": "2024-01-15"
}
```

I need you to do the following:

1. Filter the users array to include **only users whose `status` is `"active"`**.

2. From those active users, extract these fields and produce a CSV file at `/home/user/active_users.csv` with the following **exact column order and header**:

```
id,username,email,first_name,last_name,department,created_at
```

- `id` comes from the top-level user object
- `first_name`, `last_name`, and `department` come from the nested `profile` object
- Rows should be sorted by `id` in **ascending numeric order**
- No extra spaces around commas, no trailing commas, no surrounding quotes on values (unless a value itself contains a comma, but none of these values do)

3. After creating the CSV, count the number of data rows (excluding the header line) and write that count as a plain integer on a single line to `/home/user/active_count.txt`.

The final `/home/user/active_users.csv` should have a header line followed by one line per active user, and `/home/user/active_count.txt` should contain just the integer count of those rows.
