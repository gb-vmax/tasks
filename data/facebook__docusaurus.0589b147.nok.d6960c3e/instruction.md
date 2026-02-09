# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain markdown constructs are not being parsed correctly. It seems like when the parser tries multiple constructs and they fail, it's not falling back to the next construct properly.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
Some text with [invalid construct here
And more text
`;

const result = processor.processSync(markdown);
console.log(result);
```

When parsing markdown with constructs that should fail and fall back to alternative parsing strategies, the parser seems to get stuck or skip constructs instead of trying all available options.

### Expected behavior

The parser should try each construct in the list sequentially when previous ones fail. If a construct fails (nok is called), it should move to the next construct in the list and continue trying until either one succeeds or all constructs have been exhausted.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have broken markdown parsing for edge cases where multiple parsing strategies need to be attempted. The parser appears to be checking constructs in the wrong order or skipping some entirely.

---
Repository: /testbed
