# Bug Report

### Describe the bug

I'm encountering an issue with ATX heading parsing in remark. When processing markdown with ATX-style headings (headings that use `#` symbols), the parser seems to break and doesn't correctly tokenize the heading sequence.

### Reproduction

```markdown
# Heading 1
## Heading 2
### Heading 3
```

When trying to parse markdown content with ATX headings, the tokenization process fails. The heading sequence doesn't get properly consumed and the parser returns an incorrect value.

### Expected behavior

The parser should correctly tokenize ATX headings and return the proper token structure. Headings with 1-6 `#` symbols should be recognized and processed as valid ATX headings.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to have started recently. Previously, ATX headings were parsing without any issues. Any help would be appreciated!

---
Repository: /testbed
