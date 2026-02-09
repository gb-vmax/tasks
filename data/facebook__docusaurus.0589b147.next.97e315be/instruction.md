# Bug Report

### Describe the bug

I'm experiencing an issue with token position tracking in the MDX parser. It seems like the `lastTokStart` and `lastTokEnd` values are being swapped or set incorrectly, which causes problems when trying to access the positions of previously parsed tokens.

### Reproduction

```js
// Parse some MDX content
const parser = createParser(options);
parser.parse('# Hello World');

// After parsing, check token positions
console.log('Last token start:', parser.lastTokStart);
console.log('Last token end:', parser.lastTokEnd);

// The start and end positions appear to be reversed
// lastTokStart shows the end position
// lastTokEnd shows the start position
```

### Expected behavior

The `lastTokStart` should contain the start position of the last token, and `lastTokEnd` should contain the end position. Currently they seem to be swapped, which breaks any code that relies on accurate token position information for error reporting or source mapping.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
