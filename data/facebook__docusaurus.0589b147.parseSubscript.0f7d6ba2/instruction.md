# Bug Report

### Describe the bug

After a recent update, JavaScript parsing appears to be broken. The parser seems to be unable to handle basic JavaScript syntax correctly, causing parsing failures across the board.

### Reproduction

I'm experiencing parsing errors with standard JavaScript code that was working fine before. For example:

```js
// Simple function call
const result = myFunction(arg1, arg2);

// Object property access
const value = obj.property;

// Array access
const item = arr[0];
```

All of these basic patterns now fail to parse correctly. The parser seems to be cutting off mid-processing.

### Expected behavior

The parser should successfully parse valid JavaScript syntax including:
- Function calls with arguments
- Property access (both dot notation and bracket notation)
- Optional chaining operators
- Arrow functions
- Async functions

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This is blocking our entire build process. Any help would be appreciated!

---
Repository: /testbed
