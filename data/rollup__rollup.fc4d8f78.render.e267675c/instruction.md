# Bug Report

### Describe the bug

When using JSX fragments with nested property access, the fragment variable is being rendered in the wrong order. The fragment variable should come first, but it's being placed at the end after all the nested properties.

### Reproduction

```jsx
// Input JSX
<>
  <div>Content</div>
</>

// With a nested fragment like React.Fragment
// Expected output: React.Fragment
// Actual output: Fragment.React (reversed order)
```

When the JSX mode is not set to 'preserve', the fragment variable and its nested properties get concatenated in the wrong order during code generation.

### Expected behavior

The fragment variable should be rendered first, followed by any nested property access. For example, if the fragment is `React.Fragment`, it should output `React.Fragment`, not `Fragment.React`.

### System Info
- Rollup version: latest
- JSX mode: not 'preserve'

---
Repository: /testbed
