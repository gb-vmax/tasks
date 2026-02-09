# Bug Report

### Describe the bug

When using JSX with empty or whitespace-only text nodes, the compiled output includes extra commas before the empty children. This results in invalid JavaScript being generated.

### Reproduction

```jsx
function Component() {
  return (
    <div>
      {/* empty expression */}
      {}
    </div>
  );
}
```

Or with whitespace-only text:

```jsx
function Component() {
  return (
    <div>
      
    </div>
  );
}
```

### Expected behavior

Empty JSX expressions and whitespace-only text nodes should be properly filtered out without leaving trailing commas in the compiled output. The generated code should be valid JavaScript.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
