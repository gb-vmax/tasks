# Bug Report

### Describe the bug

I'm seeing duplicate variable declarations being generated in the output when using MDX. It looks like variable declarations are being written twice, which causes invalid JavaScript to be produced.

### Reproduction

When processing MDX content that contains variable declarations, the generated JavaScript output includes the same variable declaration twice in a row.

For example, if the MDX contains:
```js
const myVar = 'test';
```

The generated output becomes something like:
```js
const myVar = 'test';const myVar = 'test';
```

This results in a "SyntaxError: Identifier 'myVar' has already been declared" when trying to execute the generated code.

### Expected behavior

Variable declarations should only appear once in the generated output. Each variable should be declared exactly one time.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
