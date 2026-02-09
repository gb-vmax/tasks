# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain constructs aren't being handled correctly. It seems like partial constructs are being processed differently than they should be, causing unexpected behavior in the tokenizer.

### Reproduction

When parsing markdown with nested or partial constructs, the tokenizer appears to set `context.currentConstruct` at the wrong time or for the wrong construct types. This leads to incorrect parsing results for complex markdown structures.

```js
// Example markdown that triggers the issue
const markdown = `
Some text with [nested **bold** link](url)
`;

// The parser doesn't handle this correctly
const result = parseMarkdown(markdown);
// Expected proper nesting, but constructs are misidentified
```

### Expected behavior

Partial constructs should be handled separately from non-partial constructs. The `context.currentConstruct` should only be set for non-partial constructs, and the state should be stored at the appropriate time during tokenization.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to be affecting how the tokenizer tracks construct state during parsing. Any help would be appreciated!

---
Repository: /testbed
