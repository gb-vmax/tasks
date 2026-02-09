# Bug Report

### Describe the bug

I'm experiencing an issue with middleware execution order when using the `use()` function. Middleware functions appear to be executing in reverse order from how they're added, which is causing unexpected behavior in my processing pipeline.

### Reproduction

```js
const pipeline = trough();

pipeline
  .use((value, next) => {
    console.log('First middleware');
    next(null, value + ' -> first');
  })
  .use((value, next) => {
    console.log('Second middleware');
    next(null, value + ' -> second');
  })
  .use((value, next) => {
    console.log('Third middleware');
    next(null, value + ' -> third');
  });

pipeline.run('start', (err, result) => {
  console.log(result);
});
```

### Expected behavior

The middleware should execute in the order they were added:
```
First middleware
Second middleware
Third middleware
start -> first -> second -> third
```

### Actual behavior

The middleware executes in reverse order:
```
Third middleware
Second middleware
First middleware
start -> third -> second -> first
```

This breaks the expected flow when you need middleware to execute sequentially (e.g., validation before transformation before output).

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
