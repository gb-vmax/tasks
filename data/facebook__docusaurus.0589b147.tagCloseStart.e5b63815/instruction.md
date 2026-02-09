# Bug Report

### Describe the bug

HTML closing tags are not being parsed correctly. When trying to use closing tags in markdown content, they're being rejected even when they should be valid.

### Reproduction

```js
const markdown = `
<div>
  Some content
</div>
`;

// Process the markdown
const result = processor.processSync(markdown);
```

The closing tag `</div>` is not being recognized properly. It seems like valid alphabetic characters in closing tags are being treated as invalid, causing the parser to fail.

### Expected behavior

Valid HTML closing tags with alphabetic characters should be parsed correctly. The closing tag `</div>` should be recognized as a valid closing tag and processed normally.

### Additional context

This appears to affect any closing tag that starts with an alphabetic character. Opening tags work fine, but closing tags are broken.

---
Repository: /testbed
