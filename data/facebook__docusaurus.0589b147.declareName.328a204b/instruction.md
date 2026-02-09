# Bug Report

### Describe the bug

I'm encountering an issue with variable declaration scope checking in MDX files. It seems like the parser is incorrectly flagging certain variable declarations as redeclarations when they shouldn't be.

### Reproduction

When I try to declare a variable in MDX with the same name in different scopes, I get unexpected behavior:

```mdx
export const myVar = 'outer';

function MyComponent() {
  const myVar = 'inner'; // This should be fine but causes issues
  return <div>{myVar}</div>;
}
```

The variable `myVar` inside the function should shadow the outer declaration without any problems, but the parser seems to be treating this as a redeclaration error or allowing redeclarations that shouldn't be allowed.

### Expected behavior

Variables declared in inner scopes should properly shadow outer scope declarations without being flagged as redeclarations. The scope checking logic should correctly identify when a variable is being redeclared in the same scope vs. a different scope.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
