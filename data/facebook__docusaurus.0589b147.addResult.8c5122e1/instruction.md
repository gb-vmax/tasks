# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where certain constructs in my markdown files are being duplicated or not properly resolved. It seems like the tokenizer is not correctly handling the event resolution process.

### Reproduction

```mdx
# My Document

Some content here with **bold text** and other formatting.

- List item 1
- List item 2

More content below.
```

When parsing this MDX content, I'm seeing unexpected behavior where:
1. Some tokens appear multiple times in the output
2. The resolved events don't match what I expect based on the input

The issue seems to be related to how the tokenizer processes and resolves constructs. I noticed this started happening recently and it's affecting various MDX documents in my project.

### Expected behavior

The MDX parser should correctly resolve all constructs without duplication, and the final event list should accurately represent the parsed markdown structure.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
