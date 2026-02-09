# Bug Report

### Describe the bug

The spotlight filter is returning unexpected results when processing action groups. When I have a mix of grouped and ungrouped actions, the filtered results include extra items that shouldn't be there.

### Reproduction

```js
const actions = [
  {
    group: 'Files',
    actions: [
      { id: 'file-1', label: 'Document.pdf' },
      { id: 'file-2', label: 'Image.png' }
    ]
  },
  { id: 'action-1', label: 'Settings' },
  { id: 'action-2', label: 'Help' }
];

// When filtering these actions, the group object itself 
// appears in the results along with the individual actions
const filtered = defaultSpotlightFilter('', actions);
// Results include the group object which breaks rendering
```

### Expected behavior

The filter should only return individual action items, not the group metadata objects themselves. Ungrouped actions should also be handled correctly without causing errors.

### System Info
- @mantine/spotlight version: latest
- React version: 18.x

---
Repository: /testbed
