# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX text tag parsing where the closing tag marker seems to be incorrectly identified or processed. When using closing tags in inline JSX elements within MDX content, the parser appears to be treating them the same as opening tag markers.

### Reproduction

```mdx
Some text with <Component>inline content</Component> in the middle.
```

When parsing this MDX content, the closing tag `</Component>` doesn't seem to be properly distinguished from the opening tag marker. The tokenization appears to assign the same token type to both opening and closing markers.

### Expected behavior

Opening and closing JSX tag markers should be tokenized differently. The closing tag marker (e.g., `</`) should have its own distinct token type (`mdxJsxTextTagClosingMarker`) separate from the opening tag marker (`mdxJsxTextTagMarker`).

### Additional context

This seems to affect inline/text-level JSX components specifically. The parser should properly differentiate between:
- Opening tag marker: `<`
- Closing tag marker: `</`
- Self-closing marker: `/>`

Currently it appears the closing tag marker is being assigned the wrong token type during tokenization.

---
Repository: /testbed
