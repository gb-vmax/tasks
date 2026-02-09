# Bug Report

### Describe the bug

I'm encountering an issue where the processor's `process()` method doesn't work correctly when using the Promise-based API. When I call `process()` without a callback (expecting a Promise), it seems to hang or not resolve properly.

### Reproduction

```js
const processor = remark();

// Using promise-based API
processor.process('# Hello world')
  .then(file => {
    console.log(String(file));
  })
  .catch(err => {
    console.error('Error:', err);
  });

// The promise never resolves
```

### Expected behavior

The promise should resolve with the processed file result. When using the Promise API (not passing a callback), the method should properly resolve or reject the promise based on the processing outcome.

### Additional context

This seems to affect the async/await usage as well:

```js
async function processMarkdown() {
  const file = await processor.process('# Test');
  return String(file);
}
```

The function just hangs indefinitely. The callback-based API with `process(file, done)` might still work, but the Promise-based approach is broken.

---
Repository: /testbed
