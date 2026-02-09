# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where certain token types are not being collected properly. It seems like the logic for handling `lineEnding` tokens and other token types has changed, causing some content to be skipped or not processed correctly.

### Reproduction

```js
// When parsing MDX content with specific token types
const tokenTypes = ['emphasis', 'strong'];
const events = [
  ['enter', { type: 'emphasis' }, context],
  // ... more events
];

// The collect function doesn't process tokens as expected
const result = collect(events, tokenTypes);
// Expected tokens are missing from the result
```

### Expected behavior

The `collect` function should include tokens when either:
1. The token type is `lineEnding`, OR
2. The token type is included in the `tokenTypes` array

Currently it seems like both conditions need to be true simultaneously, which causes valid tokens to be excluded from the collection.

Additionally, when processing chunks, all leading `-1` values should be removed, not just the first one.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
