# Bug Report

### Describe the bug

I'm encountering an issue with markdown heading parsing where headings with trailing hash symbols (`#`) are not being properly closed. It appears that headings are continuing to consume content when they should be terminated.

### Reproduction

```markdown
# Heading with trailing hashes ##

Some paragraph text that should not be part of the heading.
```

When parsing the above markdown, the paragraph text is being incorrectly included as part of the heading content instead of being treated as a separate paragraph node.

### Expected behavior

The parser should properly recognize the end of ATX-style headings and exit the heading context when encountering:
- End of line (null or line ending characters)
- Content after the closing hash sequences

The paragraph text should be parsed as a separate block element, not as part of the heading text.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have started happening recently. The heading tokenizer appears to be checking conditions incorrectly when determining whether to close the heading or continue parsing.

---
Repository: /testbed
