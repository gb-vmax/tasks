# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where non-partial constructs are not being properly registered with the parser context. It seems like the `currentConstruct` property is only being set when a construct is marked as `partial`, which is the opposite of what should happen.

### Reproduction

When parsing MDX content with custom constructs that are not partial (e.g., block-level elements), the parser doesn't properly track the current construct in the context. This causes issues with construct resolution and may lead to incorrect parsing behavior.

```js
// Example MDX content that triggers the issue
const mdxContent = `
# Heading

Some paragraph text with **bold** content.

<CustomComponent />
`;

// The parser fails to properly handle non-partial constructs
// because context.currentConstruct is not being set correctly
```

### Expected behavior

Non-partial constructs should have `context.currentConstruct` set to the current construct being processed. Partial constructs should NOT set this property. This is important for the parser to correctly maintain state during tokenization.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken after a recent change to the tokenizer logic. The condition for setting `context.currentConstruct` appears to be inverted.

---
Repository: /testbed
