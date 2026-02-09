# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When a fenced code block starts with just the fence characters (like ` ``` `) without any info string, the parser seems to hang or behave incorrectly.

### Reproduction

```js
const markdown = `
\`\`\`
some code here
\`\`\`
`;

// Parser appears to hang or produce unexpected output
const result = remark.parse(markdown);
```

Also happens with tildes:

```js
const markdown = `
~~~
code block
~~~
`;
```

### Expected behavior

The parser should correctly handle fenced code blocks that don't have an info string (language identifier). These are valid markdown and should be parsed without issues.

### Additional context

This seems to affect basic code blocks without language specifications. Code blocks with language identifiers (like ` ```javascript `) appear to work fine. The issue started appearing recently, possibly after some changes to the fence tokenization logic.

---
Repository: /testbed
