# Bug Report

### Describe the bug

When parsing MDX with JSX attributes that have expression values, the parser is accessing the wrong attribute in the attributes array. This causes attribute values to be assigned to the incorrect attribute or potentially throws an error when trying to access properties on the wrong object type.

### Reproduction

```jsx
<Component attr={someExpression} />
```

When the above MDX is parsed, the expression value `someExpression` gets assigned to the wrong attribute in the AST. The parser appears to be looking at `tag.attributes[tag.attributes.length - 2]` instead of the last attribute, and also checking for the wrong type (`tail.type !== "mdxJsxAttribute"` instead of `tail.type === "mdxJsxAttribute"`).

### Expected behavior

The expression value should be correctly assigned to the last attribute in the attributes array (the one currently being processed). The parser should:
1. Access the correct attribute using `tag.attributes[tag.attributes.length - 1]`
2. Verify it's an mdxJsxAttribute with the correct type check

### Additional context

This affects any JSX component in MDX that uses expression values for attributes. The issue is in the `exitMdxJsxTagAttributeValueExpression` function in the remark-mdx parser.

---
Repository: /testbed
