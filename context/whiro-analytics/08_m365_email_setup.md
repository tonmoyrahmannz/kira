# Whiro Analytics — Microsoft 365, Email & DNS Setup

**Last updated:** 1 June 2026
**Status:** ✅ Complete and operational

---

## Source of Truth

Microsoft 365 / Exchange Online is the primary and only active email provider for Whiro Analytics. Cloudflare Email Routing is disabled and no longer used for mail delivery.

- **Organisation:** WHIRO IT LIMITED
- **Trading brand:** Whiro Analytics
- **Domain:** whiroanalytics.co.nz
- **Subscription:** Microsoft 365 Business Standard

---

## Mailboxes

| Address | Type | Purpose |
|---------|------|---------|
| tonmoy@whiroanalytics.co.nz | Licensed user | Primary — client communication, Teams, OneDrive, Office apps, business admin |
| contact@whiroanalytics.co.nz | Shared mailbox | Public enquiries, leads, website contact, LinkedIn, first-touch |
| admin@whiroanalytics.co.nz | Shared mailbox | Billing, domains, subscriptions, tax, Cloudflare, registrar, insurance, invoices |

### Shared Mailbox Permissions

Both contact@ and admin@:
- Read and manage ✅
- Send as ✅
- Send on behalf: not used
- Sent item copying: enabled

Tonmoy is a member of both shared mailboxes.

---

## DNS Records (Cloudflare)

All active DNS records for email:

| Type | Name | Value | Proxy |
|------|------|-------|-------|
| MX | whiroanalytics.co.nz | whiroanalytics-co-nz.mail.protection.outlook.com (priority 0) | DNS only |
| TXT | whiroanalytics.co.nz | v=spf1 include:spf.protection.outlook.com -all | DNS only |
| CNAME | autodiscover.whiroanalytics.co.nz | autodiscover.outlook.com | DNS only (⚠️ must NOT be proxied) |

### Removed DNS records (Cloudflare Email Routing, now deprecated)
- ~~MX: route1.mx.cloudflare.net, route2.mx.cloudflare.net, route3.mx.cloudflare.net~~
- ~~TXT: v=spf1 include:_spf.mx.cloudflare.net ~all~~

---

## Website & WWW Redirect

- **Root:** https://whiroanalytics.co.nz — live via Cloudflare Pages
- **www:** https://www.whiroanalytics.co.nz — redirects to root
- **Redirect rule:** www.whiroanalytics.co.nz/* 🡒 https://whiroanalytics.co.nz/${1} (301 Permanent, preserve query string)
- **Existing Cloudflare Worker** for root site remains active and unchanged.

---

## Email Signatures

Three signatures created and set as defaults (new messages, replies, forwards):

### tonmoy@
```
Tonmoy Rahman
Director, Data & Analytics
Whiro Analytics

M: +64 21 053 9697
E: tonmoy@whiroanalytics.co.nz
W: whiroanalytics.co.nz

[Whiro Analytics logo]

Whiro Analytics is a trading name of WHIRO IT LIMITED.
NZBN: 9429042503866
```

### contact@
```
Whiro Analytics
Modern reporting, data platforms, and analytics strategy for NZ organisations.

E: contact@whiroanalytics.co.nz
W: whiroanalytics.co.nz

Whiro Analytics is a trading name of WHIRO IT LIMITED.
NZBN: 9429042503866
```

### admin@
```
Whiro Analytics Admin
E: admin@whiroanalytics.co.nz
W: whiroanalytics.co.nz

Whiro Analytics is a trading name of WHIRO IT LIMITED.
NZBN: 9429042503866
```

**Note:** Signatures should be verified on desktop Outlook and mobile (Outlook app / iOS Mail).

---

## Testing Confirmed

- ✅ tonmoy@ receives from external senders
- ✅ contact@ receives from external senders
- ✅ contact@ appears in Outlook as shared mailbox
- ✅ Sending from contact@ works (Send as)
- ✅ Sent items visible

---

## Email Templates (Drafted)

See `09_email_templates.md` for:
1. First enquiry response
2. Discovery call follow-up
3. Proposal sent
4. Referral partner intro
5. Keep-in-touch / nurture note

---

## Next Steps

1. ✅ ~~Finish email signatures~~ — DONE
2. ⏳ Create LinkedIn company page
3. ⏳ Set up prospect/lead tracker workflow
4. ⏳ Set up email templates in Outlook (My Templates add-in)
