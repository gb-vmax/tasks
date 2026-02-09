# Bug Report

### Describe the bug

I'm encountering an issue with generated code snippets for IIFEs (Immediately Invoked Function Expressions). The generated code appears to have the function structure reversed - the opening and closing parts are swapped, resulting in malformed JavaScript.

### Reproduction

When generating code that requires an IIFE with direct return, the output is syntactically incorrect. The function declaration parts are in the wrong order.

For example, when trying to generate an IIFE like:
```js
(function() { return value })()
```

The generated code has the parentheses and function parts mixed up, making it invalid JavaScript that won't parse or execute correctly.

### Expected behavior

The code generator should produce valid IIFE syntax with:
1. Proper wrapping parentheses around the function
2. Function declaration in correct order
3. Invocation parentheses at the end

The generated code should be syntactically valid and executable.

### Additional context

This seems to affect code generation when `getDirectReturnIifeLeft` is called. The wrapping logic also appears to be checking the wrong condition for when wrapping is needed.

---
Repository: /testbed
