# Bug Report

### Ternary operator branches are swapped in conditional expressions

I'm experiencing an issue where the wrong branch of a ternary/conditional expression is being evaluated. When I have code like `condition ? trueValue : falseValue`, it seems like the branches are reversed - when the condition is true, I get the false branch value and vice versa.

### Reproduction

```js
// Simple conditional expression
const result = someCondition ? 'should be this when true' : 'should be this when false';

// When someCondition is true, result contains 'should be this when false'
// When someCondition is false, result contains 'should be this when true'
```

This is affecting my production build where conditional logic is being inverted. For example:

```js
const value = isEnabled ? enabledValue : disabledValue;
// Returns disabledValue when isEnabled is true
// Returns enabledValue when isEnabled is false
```

### Expected behavior

The consequent branch (first value after `?`) should be returned when the condition is truthy, and the alternate branch (value after `:`) should be returned when the condition is falsy.

### Additional context

This seems to have started happening recently. Not sure if this is related to tree-shaking optimizations or dead code elimination, but the behavior is definitely backwards from what it should be.

---
Repository: /testbed
