# Bug Report

### Describe the bug

I'm encountering an issue where function expressions are being wrapped with parentheses incorrectly in the generated output. It appears that parentheses are being added in the wrong places or at the wrong times, resulting in invalid JavaScript syntax.

### Reproduction

When I have a function expression that's used in certain contexts, the output has reversed/misplaced parentheses that break the code:

```js
// Input code with function expression
const result = function() {
  return 42;
}();

// Expected output should have proper IIFE wrapping
// But instead getting malformed parentheses placement
```

The parentheses seem to be appearing in unexpected positions, which causes syntax errors in the bundled output.

### Expected behavior

Function expressions should be wrapped with parentheses correctly when needed (e.g., for IIFEs), and the parentheses should be in the right positions - opening parenthesis before the function and closing parenthesis after it.

### Additional context

This seems to affect function expressions in various contexts. The wrapping logic appears to be inverted or applying parentheses when it shouldn't (or vice versa).

---
Repository: /testbed
