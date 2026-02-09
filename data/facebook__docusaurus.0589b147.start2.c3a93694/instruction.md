# Bug Report

### Describe the bug

I'm experiencing an issue with ATX heading parsing in MDX. When processing markdown headings (like `# Heading`), the parser seems to be behaving incorrectly and not properly tokenizing the heading content.

### Reproduction

```mdx
# This is a heading

Some content here.
```

When parsing this MDX content, the heading is not being recognized correctly. The tokenizer appears to be exiting the heading state prematurely before actually processing the heading sequence.

### Expected behavior

The parser should properly tokenize ATX headings by:
1. Entering the heading state
2. Processing the `#` symbols (heading sequence)
3. Processing the heading text
4. Then exiting the heading state

Instead, it seems like the heading state is being exited immediately without processing the actual heading content.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This appears to be a regression as headings were working fine in previous versions. Any help would be appreciated!

---
Repository: /testbed
