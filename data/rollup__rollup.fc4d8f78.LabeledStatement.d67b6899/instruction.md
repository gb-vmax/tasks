# Bug Report

### Describe the bug

I'm experiencing an issue with labeled statements in my code. When using a labeled `break` statement, the label is not being included in the output bundle even though it should be.

### Reproduction

```js
function test() {
  outer: {
    if (someCondition) {
      break outer;
    }
    doSomething();
  }
}
```

After bundling, the `outer:` label is missing from the output, which causes a syntax error since the `break outer;` statement references a label that doesn't exist.

### Expected behavior

When a labeled statement contains a `break` that references that label, the label should be included in the bundled output. The code should work the same way after bundling as it does before.

### Additional context

This seems to happen specifically with labeled blocks (not loops) that have break statements inside them. Regular labeled loops seem to work fine.

---
Repository: /testbed
