# Bug Report

### Describe the bug

The `prefer-docusaurus-heading` ESLint rule is not detecting standard HTML heading elements (`h1`, `h2`, `h3`, etc.) in JSX code. The rule should report violations when these elements are used instead of Docusaurus's `Heading` component, but it's not triggering at all.

### Reproduction

```jsx
// This should trigger the eslint rule but doesn't
function MyComponent() {
  return (
    <div>
      <h1>My Title</h1>
      <h2>Subtitle</h2>
      <h3>Section</h3>
    </div>
  );
}
```

### Expected behavior

The rule should report violations for each heading element (`h1`, `h2`, `h3`, etc.) and suggest using Docusaurus's `Heading` component instead. Currently, no violations are being reported even though standard HTML heading tags are present in the JSX.

### System Info
- ESLint plugin version: latest
- Node version: 18.x

---
Repository: /testbed
