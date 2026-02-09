# Bug Report

### Describe the bug

The `no-html-links` ESLint rule is flagging non-anchor elements as violations. It appears the rule is now incorrectly reporting errors on elements that are NOT `<a>` tags, when it should only be checking anchor tags.

### Reproduction

```jsx
// This should NOT trigger the rule, but it does
<div href="/some-link">Click me</div>

// This should NOT trigger the rule, but it does  
<button href="/page">Go</button>

// This SHOULD trigger the rule (and still does)
<a href="/internal-link">Link</a>
```

The rule seems to have inverted its logic - it's now checking everything except anchor tags, which is the opposite of the intended behavior.

### Expected behavior

The rule should only report violations for `<a>` elements with non-fully-resolved hrefs. Other JSX elements like `<div>`, `<button>`, etc. should be completely ignored by this rule.

### Additional context

This seems like a regression - the rule was working correctly before and only flagging actual anchor tags. Now it's reporting false positives on all other elements.

---
Repository: /testbed
