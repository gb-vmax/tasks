# Bug Report

### Describe the bug

I'm encountering an issue where literal values are not being rendered correctly in certain cases. Specifically, when working with boolean `false` values and numeric `0` values, they seem to be getting lost or not rendered as expected in the output.

### Reproduction

```js
// Case 1: Boolean false not rendering
const falsyBoolean = false;
// Expected output: "false"
// Actual output: undefined or missing

// Case 2: Number zero not rendering  
const zeroValue = 0;
// Expected output: "0"
// Actual output: returns unknown/undefined instead of the numeric value
```

### Expected behavior

- When a literal value is `false`, it should render as the string `"false"`
- When a literal value is `0`, it should render as `"0"` (the numeric representation)

Both of these are valid falsy values in JavaScript and should be handled properly instead of being treated as unknown or missing values.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
