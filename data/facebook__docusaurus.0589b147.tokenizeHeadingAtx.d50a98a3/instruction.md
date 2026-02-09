# Bug Report

### Describe the bug

I'm experiencing an issue with heading parsing in MDX where headings with 7 hash marks (`#######`) are being treated as valid ATX headings when they should be rejected according to the CommonMark spec. Valid ATX headings should only support 1-6 hash marks for h1-h6 elements.

### Reproduction

```markdown
####### This should not be a heading
```

When parsing the above MDX content, it gets treated as a valid heading instead of being rejected or treated as plain text.

### Expected behavior

According to the CommonMark specification, ATX headings must have between 1 and 6 `#` characters. A line starting with 7 or more `#` characters should not be parsed as a heading.

The parser should reject `####### text` and treat it as regular paragraph content instead of a heading element.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
