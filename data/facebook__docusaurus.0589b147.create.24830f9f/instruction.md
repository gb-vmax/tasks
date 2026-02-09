# Bug Report

### Describe the bug

The `prefer-docusaurus-heading` ESLint rule is reporting errors on elements that are NOT headings (h1-h6), when it should only flag actual heading elements. The rule logic appears to be inverted - it's checking non-heading elements instead of heading elements.

### Reproduction

```jsx
// This should NOT trigger the rule, but currently does
<div>Content</div>
<span>Text</span>
<p>Paragraph</p>

// These SHOULD trigger the rule, but currently don't
<h1>Title</h1>
<h2>Subtitle</h2>
```

When running the linter, I'm getting violations on regular HTML elements like `div`, `span`, `p`, etc., while actual heading tags (`h1` through `h6`) are passing without any warnings.

### Expected behavior

The rule should only report violations when heading elements (h1, h2, h3, h4, h5, h6) are used, suggesting to use Docusaurus `Heading` component instead. Non-heading elements should be ignored by this rule.

### System Info
- Docusaurus version: Latest
- ESLint plugin version: Current main branch

---
Repository: /testbed
