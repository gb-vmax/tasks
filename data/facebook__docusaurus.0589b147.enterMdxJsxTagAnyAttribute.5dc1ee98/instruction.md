# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX tag parsing where attributes on self-closing tags are being incorrectly flagged as errors. When I try to use attributes on a self-closing JSX component in my MDX file, the parser throws an unexpected error about attributes in closing tags.

### Reproduction

```mdx
<MyComponent name="test" />
```

When parsing this MDX content, I get an error message:
```
Unexpected attribute in closing tag, expected the end of the tag
```

This happens with any self-closing tag that has attributes. The parser seems to be treating self-closing tags as if they were closing tags.

### Expected behavior

Self-closing JSX tags with attributes should parse correctly without throwing errors. The syntax `<Component prop="value" />` is valid JSX and should be supported in MDX.

### Additional context

This appears to have started happening recently. Regular opening tags with attributes work fine, but self-closing tags are being rejected.

---
Repository: /testbed
