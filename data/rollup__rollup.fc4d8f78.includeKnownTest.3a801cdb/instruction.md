# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where the consequent branch of an if statement is being included in the bundle even when the test condition is known to be falsy at compile time.

### Reproduction

```js
if (false) {
  console.log('This should be tree-shaken');
  someFunction();
}
```

After bundling, the consequent block (`console.log` and `someFunction()`) is still present in the output even though the condition is always false. This results in unnecessary code being included in the final bundle.

### Expected behavior

When the if statement test is a known literal value (like `false`), only the appropriate branch should be included:
- If the test is `true`, only include the consequent
- If the test is `false`, only include the alternate (if present)
- Dead code from the non-executed branch should be completely removed from the bundle

### Additional context

This seems to affect static analysis and tree-shaking optimization. The bundler should be able to determine at compile time that certain branches will never execute and exclude them entirely.

---
Repository: /testbed
