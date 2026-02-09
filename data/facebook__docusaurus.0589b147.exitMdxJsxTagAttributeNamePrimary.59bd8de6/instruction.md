# Bug Report

### Describe the bug

I'm encountering an issue when parsing MDX JSX tags with attributes. It seems like attribute names are being assigned to the wrong node in the AST. When I have JSX elements with multiple attributes, the attribute name ends up on an incorrect node type.

### Reproduction

```jsx
<Component prop1="value1" prop2="value2" />
```

When parsing this JSX, the attribute name is being set on what appears to be an `mdxJsxAttributeExpression` node instead of the `mdxJsxAttribute` node. The code is accessing `tag.attributes[tag.attributes.length - 2]` and expecting it to be an attribute expression, but it should be accessing the last attribute in the array.

### Expected behavior

The parser should correctly identify and set the name property on the actual `mdxJsxAttribute` node (the last item in the attributes array), not on a different node type located at an earlier position.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
