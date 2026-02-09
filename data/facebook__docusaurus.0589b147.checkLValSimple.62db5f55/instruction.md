# Bug Report

### Describe the bug

I'm experiencing issues with MDX parsing where variable declarations and argument name validation seem to be broken. When using certain variable names or having duplicate argument names, the parser either incorrectly allows invalid code or incorrectly rejects valid code.

### Reproduction

```js
// Case 1: Duplicate argument names are not being caught
function test(a, a) {
  // This should raise an error but doesn't
}

// Case 2: Valid variable declarations are being rejected
let myVar = 'test'
// Parser incorrectly flags this as invalid
```

The behavior is completely inverted from what's expected - valid code gets rejected while invalid code gets accepted.

### Expected behavior

- Duplicate argument names should be detected and raise an error
- Valid lexically bound names should be allowed (except for reserved keywords like 'let')
- The `let` keyword restriction should only apply when used as a variable name, not for all declarations

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems like a logic error in the validation checks. The parser is doing the opposite of what it should be doing for both argument clash detection and binding type validation.

---
Repository: /testbed
