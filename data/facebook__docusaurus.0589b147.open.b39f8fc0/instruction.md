# Bug Report

### Describe the bug

When parsing HTML content in markdown, certain HTML tags are not being recognized correctly. Specifically, closing tags (like `</div>`) and regular opening tags (like `<span>`) are being rejected when they should be valid HTML text tokens.

### Reproduction

```js
// This HTML should be parsed correctly but isn't
const markdown = `
Some text with <div>content</div> here
And also <span>inline elements</span>
`;

// The closing tag </div> and opening tag <span> are not tokenized properly
// They get rejected instead of being processed as valid HTML
```

### Expected behavior

Both opening tags (e.g., `<span>`) and closing tags (e.g., `</div>`) should be properly tokenized and recognized as valid HTML text within markdown content. The parser should consume these tokens and process them correctly.

### Additional context

This seems to affect inline HTML elements in markdown. The HTML tags are being skipped or not consumed properly during the tokenization phase, causing them to be treated as plain text or rejected entirely.

---
Repository: /testbed
