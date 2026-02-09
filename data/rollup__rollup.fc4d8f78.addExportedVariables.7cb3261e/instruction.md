# Bug Report

### Describe the bug

I'm encountering a syntax error when trying to build my project after updating to the latest version. The build fails with an error related to array destructuring patterns.

### Reproduction

The error occurs when using array destructuring in export statements or variable declarations:

```js
export const [foo, bar] = someArray;
```

or

```js
const [a, b, c] = getValues();
```

The build process throws a parsing error and fails to complete. This was working fine in the previous version.

### Expected behavior

Array destructuring patterns should be parsed and compiled correctly without any syntax errors. The build should complete successfully.

### System Info
- Node version: 18.x
- Build tool: Rollup

---
Repository: /testbed
