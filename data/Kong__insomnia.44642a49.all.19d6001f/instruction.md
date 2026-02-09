# Bug Report

### Describe the bug

I'm experiencing an issue with the `database.all()` function where it's not returning the correct results. When the database is not empty, it seems to be calling the wrong internal method, which causes unexpected behavior in my application.

### Reproduction

```js
// Assuming the database is initialized and contains data
const results = await database.all('SomeModelType');

// Expected: Should return all documents of the specified type
// Actual: Returns incorrect results or behaves unexpectedly
```

The issue appears when:
1. The database has been initialized with data (not empty)
2. Calling `database.all()` with a valid type string
3. The function returns unexpected results instead of all documents of that type

### Expected behavior

`database.all()` should return all documents of the specified type from the database, regardless of whether the database is empty or not. The function should consistently fetch all records matching the type parameter.

### System Info
- Insomnia version: latest
- Platform: N/A

This seems like it might be related to the logic that checks the database state. The behavior is inconsistent depending on whether the database is empty or populated.

---
Repository: /testbed
