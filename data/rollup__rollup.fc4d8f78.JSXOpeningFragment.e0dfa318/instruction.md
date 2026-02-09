# Bug Report

### Describe the bug

When using JSX fragments with nested fragment references (e.g., `React.Fragment`), the rendered output is incorrect. The fragment variable name appears to be duplicated or incorrectly constructed in the generated code.

### Reproduction

```jsx
// Input JSX
<>
  <div>Content</div>
</>

// With jsx configuration using a nested fragment like 'React.Fragment'
// Expected output: React.Fragment
// Actual output: Fragment.Fragment (or similar duplication)
```

This affects JSX fragment rendering when the fragment is configured as a property access (like `React.Fragment` instead of just `Fragment`).

### Expected behavior

When a fragment is configured with a nested reference (e.g., `React.Fragment`), the output should correctly reference the full path without duplication. The generated code should use `React.Fragment` instead of `Fragment.Fragment`.

### Additional context

This seems to affect JSX configurations where the fragment is specified as a dotted path. The issue appears in the code generation phase where the fragment variable name is being constructed.

---
Repository: /testbed
