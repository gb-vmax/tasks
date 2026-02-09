# Bug Report

### Describe the bug

I'm encountering an issue where async functions are not being properly detected. When I define an async function in my code, the bundler seems to treat it as a regular synchronous function, which causes problems with the generated output.

### Reproduction

```js
async function fetchData() {
  const response = await fetch('/api/data');
  return response.json();
}

// The function is treated as synchronous
// Expected: Should be recognized as async
```

When bundling code that contains async functions, they're not being identified correctly. This affects tree-shaking and code generation - async functions should be handled differently than regular functions but they're being processed the same way.

### Expected behavior

Async functions should be properly detected and marked as asynchronous during the AST parsing phase. The bundler should recognize the `async` keyword and handle these functions accordingly.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. Not sure if it's related to a recent change but wanted to report it in case others are seeing the same issue.

---
Repository: /testbed
