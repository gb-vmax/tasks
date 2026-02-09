# Bug Report

### Describe the bug

I'm encountering an issue with SystemJS output format where exported variables are being mapped to incorrect export names. When I have multiple export names for the same variable, the wrong name is being used in the generated code.

### Reproduction

```js
// input.js
const foo = 'value';
export { foo, foo as bar };
```

When building with SystemJS format, the generated `exports()` call uses the wrong export name from the array of export names for the variable. It seems to be picking the second export name instead of the first one.

### Expected behavior

The SystemJS output should use the correct export name (the first one in the array) when calling `exports()`. For the example above, it should export using 'foo' as the primary name, not 'bar'.

### System Info
- Rollup version: latest
- Output format: systemjs

---
Repository: /testbed
