# Bug Report

### Describe the bug

I'm encountering an issue with setext heading parsing where line endings are not being handled correctly. When a setext heading is followed by content, the line ending behavior seems inverted - it's slurping line endings when it shouldn't be.

### Reproduction

```markdown
Heading
=======

Some paragraph text here.
```

When parsing this markdown, the line ending after the setext heading underline is being incorrectly included in elements that shouldn't contain it. This causes the subsequent paragraph to be malformed or merged incorrectly.

### Expected behavior

The line ending after a setext heading should be properly handled and not slurped into the heading or following content when it shouldn't be. Each block element should maintain proper separation.

### Additional context

This appears to affect the parsing of setext-style headings (underlined with `=` or `-`) specifically. ATX-style headings (with `#`) seem to work fine. The issue manifests when there's content immediately following the heading.

---
Repository: /testbed
