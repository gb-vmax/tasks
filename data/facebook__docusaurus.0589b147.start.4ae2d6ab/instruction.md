# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where nested block containers (like lists or blockquotes) aren't being handled correctly. When I have deeply nested structures, the parser seems to be checking continuation conditions incorrectly, which causes it to either skip processing some containers or fail to properly close them.

### Reproduction

```js
const markdown = `
> Outer blockquote
> > Nested blockquote
> > > Deep nested blockquote
> > Content here
`;

const result = remark().parse(markdown);
// The nested structure is not preserved correctly
```

Another example with lists:
```js
const markdown = `
- Item 1
  - Nested item
    - Deep nested item
  - Another nested item
`;

const result = remark().parse(markdown);
// Nested list items may not be properly associated with their parent
```

### Expected behavior

The parser should correctly maintain the stack of nested containers and properly check continuation conditions for each level. All nested block structures should be preserved in the AST with the correct parent-child relationships.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
