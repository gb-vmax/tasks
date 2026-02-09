# Bug Report

### Describe the bug

I'm encountering an issue with `export default` declarations where the code is being parsed incorrectly. It seems like the parser is not correctly identifying the start position of the declaration after the `default` keyword.

### Reproduction

```js
export default function myFunction() {
  return 'test';
}
```

When bundling code with export default declarations, the output appears to be malformed or the declaration is not being processed at the correct position. This affects both function declarations and other types of default exports.

### Expected behavior

The parser should correctly identify where the `default` keyword ends and the actual declaration begins, so that the export default statement is processed properly.

### Additional context

This seems to affect all types of default exports:
- `export default function ...`
- `export default class ...`
- `export default expression`

The issue appears to be related to how the position after the `default` keyword is calculated.

---
Repository: /testbed
