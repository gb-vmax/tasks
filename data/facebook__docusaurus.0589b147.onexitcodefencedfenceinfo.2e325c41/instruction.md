# Bug Report

### Describe the bug
When parsing fenced code blocks in markdown, the language identifier is not being set correctly on the code node. Instead of the `lang` property being populated with the language info (e.g., `javascript`, `python`), the data appears to be going to the wrong property or wrong node entirely.

### Reproduction
```js
const markdown = `
\`\`\`javascript
console.log('hello');
\`\`\`
`;

// Parse the markdown
const result = remark.parse(markdown);

// Expected: result should have a code node with lang='javascript'
// Actual: lang property is missing or incorrect
console.log(result.children[0].lang); // undefined or wrong value
```

### Expected behavior
The fenced code block should have its language identifier properly stored in the `lang` property of the code node. For example, a code block starting with ` ```javascript` should result in a node with `lang: 'javascript'`.

### System Info
- remark version: 15.0.1

This is affecting syntax highlighting and code block processing in our documentation site. The language information seems to be getting lost during the parsing phase.

---
Repository: /testbed
