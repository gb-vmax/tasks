# Bug Report

### Describe the bug

The `database.all()` function is returning incorrect data types after a recent change. When the database is not empty, it appears to be returning a single object instead of an array of objects.

### Reproduction

```js
// Assuming we have some data in the database
const requests = await database.all('Request');

// Expected: requests should be an array
// Actual: requests is a single object or wrong type

console.log(Array.isArray(requests)); // Should be true but isn't
```

### Steps to reproduce:
1. Initialize a database with some data (non-empty state)
2. Call `database.all()` with any model type
3. The return type is not an array as expected

### Expected behavior

`database.all()` should consistently return an array of models (T[]) regardless of whether the database is empty or not. Currently it seems to be returning the wrong type when the database is not empty.

### Additional context

This is affecting any code that expects `database.all()` to return an array and tries to use array methods like `.map()`, `.filter()`, etc. on the result.

---
Repository: /testbed
