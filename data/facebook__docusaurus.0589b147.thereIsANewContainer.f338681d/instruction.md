# Bug Report

### Describe the bug

I'm experiencing issues with MDX document parsing where container exit logic seems to be happening in the wrong order. When processing nested containers in MDX documents, the flow is being closed and containers are being exited at incorrect times, leading to malformed document structures.

### Reproduction

```js
// Create an MDX document with nested containers
const mdxContent = `
> Quote block
> with continuation
>
> - List item in quote
> - Another item
`;

// Parse the document
const result = compile(mdxContent);
```

The parser appears to be exiting containers before completing the document continuation flow, which causes the structure to be processed incorrectly.

### Expected behavior

Containers should be exited after the document flow has been properly continued and processed. The order of operations should ensure that:
1. Flow is closed
2. Document continuation is processed
3. Containers are exited

Currently it seems like containers are being exited at the wrong point in the sequence.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
