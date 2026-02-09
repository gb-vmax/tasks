# Bug Report

### Describe the bug

I'm experiencing an issue with MDX link parsing where regular links and reference-style links are being processed incorrectly. It seems like the logic for determining whether a link is a reference or a regular link has been inverted.

### Reproduction

When parsing MDX content with both regular and reference-style links:

```markdown
This is a [regular link](https://example.com)

This is a [reference link][ref]

[ref]: https://example.com
```

The regular links are being treated as reference links and vice versa. The AST nodes have the wrong `type` property - regular links get `linkReference` type when they should be `link`, and reference links get `link` type when they should be `linkReference`.

### Expected behavior

- Regular inline links like `[text](url)` should produce nodes with `type: "link"` and have `url` and `title` properties
- Reference-style links like `[text][ref]` should produce nodes with `type: "linkReference"` and have `identifier` and `label` properties

### Additional context

This appears to affect all link parsing in MDX documents. The `url` and `title` properties are being deleted from regular links while `identifier` and `label` are being deleted from reference links, which is backwards from what should happen.

---
Repository: /testbed
