# Bug Report

### Describe the bug

The `prefer-docusaurus-heading` ESLint rule is reporting errors on non-heading JSX elements instead of actual heading elements (h1-h6). The rule seems to be triggering on the wrong elements.

### Reproduction

```jsx
// This should trigger the rule but doesn't
<h1>My Heading</h1>

// This should NOT trigger the rule but does
<div>Content</div>
<span>Text</span>
<p>Paragraph</p>
```

When running the linter, it's flagging elements like `div`, `span`, `p`, etc. instead of the actual heading tags that should be using the Docusaurus `Heading` component.

### Expected behavior

The rule should only report violations for actual HTML heading elements (`h1`, `h2`, `h3`, `h4`, `h5`, `h6`) and suggest replacing them with the Docusaurus `Heading` component. Other JSX elements should not trigger this rule.

### System Info
- @docusaurus/eslint-plugin version: latest
- Node version: 18.x

---
Repository: /testbed
