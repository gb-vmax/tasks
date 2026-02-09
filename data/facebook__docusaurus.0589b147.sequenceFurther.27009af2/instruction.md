# Bug Report

### Describe the bug

I'm encountering an issue with ATX heading parsing in markdown. When using multiple consecutive `#` characters in a heading, the parser seems to be consuming characters incorrectly, which affects how headings are being tokenized.

### Reproduction

```markdown
### Heading with multiple hashes
```

When parsing ATX headings (the ones that use `#` symbols), the tokenizer appears to handle the sequence of hash characters in an unexpected way. The issue manifests when processing the heading sequence - characters that should be part of the heading sequence are being handled differently than expected.

### Expected behavior

The parser should correctly tokenize ATX headings by:
1. Consuming all consecutive `#` characters as part of the heading sequence
2. Properly transitioning to the heading text content
3. Maintaining the correct structure of the heading tokens

The current behavior seems to be breaking this flow, particularly in the `sequenceFurther` function which handles consecutive hash characters.

### System Info
- remark version: 15.0.1
- Using the vendored version in jest

---
Repository: /testbed
