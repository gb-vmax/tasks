# Bug Report

### Describe the bug

I'm encountering an issue where parsing MDX content fails when the input string ends at a specific position. The parser seems to miss the final token in some cases, causing unexpected behavior when processing MDX files.

### Reproduction

```js
const mdx = require('@mdx-js/mdx');

// This fails to parse correctly
const content = `# Hello`;
const result = await mdx.compile(content);

// The parser doesn't properly handle end-of-file detection
// when position equals input length
```

### Expected behavior

The parser should correctly detect end-of-file and finish tokenization when reaching the end of the input string. All valid MDX content should be parsed completely, including the last character.

### Additional context

This appears to be related to how the tokenizer checks for end-of-file. The issue manifests when parsing content where the position counter reaches exactly the input length - the final token isn't being processed as expected.

---
Repository: /testbed
