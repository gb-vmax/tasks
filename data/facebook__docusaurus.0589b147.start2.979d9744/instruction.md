# Bug Report

### Describe the bug

After a recent update, MDX link references are not being parsed correctly. When using reference-style links with defined identifiers, the links fail to render and appear as plain text instead.

### Reproduction

```md
[example link][ref]

[ref]: https://example.com
```

Expected: The link should render as a clickable link to `https://example.com`

Actual: The text appears as plain text `[example link][ref]` without being converted to a link

This also affects image references:

```md
![alt text][image-ref]

[image-ref]: /path/to/image.png
```

The image reference is not being resolved and shows up as raw markdown text.

### Expected behavior

Reference-style links and images should be properly resolved when their identifiers are defined elsewhere in the document. The parser should recognize the defined references and convert them to their corresponding HTML elements.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This was working fine in the previous version. It seems like something changed in how the label end tokenizer handles defined references.

---
Repository: /testbed
