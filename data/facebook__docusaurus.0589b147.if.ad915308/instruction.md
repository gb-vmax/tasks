# Bug Report

### Bug: Previous/Next navigation links not appearing in docs

I'm experiencing an issue where the previous/next navigation links at the bottom of documentation pages have completely disappeared. The navigation arrows that should allow users to move between docs are no longer rendering.

### Reproduction

1. Set up a docs plugin with multiple pages
2. Configure sidebar with sequential docs
3. Navigate to any doc page
4. Check the bottom of the page - prev/next links are missing

Example configuration:
```js
{
  docs: [
    'intro',
    'getting-started',
    'advanced'
  ]
}
```

When viewing the 'getting-started' page, I would expect to see navigation links to both 'intro' (previous) and 'advanced' (next), but neither link appears.

### Expected behavior

Navigation links should appear at the bottom of doc pages to allow users to navigate between sequential documents. The links should show when valid previous/next documents exist in the sidebar.

### Additional context

This seems to have broken recently. The navigation was working fine before, and I haven't changed any configuration on my end. The sidebar itself still works correctly, it's just the prev/next navigation that's affected.

---
Repository: /testbed
