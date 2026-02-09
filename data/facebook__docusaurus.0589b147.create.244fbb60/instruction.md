# Bug Report

### Describe the bug

The `prefer-docusaurus-heading` ESLint rule is reporting errors on JSX elements that are NOT heading tags, while completely ignoring actual heading tags like `<h2>`, `<h3>`, etc. This is the opposite of what the rule should be doing.

### Reproduction

```jsx
// This incorrectly triggers the rule error
<div>Content</div>
<span>Text</span>
<p>Paragraph</p>

// These should trigger the rule but don't
<h2>My Heading</h2>
<h3>Subheading</h3>
<h4>Another heading</h4>
```

When linting the above code, the rule reports violations for `<div>`, `<span>`, and `<p>` tags, but completely ignores the actual heading tags that should be flagged.

### Expected behavior

The rule should only flag actual HTML heading elements (`h2`, `h3`, `h4`, `h5`, `h6`) and suggest using Docusaurus `<Heading>` component instead. Non-heading elements should be ignored.

### Additional context

This seems like the rule logic got inverted somehow - it's checking if elements are NOT in the headingTypes array instead of checking if they ARE in the array.

---
Repository: /testbed
