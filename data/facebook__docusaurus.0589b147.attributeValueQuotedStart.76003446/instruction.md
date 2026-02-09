# Bug Report

### Describe the bug

I'm experiencing an issue with quoted attribute values in JSX tags when they span multiple lines. After a line break within a quoted attribute value, the parser seems to lose track of the quote context and doesn't properly handle the continuation of the attribute value.

### Reproduction

```mdx
<Component
  attr="value
  continued on next line"
/>
```

When parsing JSX tags with quoted attribute values that contain line breaks, the attribute value handling appears to break. The parser doesn't correctly resume parsing the quoted value after the newline.

### Expected behavior

Quoted attribute values should be able to span multiple lines, and the parser should maintain the quote context across line breaks. The attribute value should be parsed as a single continuous value until the closing quote is encountered.

### Additional context

This seems to affect attributes with both single and double quotes. The issue appears when there's a line ending character within the quoted value - the parser state doesn't properly restore to continue parsing the quoted content.

---
Repository: /testbed
