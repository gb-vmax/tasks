# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where tokens are being added twice during the tokenization process. This appears to be causing duplicate entries in the event stream when constructs are successfully parsed.

### Reproduction

```js
// When parsing MDX content with constructs
const mdx = `
# Heading
Some content
`;

// The tokenizer adds results multiple times
// Leading to duplicate token events in context.events
```

### Steps to reproduce:
1. Parse any MDX document with standard constructs (headings, paragraphs, etc.)
2. Check the internal event stream during tokenization
3. Notice that `addResult` is being called with both `info.from` and the full `info` object

### Expected behavior

Each successful construct should only add a single result to the event stream. The `addResult` function should be called once per construct, not twice with different parameters.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems like it might be a copy-paste error or accidental duplication in the tokenizer code. The second `addResult` call doesn't match the pattern used elsewhere in the codebase.

---
Repository: /testbed
