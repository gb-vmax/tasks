# Bug Report

### Describe the bug

I'm experiencing an issue with MDX link processing where regular links (non-reference links) are getting a `referenceType` property set incorrectly. When I create a standard markdown link, the resulting AST node contains a `referenceType` property that shouldn't be there for non-reference links.

### Reproduction

```mdx
[Click here](https://example.com)
```

When parsing this regular link, the output node incorrectly includes a `referenceType` property. This property should only exist on reference-style links like `[link][ref]` or `[link]`.

### Expected behavior

For regular inline links with explicit URLs, the AST node should not have a `referenceType` property. Only reference-style links should have this property.

Regular link: `[text](url)` → should NOT have `referenceType`
Reference link: `[text][ref]` → should have `referenceType`

### Additional context

This seems to affect how links are processed and could cause issues downstream when tools expect standard link nodes to not have reference-related properties.

---
Repository: /testbed
