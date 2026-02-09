# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where bold/strong text is not being rendered correctly. When I use double asterisks or double underscores to create bold text, the output seems to be broken.

### Reproduction

```js
const markdown = '**This should be bold**';
const result = remark().parse(markdown);
// The AST node type is incorrect and children is null instead of an array
```

Another example:
```js
const text = 'Some __bold text__ here';
const parsed = remark().process(text);
// Bold formatting is not applied in the output
```

### Expected behavior

Bold/strong text should be properly parsed and rendered. The AST should contain nodes with type "strong" and the children property should be an array containing the text nodes.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
