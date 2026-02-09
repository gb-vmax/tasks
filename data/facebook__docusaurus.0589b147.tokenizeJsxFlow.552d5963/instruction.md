# Bug Report

### Describe the bug

I'm experiencing an issue with parsing MDX JSX flow tags after a recent update. The parser seems to be cutting off or incorrectly handling JSX tag attributes, causing the entire parsing to fail.

### Reproduction

```mdx
<Component 
  attributeName="value"
  anotherAttribute="test"
/>
```

When trying to parse MDX content with JSX flow tags that have attributes, the parser appears to truncate or mishandle the attribute token names. This results in incomplete parsing and the content not rendering properly.

### Expected behavior

JSX flow tags with attributes should be parsed completely and correctly. All attribute names and values should be properly tokenized and the component should render as expected.

### Additional context

This seems to affect JSX components in flow context (block-level) with attributes. The issue appears to be related to how attribute names are being tokenized - specifically around the longer token type names like `mdxJsxFlowTagAttributeNamePrefixMarker` and similar tokens.

---
Repository: /testbed
