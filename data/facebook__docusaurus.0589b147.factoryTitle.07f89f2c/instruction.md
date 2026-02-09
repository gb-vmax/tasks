# Bug Report

### Describe the bug

I'm encountering an issue with markdown link/image title parsing. When I try to use titles in markdown links or images with quotes, the parser doesn't recognize them correctly and fails to parse the title string.

### Reproduction

```js
// This should parse correctly but doesn't
const markdown = '[link](url "title")'

// Also fails with single quotes
const markdown2 = "[link](url 'title')"

// Image titles are also broken
const markdown3 = '![alt](image.png "image title")'
```

When trying to parse markdown with titles enclosed in quotes (both single and double), the title string is not being recognized or extracted properly. It seems like the quote matching logic isn't working as expected.

### Expected behavior

The parser should correctly identify and extract title strings when they're enclosed in matching quotes. The title should be parsed as part of the link/image definition.

### Additional context

This seems to have broken recently - I was able to parse titles with quotes before. The issue affects both links and images with titles.

---
Repository: /testbed
