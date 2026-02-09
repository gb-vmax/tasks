# Bug Report

### Describe the bug

I'm experiencing an issue with inline code backticks in markdown content titles. When I have multiple inline code segments in a title, only the first one is being processed correctly. The rest remain with their backticks intact.

### Reproduction

```js
// Example markdown content with title containing multiple inline code segments
const title = "Use `React` and `Vue` together";

// After processing, I get:
// "Use React and `Vue` together"
// 
// Expected:
// "Use React and Vue together"
```

It seems like only the first backtick pair is being replaced, while subsequent ones are ignored.

### Expected behavior

All inline code segments (text wrapped in backticks) should have their backticks removed from the title, not just the first occurrence.

### Additional context

This is affecting documentation titles that reference multiple code elements or technical terms. For example:
- `` Use `useState` and `useEffect` hooks ``
- `` Comparing `npm`, `yarn`, and `pnpm` ``

Only the first code segment gets properly converted to plain text.

---
Repository: /testbed
