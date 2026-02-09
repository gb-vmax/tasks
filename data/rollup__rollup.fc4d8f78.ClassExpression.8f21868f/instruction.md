# Bug Report

### Describe the bug

I'm encountering an issue with class expressions when they appear in certain contexts. The parentheses wrapping seems to be inverted - they're being added in the wrong positions and at the wrong times.

### Reproduction

When I have a class expression that's NOT part of an expression statement, I'm seeing misplaced parentheses in the output. For example:

```js
// Input code with a class expression
const MyClass = class {
  constructor() {}
};

// Or using it in other contexts like:
export default class {};
```

The generated code has parentheses in unexpected places - they appear to be backwards (closing paren before opening paren) and they're being added when they shouldn't be.

### Expected behavior

Class expressions should only be wrapped in parentheses when they're used as expression statements (to avoid being parsed as class declarations). In other contexts, they shouldn't have extra parentheses added, and definitely not in reverse order.

The output should be valid JavaScript without malformed parentheses.

### Additional context

This seems to affect any class expression that's not directly in an expression statement context - assignments, exports, etc. The logic for when to add parentheses appears to be inverted.

---
Repository: /testbed
