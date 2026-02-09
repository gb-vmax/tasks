# Bug Report

### Describe the bug

I'm experiencing an infinite loop/stack overflow when using `await` expressions in my code. The bundler hangs and eventually crashes with a "Maximum call stack size exceeded" error.

### Reproduction

```js
async function fetchData() {
  const result = await fetch('/api/data');
  return result.json();
}

// Using this in a module causes the bundler to crash
export { fetchData };
```

When I try to bundle code containing await expressions, the process never completes and eventually crashes. This seems to happen specifically when the await expression is being analyzed or included in the bundle.

### Expected behavior

The bundler should process await expressions normally without hanging or crashing. The code should bundle successfully.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This is blocking my project as I can't bundle any async/await code. Any help would be appreciated!

---
Repository: /testbed
