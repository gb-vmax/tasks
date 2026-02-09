# Bug Report

### Describe the bug

Links in MDX documents are being incorrectly parsed and converted to reference-style links when they should be regular inline links. The condition for determining whether a link is a reference or inline link appears to be inverted, causing standard markdown links to be treated as references.

### Reproduction

```mdx
This is a [regular link](https://example.com) in my document.
```

When parsing this MDX content, the link is being incorrectly identified as a reference-style link instead of an inline link. The `url` and `title` properties are being deleted from the node while `identifier` and `label` properties (which should only exist for reference links) are being preserved.

### Expected behavior

Regular inline links like `[text](url)` should be parsed as inline links with `url` and `title` properties, not as reference-style links. Reference-style links like `[text][ref]` or `[text]` should be the ones converted to reference types.

The parser should correctly distinguish between:
- Inline links: `[link text](https://example.com)`
- Reference links: `[link text][reference-id]` or `[link text]`

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
