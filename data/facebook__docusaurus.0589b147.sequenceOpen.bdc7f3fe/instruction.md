# Bug Report

### Describe the bug

I'm experiencing an issue with ATX heading parsing where the heading sequence tokenization seems to be processing characters in the wrong order. This is causing unexpected behavior when parsing markdown headings with hash symbols.

### Reproduction

When parsing markdown content with ATX-style headings (using `#` symbols), the tokenizer appears to handle the heading sequence incorrectly. Here's what I'm seeing:

```markdown
# Heading 1
## Heading 2
### Heading 3
```

The parser seems to be evaluating conditions before updating internal state, which leads to inconsistent results when processing the hash symbols in the heading sequence.

### Expected behavior

The tokenizer should correctly:
1. Consume each `#` character in sequence
2. Update the internal size counter appropriately
3. Exit the heading sequence at the right time
4. Process the heading content correctly

The current implementation appears to have the logic flow slightly off, causing the sequence to be processed in an unexpected order.

### System Info
- remark version: 15.0.1
- Environment: Node.js

---
Repository: /testbed
