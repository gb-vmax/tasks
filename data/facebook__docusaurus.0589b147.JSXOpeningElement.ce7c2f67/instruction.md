# Bug Report

### Describe the bug

The `prefer-docusaurus-heading` ESLint rule is now flagging all JSX elements as violations, not just HTML heading elements. It's reporting errors on components like `<div>`, `<span>`, `<MyComponent>`, etc., which should not be flagged by this rule.

### Reproduction

```jsx
// This incorrectly triggers the rule violation
<div>Content</div>

// This also incorrectly triggers the rule violation
<MyCustomComponent />

// These should still trigger the rule (and they do)
<h1>Heading</h1>
<h2>Subheading</h2>
```

### Expected behavior

The rule should only report violations for actual HTML heading elements (`h1`, `h2`, `h3`, `h4`, `h5`, `h6`). Other JSX elements like `div`, `span`, or custom components should be ignored.

### System Info
- ESLint plugin version: latest
- Node version: 18.x

---
Repository: /testbed
