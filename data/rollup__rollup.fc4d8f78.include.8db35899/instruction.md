# Bug Report

### Labeled statements with break not being included correctly

I'm experiencing an issue where labeled statements containing break statements aren't being tree-shaken properly. It seems like labels that should be included are getting removed from the bundle.

### Reproduction

```js
// Input code
function test() {
  outer: {
    if (condition) {
      break outer;
    }
    console.log('unreachable');
  }
  console.log('after label');
}
```

When bundling this code, the `outer` label is being removed even though there's a `break outer` statement that references it. The resulting output is invalid because the break statement references a label that no longer exists.

### Expected behavior

The labeled statement should be preserved in the output when it's referenced by a break statement inside its body. The bundler should detect that the label is needed and include it in the final bundle.

### Additional context

This appears to affect nested labeled blocks where inner statements break to outer labels. The label information seems to be getting lost during the inclusion phase of tree-shaking.

---
Repository: /testbed
