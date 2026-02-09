# Bug Report

### Describe the bug

I'm encountering an issue with setext heading parsing in markdown. When parsing setext-style headings (headings with underlines using `=` or `-`), the output appears to be malformed or missing content.

### Reproduction

```js
const markdown = `This is a heading
=================

Some content here.`

// Parse the markdown
const result = remark().parse(markdown)

// The heading node structure seems incorrect
// Expected the heading to include all the text above the underline
```

### Expected behavior

Setext headings should be properly parsed with the correct content and structure. The heading text should be fully captured and the AST should reflect the proper node relationships.

### Additional context

This seems to affect markdown documents that use setext-style headings (underlined headings). The issue might be related to how the parser resolves and constructs the heading nodes from the events.

---
Repository: /testbed
