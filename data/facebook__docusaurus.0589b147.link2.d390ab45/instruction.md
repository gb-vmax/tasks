# Bug Report

### Describe the bug

I'm experiencing an issue with link parsing in MDX content. When I include links in my MDX files, they're not being rendered correctly - the link elements appear to be missing their type information and children are not being processed.

### Reproduction

```mdx
This is a [test link](https://example.com) in my content.
```

When this MDX is compiled, the link doesn't render as expected. Instead of getting a proper anchor tag, the output seems to be missing critical link metadata.

### Expected behavior

Links should be properly parsed and rendered as anchor elements with the correct href attribute and link text. The compiled output should include:
- Proper link type identification
- URL from the markdown syntax
- Children nodes containing the link text

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
