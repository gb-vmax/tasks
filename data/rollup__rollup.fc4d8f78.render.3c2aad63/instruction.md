# Bug Report

### Describe the bug

I'm experiencing an issue with `yield` expressions where the spacing between the `yield` keyword and its argument is not being handled correctly. When the argument immediately follows `yield` without a space, the generated code appears malformed.

### Reproduction

```js
function* generator() {
  yield(someValue);
}
```

After bundling/processing, the output seems to have incorrect spacing or the space is being added in the wrong position, causing the generated code to look wrong.

### Expected behavior

The `yield` keyword should always be properly separated from its argument with a space when needed. For example, `yield(someValue)` should remain as `yield (someValue)` or maintain proper spacing in the output.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
