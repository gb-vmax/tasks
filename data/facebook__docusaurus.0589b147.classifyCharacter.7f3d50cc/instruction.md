# Bug Report

### Describe the bug

I'm experiencing an issue with character classification in markdown parsing. It seems like the parser is misclassifying certain characters, particularly when dealing with null values or whitespace characters. This is causing unexpected behavior when parsing markdown content.

### Reproduction

```js
// When parsing markdown with specific character sequences
const markdown = `
Some text with special characters
  
And whitespace handling
`;

// The parser appears to be treating null/whitespace characters incorrectly
// resulting in wrong classification values
```

### Expected behavior

Characters should be properly classified:
- Null characters and whitespace should return classification value `1`
- Punctuation should return classification value `2`

Currently it seems like the classification logic is inverted or broken, causing whitespace and null values to be classified incorrectly.

### System Info
- remark version: 15.0.1
- Environment: Node.js

This is affecting markdown parsing reliability, especially with edge cases involving whitespace and special characters. Any help would be appreciated!

---
Repository: /testbed
