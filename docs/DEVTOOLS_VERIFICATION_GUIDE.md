# DevTools Verification Guide

Every module should include DevTools verification notes.

## Network

Check:

- document request status
- API status codes
- request/response headers
- payload shape
- waterfall timing
- cache behavior
- failed or blocked requests

## Console

Check:

- uncaught errors
- warnings
- deprecation messages
- noisy debug logs
- security messages

## Sources

Use for:

- breakpoints
- step debugging
- call stack inspection
- source map verification
- runtime behavior tracing

## Application

Check:

- Local Storage
- Session Storage
- Cookies
- IndexedDB
- Cache Storage
- Service Workers
- Web App Manifest

## Security

Check:

- HTTPS
- certificate state
- mixed content
- insecure resources
- cookie security implications

## Lighthouse

Record:

- Performance
- Accessibility
- Best Practices
- SEO
- PWA when applicable

## Performance

Use for:

- main thread activity
- long tasks
- layout shift
- render-blocking resources
- cold start / warm start comparison where applicable

## Memory

Use for:

- heap snapshots
- detached nodes
- leak investigation
- repeated interaction profiling

## Accessibility

Check:

- semantic HTML
- contrast
- labels
- keyboard navigation
- focus behavior
- Lighthouse accessibility issues

## Service Worker / PWA

Check:

- registration
- lifecycle
- cache entries
- offline behavior
- update behavior
