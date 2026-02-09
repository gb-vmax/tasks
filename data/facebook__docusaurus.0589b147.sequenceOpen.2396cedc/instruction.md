# Bug Report

### Describe the bug

I'm experiencing an issue with ATX heading parsing where headings with 7 or more `#` symbols are being accepted as valid headings. According to the CommonMark spec, ATX headings should only support 1-6 levels (i.e., `#` through `######`), but it appears that headings with 7 hash symbols are now being parsed incorrectly.

### Reproduction

```js
const markdown = `####### This should not be a valid heading`;

// This is being parsed as a valid heading when it shouldn't be
```

When parsing markdown with 7 consecutive `#` symbols at the start of a line, the parser treats it as a valid heading instead of rejecting it or treating it as plain text.

### Expected behavior

According to the CommonMark specification, only 1-6 `#` symbols should create valid ATX headings. A line starting with 7 or more `#` symbols should not be recognized as a heading.

For example:
- `# Heading 1` - valid
- `###### Heading 6` - valid  
- `####### Not a heading` - should NOT be parsed as a heading

### System Info

- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
