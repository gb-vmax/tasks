# Bug Report

Title: ESLint rule `prefer-docusaurus-heading` incorrectly flagging non-heading JSX elements

### Describe the bug
The `prefer-docusaurus-heading` ESLint rule is now incorrectly reporting errors on JSX elements that are NOT heading elements (h1-h6). The rule seems to have inverted logic - it's flagging everything except the headings it's supposed to check.

### Reproduction
```jsx
// This now incorrectly triggers the rule error
<div>Content</div>
<span>Text</span>
<p>Paragraph</p>

// But these heading elements don't trigger anything (when they should)
<h1>Title</h1>
<h2>Subtitle</h2>
```

### Expected behavior
The rule should only flag actual heading elements (h1, h2, h3, h4, h5, h6) and suggest using the Docusaurus `Heading` component instead. Non-heading elements like `div`, `span`, `p`, etc. should not trigger this rule at all.

### System Info
- Using the latest version of the eslint-plugin
- This seems to have broken recently, was working fine before

---
Repository: /testbed
