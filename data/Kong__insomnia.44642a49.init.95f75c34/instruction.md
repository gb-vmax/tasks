# Bug Report

### Describe the bug

After a recent update, I'm seeing unexpected behavior with response objects. When creating new responses, the `bytesRead` property is being initialized to `-1` instead of `0`, and the `headers` property is being set to `null` instead of an empty array `[]`.

This is causing issues in my workflow where I check response metrics and iterate over headers. Code that previously worked now throws errors because it expects `headers` to be an array.

### Reproduction

```js
const response = init();

// This now returns -1 instead of 0
console.log(response.bytesRead); // Expected: 0, Actual: -1

// This now returns null instead of []
console.log(response.headers); // Expected: [], Actual: null

// This will throw an error now
response.headers.forEach(header => {
  // Process headers
});
```

### Expected behavior

- `bytesRead` should be initialized to `0` for new responses (not `-1`)
- `headers` should be initialized to an empty array `[]` (not `null`)

This seems like it might have been an unintended change when removing comments from the code. The previous behavior was more consistent with how the rest of the codebase handles these properties.

---
Repository: /testbed
