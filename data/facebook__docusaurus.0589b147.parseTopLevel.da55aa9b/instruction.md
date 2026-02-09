# Bug Report

### Describe the bug

I'm experiencing an issue where parsing MDX files with a large number of top-level statements causes the parser to stop prematurely. The parser seems to be cutting off after a certain number of statements, even though there's more content to parse.

### Reproduction

```js
// Create an MDX file with many top-level statements
const mdxContent = `
${Array(1500).fill(0).map((_, i) => `export const var${i} = ${i};`).join('\n')}
`;

// Parse the content
const result = parse(mdxContent);

// Only the first ~1000 statements are parsed
console.log(result.body.length); // Expected: 1500, Actual: 1000
```

### Expected behavior

The parser should process all statements in the file regardless of how many there are. There shouldn't be an arbitrary limit on the number of top-level statements that can be parsed.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

This is blocking our use case where we generate large MDX files programmatically with many exports.

---
Repository: /testbed
