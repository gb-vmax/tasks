# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where certain characters are not being processed correctly. It seems like the tokenizer is treating valid construct definitions as `null` values, causing them to be skipped during parsing.

### Reproduction

```js
// Parse markdown with specific character codes
const result = parse(`
# Heading
Some text with special characters
`);

// Expected: proper AST nodes for all content
// Actual: some nodes are missing or incorrectly parsed
```

When processing markdown with certain character codes, the parser appears to be checking if the construct definition itself is null rather than retrieving the actual construct from the map. This causes valid constructs to be ignored.

### Expected behavior

All valid markdown constructs should be properly tokenized and parsed into the AST, regardless of the character code. The tokenizer should correctly look up construct definitions from the character map and process them accordingly.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
