# Bug Report

### Describe the bug

I'm encountering an issue with switch statements that have only a single case. When bundling code that contains a switch statement with exactly one case, the output appears to be malformed or the case is not being rendered correctly.

### Reproduction

```js
switch (value) {
  case 'foo':
    doSomething();
    break;
}
```

When this code is processed through the bundler, the single case doesn't seem to be handled properly. 

### Expected behavior

Switch statements with a single case should be rendered correctly in the output bundle, just like switch statements with multiple cases.

### Additional context

This seems to specifically affect switch statements that have exactly one case. Switch statements with zero cases or multiple cases appear to work fine. Not sure if this is a recent regression or if it's been there for a while.

---
Repository: /testbed
