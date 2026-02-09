# Bug Report

### Describe the bug
When calling `database.all()` on an empty database, the function returns incorrect results. The logic appears to be inverted - it's checking for `!db._empty` instead of `db._empty`, which causes the function to use the wrong code path depending on whether the database is empty or not.

### Reproduction
```js
// When the database is empty
const results = await database.all('SomeModel');
// Expected: Should use _send() to fetch all records
// Actual: Uses database.find() instead

// When the database is NOT empty
const results = await database.all('SomeModel');
// Expected: Should use database.find() 
// Actual: Uses _send() instead
```

### Expected behavior
The `database.all()` method should use `_send()` when the database is empty (`db._empty === true`) and use `database.find()` when the database is not empty (`db._empty === false`). Currently the behavior is reversed.

### Additional context
This is causing issues when trying to fetch all records of a specific type, as the wrong method is being called based on the database state.

---
Repository: /testbed
