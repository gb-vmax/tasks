# Bug Report

### Describe the bug

I'm experiencing an issue where async functions are not being detected correctly. When I have an async function in my code, the bundler seems to treat it as a regular synchronous function, which is causing problems with my build output.

### Reproduction

```js
// This async function is not being recognized as async
async function fetchData() {
  const response = await fetch('/api/data');
  return response.json();
}

// The bundler treats this as if it were:
function fetchData() {
  const response = await fetch('/api/data');
  return response.json();
}
```

When bundling code with async functions, they seem to lose their async nature. This is breaking my application because the generated code doesn't properly handle the async/await pattern.

### Expected behavior

Async functions should be correctly identified and preserved as async in the output. The bundler should recognize when a function is declared with the `async` keyword and maintain that property throughout the compilation process.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This seems to have started recently, possibly after a recent update. The async detection logic might not be working as expected.

---
Repository: /testbed
