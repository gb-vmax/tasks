# Bug Report

### Describe the bug

Function expressions are being wrapped in parentheses when they shouldn't be, causing incorrect output in the generated code. It seems like the wrapping logic is inverted - parentheses are added in cases where they're not needed and omitted where they should be present.

### Reproduction

When bundling code with function expressions, they get wrapped incorrectly:

```js
// Input code
const foo = function() {
  return 42;
};

// Expected output
const foo = function() {
  return 42;
};

// Actual output (incorrectly wrapped)
const foo = (function() {
  return 42;
})();
```

Conversely, when a function expression is used as an expression statement (where wrapping IS needed), the parentheses are missing:

```js
// Input code
function() {
  console.log('test');
}();

// Expected output
(function() {
  console.log('test');
})();

// Actual output (missing parentheses)
function() {
  console.log('test');
}();
```

### Expected behavior

Function expressions should only be wrapped in parentheses when they appear as expression statements (like IIFEs). Regular function expressions assigned to variables or used in other contexts should not be wrapped.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
