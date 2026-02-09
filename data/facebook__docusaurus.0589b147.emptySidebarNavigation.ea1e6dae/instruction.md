# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar navigation where the navigation data structure has unexpected values. When accessing sidebar navigation for a document, the `sidebarName` property is returning `null` instead of `undefined`, and the `previous` property is returning an empty object `{}` instead of `undefined`.

This is causing problems in my code that checks for the presence of navigation items using truthiness checks like `if (navigation.previous)` - the empty object is truthy even when there's no actual previous page.

### Reproduction

```js
const navigation = getDocNavigation({ docId: 'some-doc' });

console.log(navigation.sidebarName); // Expected: undefined, Got: null
console.log(navigation.previous); // Expected: undefined, Got: {}

// This check fails because {} is truthy
if (navigation.previous) {
  // This code block executes even when there's no previous page
  console.log('Has previous page');
}
```

### Expected behavior

The `emptySidebarNavigation()` function should return:
- `sidebarName: undefined` (not `null`)
- `previous: undefined` (not `{}`)
- `next: undefined`

This would be consistent with the expected behavior where undefined values indicate the absence of navigation items.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
