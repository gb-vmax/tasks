# Bug Report

### Describe the bug

I'm encountering an issue with setext heading parsing in markdown. When I try to use setext-style headings (underlined with `=` or `-`), they're not being recognized correctly. The parser seems to be treating the underline as a separate element instead of converting the text above into a heading.

### Reproduction

```markdown
This should be a heading
========================

This should also be a heading
-----------------------------
```

When parsing this markdown, the headings aren't being detected properly. The text and underlines are being treated as separate blocks instead of being combined into setext headings.

### Expected behavior

The parser should recognize setext-style headings where:
- Text underlined with `===` becomes an h1
- Text underlined with `---` becomes an h2

The underline characters should all match (all `=` or all `-`) and the heading should be properly formed in the output.

### Additional context

This seems to have started recently. ATX-style headings (using `#`) still work fine, but setext headings are completely broken. This is affecting our documentation rendering.

---
Repository: /testbed
