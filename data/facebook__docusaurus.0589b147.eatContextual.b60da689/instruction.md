# Bug Report

### Describe the bug

I'm experiencing an issue with contextual keyword parsing in the MDX parser. When the parser encounters a contextual keyword that doesn't match the expected name, it's advancing the token stream when it shouldn't be, and vice versa - when it finds the correct contextual keyword, it's not advancing.

### Reproduction

```js
// When parsing MDX content with contextual keywords
const mdx = `
export const meta = { title: 'Test' }

Some content here
`

// The parser incorrectly handles contextual keywords
// For example, when expecting 'as' but encountering something else,
// it advances the token anyway
```

### Expected behavior

The `eatContextual` method should:
1. Return `false` and NOT advance the token stream when the contextual keyword doesn't match
2. Return `true` and advance the token stream when the contextual keyword matches

Currently it's doing the opposite - advancing when it shouldn't and not advancing when it should.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is causing parsing errors in MDX files that use contextual keywords in various positions.

---
Repository: /testbed
