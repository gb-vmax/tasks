# Bug Report

### Describe the bug

I'm encountering an issue with assignment expressions where the left-hand side is not included in the output. When the left side of an assignment is tree-shaken/removed, the generated code appears to be incorrect and contains incomplete/truncated output.

### Reproduction

```js
// Input code with unused destructuring assignment
const obj = { a: 1, b: 2 };
const { a } = (someCondition, obj);

// When 'a' is not used and gets removed during tree-shaking,
// the output seems to be malformed
```

The generated output appears to be cut off or improperly rendered when the assignment's left-hand side is excluded from the bundle.

### Expected behavior

When the left-hand side of an assignment expression is tree-shaken out, the right-hand side should still be properly rendered in the output with correct code removal boundaries. The generated code should be valid JavaScript without any truncation.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to be affecting code generation during the rendering phase when assignment expressions have their left side excluded.

---
Repository: /testbed
