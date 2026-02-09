# Bug Report

### Describe the bug

After a recent update, template rendering is behaving unexpectedly when using variables-only render mode. The templating system appears to be invalidating cached Nunjucks instances even when they should still be valid, causing performance issues and potential rendering inconsistencies.

### Reproduction

```js
// First render with RENDER_VARS mode
const result1 = await render(template, { renderMode: RENDER_VARS });

// Wait a short time (less than cache TTL)
await sleep(1000);

// Second render with same mode - should reuse cached instance
const result2 = await render(template, { renderMode: RENDER_VARS });

// Expected: Both renders use the same cached Nunjucks instance
// Actual: Cache appears to be invalidated prematurely
```

### Expected behavior

When rendering templates in `RENDER_VARS` mode, the system should reuse the cached Nunjucks instance (`nunjucksVariablesOnly`) as long as it exists and is still valid. The cache should only be invalidated after the configured TTL period.

### Additional context

This seems to have started happening after changes were made to the caching logic. The `RENDER_TAGS` mode doesn't appear to have the same issue - it still returns the cached instance correctly without checking staleness.

The inconsistency between how `RENDER_VARS` and `RENDER_TAGS` modes handle caching is causing unexpected behavior in production.

---
Repository: /testbed
