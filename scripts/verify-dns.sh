#!/bin/bash

# DNS Verification Script for sp-wiki.octol.ing
echo "========================================="
echo "DNS Verification Script"
echo "Target: sp-wiki.octol.ing"
echo "========================================="
echo ""

# Check if dig is available
if command -v dig &> /dev/null; then
    echo "1. Checking DNS resolution with dig..."
    DIG_RESULT=$(dig +short sp-wiki.octol.ing)
    if [ -n "$DIG_RESULT" ]; then
        echo "   ✓ DNS resolves to: $DIG_RESULT"
        if [[ "$DIG_RESULT" == *"dev-jelly.github.io"* ]] || [[ "$DIG_RESULT" == *"github.io"* ]]; then
            echo "   ✓ Correct CNAME target detected"
        else
            echo "   ⚠ Warning: CNAME target doesn't match expected (dev-jelly.github.io)"
        fi
    else
        echo "   ✗ DNS does not resolve yet"
        echo "   → DNS not configured or still propagating"
    fi
else
    echo "1. dig command not found, trying nslookup..."
fi

echo ""
echo "2. Checking with nslookup..."
if command -v nslookup &> /dev/null; then
    NSLOOKUP_RESULT=$(nslookup sp-wiki.octol.ing 2>&1 | grep -A 1 "Name:" | tail -1)
    if [ -n "$NSLOOKUP_RESULT" ]; then
        echo "   $NSLOOKUP_RESULT"
    else
        echo "   ✗ nslookup failed"
    fi
else
    echo "   nslookup command not found"
fi

echo ""
echo "3. Testing HTTP connection..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" https://sp-wiki.octol.ing 2>&1 || echo "000")
if [ "$HTTP_CODE" = "200" ]; then
    echo "   ✓ Site is accessible (HTTP 200)"
elif [ "$HTTP_CODE" = "301" ] || [ "$HTTP_CODE" = "302" ]; then
    echo "   → Site redirects (HTTP $HTTP_CODE)"
    REDIRECT_URL=$(curl -s -I https://sp-wiki.octol.ing 2>&1 | grep -i "location:" | head -1)
    echo "   $REDIRECT_URL"
elif [ "$HTTP_CODE" = "000" ]; then
    echo "   ✗ Cannot connect to site"
    echo "   → DNS not configured or site not yet accessible"
else
    echo "   ⚠ Unexpected HTTP code: $HTTP_CODE"
fi

echo ""
echo "4. Checking GitHub Pages status..."
echo "   Repository: https://github.com/dev-jelly/splat-jelly-wiki"
echo "   Pages URL: https://github.com/dev-jelly/splat-jelly-wiki/settings/pages"

echo ""
echo "5. Checking HTTPS certificate..."
if command -v openssl &> /dev/null; then
    SSL_INFO=$(echo | openssl s_client -connect sp-wiki.octol.ing:443 -servername sp-wiki.octol.ing 2>&1 | grep "Verify return code" | head -1)
    if [ -n "$SSL_INFO" ]; then
        echo "   $SSL_INFO"
    else
        echo "   ✗ Could not check SSL certificate"
        echo "   → Site may not be accessible yet"
    fi
else
    echo "   openssl command not found"
fi

echo ""
echo "========================================="
echo "Summary"
echo "========================================="
echo ""
echo "Next Steps:"
echo "1. If DNS is not configured:"
echo "   → Add CNAME record in your DNS provider"
echo "   → Name: sp-wiki"
echo "   → Value: dev-jelly.github.io"
echo "   → TTL: 3600 or Auto"
echo ""
echo "2. Wait for DNS propagation (5 min - 24 hours)"
echo ""
echo "3. Verify DNS is configured:"
echo "   → Run: dig sp-wiki.octol.ing"
echo "   → Should return: dev-jelly.github.io"
echo ""
echo "4. Test site access:"
echo "   → Open: https://sp-wiki.octol.ing"
echo ""
echo "For detailed instructions, see: DNS_SETUP.md"
echo "========================================="
