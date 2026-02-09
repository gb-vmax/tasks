# Bug Report

### Describe the bug

I'm experiencing an issue with SystemJS export statements when using the `system` output format. The generated code has parentheses and export statements in the wrong positions, causing syntax errors in the output.

### Reproduction

When bundling code that exports variables with expressions that need parentheses wrapping, the output generates malformed JavaScript:

```js
// Input code
export const foo = someExpression;

// Expected output (correct):
System.register([], function (_export) {
  return {
    execute: function () {
      _export('foo', foo = (someExpression));
    }
  };
});

// Actual output (incorrect):
// Parentheses and export statement are placed incorrectly
// causing syntax errors
```

### Steps to reproduce
1. Configure rollup with `output.format: 'system'`
2. Bundle a module that exports a variable with an expression that requires parentheses
3. Check the generated output - the parentheses and export statements are in the wrong order

### Expected behavior
The SystemJS export statement and parentheses should be positioned correctly to generate valid JavaScript syntax.

### Environment
- Rollup version: latest
- Output format: system

---
Repository: /testbed
