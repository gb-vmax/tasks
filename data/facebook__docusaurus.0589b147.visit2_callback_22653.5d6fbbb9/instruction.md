# Bug Report

### Describe the bug

I'm experiencing an issue with footnote and definition references in MDX. When I have both a footnote and a definition with the same identifier, the wrong one gets used. It seems like footnotes and definitions are getting mixed up internally.

### Reproduction

```mdx
Here's a reference to a definition [foo].

And here's a footnote reference[^foo].

[foo]: https://example.com
[^foo]: This is a footnote
```

When rendering this, the definition link `[foo]` incorrectly resolves to the footnote content, and vice versa. The two different reference types are interfering with each other.

### Expected behavior

Definitions and footnotes should be handled separately. A definition reference `[foo]` should link to the URL defined in `[foo]: https://example.com`, and a footnote reference `[^foo]` should display the footnote text from `[^foo]: This is a footnote`.

The two types of references shouldn't interfere with each other even when they share the same identifier.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
