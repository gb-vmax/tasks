# Bug Report

### Describe the bug

I'm experiencing an issue with yield expressions in generator functions where the tree-shaking behavior seems incorrect. When using `yield` with arguments in my code, some statements that should be included in the output bundle are being incorrectly removed.

### Reproduction

```js
function* myGenerator() {
  const result = yield someValue;
  console.log('This should be included');
  return result;
}
```

After bundling, the code after the yield statement gets removed even though it has side effects and should be preserved.

### Expected behavior

The bundler should correctly identify that yield expressions with arguments have effects and preserve all subsequent code that depends on them. The tree-shaking logic should not incorrectly eliminate code following yield statements.

### Additional context

This appears to affect generator functions specifically when they contain yield expressions with arguments. Simple yields without arguments seem to work fine. The issue manifests during the bundling process where valid code gets stripped out.

---
Repository: /testbed
