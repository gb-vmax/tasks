# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX tag parsing where attributes in opening tags are being incorrectly rejected with an error message about closing tags. The error message says "Unexpected attribute in closing tag, expected the end of the tag" even when working with opening tags that should allow attributes.

### Reproduction

```jsx
<Component attribute="value">
  content
</Component>
```

When parsing the above MDX content, the attribute on the opening tag triggers an error with the message:
```
Unexpected attribute in closing tag, expected the end of the tag
```

This is confusing because:
1. The tag is an opening tag, not a closing tag
2. Opening tags should be able to have attributes

### Expected behavior

Opening tags with attributes should parse correctly without errors. The error about "closing tag" should only appear when actually encountering attributes on a closing tag like `</Component attribute="invalid">`.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
