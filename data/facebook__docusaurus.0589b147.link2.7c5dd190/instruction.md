# Bug Report

### Describe the bug

I'm experiencing an issue with link parsing in MDX content. When I try to use markdown links in my MDX files, they're not being rendered correctly. The links appear to be parsed but the resulting structure seems malformed.

### Reproduction

```mdx
Here's a [simple link](https://example.com) in my content.

And another [link with title](https://test.com "Test Title").
```

When processing this MDX content, the links don't render as expected. Instead of creating proper link elements, something else is being generated.

### Expected behavior

Links should be properly parsed and rendered as clickable anchor elements with the correct href and children text. The parser should create a proper link node structure with:
- type: "link"
- url: the href value
- children: array containing the link text
- title: optional title attribute

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started recently, possibly after an update. Links were working fine before.

---
Repository: /testbed
