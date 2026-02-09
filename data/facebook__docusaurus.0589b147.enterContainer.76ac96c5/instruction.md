# Bug Report

### Describe the bug

I'm experiencing a crash when using container directives in my markdown content. The parser throws a `TypeError` saying it cannot read properties of undefined when processing container directive blocks.

### Reproduction

```js
const markdown = `
:::note
This is a container directive
:::
`;

// Parser crashes when trying to serialize back to markdown
const result = unified()
  .use(remarkParse)
  .use(remarkDirective)
  .use(remarkStringify)
  .processSync(markdown);
```

The error message I'm getting is:
```
TypeError: Cannot read properties of undefined (reading 'call')
```

This seems to happen specifically with container directives (the `:::` syntax). Leaf directives with single colons work fine.

### Expected behavior

The markdown should be parsed and serialized without errors. Container directives should be handled the same way as other directive types.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
