# Bug Report

### Describe the bug

I'm experiencing an issue with conditional statements where the branches are being evaluated incorrectly. When I have an if-else statement, it seems like the wrong branch is being executed or analyzed.

### Reproduction

```js
if (someCondition) {
  // This block should execute when someCondition is true
  doSomething();
} else {
  // This block should execute when someCondition is false
  doSomethingElse();
}
```

The behavior is inverted - when `someCondition` evaluates to true, the code acts as if it's false, and vice versa. This is causing my build to include/exclude the wrong code branches.

### Expected behavior

When the condition is true, the consequent block should be evaluated. When the condition is false, the alternate block should be evaluated. Currently it seems to be doing the opposite.

### Additional context

This seems to affect how the bundler determines which code has side effects and should be included in the output. I'm seeing unexpected code being tree-shaken or included based on inverted logic.

---
Repository: /testbed
