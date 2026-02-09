# Bug Report

### Describe the bug

I'm encountering an issue with parsing MDX code that contains braces. The parser seems to be incorrectly handling the context stack when encountering opening braces `{`, which leads to unexpected parsing errors or incorrect AST generation.

### Reproduction

```js
const mdx = `
# Hello

{someExpression}

More content here
`

// Parsing this MDX content fails or produces incorrect output
const result = compile(mdx)
```

Also happens with more complex cases:

```js
const mdx = `
export const foo = () => {
  return <div>test</div>
}
`
```

### Expected behavior

The MDX parser should correctly handle opening braces and maintain the proper context stack, allowing expressions and block statements to be parsed without errors.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
