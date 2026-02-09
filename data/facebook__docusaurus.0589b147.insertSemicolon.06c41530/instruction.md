# Bug Report

### Describe the bug

I'm experiencing an issue with automatic semicolon insertion (ASI) in the MDX parser. When a semicolon is automatically inserted, the callback `onInsertedSemicolon` is being called with incorrect position information.

### Reproduction

```js
const mdx = require('@mdx-js/mdx');

const code = `
export const foo = 1
export const bar = 2
`;

mdx.compile(code, {
  onInsertedSemicolon: (start, end) => {
    console.log('Semicolon inserted at position:', start);
    // Expected: position should be at the end of the statement
    // Actual: position is at the start of the token instead
  }
});
```

### Expected behavior

The `onInsertedSemicolon` callback should receive the position where the semicolon was inserted (the end of the previous token), but it's currently receiving the start position of the last token instead. This makes it difficult to accurately track where ASI occurred in the source code.

Also noticed that the function no longer returns `true` when a semicolon can be inserted, which might affect downstream code that relies on this return value.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
