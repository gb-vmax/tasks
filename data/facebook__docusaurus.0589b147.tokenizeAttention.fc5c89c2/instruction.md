# Bug Report

### Describe the bug

I'm experiencing an issue with emphasis/strong markers (asterisks and underscores) in MDX content. The opening and closing detection seems to be inverted - text that should be emphasized/bold isn't being rendered correctly, and in some cases text that shouldn't be emphasized is getting the wrong formatting.

### Reproduction

```md
**bold text**
*italic text*
_underscored text_
__double underscored__
```

When parsing the above MDX content, the emphasis markers are not being properly detected. It seems like the logic for determining which markers are "opening" vs "closing" is backwards - what should open an emphasis sequence is being treated as closing it, and vice versa.

### Expected behavior

- `**bold text**` should render as bold
- `*italic text*` should render as italic  
- `_underscored text_` should render as italic
- `__double underscored__` should render as bold

The parser should correctly identify when an attention sequence (emphasis/strong marker) is opening a span vs closing it based on the surrounding whitespace and punctuation.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
