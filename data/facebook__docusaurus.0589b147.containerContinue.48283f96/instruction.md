# Bug Report

### Describe the bug

I'm experiencing issues with MDX parsing where the document state seems to be getting corrupted during container continuation. The parser appears to be handling nested containers incorrectly, which causes unexpected behavior when processing complex MDX structures.

### Reproduction

```js
// Example MDX content with nested containers
const mdxContent = `
> Blockquote
> 
> > Nested blockquote
> > with multiple lines
`;

// When parsing this content, the container state gets mixed up
const result = compile(mdxContent);
```

The issue seems to occur specifically when:
1. Processing nested container blocks (like blockquotes, lists, etc.)
2. The parser needs to continue processing a container across multiple lines
3. Multiple levels of nesting are involved

### Expected behavior

The parser should correctly maintain the container state stack and properly track which container construct is being processed at each nesting level. Nested containers should be parsed correctly without state corruption.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This appears to be a regression as similar MDX content was working correctly in previous versions. The container continuation logic seems to have changed in a way that breaks the state management.

---
Repository: /testbed
