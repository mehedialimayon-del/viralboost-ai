# ViralBoost AI — Bangladesh prototype

A standalone, mobile-responsive, Bengali-first prototype with creator planning, multi-platform growth campaign drafts, subscription plan selection, and a basic order manager.

## Run
Open `index.html` in a modern browser, or serve the folder with `python3 -m http.server 8000`.

## Scope / limitations
- Local demo only: campaign drafts and orders are stored in browser `localStorage`.
- Content Studio is deterministic templates, **not** a live AI service.
- Subscription buttons do not charge or activate accounts.
- No real social media posting, follower delivery, analytics, or ads execution.
- No payment, authentication, or production customer-data storage.
- Avoid entering real customer personal data in this prototype.
- All amounts are in BDT; ad budgets are separate from subscription prices.
- Do not promise guaranteed virality or follower delivery.

## Backend
Existing isolated `public.vb_*` tables have been created on an existing Supabase project, but this prototype intentionally does not connect to them until authentication, secure subscription activation, and payment verification are implemented.

## Version 3 additions
- Growth Recovery Lab: manual goal vs. actual views, percentage calculation, 7-day recommendations by content format.
- JSON export for locally stored campaign and order drafts. Export files may contain entered customer data; keep them private.
- No claim of live social analytics, automated publishing, or guaranteed results.

## Update: Growth Recovery History
- Save up to 50 reports locally; view saved reports; confirm before clearing history.
- JSON export now includes growthReports.
- This remains a local prototype, not a live AI/Ads/payment service.

## Version 5: Cloud account (experimental)
Open `cloud.html` from a web server. Enter the **publishable** Supabase key for project `rdiqkzspipnqdtatmflv` (never a secret/service-role key). Sign up, confirm email if required, and sign in. The cloud page writes user-owned campaign drafts, orders and growth reports to `public.vb_campaigns`, `public.vb_orders`, and `public.vb_growth_reports` with RLS. The existing homepage still uses localStorage and does not automatically sync. No payment, live ads, actual AI model, or social platform publishing is implemented. Do not enter real customer personal data until end-to-end security testing and privacy controls are completed. The legacy campaign budget database column is in MYR, so the cloud form currently saves zero budget instead of mislabeling BDT. This version has passed static JavaScript syntax and ZIP integrity checks only; real browser and authenticated end-to-end tests are pending.

## Version 6: Bangladesh budget correction
- Cloud campaigns now save **budget_bdt** in BDT; the older `budget_myr` remains unchanged for compatibility and is no longer populated by the Cloud UI.
- Requires the `viralboost_campaign_budget_bdt_v1` migration already applied to the shared Supabase project.
- Cloud login still requires a publishable key and a hosted page; real authenticated browser QA and payment integration remain pending.

## Version 7: Verified BDT plan catalog
- Cloud dashboard reads plan prices in BDT directly from Supabase `vb_plans` and reads the signed-in user's subscription status from `vb_subscriptions`.
- Paid purchase controls are deliberately disabled until a real payment provider and server-side webhook verification exist. Client cannot insert or update subscriptions.
- Database migration `viralboost_bdt_plan_catalog_v1` added `price_bdt` while retaining legacy `price_myr` for compatibility.
- This is **not** a completed payment gateway; no payment or subscription activation is offered.
- Tests performed: static syntax, HTML selectors, ZIP integrity, SQL migration and plan readback. Authenticated browser E2E tests are pending.


## Version 8: Subscription request workflow
- Paid-plan buttons create an idempotent request via `vb_request_subscription` RPC.
- Requests do not charge customers, verify payments, or unlock premium access.
- Request history is read-only for users; RLS restricts it to the signed-in owner.
- Payment provider webhook verification, subscription activation, entitlement enforcement and live QA are still pending.


## Version 9: Server-verified entitlements
- `vb_my_entitlements` derives effective plan server-side, defaulting to Free unless active.
- `vb_cancel_subscription_request` allows cancellation only for the signed-in owner's pending request.
- No payment processing, activation, or enforced AI quota yet.
- Cloud UI displays verified limits and pending-request cancellation.
- Authenticated browser end-to-end tests are still pending.


## Version 10 — Content quota enforcement
- `vb_content_plans` read-only to authenticated users with own-row RLS.
- `vb_create_content_plan` is the only client-write entry point. It enforces monthly quota server-side under a per-user transaction advisory lock.
- Quota uses the Asia/Dhaka calendar month. Paid access is derived from `vb_subscriptions.status = active`, not from client-side selections.
- Content Studio saves manually authored ideas; AI generation is not integrated.
- No payment processing, social publishing, or follower guarantees.
- End-to-end authenticated browser tests remain pending.


## Version 11 — exact server-side monthly usage meter
- `vb_my_content_usage()` returns current Bangladesh-calendar-month usage, plan limit, remaining capacity and UTC month boundaries.
- UI uses server count instead of estimating from the most recent 30 records.
- Save Content Plan button is disabled at quota; the database remains authoritative and prevents over-limit writes.
- `vb_plans` and `vb_subscriptions` client roles are restricted to read-only grants.
- No AI generation, billing, live ads, or authenticated browser E2E test is claimed.


## Version 12 — Cloud Data Export
- Signed-in users can export their own Campaigns, Orders, Growth Reports, Content Plans, and Subscription Requests to JSON.
- Every query filters by authenticated user ID; server-side RLS still applies. Export is capped at 10,000 records per table, with an explicit error if exceeded.
- Backups can contain personal information; keep downloaded files private. No import or delete functionality is added.
- Added logout event handling for session changes.
- No AI model API or payment gateway has been integrated.

## Version 13 — Social Page Manager
- Authenticated users can save HTTPS page URLs using `vb_add_page`, with a server-enforced subscription page quota.
- `vb_pages` direct write grants revoked for anon/authenticated; read access stays protected by RLS.
- Social page records are included in Cloud JSON export.
- Page URLs are only bookmarks; OAuth/social APIs and automatic posting are NOT connected.

## Version 14 — Security review and QA
- Sign-out now clears account-specific rendered lists and status fields from the DOM, not merely hiding the workspace.
- Reviewed actual Supabase role privileges: anon cannot insert subscriptions or invoke page/content creation RPCs; authenticated cannot update subscriptions or directly insert pages.
- Automated static checks are included in `qa_static.py`. Run `python qa_static.py`.
- Chromium browser navigation was attempted but blocked by the execution environment's administrator policy. No authenticated end-to-end test or browser interaction success is claimed.
- No production payment, social OAuth, AI API or GitHub deployment.


## Version 15 — quota-safe form submission
- Fixes a client-side bug: after saving a content plan or social page, the generic form handler used to re-enable the Save button even when the server quota was exhausted. The form now re-fetches server usage in `finally`, preserving disabled state.
- Fails closed (Save stays disabled) if usage cannot be verified. Server RPC quotas remain authoritative.
- Hides cloud setup after connection and refuses to render non-HTTPS saved-page links.
- No payment, AI generation, or real social media OAuth has been added.