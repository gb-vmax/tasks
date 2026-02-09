# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in markdown parsing. When using code blocks with language identifiers, the language info seems to be getting assigned to the wrong node in the AST, causing unexpected behavior in the parsed output.

### Reproduction

```js
const markdown = `
\`\`\`javascript
console.log('hello');
\`\`\`
`;

// Parse the markdown
const result = parse(markdown);

// The code block node doesn't have the correct lang property
// Instead, something else seems to be getting modified
```

### Expected behavior

The fenced code block should have its `lang` property set to "javascript" and the code content should be preserved correctly. The language identifier from the fence info line should be attached to the code block node itself, not to some other node in the tree.

### Additional context

This seems to affect any fenced code block with a language identifier. The parser appears to be modifying the wrong part of the AST when processing the fence info.

---
Repository: /testbed
