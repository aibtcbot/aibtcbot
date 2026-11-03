# Sources and changes

## Platform documentation

The main content was exported from the platform documentation at source revision `22d8d56aef0aee00c919ff5ccdd5b16cfe8333a5`. It includes the quick guide, all six platform chapters, Build tools and Support, preserving their paragraphs, tables, lists, code examples and text diagrams.

| Original source | Documentation files |
| --- | --- |
| `apps/web/lib/docs-quick.ts` | `README.md` |
| `apps/web/lib/docs-guide.ts` | `docs/guide/` |
| `apps/web/lib/docs-pages.ts` | `docs/build-tools.md`, `docs/support.md` |

The source files are platform documentation data, not the platform's execution backend. This repository contains rendered documentation sources and public examples only.

## Existing GitHub material

- The wallet-signature page preserves the existing `aibtcbot/aibtcbot` README (Git blob `99f34c778c5360d58e95b5503c62725ce7572b39`).
- The two files under `proofs/` are copied unchanged from that repository. The script SHA-256 is `0abc5bb367003ab5af34d80502de4a79133d6528468e60da6c6d291071d4956e` and includes CRLF compatibility.
- The old statement that the script is byte-identical to the trading website has been replaced with an explicit explanation that the two copies are independently versioned.

## Added or adapted for this site

1. Static documentation build, navigation, search, desktop contents panels and a collapsible mobile menu.
2. A dark theme with monochrome text based on the existing AIBRC documentation site's public stylesheet. The header and browser-tab icon reuse the platform's orange-and-white @ icon (`apps/web/app/icon.png`), unchanged. No external fonts, wallet connection or live market requests are added.
3. A code-examples index using existing public API/MCP examples and already-published wallet-signing excerpts.
4. A reference-script download page, plus relative links that work on both GitHub and the documentation site.
5. Cloudflare Workers Static Assets configuration and setup instructions for `aibtc.io`.
6. In this site's official-entry table, `aibtc.io` is documented as the documentation domain rather than a platform backup. Trading and API links continue to use `aibtc.bot`.
7. A terminology page follows the current homepage, Create token, Liquidity and Explorer wording while preserving code identifiers and signing-message literals.
8. The phrase “Don't trust, verify” is retained without an unverified personal attribution. No protocol or business rule is changed.

The content is English, following the platform's existing English documentation and the repository's English signing notes. Original source-version labels inside the signing notes are retained for traceability. This package does not update the live platform, its documentation pages, the AIBRC protocol site, or any DNS configuration.
