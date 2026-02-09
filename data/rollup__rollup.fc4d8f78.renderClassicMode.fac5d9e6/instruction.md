# Bug Report

### Describe the bug

When using JSX fragments in classic mode, the generated code has incorrect positioning of the fragment wrapper and null argument. The opening parenthesis and null parameter are being inserted at the wrong positions in the output, causing malformed JavaScript code.

### Reproduction

```jsx
const Fragment = () => (
  <>
    <div>First</div>
    <div>Second</div>
  </>
);
```

When compiled in classic JSX mode, the fragment wrapper function call and its arguments are not being placed at the correct positions in the generated code.

### Expected behavior

The compiled output should have:
- The opening parenthesis correctly positioned relative to the fragment start
- The null argument properly placed after the opening fragment tag
- All parts of the fragment function call in their correct positions

### System Info
- rollup version: latest
- JSX mode: classic

---
Repository: /testbed
