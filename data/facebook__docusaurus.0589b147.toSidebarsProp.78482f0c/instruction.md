# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar items where the `linkUnlisted` property is being set incorrectly. When I have a sidebar category with `linkUnlisted: false`, it's appearing in the normalized sidebar props even though it shouldn't be included.

### Reproduction

```js
const sidebar = {
  type: 'category',
  label: 'My Category',
  items: [...],
  href: '/docs/category',
  linkUnlisted: false
}

// After normalization, the output incorrectly includes:
// { ..., linkUnlisted: false }
// Expected: linkUnlisted should not be present in the output
```

### Expected behavior

The `linkUnlisted` property should only be included in the normalized sidebar item when its value is `true`. When `linkUnlisted` is `false`, it should be omitted from the final props object.

### Additional context

This seems to affect how sidebar categories are rendered, particularly when dealing with unlisted documents. The property is being spread into the result object when it shouldn't be.

---
Repository: /testbed
