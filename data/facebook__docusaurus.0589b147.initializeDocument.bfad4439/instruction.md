# Bug Report

### Describe the bug

I'm encountering an issue with parsing nested Markdown containers where the parser seems to be exiting containers incorrectly. When I have deeply nested block structures (like lists within blockquotes), the parser doesn't properly handle the container boundaries.

### Reproduction

```markdown
> - Item 1
>   - Nested item
> - Item 2
```

When parsing this structure, the nested containers aren't being closed/exited at the right points. It seems like the logic for determining when to exit a container is off by one somewhere.

### Expected behavior

The parser should correctly handle nested container structures and exit containers at the appropriate boundaries. Each level of nesting should be properly tracked and closed when the container ends.

### Additional context

This appears to affect the document initialization logic, specifically around how the parser determines continuation of containers and when to exit them. The issue manifests when working with multiple levels of nesting.

---
Repository: /testbed
