# Bug Report

### Describe the bug

I'm experiencing an issue where token position tracking seems to be incorrect when parsing MDX content. The `lastTokEnd` and `lastTokStart` values appear to be referencing the wrong token positions, causing position information to be off by one token.

### Reproduction

```js
// Parse MDX content with multiple tokens
const parser = new MDXParser();
parser.parse(`
# Hello World
<Component />
`);

// Check token positions
// lastTokStart and lastTokEnd are pointing to the current token
// instead of the previous token as expected
```

When iterating through tokens, the "last token" position properties are actually holding the current token's position instead of the previous one. This breaks any logic that relies on comparing the current token position with the previous token position.

### Expected behavior

`lastTokStart` and `lastTokEnd` should contain the position information of the *previous* token, not the current one. The position should be captured before calling `nextToken()` to advance to the next token.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
