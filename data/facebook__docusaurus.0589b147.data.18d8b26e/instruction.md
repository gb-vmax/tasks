# Bug Report

### Describe the bug

I'm encountering an issue with text parsing in remark where line breaks in markdown content are not being handled correctly. The parser seems to be consuming characters incorrectly when it encounters break points in the data, leading to malformed output or unexpected behavior.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
Some text here
with a line break
and more content
`;

const result = processor.processSync(markdown);
console.log(result);
```

When processing markdown with line breaks, the output doesn't match what's expected. It appears that the parser is not properly transitioning between states when it encounters break points in the text data.

### Expected behavior

The markdown parser should correctly handle line breaks and preserve the structure of the text. Each line should be processed independently and the output should maintain the proper formatting.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
