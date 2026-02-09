# Bug Report

### Describe the bug

I'm experiencing an issue with the sidebar navigation when a document has no previous or next links. The `emptySidebarNavigation()` function is returning `undefined` for the `previous` and `next` properties, but this is causing problems in my component that expects these values to be `null` when there's no navigation item.

### Reproduction

When accessing a document that's at the beginning or end of a sidebar (or standalone), the navigation object returned has `previous: undefined` and `next: undefined` instead of `null`. This breaks type checking and conditional rendering logic that specifically checks for `null`.

```js
const navigation = getDocNavigation({ docId: 'some-doc' });

// Expected: navigation.previous === null
// Actual: navigation.previous === undefined

if (navigation.previous === null) {
  // This condition never matches because it's undefined
  console.log('No previous page');
}
```

### Expected behavior

The `previous` and `next` properties should be `null` (not `undefined`) when there are no navigation links, to maintain consistency with TypeScript types and make conditional checks more reliable.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
