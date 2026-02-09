# Bug Report

### Describe the bug

I'm experiencing an issue with conditional statement handling where the consequent branch is being rendered when the test condition evaluates to `false`, and the alternate branch is being rendered when the condition evaluates to `true`. This appears to be backwards from the expected behavior.

### Reproduction

```js
if (false) {
  console.log('This should NOT be included');
} else {
  console.log('This SHOULD be included');
}
```

When the above code is processed, the consequent branch (`console.log('This should NOT be included')`) is being included in the output when it should be tree-shaken away, while the alternate branch is being removed when it should be kept.

The same issue occurs with truthy conditions:

```js
if (true) {
  console.log('This SHOULD be included');
} else {
  console.log('This should NOT be included');
}
```

Here, the consequent branch gets removed when it should be kept, and the alternate branch is included when it should be tree-shaken.

### Expected behavior

When an if statement has a statically known test value:
- If the condition is `true` or truthy, the consequent branch should be included and the alternate should be removed
- If the condition is `false` or falsy, the alternate branch should be included and the consequent should be removed

The current behavior seems to have these cases reversed.

---
Repository: /testbed
