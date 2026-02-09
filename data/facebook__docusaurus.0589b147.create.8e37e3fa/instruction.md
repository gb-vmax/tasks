# Bug Report

### Describe the bug

The `prefer-docusaurus-heading` ESLint rule is not triggering warnings for `<h3>` heading elements, even though it should be enforcing the use of Docusaurus `Heading` component for all heading levels.

### Reproduction

```jsx
// This should trigger a warning but doesn't
function MyComponent() {
  return <h3>My Heading</h3>;
}
```

The rule correctly flags `<h1>`, `<h2>`, `<h4>`, `<h5>`, and `<h6>` elements, but `<h3>` elements are not being caught.

### Expected behavior

The ESLint rule should report a violation when `<h3>` elements are used, suggesting to use the Docusaurus `Heading` component instead (consistent with all other heading levels).

### Additional context

This appears to have started recently. All other heading levels are working as expected, only `<h3>` seems to be skipped by the linter.

---
Repository: /testbed
