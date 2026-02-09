# Bug Report

### Describe the bug

I'm experiencing an issue with conditional statements where the `else` branch is being incorrectly included in the output when the condition evaluates to `false`. It seems like falsy values (like `false`, `0`, `null`) are not being handled correctly.

### Reproduction

```js
if (false) {
  console.log('consequent');
} else {
  console.log('alternate');
}
```

When bundling code like this, both branches appear to be included in the output instead of just the `else` block. This is causing unnecessary code bloat.

Another example:
```js
const value = 0;
if (value) {
  doSomething();
} else {
  doSomethingElse();
}
```

The same issue occurs - it looks like `0` is being treated differently than expected.

### Expected behavior

When the test condition is a known falsy value (like `false`, `0`, `null`), only the alternate/else branch should be included in the bundle. The consequent/if branch should be tree-shaken away.

Similarly, when the condition is `true` or a truthy value, only the consequent should be included.

### Additional context

This might be related to how literal values are being evaluated during the tree-shaking phase. It worked correctly in previous versions but seems to have regressed recently.

---
Repository: /testbed
