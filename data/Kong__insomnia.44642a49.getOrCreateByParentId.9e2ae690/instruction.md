# Bug Report

### Describe the bug

After a recent update, the app has become noticeably slower when working with gRPC requests. There's a significant delay (several seconds) when switching between requests or opening request details, especially in workspaces with many gRPC requests.

### Reproduction

1. Create a workspace with multiple gRPC requests (20+ requests works well to reproduce)
2. Switch between different requests in the sidebar
3. Notice significant lag/delay when selecting each request
4. The delay gets worse the more requests you have in the workspace

### Expected behavior

Switching between gRPC requests should be instant or near-instant, similar to how it works with REST requests. There shouldn't be any noticeable delay when navigating between requests.

### Additional context

This seems to have started happening recently. I have a workspace with around 50 gRPC requests and it's now taking 3-4 seconds just to switch between them. Makes the app pretty much unusable for my workflow.

The performance was fine before, so I'm wondering if something changed in how request metadata is being handled?

---
Repository: /testbed
