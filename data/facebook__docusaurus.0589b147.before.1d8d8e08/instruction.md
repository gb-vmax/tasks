# Bug Report

### Describe the bug

When parsing MDX JSX flow tags, the token names appear to be incorrectly ordered in the factory function call. This causes attributes and tag names to potentially be assigned the wrong token types during parsing.

### Reproduction

```jsx
<Component attribute="value" />
```

When parsing JSX flow tags like the above, the internal token classification seems to be mixing up tag name tokens with attribute name tokens. Specifically, `"mdxJsxFlowTagNamePrimary"` and `"mdxJsxFlowTagAttributeNamePrimary"` appear to be swapped in position, along with several other token type parameters being out of order.

This affects the parsing of JSX elements at the block level in MDX documents.

### Expected behavior

Token types should be correctly assigned to their corresponding syntax elements during parsing. Tag names should receive tag name tokens, and attributes should receive attribute tokens in the proper sequence.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
