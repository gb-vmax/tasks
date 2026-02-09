# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where certain markdown constructs are not being recognized correctly. It seems like the parser is skipping over valid syntax and treating it as plain text instead of processing it as the intended construct.

### Reproduction

When I try to parse MDX content with specific constructs, they don't get processed properly:

```mdx
# This is a heading

Some text with **bold** and *italic* formatting.

- List item 1
- List item 2
```

The parser seems to be treating some of these constructs as regular data/text instead of recognizing them as their respective markdown elements. This causes the output to be incorrectly formatted.

### Expected behavior

The parser should correctly identify and process markdown constructs (headings, emphasis, lists, etc.) instead of treating them as plain text. Each construct should be tokenized and handled according to its type.

### Additional context

This appears to be related to how the text tokenizer determines when to break and attempt parsing constructs versus continuing to consume characters as data. The issue is intermittent and seems to depend on the specific combination of constructs used.

---
Repository: /testbed
