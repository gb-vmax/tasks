# Bug Report

### Describe the bug

I'm encountering an issue with MDX expression parsing where curly braces in expressions are not being handled correctly. The parser seems to be tracking brace depth incorrectly, which causes expressions with nested braces to fail or behave unexpectedly.

### Reproduction

```mdx
{/* Simple expression - works */}
{someVariable}

{/* Nested object - doesn't work as expected */}
{{ key: 'value' }}

{/* Function with object parameter - fails */}
{myFunction({ param: 'test' })}
```

When using expressions that contain nested curly braces (like object literals or function calls with object parameters), the parser doesn't properly match the opening and closing braces. This results in either premature closing of the expression or the expression not being recognized at all.

### Expected behavior

The parser should correctly track brace depth and handle nested curly braces within MDX expressions. Expressions containing object literals, nested objects, or function calls with object parameters should be parsed correctly.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
