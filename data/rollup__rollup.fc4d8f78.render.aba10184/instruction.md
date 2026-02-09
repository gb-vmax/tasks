# Bug Report

### Describe the bug

When using JSX attributes without values in automatic mode, the code generation is placing the `: true` in the wrong position. The boolean attribute shorthand gets inserted at an incorrect location, causing malformed output.

### Reproduction

```jsx
// Input JSX
<Component disabled />

// When compiled with jsxMode: 'automatic'
// The output is malformed with `: true` appearing in the wrong place
```

This seems to affect JSX attributes that don't have an explicit value (boolean attributes). The transformation is adding `: true` but not at the correct position in the generated code.

### Expected behavior

Boolean JSX attributes should be properly transformed to `disabled: true` in the output, with the `: true` appended at the correct location after the attribute name.

### System Info
- Rollup version: latest
- JSX mode: automatic

---
Repository: /testbed
