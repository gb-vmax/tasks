# Bug Report

### Describe the bug

I'm experiencing an issue where the first element of arrays in environment variables is not being properly tracked or rendered. When I reference array elements in my templates using bracket notation, the first element (index 0) seems to be skipped or ignored.

### Reproduction

```js
// Environment variable setup
{
  "myArray": ["first", "second", "third"]
}

// Template usage
{{ _.myArray[0] }}  // This doesn't work - returns undefined or empty
{{ _.myArray[1] }}  // This works - returns "second"
{{ _.myArray[2] }}  // This works - returns "third"
```

The first element of the array is not accessible, but all subsequent elements work fine. This also affects nested objects within arrays - the first item is always missing.

### Expected behavior

All array elements should be accessible, including the element at index 0. `{{ _.myArray[0] }}` should return `"first"`.

### Additional context

This seems to have started recently. I'm using arrays in environment variables to store lists of API endpoints, and now I can't access the first endpoint in any of my arrays. As a workaround, I've been adding a dummy element at index 0, but this is not ideal.

---
Repository: /testbed
