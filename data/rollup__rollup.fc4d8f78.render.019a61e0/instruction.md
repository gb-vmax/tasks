# Bug Report

### Describe the bug

When using JSX fragments with nested property access, the output is generating an extra dot separator in the fragment variable name. This causes invalid JavaScript to be generated during the build process.

### Reproduction

```jsx
// Input JSX
<>
  <div>Content</div>
</>

// When the fragment is accessed as a nested property like React.Fragment
// The generated output includes an extra dot: React..Fragment
```

The issue appears when JSX mode is not set to 'preserve' and the fragment variable needs to be resolved. The generated code has consecutive dots (e.g., `React..Fragment`) instead of a single dot separator.

### Expected behavior

The fragment variable should be rendered with proper dot notation without any extra separators. For example, if the fragment is `React.Fragment`, it should remain as `React.Fragment` in the output, not `React..Fragment`.

### System Info
- Rollup version: latest
- JSX mode: Not 'preserve'

---
Repository: /testbed
