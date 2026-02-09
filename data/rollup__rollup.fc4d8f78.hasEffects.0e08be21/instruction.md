# Bug Report

### Describe the bug

I'm encountering an issue where member expressions with side effects are not being properly evaluated during the tree-shaking process. It appears that certain property accesses that should be considered as having side effects are being incorrectly removed from the bundled output.

### Reproduction

```js
const obj = {
  get prop() {
    console.log('side effect');
    return 42;
  }
};

// This access should be preserved due to the getter's side effect
obj.prop;
```

When bundling this code, the property access `obj.prop` gets removed even though the getter has a side effect (the console.log). The expected behavior is that this access should be preserved in the output since it triggers observable behavior.

### Expected behavior

Member expressions that trigger getters with side effects should be preserved during tree-shaking. The bundler should recognize that accessing properties can have observable effects and should not remove these accesses from the final output.

### Additional context

This seems to affect any member expression where:
1. The object itself has side effects when evaluated
2. The property access triggers a getter or proxy trap

The issue is particularly problematic when working with objects that have getters performing logging, state updates, or other side effects that are important for the application's behavior.

---
Repository: /testbed
