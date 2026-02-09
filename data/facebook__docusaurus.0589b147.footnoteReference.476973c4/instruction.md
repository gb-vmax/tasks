# Bug Report

### Describe the bug

Footnote references are generating incorrect `href` attributes. When a footnote is referenced multiple times in a document, the links are pointing to the wrong targets, causing navigation issues.

### Reproduction

```mdx
Here's a footnote reference[^1].

And here's the same footnote referenced again[^1].

[^1]: This is the footnote content.
```

When rendered, the footnote reference links have `href="#fnref-..."` instead of `href="#fn-..."`, which means they're pointing to themselves rather than to the actual footnote definition at the bottom of the page.

### Expected behavior

Footnote reference links should use `href="#fn-{id}"` to point to the footnote definition. The `id` attribute can use `fnref-{id}` to identify the reference itself, but the `href` should point to where the footnote content is located (using the `fn-` prefix).

### Additional context

This affects all footnote references in MDX documents. When users click on a footnote number, they expect to be taken to the footnote definition, but instead the link doesn't work as expected.

---
Repository: /testbed
