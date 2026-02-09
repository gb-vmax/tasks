# Bug Report

### Describe the bug

HTML text parsing is broken when processing inline HTML elements. The parser appears to exit the `htmlText` state prematurely before consuming the opening character, causing HTML content to not be recognized or parsed correctly.

### Reproduction

```js
const markdown = 'Some text with <span>inline HTML</span> content';
const result = remark().parse(markdown);
// The HTML span is not properly recognized as an htmlText node
```

When parsing markdown with inline HTML tags, the HTML elements are not being correctly identified. The opening `<` character seems to trigger the parser to exit the HTML text state immediately instead of continuing to process the HTML content.

### Expected behavior

Inline HTML elements should be properly parsed and represented in the AST. The `htmlText` node should encompass the entire HTML tag/element, not exit before consuming any characters.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
