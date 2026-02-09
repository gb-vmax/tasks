# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX tag attributes where the attribute type is being set incorrectly. When parsing JSX tags with attributes, the parser creates attribute nodes with the wrong `type` field.

### Reproduction

```jsx
<Component foo="bar" />
```

When parsing this MDX content, the attribute node for `foo` is created with `type: "mdxJsxExpressionAttribute"` instead of the expected `type: "mdxJsxAttribute"`.

### Expected behavior

Regular JSX attributes (like `foo="bar"`) should be parsed as `mdxJsxAttribute` nodes, not `mdxJsxExpressionAttribute` nodes. Expression attributes are meant for spread syntax and JSX expressions (e.g., `{...props}`), not regular name-value pairs.

The AST node should have:
```js
{
  type: "mdxJsxAttribute",
  name: "foo",
  value: "bar"
}
```

But instead it's being created as:
```js
{
  type: "mdxJsxExpressionAttribute",
  name: "foo", 
  value: "bar"
}
```

This is causing issues downstream when tools expect the correct node type for standard JSX attributes.

---
Repository: /testbed
