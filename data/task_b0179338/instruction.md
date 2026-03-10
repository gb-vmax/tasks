I'm a technical writer cleaning up our API documentation. I have a file at `/home/user/docs/api_endpoints.txt` that lists all our API endpoints in a somewhat messy format. Each line looks like this:

```
[METHOD] /path/to/endpoint - Description of what it does
```

For example:
```
[GET] /api/users - Retrieve list of all users
[POST] /api/users - Create a new user
[DELETE] /api/users/{id} - Remove a user by ID
[GET] /api/products - List all products
```

I need you to do three things with this file:

**1. Create a sorted index file at `/home/user/docs/endpoints_index.txt`**

Extract just the endpoint paths (the `/api/...` parts, no method, no description) from every line, sort them alphabetically, remove any duplicates, and write them one per line to that file. The file should contain only the paths, nothing else.

**2. Create a filtered file at `/home/user/docs/get_endpoints.txt`**

Extract only the lines where the method is `GET`, and write them to this file exactly as they appear in the original (preserving the full original line format including method, path, and description), in the same order they appear in the source file. Do not sort or reformat them.

**3. Create a summary file at `/home/user/docs/endpoints_summary.txt`**

This file should contain a count of how many endpoints exist for each HTTP method. The format must be exactly:

```
DELETE: <count>
GET: <count>
POST: <count>
PUT: <count>
```

Only include methods that actually appear in the source file (skip methods with zero occurrences), and list them in alphabetical order. Each line must follow the pattern `METHOD: N` with no extra spaces.

Please process `/home/user/docs/api_endpoints.txt` and produce all three output files.
