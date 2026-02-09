# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where member expressions that reference variables are not being included in the output bundle. When a member expression uses a variable (rather than direct object access), the code gets incorrectly removed during the tree-shaking process.

### Reproduction

```js
const obj = {
  nested: {
    value: 42
  }
};

const myVar = obj;
console.log(myVar.nested.value); // This gets removed from bundle
```

Expected the variable reference to be preserved, but it's being tree-shaken out even though it's clearly used.

### Expected behavior

Member expressions that reference variables should be included in the bundle when they are part of the execution path. The code should not be removed during tree-shaking.

### Additional context

This seems to happen specifically when:
1. Using a variable as the base of a member expression
2. The member expression is part of the included code path

The direct object access works fine, but referencing through a variable causes the code to be incorrectly eliminated.

---
Repository: /testbed
