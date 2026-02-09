# Bug Report

### Describe the bug

I'm experiencing an issue with ATX heading parsing where headings with 7 hash marks (`#######`) are being accepted as valid headings, when they should be rejected according to the CommonMark spec. Additionally, headings that should be valid (ending with a newline or EOF) are not being recognized properly.

### Reproduction

```markdown
####### This should not be a valid heading
```

The above markdown is being parsed as a valid heading when it should be treated as regular text since it has 7 hash marks instead of the maximum allowed 6.

Also, valid headings like:
```markdown
## Valid heading
```

Are not being recognized correctly in certain cases where they end with a newline character.

### Expected behavior

- Headings with more than 6 hash marks should NOT be parsed as headings
- Headings with 1-6 hash marks followed by whitespace and ending with newline or EOF should be parsed correctly as headings

According to CommonMark, ATX headings can only have 1-6 `#` characters at the start.

### System Info
- MDX version: 3.0.0
- Parser: micromark

---
Repository: /testbed
