# Bug Report

### Describe the bug

After a recent update, internal link validation appears to be completely broken. All internal links in my documentation are now being flagged as broken links, even though they work perfectly fine when I navigate to them in the browser.

### Reproduction

```js
// In my docusaurus.config.js
module.exports = {
  onBrokenLinks: 'throw',
  // ... other config
};
```

When building the site with any internal links like:
- `[Link to docs](/docs/intro)`
- `[Link to API](/api/reference)`

All of these valid links are now being reported as broken during the build process.

### Expected behavior

Valid internal links that match existing routes should not be flagged as broken. The link checker should correctly match pathnames against the route configuration and only report actual broken links.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

This is blocking our documentation deployments since we have `onBrokenLinks: 'throw'` enabled. Any help would be appreciated!

---
Repository: /testbed
