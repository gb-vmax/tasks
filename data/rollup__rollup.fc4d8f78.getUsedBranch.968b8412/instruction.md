# Bug Report

### Describe the bug

I'm experiencing an issue with logical `&&` operator evaluation in my bundled code. When using `&&` with a truthy left operand, the expression is incorrectly evaluating to the left side instead of the right side.

### Reproduction

```js
const config = {
  enabled: true,
  value: 'result'
}

// This should evaluate to 'result' but evaluates to true instead
const output = config.enabled && config.value
console.log(output) // Expected: 'result', Actual: true
```

Another example:
```js
const x = 1 && 'hello'
console.log(x) // Expected: 'hello', Actual: 1
```

### Expected behavior

When using the `&&` operator:
- If the left operand is truthy, it should return the right operand
- If the left operand is falsy, it should return the left operand

This is standard JavaScript behavior but something seems wrong with how the bundler is handling these expressions.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
