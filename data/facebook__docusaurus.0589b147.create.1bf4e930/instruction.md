# Bug Report

## ESLint rule `prefer-docusaurus-heading` not triggering on heading elements

I'm experiencing an issue with the `prefer-docusaurus-heading` ESLint rule where it's not reporting violations when I use standard HTML heading elements (`h1`, `h2`, etc.) in my JSX code.

### Reproduction

```jsx
// This should trigger the ESLint rule but doesn't
function MyComponent() {
  return (
    <div>
      <h1>My Heading</h1>
      <h2>Subheading</h2>
    </div>
  );
}
```

### Expected behavior

The ESLint rule should report a violation when using `h1`, `h2`, `h3`, `h4`, `h5`, or `h6` elements, suggesting to use Docusaurus heading components instead.

### Actual behavior

The rule doesn't trigger any warnings or errors. It seems like the rule is checking for the wrong condition - it only reports violations on elements that are NOT headings, which is the opposite of what it should do.

Has anyone else run into this? The rule worked fine in previous versions.

---
Repository: /testbed
