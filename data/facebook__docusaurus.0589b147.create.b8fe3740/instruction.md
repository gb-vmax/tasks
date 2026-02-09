# Bug Report

### Describe the bug

The `prefer-docusaurus-heading` ESLint rule is not correctly detecting heading elements in JSX. It seems to be reporting errors on non-heading elements while ignoring actual heading tags.

### Reproduction

```jsx
// This should trigger the rule but doesn't
<h1>My Heading</h1>
<h2>Subheading</h2>

// This incorrectly triggers the rule
<div>Content</div>
<span>Text</span>
```

When running the linter on a file with standard heading elements like `<h1>`, `<h2>`, etc., they are not being flagged even though they should be. Instead, the rule seems to be triggering on other elements that aren't headings at all.

### Expected behavior

The rule should:
- Flag lowercase heading elements (`h1`, `h2`, `h3`, `h4`, `h5`, `h6`)
- Not flag non-heading elements like `div`, `span`, etc.

This appears to have broken recently, as it was working correctly before.

---
Repository: /testbed
