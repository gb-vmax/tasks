# Bug Report

### Describe the bug

I'm experiencing an issue with parsing markdown titles that contain quotes. It seems like the parser is not correctly handling the closing marker for quoted titles, and the logic appears to be reversed or executing in the wrong order.

### Reproduction

```js
// Example markdown that fails to parse correctly
const markdown = `
[link](url "title with quotes")
`;

// The title parsing seems to break when it encounters the closing quote
// The parser either exits too early or processes the marker check incorrectly
```

### Expected behavior

The parser should correctly identify when it encounters the closing quote marker and properly exit the string type before beginning a new section. The title should be parsed completely and the link should be valid.

### Additional context

This appears to be related to the title parsing logic in the remark vendor code. The behavior changed recently and now quoted titles in links are not being recognized properly. The parser seems to be checking conditions in the wrong order or returning before completing necessary operations.

---
Repository: /testbed
