# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where closing tags with whitespace are not being handled correctly. When there's whitespace between the closing marker `/` and the tag name in a closing tag, the parser fails to process it properly.

### Reproduction

```mdx
<Component>
  content
</ Component>
```

When parsing MDX with a closing tag that has whitespace after the `/`, the parser doesn't recognize it as a valid closing tag structure.

### Expected behavior

The parser should handle whitespace between the closing marker and tag name in closing tags, similar to how JSX/XML parsers typically work. The closing tag `</ Component>` should be parsed the same way as `</Component>`.

### Additional context

This seems to affect any MDX component with whitespace in the closing tag. The issue appears specifically when there's a space character (code 32) between the `/` and the tag name.

---
Repository: /testbed
