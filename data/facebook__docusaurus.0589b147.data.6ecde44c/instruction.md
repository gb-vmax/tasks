# Bug Report

### Describe the bug

I'm experiencing an issue with text parsing in remark where certain markdown content is not being processed correctly. It seems like the parser is exiting the data state prematurely, which causes text content to be split or handled incorrectly.

### Reproduction

```js
const remark = require('remark');

const markdown = `
This is some text content that should be parsed as a single data block.
`;

const result = remark().parse(markdown);
console.log(result);
```

When processing markdown with continuous text content, the parser appears to be exiting the data state too early, before all the text has been consumed. This results in unexpected parsing behavior where text nodes are not properly formed.

### Expected behavior

The parser should continue consuming characters in the data state until it reaches an actual break point (like null, newline, etc.). Text content should be properly grouped into data nodes before transitioning to the next state.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
