# Bug Report

### Describe the bug

I'm encountering an issue with async function detection. When working with async functions in my code, the `async` property seems to be inverted - async functions are being treated as non-async and vice versa.

### Reproduction

```js
// Define an async function
async function myAsyncFunction() {
  return await Promise.resolve('test');
}

// The function should be detected as async
// but it's being treated as non-async

// Similarly, regular functions are being detected as async
function regularFunction() {
  return 'test';
}
```

When checking whether functions are async or not, the behavior is completely reversed from what's expected.

### Expected behavior

- Async functions should be correctly identified as async (async property should be `true`)
- Regular synchronous functions should be identified as non-async (async property should be `false`)

The async flag appears to be inverted somewhere in the processing logic.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
