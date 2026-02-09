# Bug Report

### Describe the bug

The `no-html-links` ESLint rule is incorrectly flagging all JSX elements that are **not** anchor tags (`<a>`), instead of flagging actual anchor tags. This causes the rule to report errors on divs, spans, buttons, and every other JSX element while completely ignoring actual `<a>` tags.

### Reproduction

```jsx
// This should trigger the rule but doesn't
<a href="/docs">Link</a>

// These should NOT trigger the rule but they do
<div>Content</div>
<button>Click me</button>
<span>Text</span>
```

When running ESLint with the `no-html-links` rule enabled, all non-anchor elements are being flagged as violations, while actual anchor tags pass without any warnings.

### Expected behavior

The rule should only flag `<a>` elements (anchor tags) and ignore all other JSX elements like `<div>`, `<button>`, `<span>`, etc.

### Additional context

This appears to be a logic inversion issue - the rule is checking if the element name is NOT equal to 'a' and then returning early, when it should be doing the opposite.

---
Repository: /testbed
