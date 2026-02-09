# Bug Report

### Describe the bug

After a recent update, the OS template tag is not working correctly when using JSONPath filters with array indices. When trying to access a specific array element using bracket notation (e.g., `[0]`, `[1]`), the template always returns the first element regardless of the specified index.

### Reproduction

```js
// Template using OS tag with cpus function
{% os 'cpus', '$[1].model' %}

// Expected: Returns the model of the second CPU
// Actual: Always returns the model of the first CPU
```

Another example:
```js
// Trying to access different CPU cores
{% os 'cpus', '$.cpus[2].speed' %}

// Expected: Returns speed of third CPU core
// Actual: Returns speed of first CPU core instead
```

### Expected behavior

When using JSONPath filters with specific array indices, the template should return the element at the specified index, not always the first element. For example:
- `$[0]` should return the first element
- `$[1]` should return the second element  
- `$[2]` should return the third element
- etc.

### System Info
- Insomnia version: Latest
- OS: Multiple (Windows/Mac/Linux)

This seems to have started happening after the recent templating changes. The array index in the filter is being ignored and it always defaults to index 0.

---
Repository: /testbed
