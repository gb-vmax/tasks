# Bug Report

### Describe the bug

I'm experiencing an issue with autolink detection in GFM (GitHub Flavored Markdown) parsing. It seems like autolinks at the beginning of a document or line are not being properly recognized, while autolinks in the middle of text work fine.

### Reproduction

```js
// This doesn't work - autolink at the start
const markdown1 = 'https://example.com is a website'

// This works fine - autolink in the middle
const markdown2 = 'Check out https://example.com for more info'
```

When parsing the first example, the URL is not being converted to a proper autolink, but the second example works as expected.

### Expected behavior

Autolinks should be detected and converted correctly regardless of their position in the text. A URL at the beginning of a line should be treated the same as a URL in the middle of a line.

### Additional context

This seems to have started happening recently. I'm using remark-gfm for parsing GitHub Flavored Markdown and the autolink literal extension should handle bare URLs automatically.

---
Repository: /testbed
