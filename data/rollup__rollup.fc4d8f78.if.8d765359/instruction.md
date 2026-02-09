# Bug Report

### Describe the bug

When bundling code with function calls that have trailing arguments marked for tree-shaking, the output is incorrect. Some arguments that should be included in the final bundle are being removed, or arguments are being rendered when they shouldn't be.

### Reproduction

```js
// Input code
function myFunc(a, b, c, d) {
  console.log(a, b);
}

// When 'c' and 'd' are marked as not included (tree-shaken)
// but 'a' and 'b' should remain
myFunc(getValue1(), getValue2(), unusedValue(), anotherUnused());

// Expected output after tree-shaking:
// myFunc(getValue1(), getValue2());

// Actual output appears to be missing arguments or including wrong ones
```

The issue seems to happen specifically when:
1. A function call has multiple arguments
2. Some trailing arguments are excluded from the bundle
3. The logic for determining which arguments to keep and render is producing incorrect results

### Expected behavior

The bundler should correctly identify and render only the arguments that are marked as included, removing trailing arguments that have been tree-shaken out, while preserving the correct number of arguments that are actually used.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
