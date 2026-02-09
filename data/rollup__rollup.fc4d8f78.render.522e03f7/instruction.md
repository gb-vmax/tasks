# Bug Report

### Describe the bug

I'm experiencing an issue with return statements in my bundled code. After bundling, some return statements are missing semicolons where they should be present, causing ASI (Automatic Semicolon Insertion) issues in certain edge cases.

### Reproduction

```js
// Input code
function test() {
  return
  [1, 2, 3].forEach(x => console.log(x))
}

// After bundling, the code doesn't properly handle ASI
// Expected: return; [1, 2, 3]...
// Actual: return [1, 2, 3]... (incorrect behavior)
```

Another case:

```js
function example() {
  return
  (function() {
    console.log('test')
  })()
}
```

### Expected behavior

The bundler should preserve or insert semicolons after return statements when necessary to prevent ASI-related bugs. Return statements followed by expressions on the next line should be handled correctly to avoid unintended behavior.

### Additional context

This seems to affect return statements where the returned expression starts on the same line or immediately after the return keyword. The bundled output doesn't properly prevent ASI issues in these scenarios.

---
Repository: /testbed
