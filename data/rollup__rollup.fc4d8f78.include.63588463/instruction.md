# Bug Report

### Describe the bug

I'm experiencing an issue with conditional statements where the test condition logic appears to be inverted. When I have an if-statement with a constant/known test condition, the wrong branch is being included in the output bundle.

### Reproduction

```js
// Input code
if (true) {
  console.log('This should be included');
} else {
  console.log('This should be removed');
}

// Expected output: Only the consequent branch
// Actual output: The alternate branch is included instead
```

This also happens with other constant conditions:

```js
if (false) {
  doSomething();
} else {
  doSomethingElse();
}

// The wrong branch gets included in the bundle
```

### Expected behavior

When the test condition can be statically determined (e.g., literal `true` or `false`), only the appropriate branch should be included in the final bundle. Dead code from the unused branch should be eliminated.

### Additional context

This seems to affect tree-shaking - code that should be removed is being kept, and code that should be kept is being removed. The behavior is reversed from what it should be.

---
Repository: /testbed
