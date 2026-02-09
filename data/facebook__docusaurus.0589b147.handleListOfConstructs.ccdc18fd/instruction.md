# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where certain markdown constructs are being skipped or not processed correctly. It seems like the tokenizer is jumping over valid constructs instead of processing them in order.

### Reproduction

```mdx
# Heading

Some content here

- List item 1
- List item 2

More content
```

When parsing this MDX content, the first construct in the list gets skipped and the parser tries to process the second one instead. This causes parsing errors or unexpected output where the first element of certain markdown structures is not recognized.

### Expected behavior

The tokenizer should process all constructs in sequence, starting from index 0. Each construct in the list should be evaluated in order without skipping any.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The parser appears to be incrementing the construct index before it should, causing it to miss the first construct in the list.

---
Repository: /testbed
