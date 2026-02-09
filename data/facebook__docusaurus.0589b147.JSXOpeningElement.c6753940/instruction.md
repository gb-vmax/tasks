# Bug Report

### Describe the bug

The `prefer-docusaurus-heading` ESLint rule is reporting violations on elements that are NOT heading tags (h1-h6), which is the opposite of its intended behavior. The rule should only flag actual heading elements like `<h1>`, `<h2>`, etc., but instead it's flagging everything else.

### Reproduction

```jsx
// This should trigger the rule but doesn't
<h1>My Heading</h1>
<h2>Another Heading</h2>

// These should NOT trigger the rule but they do
<div>Content</div>
<p>Paragraph</p>
<span>Text</span>
```

When running the linter, I'm getting violations on `<div>`, `<p>`, `<span>` and other non-heading elements, while actual heading tags like `<h1>` and `<h2>` are not being flagged at all.

### Expected behavior

The rule should only report violations when it encounters HTML heading elements (h1, h2, h3, h4, h5, h6), suggesting to use Docusaurus `Heading` component instead. Non-heading elements should be ignored.

### Additional context

This seems to have started happening recently. The rule logic appears to be inverted - it's checking for elements that are NOT in the headingTypes array instead of elements that ARE in the array.

---
Repository: /testbed
