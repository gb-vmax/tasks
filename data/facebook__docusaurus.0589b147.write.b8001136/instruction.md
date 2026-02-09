# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where content is being processed incorrectly. It seems like the parser is checking the wrong position in the chunks array and also using an incorrect index when adding results.

### Reproduction

```js
// When parsing markdown content with the remark tokenizer
const parser = createTokenizer(/* ... */);

// Writing content to the parser
parser.write(someMarkdownSlice);

// The parser returns an empty array prematurely
// and processes tokens with wrong offsets
```

### Expected behavior

The tokenizer should:
1. Check if the last chunk (not the first chunk) is null before returning early
2. Add results starting from the correct initial position (0, not 1)

The current behavior causes markdown content to be parsed incorrectly, potentially missing content or applying wrong token positions.

### System Info
- Using remark@15.0.1
- Issue appears in the tokenizer's write function

---
Repository: /testbed
