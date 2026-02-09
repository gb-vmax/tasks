# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the tokenizer seems to be skipping the first construct in a list. When processing markdown content, it appears that the parser is starting from the second element instead of the first, causing parsing failures or incorrect output.

### Reproduction

```js
// When parsing MDX content with multiple constructs
const mdxContent = `
# Heading
Some text
- List item 1
- List item 2
`;

// The first construct appears to be skipped
// Leading to incorrect parsing or missing content
```

### Expected behavior

The tokenizer should process all constructs in the list starting from index 0, not skip the first one. All markdown elements should be correctly parsed and rendered.

### Additional context

This seems to affect any MDX content that relies on the tokenizer processing a list of constructs. The parser appears to be incrementing the index before accessing the first element, causing it to miss the initial construct.

---
Repository: /testbed
