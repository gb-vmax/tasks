# Bug Report

### Describe the bug

I'm experiencing an issue with MDX link parsing where the link text/children are not being properly extracted. When I create a link in my MDX file, the resulting AST seems to have incorrect or missing children nodes.

### Reproduction

```mdx
[Click here](https://example.com)
```

When this gets parsed, the link node doesn't contain the expected children. It seems like the parser is looking at the wrong part of the stack when processing the link label.

### Expected behavior

The link node should have its children properly populated with the text content "Click here". The AST should look something like:

```js
{
  type: 'link',
  url: 'https://example.com',
  children: [{ type: 'text', value: 'Click here' }]
}
```

But instead the children array appears to be empty or contains unexpected nodes.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This might be related to how the label exit handler is accessing the stack. Any help would be appreciated!

---
Repository: /testbed
