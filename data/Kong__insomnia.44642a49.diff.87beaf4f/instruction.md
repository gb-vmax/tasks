# Bug Report

### Describe the bug

I'm experiencing an issue with the diff algorithm when comparing strings. It seems like the matching logic isn't working correctly, causing incorrect operations to be generated when there are differences between source and target strings.

### Reproduction

```js
const source = "hello world";
const target = "hello beautiful world";
const blockSize = 4;

const operations = diff(source, target, blockSize);
// Operations generated are incorrect - blocks aren't being matched properly
```

When I run this, the diff operations don't correctly identify the matching portions between the strings. It looks like the character-by-character matching after finding a block match is broken.

### Expected behavior

The diff function should correctly identify matching blocks between source and target strings and generate appropriate COPY and INSERT operations. Matching characters should be properly extended beyond the initial block match.

### Additional context

This appears to affect the sync functionality when comparing document changes. The algorithm should be able to match blocks and then extend those matches character-by-character, but something seems off with the matching logic.

---
Repository: /testbed
