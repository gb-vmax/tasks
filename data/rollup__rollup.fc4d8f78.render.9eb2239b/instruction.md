# Bug Report

### Describe the bug

When bundling code with variable declarations that should be exported, I'm getting duplicate semicolons appended to the output. It looks like the semicolon insertion logic is checking the wrong position in the source code.

### Reproduction

```js
// Input code
export const foo = 'bar';
const baz = 'qux';

// Expected output
export const foo = 'bar';
const baz = 'qux';

// Actual output
export const foo = 'bar';;
const baz = 'qux';
```

The issue appears when variable declarations are processed and a semicolon is being added even though one already exists at the end of the statement.

### Expected behavior

The bundler should check if a semicolon already exists before appending one. Variable declarations should only get a semicolon added if they don't already have one.

### Additional context

This started happening recently and is affecting the output of bundled code. The extra semicolons don't break functionality but they make the output look incorrect and could potentially cause issues with minifiers or other tools that expect clean code.

---
Repository: /testbed
