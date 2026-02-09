# Bug Report

### Describe the bug

I'm encountering an issue with directive containers where the parsing seems to be producing incorrect results. The container content and container itself appear to be getting closed in the wrong order, which is causing problems when processing nested directive structures.

### Reproduction

```js
const markdown = `
:::note
This is a container directive
:::
`;

// Parse the markdown with remark-directive
const result = parser.parse(markdown);

// The AST structure is malformed - the exit events 
// are happening in the wrong sequence
```

When parsing directive containers, the content exit and container exit events are not properly ordered. This affects the resulting AST structure and can lead to unexpected behavior when transforming or rendering the directives.

### Expected behavior

The directive container should be properly closed with the correct event ordering - the content should be exited before the container itself is exited. The AST should have a well-formed structure that correctly represents the nesting hierarchy.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
