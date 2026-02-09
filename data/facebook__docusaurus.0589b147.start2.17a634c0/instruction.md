# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where certain null character handling seems broken. When processing content with specific character codes, the parser appears to be constructing an incorrect list of constructs to handle, leading to unexpected behavior.

### Reproduction

```js
// When the tokenizer encounters a null character or specific code points,
// the construct list is built incorrectly

const parser = createParser(/* ... */);
const tokenizer = createTokenizer(parser, initialize, from);

// Processing content with null characters or edge case code points
// results in wrong construct handling
```

### Expected behavior

The tokenizer should correctly build the list of constructs by:
1. Including constructs specific to the current code point (if available)
2. Including fallback constructs from `map.null` (if available)
3. Properly handling both cases regardless of whether the code is null or not

### Current behavior

The construct list appears to be built with the wrong values, causing the parser to either skip valid constructs or include incorrect ones when processing certain characters.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems like it might be related to how the `all3` variable is computed and how it's being spread into the `list3` array. The logic for determining which constructs to include doesn't seem right.

---
Repository: /testbed
