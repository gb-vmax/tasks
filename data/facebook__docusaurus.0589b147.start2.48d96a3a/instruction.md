# Bug Report

### Describe the bug

When parsing MDX content with non-partial constructs, the `currentConstruct` property is not being set correctly on the context. This causes issues when the parser needs to reference the current construct during tokenization.

### Reproduction

```js
// Parse MDX content with a construct that is not partial
const result = compile('# Heading\n\nSome content', {
  // ... mdx options
})

// During parsing, context.currentConstruct should be set
// but it remains undefined for non-partial constructs
```

### Expected behavior

The `context.currentConstruct` should be set for all constructs that are not marked as `partial`. Currently it appears to only be set when `construct.partial` is true, which is the opposite of the intended behavior.

### Additional context

This affects the parser's ability to properly track state during tokenization, especially when constructs need to reference the current parsing context or when interrupt handling is involved.

---
Repository: /testbed
