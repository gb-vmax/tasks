# Bug Report

### Describe the bug

The "Parent Index" field in the request template tag is not showing up correctly when selecting the 'folder' attribute. It seems like the visibility logic for this field got broken somehow.

### Reproduction

```js
// In the template tag editor:
1. Add a request template tag
2. Set the attribute dropdown to 'folder'
3. Expected: "Parent Index" field should be visible
4. Actual: "Parent Index" field is hidden
```

The field should only be visible when the attribute is set to 'folder', but it's not appearing even when that condition is met.

### Expected behavior

When the attribute is set to 'folder', the "Parent Index" field should be displayed so users can specify how high up the folder tree to look (starting at index 0).

### Additional context

This appears to have broken recently. The field was working before and allowed users to navigate up the folder hierarchy. Now there's no way to specify the parent index when using the folder attribute.

---
Repository: /testbed
