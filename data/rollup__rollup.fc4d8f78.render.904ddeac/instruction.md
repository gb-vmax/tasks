# Bug Report

### Describe the bug

I'm experiencing an issue with function expression rendering where parentheses are being added in the wrong places. It seems like function expressions are getting wrapped with parentheses when they shouldn't be, and not getting wrapped when they should be.

### Reproduction

When I have a function expression that's used as an expression statement, it's not being wrapped in parentheses anymore. But in other contexts where parentheses shouldn't be added, they are appearing.

Example code that demonstrates the issue:

```js
// This should be wrapped in parens but isn't:
function() { console.log('test'); }();

// This shouldn't have extra parens but does:
const fn = function() { return 42; };
```

The output is generating incorrect parentheses placement, which is causing syntax errors in the bundled code.

### Expected behavior

Function expressions should only be wrapped in parentheses when they appear as expression statements (to make them valid IIFEs). In other contexts like variable assignments or return statements, they should not have additional parentheses added.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
