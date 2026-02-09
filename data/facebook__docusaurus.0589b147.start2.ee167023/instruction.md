# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where text content is being incorrectly handled. It seems like the parser is swapping the behavior when deciding whether to treat content as text or not-text based on line breaks.

### Reproduction

When parsing MDX content with specific line break patterns, the parser appears to make the wrong decision about how to handle the text. For example:

```mdx
Some text content
with line breaks

And more content
```

The parser seems to be inverting its logic - treating text as non-text and vice versa when encountering break points.

### Expected behavior

The parser should correctly identify text content and handle it appropriately. When `atBreak()` returns true, it should process the content as text, and when it returns false, it should process it as non-text.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is causing unexpected parsing results in my MDX documents. Any help would be appreciated!

---
Repository: /testbed
