# Bug Report

### Describe the bug

I'm experiencing an issue with inline code rendering in markdown parsing. When using inline code blocks (backticks) in my markdown content, the parsed output is getting corrupted or showing unexpected behavior. It seems like the code text is being assigned to the wrong node in the AST.

### Reproduction

```js
const markdown = `
This is some text with \`inline code\` in the middle.
`;

// Parse the markdown
const result = parseMarkdown(markdown);

// The inline code node doesn't have the correct value
console.log(result); // Shows unexpected structure
```

When I parse markdown containing inline code blocks, the code text appears to be going to the wrong place in the tree structure. This breaks rendering of inline code snippets.

### Expected behavior

Inline code blocks should be parsed correctly and the text content should be properly associated with the code node in the AST. The rendered output should display the inline code as expected.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
