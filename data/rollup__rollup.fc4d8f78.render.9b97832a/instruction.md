# Bug Report

### Describe the bug

I'm encountering an issue where semicolons are being added incorrectly to variable declarations in certain contexts. When a variable declaration already ends with a semicolon and is used in a specific statement context, an extra semicolon gets appended, resulting in double semicolons in the output.

### Reproduction

```js
// Input code with variable declaration in a for loop init
for (let i = 0; i < 10; i++) {
  console.log(i);
}

// Output incorrectly contains double semicolon
for (let i = 0;; i < 10; i++) {
  console.log(i);
}
```

The issue seems to occur when variable declarations are used in contexts where they shouldn't have a trailing semicolon (like for-loop initializers), but the code is still getting a semicolon appended.

### Expected behavior

Variable declarations in statement contexts that don't require semicolons (such as for-loop initializers) should not have semicolons appended to them. The output should match the input structure without adding extra punctuation.

### Additional context

This appears to be related to how the `isNoStatement` flag is being handled when rendering variable declarations. The semicolon handling logic seems to be inverted - it's adding semicolons when it should be skipping them.

---
Repository: /testbed
