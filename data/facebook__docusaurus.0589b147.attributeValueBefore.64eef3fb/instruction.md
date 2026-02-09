# Bug Report

### Describe the bug

Single-quoted attribute values in MDX are not being parsed correctly. When using single quotes (`'`) for attribute values in JSX tags, the parser seems to treat them the same as double quotes, which breaks the parsing of the closing quote.

### Reproduction

```mdx
<Component name='value' />
```

The above MDX fails to parse correctly. The single quote closing the attribute value is not recognized properly, causing the parser to continue looking for a double quote instead.

### Expected behavior

Both single quotes and double quotes should work interchangeably for attribute values in JSX tags, just like in regular JSX/React:

```mdx
<Component name="value" />  // should work
<Component name='value' />  // should also work
```

The parser should correctly identify and match the closing quote character based on the opening quote character used.

### Additional context

This appears to be a regression as single-quoted attributes used to work in previous versions. The issue seems related to how the quote marker is being tracked during attribute value parsing.

---
Repository: /testbed
