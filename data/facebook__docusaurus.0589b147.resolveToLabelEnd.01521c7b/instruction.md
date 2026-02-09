# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link parsing where links at the beginning of a document are not being processed correctly. It seems like the parser is skipping or mishandling the first link when there are multiple links present.

### Reproduction

```markdown
[First link](https://example.com) and [Second link](https://example.org)
```

When parsing the above markdown, the first link doesn't get recognized properly while subsequent links work fine. If I add some text before the first link, it works as expected:

```markdown
Some text [First link](https://example.com) and [Second link](https://example.org)
```

This works correctly.

### Expected behavior

All links should be parsed correctly regardless of their position in the document. The first link in a document should be processed the same way as any other link.

### Additional context

This appears to have started happening recently. I'm using remark@15.0.1 for markdown processing. The issue is particularly noticeable when the link is the very first element in the markdown content.

---
Repository: /testbed
