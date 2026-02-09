# Bug Report

### Describe the bug

The `prefer-docusaurus-heading` ESLint rule is not reporting violations when it should. When I use standard HTML heading tags like `<h1>`, `<h2>`, etc. in my JSX components, the linter doesn't flag them anymore even though the rule is enabled.

### Reproduction

```jsx
// This should be flagged by the rule but isn't
function MyComponent() {
  return (
    <div>
      <h1>My Heading</h1>
      <h2>Subheading</h2>
    </div>
  );
}
```

Expected the linter to report that I should use Docusaurus heading components instead of raw HTML heading tags, but no warnings are shown.

### Expected behavior

The rule should report a violation when HTML heading elements (`h1`, `h2`, `h3`, `h4`, `h5`, `h6`) are used, suggesting to use Docusaurus heading components instead.

### Additional context

This seems to have broken recently. The rule was working correctly before and would catch these cases. Now it's completely silent on heading elements that should be flagged.

---
Repository: /testbed
