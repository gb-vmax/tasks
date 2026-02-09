# Bug Report

### Describe the bug

I'm experiencing an issue with function calls where the first argument is not being rendered correctly when all subsequent arguments are excluded during tree-shaking. The opening parenthesis is being removed along with the excluded arguments, resulting in malformed output.

### Reproduction

```js
// Input code
myFunction(includedArg, excludedArg1, excludedArg2)

// When excludedArg1 and excludedArg2 are tree-shaken out,
// the expected output should be:
myFunction(includedArg)

// But instead I'm getting:
myFunctionincludedArg)
```

This happens specifically when:
1. A function has multiple arguments
2. Only the first argument is included
3. All other arguments are excluded during the build process

### Expected behavior

When tree-shaking removes trailing arguments but keeps the first argument, the opening parenthesis should remain in place and the output should be valid JavaScript syntax.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
