# Bug Report

### Describe the bug

I'm experiencing an issue with the sidebar items generator where the `id` field is no longer available in the doc object passed to custom sidebar generators. This is breaking my custom sidebar generation logic that relies on the document ID to create links and organize items.

### Reproduction

```js
module.exports = {
  mySidebar: [
    {
      type: 'category',
      label: 'Docs',
      items: async ({defaultSidebarItemsGenerator, ...args}) => {
        const items = await defaultSidebarItemsGenerator(args);
        
        // This no longer works - doc.id is undefined
        const customItems = args.docs.map(doc => {
          console.log(doc.id); // undefined
          return {
            type: 'doc',
            id: doc.id, // This breaks the sidebar
            label: doc.title
          };
        });
        
        return customItems;
      }
    }
  ]
};
```

### Expected behavior

The `doc.id` property should be available in the document objects passed to sidebar item generators, as it's essential for creating doc-type sidebar items programmatically. Without the ID, there's no way to reference specific documents when building custom sidebars.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started recently. The `id` field used to be available before and is crucial for custom sidebar generation workflows.

---
Repository: /testbed
