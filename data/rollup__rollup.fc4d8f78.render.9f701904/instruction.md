# Bug Report

### Describe the bug

Getting a runtime error when rendering switch statements with no case clauses. The code crashes when trying to access `this.cases[0].start` on an empty cases array.

### Reproduction

```js
// This switch statement has no cases
switch (someValue) {
}
```

When bundling code that contains an empty switch statement like above, the build process throws an error trying to access properties on an undefined element.

### Expected behavior

Empty switch statements should be handled gracefully without throwing errors. The code should render the switch statement correctly even when there are zero case clauses.

### Additional context

This appears to happen during the rendering phase when the code tries to call `renderStatementList` with `this.cases[0].start` even though the cases array is empty. While empty switch statements might not be common, they are valid JavaScript syntax and shouldn't cause the bundler to crash.

---
Repository: /testbed
