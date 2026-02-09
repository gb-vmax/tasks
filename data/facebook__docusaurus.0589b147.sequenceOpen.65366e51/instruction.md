# Bug Report

### Describe the bug

I'm experiencing an issue with ATX heading parsing where headings with 7 or more hash marks (`#`) are being incorrectly accepted as valid headings. According to the CommonMark spec, ATX headings should only support 1-6 levels, but it appears that headings with 7+ hashes are now being parsed as valid level 6 headings.

### Reproduction

```markdown
####### This should not be a valid heading
######## Neither should this
```

When parsing the above markdown, both lines are being treated as valid headings when they should be rejected or treated as plain text.

### Expected behavior

Only headings with 1-6 hash marks should be recognized as valid ATX headings. Any line starting with 7 or more consecutive `#` characters should not be parsed as a heading.

For example:
- `# Heading 1` ✓ Valid
- `###### Heading 6` ✓ Valid  
- `####### Not a heading` ✗ Should be invalid

### Additional context

This seems to have started happening recently. The parser is now allowing one extra level beyond the maximum of 6 that the spec allows.

---
Repository: /testbed
