# Bug Report

### Describe the bug

JSX elements with single children are being incorrectly wrapped with array brackets when using automatic JSX runtime mode. The generated code includes closing brackets `]` even when there's only one child element, which breaks the output.

### Reproduction

```jsx
// Input JSX
const element = <div>Hello World</div>;

// Expected output (automatic runtime)
jsx('div', { children: 'Hello World' })

// Actual output
jsx('div', { children: 'Hello World'] })
// Notice the incorrect closing bracket
```

This also happens with single element children:

```jsx
const element = <div><span>test</span></div>;

// Gets rendered with incorrect bracket
jsx('div', { children: jsx('span', { children: 'test' })] })
```

### Expected behavior

Single children should not be wrapped in array brackets. Only multiple children should use the array syntax:

```jsx
// Single child - no brackets
<div>text</div> → jsx('div', { children: 'text' })

// Multiple children - with brackets
<div>text<span/></div> → jsx('div', { children: ['text', jsx('span', {})] })
```

### System Info
- Rollup version: latest
- JSX runtime: automatic mode

---
Repository: /testbed
