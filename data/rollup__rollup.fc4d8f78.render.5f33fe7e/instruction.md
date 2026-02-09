# Bug Report

### Describe the bug
When using JSX fragments with the `preserve` mode, the output is being incorrectly rendered. It looks like the fragment identifier is being duplicated or transformed in an unexpected way.

### Reproduction
```jsx
// Input JSX with fragment
<>
  <div>Content</div>
</>
```

When bundling with `jsx: { mode: 'preserve' }`, the fragment opening tag gets transformed incorrectly instead of being preserved as-is.

### Expected behavior
With `mode: 'preserve'`, JSX fragments should be left untouched in the output. The fragment syntax should remain exactly as written in the source code without any transformation or replacement.

### System Info
- Rollup version: latest
- JSX mode: preserve

---
Repository: /testbed
