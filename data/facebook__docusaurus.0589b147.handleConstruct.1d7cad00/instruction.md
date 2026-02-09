# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where constructs are being incorrectly assigned to the context. It appears that the logic for handling partial vs non-partial constructs has been inverted, causing the parser to behave unexpectedly.

### Reproduction

When parsing MDX content with constructs that have the `partial` property set, the context assignment seems backwards:

```js
// Example MDX content that triggers the issue
const mdxContent = `
# Heading

Some content with **bold** text
`;

// Parse the content
const result = compile(mdxContent);
```

The parser should assign `context.currentConstruct` for non-partial constructs, but it's currently doing the opposite - only assigning it when `construct.partial` is true.

### Expected behavior

Non-partial constructs should update `context.currentConstruct`, while partial constructs should not. This is important for proper interrupt handling and construct tracking during the tokenization process.

### Additional context

This seems to have broken after a recent change to the tokenizer logic. The condition for when to set `context.currentConstruct` appears to be inverted from what it should be.

---
Repository: /testbed
