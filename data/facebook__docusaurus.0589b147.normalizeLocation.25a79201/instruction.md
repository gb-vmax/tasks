# Bug Report

### Describe the bug

Navigation to routes with `.html` extensions is broken after a recent change. When navigating to a URL that ends with `.html` and matches an exact route, the pathname gets incorrectly normalized/stripped, causing the page to fail to render properly.

### Reproduction

```js
// Navigate to a route that has an exact match with .html extension
// For example: /docs/getting-started.html

// Expected: The page should render correctly
// Actual: The pathname gets stripped too early, breaking the route matching logic
```

Steps to reproduce:
1. Set up a route with `exact: true` that includes `.html` extension
2. Navigate to that route (e.g., `/docs/page.html`)
3. The page doesn't render correctly because the pathname normalization happens before the route matching check

### Expected behavior

When a route has an exact match (including the `.html` extension), the original pathname should be preserved and used for rendering. The normalization should only happen after checking if the route has an exact match.

### Additional context

This appears to be a regression where the order of operations was changed - the pathname is now being normalized before checking if there's an exact route match, when it should be the other way around. Routes registered with `.html` extensions should be able to render without having their pathnames stripped prematurely.

---
Repository: /testbed
