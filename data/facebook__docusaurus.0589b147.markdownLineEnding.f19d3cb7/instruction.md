# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing in markdown content. When processing directives that span multiple lines or contain line breaks, the parser doesn't correctly recognize line endings, causing directives to either fail to parse or parse incorrectly.

### Reproduction

```js
const content = `
:::note
This is a note
with multiple lines
:::
`;

// Parser fails to recognize the directive properly
// Line breaks within the directive are not handled correctly
```

Another case:
```js
const content = `::directive content with\nline break`;
// The line break isn't detected as expected
```

### Expected behavior

The parser should correctly identify markdown line endings (newlines, carriage returns) and properly parse directives that contain them. Multi-line directives should be fully supported.

### Additional context

This seems to affect both container directives (:::) and inline directives (::) when they contain line breaks. The issue appears to be related to how line ending characters are detected during parsing.

---
Repository: /testbed
