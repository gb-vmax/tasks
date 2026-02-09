# Bug Report

### Describe the bug

I'm encountering an issue with self-closing JSX tags in MDX files. When using self-closing tags, they appear to be incorrectly added to the tag stack, which causes problems with subsequent tag parsing.

### Reproduction

```mdx
<Component />
<AnotherComponent>
  content here
</AnotherComponent>
```

When parsing MDX with self-closing tags followed by other elements, the self-closing tag seems to remain on the internal stack even though it shouldn't (since it's self-closing). This leads to unexpected behavior when processing the document.

### Expected behavior

Self-closing tags should not be pushed onto the tag stack since they don't have corresponding closing tags. The parser should handle them as complete elements that don't affect the nesting of subsequent elements.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
