# Bug Report

### Describe the bug

I'm experiencing an issue where broken link detection is not working correctly. All links are being treated as valid, even when they point to non-existent routes. This means broken links are going undetected during the build process.

### Reproduction

```js
// Setup a Docusaurus site with broken link checking enabled
// Add a link to a non-existent page
<Link to="/this-page-does-not-exist">Broken Link</Link>

// Expected: Build should fail or warn about broken link
// Actual: Build succeeds without any warnings
```

### Steps to reproduce:
1. Create a Docusaurus site with `onBrokenLinks: 'throw'` in config
2. Add a link to a route that doesn't exist
3. Run the build
4. Notice that no error is thrown for the broken link

### Expected behavior

The broken link checker should properly identify links that don't match any existing routes and report them according to the `onBrokenLinks` configuration.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started happening recently. Previously broken links were being caught correctly during builds.

---
Repository: /testbed
