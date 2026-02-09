# Bug Report

### Describe the bug

When working with bigint literals in the code generator, the output is missing the required `n` suffix. This causes the generated code to be invalid JavaScript since bigint values must always end with `n`.

### Reproduction

```js
// Create a node with a bigint value
const node = {
  type: 'Literal',
  bigint: '12345',
  value: 12345n
}

// The generator outputs: 12345
// Expected output: 12345n
```

The generated code will fail to parse as valid JavaScript because bigint literals without the `n` suffix are treated as regular numbers, which can't represent the full range of bigint values.

### Expected behavior

Bigint literals should be generated with the `n` suffix appended to maintain valid JavaScript syntax. For example, `12345n` instead of `12345`.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
