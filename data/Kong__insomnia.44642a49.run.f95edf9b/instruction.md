# Bug Report

### Describe the bug

The OS template tag is not handling array indexing correctly when using bracket notation in the function name. When trying to access a specific element from an array-returning OS function like `cpus[0]`, the indexing doesn't work as expected and the full array is returned instead of the indexed element.

### Reproduction

```js
// Trying to get the first CPU from the cpus array
{{ _.os.cpus[0] }}

// Expected: Returns the first CPU object
// Actual: Returns the entire cpus array or doesn't parse the index correctly
```

Also having issues with negative indexing:
```js
// Trying to get the last CPU
{{ _.os.cpus[-1] }}

// This should return the last element but doesn't work
```

### Expected behavior

When using bracket notation with array indices (e.g., `cpus[0]`, `cpus[-1]`), the template tag should:
1. Parse the function name to extract the base function and index
2. Call the OS function to get the array
3. Return the element at the specified index
4. Support negative indices to access elements from the end of the array

### Additional context

This seems to be related to how the template tag parses the `fnName` parameter. The current implementation doesn't appear to handle bracket notation for array access, so it's likely treating `cpus[0]` as a literal function name rather than parsing out the index.

---
Repository: /testbed
