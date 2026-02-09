# Bug Report

### Describe the bug

I'm encountering an issue with JSX flow tag parsing in MDX where the closing marker and self-closing marker appear to be in the wrong order. This causes JSX tags to be parsed incorrectly when they have specific structures.

### Reproduction

When parsing MDX content with JSX flow tags, the tag markers are not being processed in the correct sequence. This affects how self-closing tags and closing tags are identified during the tokenization phase.

Example MDX content that triggers the issue:
```mdx
<Component />

<AnotherComponent>
  content
</AnotherComponent>
```

The parser seems to be looking for markers in an unexpected order, which can lead to incorrect parsing results or unexpected token sequences.

### Expected behavior

JSX flow tags should be parsed correctly with the proper marker order:
1. Opening tag marker
2. Self-closing marker (for self-closing tags like `<Component />`)
3. Closing marker (for closing tags like `</Component>`)

The current implementation appears to have these markers swapped, causing the parser to misidentify tag types.

### System Info
- Package: @mdx-js/mdx@3.0.0
- Node version: Latest

---
Repository: /testbed
