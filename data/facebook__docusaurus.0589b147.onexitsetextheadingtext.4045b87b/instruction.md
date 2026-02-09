# Bug Report

### Describe the bug

I'm experiencing an issue with setext-style heading parsing in the markdown processor. When using setext headings (underlined with `=` or `-`), the parser seems to be handling line endings incorrectly after the heading text.

### Reproduction

```markdown
This is a heading
=================
Some text after the heading
```

When parsing this markdown, the text following the setext heading is not being processed correctly. It appears that line endings are being consumed or handled improperly, causing the subsequent content to be malformed or merged incorrectly with the heading.

### Expected behavior

The parser should correctly handle setext-style headings and preserve proper line ending behavior so that content following the heading is parsed as separate blocks. The heading text should be properly terminated and the next line of content should be treated independently.

### Additional context

This seems to affect both level 1 headings (underlined with `=`) and level 2 headings (underlined with `-`). The issue manifests when there's content immediately following the heading underline.

---
Repository: /testbed
