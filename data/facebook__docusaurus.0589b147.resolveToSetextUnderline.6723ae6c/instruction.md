# Bug Report

### Describe the bug

I'm experiencing an issue with setext headings in markdown parsing. When I try to parse markdown content with setext-style headings (underlined with `=` or `-`), the parser is not correctly handling the content above the underline.

### Reproduction

```js
const markdown = `
This is a heading
=================

Some paragraph text here.
`;

// Parse the markdown
const result = remark().parse(markdown);

// The heading node is not properly formed
// Content that should be part of the heading is missing or malformed
```

### Expected behavior

The parser should correctly identify the text above the setext underline as heading content and create a proper heading node with all the content preserved. The paragraph following the heading should remain separate.

### Additional context

This seems to affect markdown documents that use setext-style headings (the underline style with `=` or `-` characters). ATX-style headings (with `#` prefix) appear to work fine. The issue manifests when there's content that needs to be resolved into the heading structure.

---
Repository: /testbed
