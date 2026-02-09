# Bug Report

### Describe the bug

I'm encountering an issue where top-level `await` expressions are being included/processed incorrectly in my code. It seems like the bundler is not handling await expressions properly when they appear at the module top level.

### Reproduction

```js
// module.js
const data = await fetch('/api/data');
console.log(data);

// When bundling this module, the await expression doesn't get included correctly
```

The issue appears when using top-level await in ES modules. The code either doesn't bundle correctly or the await expression is skipped during the inclusion phase.

### Expected behavior

Top-level await expressions should be properly included and processed during bundling. The await expression and its argument should be included in the output bundle.

### Additional context

This seems to have started happening recently. I'm using top-level await which is a valid ES2022 feature, but the bundler appears to be skipping or incorrectly handling these expressions during the inclusion phase.

---
Repository: /testbed
