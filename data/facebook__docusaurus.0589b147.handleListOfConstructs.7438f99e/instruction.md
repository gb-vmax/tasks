# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where the tokenizer is skipping the first construct in the list when processing markdown content. This causes certain markdown elements to not be recognized or parsed correctly.

### Reproduction

When parsing MDX content that should match multiple constructs, the first construct in the list is being skipped entirely. For example:

```js
// MDX content with elements that should match the first construct
const mdxContent = `
# Heading
Some paragraph text
`

// The heading or other first-matching elements are not being parsed
```

The tokenizer appears to be starting from the wrong index when iterating through the list of constructs, causing it to miss valid markdown syntax that should be handled by the first construct in the list.

### Expected behavior

All constructs in the list should be evaluated in order, starting from index 0. The first construct should be checked before moving to subsequent constructs.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems like it might be a regression as this was working in previous versions. Any markdown elements that rely on being the first construct to match are now being ignored.

---
Repository: /testbed
