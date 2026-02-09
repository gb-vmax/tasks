# Bug Report

### Describe the bug

I'm encountering an issue with tree-shaking when using if statements without an else branch. It appears that the consequent (then branch) is not being included in the bundle when there's no alternate (else branch), even though the condition might be true at runtime.

### Reproduction

```js
// input.js
let condition = true;

if (condition) {
  console.log('This should be included');
}

// The console.log statement is being incorrectly removed from the bundle
```

Another example:

```js
function test(x) {
  if (x > 0) {
    doSomething();
  }
  // No else branch
}

// doSomething() call is missing from the output
```

### Expected behavior

When an if statement doesn't have an else branch, the consequent block should still be included in the bundle if it contains side effects or is otherwise needed. The presence or absence of an alternate branch shouldn't affect whether the consequent is included.

### Additional context

This seems to be related to how the bundler handles inclusion of AST nodes for if statements. The issue only appears when there's no else clause - if statements with else branches work fine.

---
Repository: /testbed
