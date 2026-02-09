# Bug Report

### Describe the bug
The `getContentTypeName()` function is returning incorrect content type names. When calling the function with `useLong=false`, it returns the long format name instead of the short format, and vice versa.

### Reproduction
```js
// Getting short name but receives long name instead
const shortName = getContentTypeName('application/json', false);
console.log(shortName); // Expected: 'JSON', Actual: 'JavaScript Object Notation'

// Getting long name but receives short name instead  
const longName = getContentTypeName('application/json', true);
console.log(longName); // Expected: 'JavaScript Object Notation', Actual: 'JSON'
```

### Expected behavior
- When `useLong` is `false`, the function should return the short format name
- When `useLong` is `true`, the function should return the long format name

### Additional context
This affects all content types including the fallback to `CONTENT_TYPE_OTHER`. The returned names are consistently swapped between short and long formats.

---
Repository: /testbed
