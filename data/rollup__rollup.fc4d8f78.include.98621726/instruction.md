# Bug Report

### Describe the bug

I'm experiencing an issue with do-while loops in my code where the test condition appears to be evaluated incorrectly during tree-shaking. When I have a do-while statement with a test condition that should be included in the bundle, it seems like the condition is being excluded or not properly included when it should be.

### Reproduction

```js
let x = 0;
do {
  x++;
  console.log(x);
} while (someCondition());
```

When bundling code with do-while loops, the test condition (`someCondition()`) doesn't seem to be included properly in certain cases. This appears to happen when the condition has side effects or references that should be preserved.

### Expected behavior

The test condition of a do-while loop should always be included in the bundle when the loop body is included, regardless of the inclusion context. The condition needs to be evaluated to determine whether the loop continues, so it should be treated as a necessary part of the statement.

### Additional context

This seems related to how the AST nodes handle inclusion during the tree-shaking phase. The test expression should be included with the same context as the rest of the do-while statement.

---
Repository: /testbed
