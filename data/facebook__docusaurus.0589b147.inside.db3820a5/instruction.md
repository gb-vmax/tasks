# Bug Report

### Describe the bug
When using nested curly braces in MDX expressions, the parser incorrectly handles the brace matching. Specifically, expressions with nested objects or function calls that contain braces are not being parsed correctly, causing the expression to terminate prematurely or behave unexpectedly.

### Reproduction
```mdx
{someFunction({ nested: { value: 'test' } })}
```

or

```mdx
{user.map(u => ({ id: u.id, name: u.name }))}
```

### Expected behavior
The parser should correctly match opening and closing braces even when they are nested within the expression. The entire expression should be parsed as a single unit, allowing for nested object literals, arrow functions with object returns, and other valid JavaScript expressions that contain multiple levels of braces.

### Additional context
This seems to affect any MDX expression that has nested curly braces. The issue appears to be related to how the parser tracks brace depth when determining where an expression ends.

---
Repository: /testbed
