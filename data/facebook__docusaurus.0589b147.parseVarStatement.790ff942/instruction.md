# Bug Report

### Describe the bug

I'm encountering an issue with variable declarations in MDX files. When declaring variables without initialization (e.g., `let x;`), I'm getting unexpected parsing errors. It seems like the parser is now requiring initializers for variable declarations even when they should be optional.

### Reproduction

```js
// This should be valid JavaScript but throws a parsing error
let myVariable;

// This also fails
var anotherVar;

// Only this works now
const initialized = 'value';
```

The issue appears to be related to how variable statements are being parsed. Variables that don't have an initializer are being rejected when they should be allowed.

### Expected behavior

Variable declarations without initializers should be parsed correctly, as they are valid JavaScript. The parser should only require initializers when the context demands it (like for `const` declarations).

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have started recently. Any help would be appreciated!

---
Repository: /testbed
