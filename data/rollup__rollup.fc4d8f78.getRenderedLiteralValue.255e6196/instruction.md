# Bug Report

### Describe the bug

I'm experiencing an issue where literal values are not being rendered correctly in certain cases. Specifically, when I have `false` boolean values or positive/zero numbers, they're not being converted to their string representations as expected.

### Reproduction

```js
// Boolean false is not rendered
const result1 = getRenderedLiteralValue(false);
// Expected: 'false'
// Actual: UnknownValue

// Positive numbers are not rendered
const result2 = getRenderedLiteralValue(42);
// Expected: '42'
// Actual: UnknownValue

// Zero is not rendered
const result3 = getRenderedLiteralValue(0);
// Expected: '0'
// Actual: UnknownValue
```

### Expected behavior

All literal values should be properly converted to their string representations:
- `false` should return `'false'`
- Positive numbers should return their string representation (e.g., `42` → `'42'`)
- Zero should return `'0'`

Currently only `true` and negative numbers seem to work correctly.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
