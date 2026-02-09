# Bug Report

### Describe the bug

When using conditional expressions (ternary operators) in MDX files, the consequent and alternate branches are being swapped in the generated output. The code that should execute when the condition is true is instead executed when it's false, and vice versa.

### Reproduction

```jsx
// Input MDX
const result = condition ? 'true-value' : 'false-value'

// Expected output when condition is true: 'true-value'
// Actual output when condition is true: 'false-value'
```

Another example:
```jsx
{isLoggedIn ? <Dashboard /> : <Login />}

// When isLoggedIn is true, <Login /> is rendered instead of <Dashboard />
// When isLoggedIn is false, <Dashboard /> is rendered instead of <Login />
```

### Expected behavior

The ternary operator should follow standard JavaScript semantics where `condition ? consequent : alternate` evaluates to `consequent` when the condition is truthy and `alternate` when the condition is falsy.

Currently, it appears the branches are reversed in the generated code.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
