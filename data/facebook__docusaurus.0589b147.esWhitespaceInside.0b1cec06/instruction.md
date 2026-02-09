# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where newlines/line endings inside JSX expressions are being handled incorrectly. When I have JSX code that spans multiple lines with whitespace, the parser seems to be treating line endings differently than expected.

### Reproduction

```jsx
<Component
  prop={
    someValue
  }
/>
```

When parsing the above MDX content, the whitespace handling appears to be broken for expressions that contain line breaks. The parser doesn't seem to recognize line endings properly within the JSX expression context.

### Expected behavior

The parser should correctly handle line endings (newlines) within JSX expressions and treat them as valid whitespace. Multi-line JSX expressions should parse without issues, just like they do in regular JSX/React code.

### Additional context

This seems to affect any JSX expression that spans multiple lines. Single-line expressions work fine, but as soon as there's a newline character involved, the parsing behavior changes unexpectedly.

---
Repository: /testbed
