# Bug Report

### Describe the bug

I'm encountering an issue where variable scoping seems to be broken in MDX parsing. When using variables in nested scopes (like inside functions or blocks), the parser appears to be looking at the wrong scope level, causing variables to be resolved incorrectly or not found at all.

### Reproduction

```jsx
export function MyComponent() {
  const localVar = 'test';
  
  return (
    <div>
      {localVar}
    </div>
  );
}
```

When parsing this MDX code, the parser fails to correctly identify `localVar` in its proper scope. It seems like the scope resolution is off by one level.

### Expected behavior

Variables declared in a local scope should be correctly identified and resolved within that scope. The parser should track the current scope accurately so that variable lookups work as expected.

### Additional context

This appears to affect any code with nested scopes - functions, blocks, etc. The variable resolution seems to be checking the parent scope instead of the current scope, which causes legitimate local variables to either not be found or to incorrectly shadow outer variables.

---
Repository: /testbed
