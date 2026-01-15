#!/bin/bash

# Automatic DNS Checker - Runs continuously until DNS is configured

echo "========================================="
echo "Automatic DNS Checker"
echo "Domain: sp-wiki.octol.ing"
echo "Target: dev-jelly.github.io"
echo "========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

check_interval=30  # seconds
max_checks=60     # 30 minutes max
check_count=0

echo "Starting automatic DNS monitoring..."
echo "Press Ctrl+C to stop"
echo ""

while [ $check_count -lt $max_checks ]; do
    ((check_count++))
    echo -e "${BLUE}[Check #$check_count at $(date '+%H:%M:%S')]${NC}"

    # Check DNS resolution
    echo -n "  DNS Resolution... "
    DNS_RESULT=$(dig +short sp-wiki.octol.ing 2>/dev/null)

    if [ -n "$DNS_RESULT" ]; then
        if [[ "$DNS_RESULT" == *"dev-jelly.github.io"* ]] || [[ "$DNS_RESULT" == *"github.io"* ]]; then
            echo -e "${GREEN}✓ RESOLVES${NC}"
            echo -e "    Target: $DNS_RESULT"

            # Check HTTP connection
            echo -n "  HTTP Status... "
            HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" https://sp-wiki.octol.ing 2>&1)

            if [ "$HTTP_CODE" = "200" ]; then
                echo -e "${GREEN}✓ 200 OK${NC}"

                # Check HTTPS
                echo -n "  HTTPS Certificate... "
                if command -v openssl &> /dev/null; then
                    SSL_CHECK=$(echo | openssl s_client -connect sp-wiki.octol.ing:443 -servername sp-wiki.octol.ing 2>&1 | grep "Verify return code" | head -1)

                    if [[ "$SSL_CHECK" == *"0"* ]]; then
                        echo -e "${GREEN}✓ VALID${NC}"

                        # Success!
                        echo ""
                        echo -e "${GREEN}=========================================${NC}"
                        echo -e "${GREEN}SUCCESS: DNS is configured!${NC}"
                        echo -e "${GREEN}=========================================${NC}"
                        echo ""
                        echo -e "Production URL: ${BLUE}https://sp-wiki.octol.ing${NC}"
                        echo ""
                        echo "You can now access your site!"
                        exit 0
                    else
                        echo -e "${YELLOW}⚠ PENDING (SSL not ready yet)${NC}"
                    fi
                else
                    echo -e "${YELLOW}⚠ HTTP $HTTP_CODE${NC}"
                fi
            else
                echo -e "${RED}✗ NOT CONFIGURED YET${NC}"
            fi
        else
            echo -e "${RED}✗ WRONG TARGET${NC}"
            echo -e "    Got: $DNS_RESULT"
            echo -e "    Expected: dev-jelly.github.io"
        fi
    else
        echo -e "${RED}✗ NOT RESOLVING${NC}"
        echo -e "    DNS record not found"
    fi

    echo ""
    echo "Waiting $check_interval seconds before next check..."
    echo "Press Ctrl+C to stop"
    sleep $check_interval
    echo ""
done

echo ""
echo -e "${YELLOW}=========================================${NC}"
echo -e "${YELLOW}TIMEOUT: Max checks reached${NC}"
echo -e "${YELLOW}=========================================${NC}"
echo ""
echo "DNS is not yet configured."
echo ""
echo "Next steps:"
echo "1. Configure DNS at your DNS provider"
echo "2. Add CNAME record:"
echo "   - Name: sp-wiki"
echo "   - Type: CNAME"
echo "   - Value: dev-jelly.github.io"
echo "3. Run this script again to verify"
echo ""
echo "See DNS_SETUP.md for detailed instructions."
