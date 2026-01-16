<!DOCTYPE html>
<html lang="ja">
<head prefix="og: https://ogp.me/ns# fb: https://ogp.me/ns/fb# article: https://ogp.me/ns/article#">
    <meta charset="utf-8">
    <meta name="viewport" content="width=980">

    <meta name="description" content="このサイトは、スプラトゥーン3の攻略・検証を目的とした非公式wikiです。">
        <meta property="og:url" content="https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF" />
    <meta property="og:type" content="article" />
    <meta property="og:title" content="トキシラズいぶし工房 - Splatoon3 - スプラトゥーン3 攻略＆検証  Wiki*" />
    <meta property="og:description" content="このサイトは、スプラトゥーン3の攻略・検証を目的とした非公式wikiです。" />
    <meta property="og:site_name" content="Splatoon3 - スプラトゥーン3 攻略＆検証  Wiki*" />
    <meta property="og:image" content="https://icon.wikiwiki.jp/symbolicon/splatoon3mix/ogImage/f1fa837847c5.png" />
    <title>トキシラズいぶし工房 - Splatoon3 - スプラトゥーン3 攻略＆検証  Wiki*</title>

    <link rel="alternate" href="/splatoon3mix/::cmd/mixirss" type="application/rss+xml" title="RSS" />
        <link rel="icon" href="https://icon.wikiwiki.jp/symbolicon/splatoon3mix/favicon/fcb0de74bdf2.png" />
    <link rel="apple-touch-icon" href="https://icon.wikiwiki.jp/symbolicon/splatoon3mix/appleTouchIcon/dbed77543aea.png" />
    <link rel="manifest" href="https://icon.wikiwiki.jp/symbolicon/splatoon3mix/manifest.webmanifest">
    <link rel="stylesheet" href="https://cdn.wikiwiki.jp/to/w/common/assets/dist/wikiwiki-ad217af191780b21c7f8.min.css" type="text/css">
<link rel="stylesheet" href="https://cdn.wikiwiki.jp/to/w/common/assets/dist/skin-default-8896c2d3fdf78b1e81a0.min.css" type="text/css">
    
    <script type="text/javascript" src="https://cdn.wikiwiki.jp/to/w/common/assets/dist/ad-1bf004520fc167abbea6.min.js"></script>
    <script>
    var wi_stay = (function () {
        var wi_data_raw = localStorage.getItem('browsingStatistics');
        var wi_data = wi_data_raw ? (JSON.parse(wi_data_raw) || {}) : {};
        var stay = Number(wi_data.stay);
        if (isNaN(stay)) {
            stay = 0;
        }
        return stay;
    })();
    var wi_data_raw = localStorage.getItem('usageStatistics');
    var wi_data =     wi_data_raw ? (JSON.parse(wi_data_raw) || {}) : {};
    var wi_edit =     String(wi_data.edit || 0);
    var wi_freeze =   String(wi_data.freeze || 0);
    var wi_comment =  String(wi_data.comment || 0);
    var wi_group = String(wi_data.group || "N");
    var wi_smsAuth = wi_data.smsAuth || false;
    var wi_hasPosted = wi_data.hasPosted || false;
    var wi_agreement = String(wi_data.agreementStatus || "false");
    if (document.referrer.length !== 0) {
        var wi_uri = new URL(document.referrer);
        var wi_referer = wi_uri.hostname;
    } else {
        var wi_referer = "unknown";
    }

    // Chromium系判定
    function isChromium() {
        var ua = navigator.userAgent;
        // Edge, Opera, Chrome, Chromium, Brave など
        return /\b(Chrome|Chromium|Edg|OPR|Brave)\b/.test(ua) && !/Silk|UCBrowser|SamsungBrowser|CriOS|FxiOS|OPiOS|EdgiOS/.test(ua);
    }

    var wi_ismobile;
    var wi_device;
    if (isChromium() && navigator.userAgentData) {
        wi_ismobile = navigator.userAgentData.mobile;
        if (wi_ismobile) {
            if (navigator.userAgentData.platform === "Android") {
                wi_device = "and";
            } else {
                wi_device = "ios";
            }
        } else {
            wi_device = "pc";
        }
    } else {
        wi_ismobile = !!navigator.userAgent.match(/iPhone|Android.+Mobile/);
        if (navigator.userAgent.match(/Android.+Mobile/)) {
            wi_device = "and";
        } else if (navigator.userAgent.match(/iPhone/)) {
            wi_device = "ios";
        } else {
            wi_device = "pc";
        }
    }

    var wi_isportrait = window.matchMedia("(orientation: portrait)").matches;
    var wi_isinbound = wi_referer.includes(window.location.hostname) ? false : true;
    var wi_random100 = Math.floor(Math.random() * (100 - 1) + 1);
    var wi_random110 = Math.floor(Math.random() * 10) + 1;
    var wi_isread_yet = true;
    var wi_location_hash = location.hash || false;
</script>

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-3Y8FN9EFS7"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-3Y8FN9EFS7', {
        'content_group': 'splatoon3mix',
        'user_properties': {
            'user_group':     wi_group,
            'user_agreement': wi_agreement,
            'edit_count':     wi_edit,
            'comment_count':  wi_comment,
            'sms_auth':       String(wi_smsAuth)
        }
    });
    gtag('config', 'G-RZP92W798E');

</script>

<script>
    window.wikiFq = createWikiFq();
</script>
<script>
    var wi_recref = recordReferrerDomain();
</script>

<script>
const visitData_20241117 = (() => {
const RESET_INTERVAL_MINUTES = 30;
const now = Date.now();
const resetIntervalMs = RESET_INTERVAL_MINUTES * 60 * 1000;
const storageKey = "internalVisitData";
let data = JSON.parse(localStorage.getItem(storageKey)) || { count: 0, lastVisit: now };
if (now - data.lastVisit > resetIntervalMs) data = { count: 0, lastVisit: now };
if (document.referrer && new URL(document.referrer).hostname === window.location.hostname) {
data = { count: data.count + 1, lastVisit: now };
localStorage.setItem(storageKey, JSON.stringify(data));
}
return data;
})();

const int_conditions = [
wi_ismobile,
wi_group === 'N',
wi_agreement === 'false',
!wi_isinbound,
visitData_20241117.count === 1,
];

const int_conditions_pc = [
    !wi_ismobile,
    wi_group === 'N',
    wi_agreement === 'false',
    !wi_isinbound,
    visitData_20241117.count === 1,
];
</script>
<script>
(function(){
  const FLAG="fluxinst_pc";
  const url=new URL(location.href);

  if(url.searchParams.get(FLAG)==="1"){
    url.searchParams.delete(FLAG);
    history.replaceState(null,"",url.toString());
    return;
  }

  if(
    Array.isArray(int_conditions_pc) &&
    int_conditions_pc.every(Boolean)
  ){
    url.searchParams.set(FLAG,"1");
    location.href=url.toString();
  }
})();
</script>


<script>
(function(){
  const url=new URL(location.href);
  const f=wi_device==="ios"?"iminst_ios":wi_device==="and"?"iminst_and":null;
  if(!f)return;
  if(url.searchParams.get(f)==="1"){
    url.searchParams.delete(f);
    history.replaceState(null,"",url.toString());
    return;
  }
  if(Array.isArray(int_conditions)&&int_conditions.every(Boolean)){
    url.searchParams.set(f,"1");
    location.href=url.toString();
  }
})();
</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-KQ52VZ3');</script>
<!-- End Google Tag Manager -->


<script async="async" src="https://flux-cdn.com/client/ukiuki/flux_wikiwiki_AS_TM_AT.min.js"></script>
<script type="text/javascript">
    var pbjs = pbjs || {};
    pbjs.que = pbjs.que || [];
</script>
<script async src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"></script>
<script>
var googletag = googletag || {};
googletag.cmd = googletag.cmd || [];

var wi_adslot_rectangle = [[300,250],[1,1]];
var wi_adslot = [[300,250],[1,1]];
if (document.documentElement.clientWidth > 406) {
  wi_adslot_rectangle = [[300,250],[336,280],[1,1]];
  wi_adslot = [[468,60],[300,250],[1,1]];
}

window.defineSlotFlux = [];
    if (wi_isinbound && wi_ismobile && wi_group == "N" && wi_agreement === "false") {
      defineSlotFlux.push({"slotID": "div-gpt-ad-1563430750445-0", "sizes": [[300,250]], "slotName":"WIKIWIKI_SP_INBOUND"});
    } else if (wi_isinbound && wi_group == "N" && wi_agreement === "false") {
      defineSlotFlux.push({"slotID": "div-gpt-ad-1567409776345-0", "sizes": [[300,250]], "slotName":"WIKIWIKI_PC_INBOUND"});
      defineSlotFlux.push({"slotID": "div-gpt-ad-1658802281376-0", "sizes": [[300,250]], "slotName":"WIKIWIKI_PC_INBOUND_RIGHT"});
    }
  if (wi_ismobile && !wi_isinbound) {
    defineSlotFlux.push({"slotID": "div-gpt-ad-1562925510696-0", "sizes": [[300,250]], "slotName":"WIKIWIKI_SP_CAPTION"});
  } else if (wi_group === 'N' && wi_agreement === 'false' && !wi_isinbound) {
    defineSlotFlux.push({"slotID": "div-gpt-ad-1565253136679-0", "sizes": [[300,250]], "slotName":"WIKIWIKI_PC_CAPTION"});
  }
  if (wi_ismobile && !wi_isinbound) {
    defineSlotFlux.push({"slotID": "div-gpt-ad-1567408559923-0", "sizes": [[300,250]], "slotName":"WIKIWIKI_SP_SECOND"});
  } else if (!wi_ismobile && (!wi_isinbound || (wi_isinbound && wi_group !== "N"))) {
    defineSlotFlux.push({"slotID": "div-gpt-ad-1567408559923-0", "sizes": [[300,250]], "slotName":"WIKIWIKI_PC_BOTTOM_LEFT"});
    defineSlotFlux.push({"slotID": "div-gpt-ad-1658912377789-0", "sizes": [[300,250]], "slotName":"WIKIWIKI_PC_BOTTOM_RIGHT"});
  }
if (wi_ismobile && wi_isportrait) {
  defineSlotFlux.push({"slotID": "div-gpt-ad-1563441919648-0", "sizes": [[320, 100], [320, 50]], "slotName":"WIKIWIKI_SP_OVERLAY"});
}
</script>
<script type="text/javascript">
if (defineSlotFlux.length) {
    var readyBids = {
        prebid: false,
        google: false
    };
    var failSafeTimeout = 3e3;
    var launchAdServer = function () {
        if (!readyBids.prebid) {
            return;
        }
        requestAdServer();
    };
    var requestAdServer = function () {
        if (!readyBids.google) {
            readyBids.google = true;
            googletag.cmd.push(function () {
                pbjs.que.push(function () {
                    pbjs.setTargetingForGPTAsync();
                });
                googletag.pubads().refresh();
            });
        }
    };
}
</script>
<script>
googletag.cmd.push(function() {
    if (wi_isinbound && wi_ismobile && wi_group == "N" && wi_agreement === "false") {
      googletag.defineSlot('/19033742/WIKIWIKI_SP_INBOUND',[[300,250]],
        'div-gpt-ad-1563430750445-0').setCollapseEmptyDiv(true).addService(googletag.pubads());
    } else if (wi_isinbound && wi_group == "N" && wi_agreement === "false") {
      googletag.defineSlot('/19033742/WIKIWIKI_PC_INBOUND',[[336,280],[300,250]],
        'div-gpt-ad-1567409776345-0').setCollapseEmptyDiv(true).addService(googletag.pubads());
      googletag.defineSlot('/19033742/WIKIWIKI_PC_INBOUND_RIGHT',[[336,280],[300,250]],
        'div-gpt-ad-1658802281376-0').setCollapseEmptyDiv(true).addService(googletag.pubads());
    }
  if (wi_ismobile && !wi_isinbound) {
    googletag.defineSlot('/19033742/WIKIWIKI_SP_CAPTION',[[300,250],[1,1]],'div-gpt-ad-1562925510696-0').addService(googletag.pubads());
  } else if (wi_group === 'N' && wi_agreement === 'false' && !wi_isinbound) {
    googletag.defineSlot('/19033742/WIKIWIKI_PC_CAPTION',[[300,250],[1,1]],'div-gpt-ad-1565253136679-0').addService(googletag.pubads());
  }
    if (wi_ismobile && !wi_isinbound) {
        googletag.defineSlot('/19033742/WIKIWIKI_SP_SECOND',[[300,250]],
        'div-gpt-ad-1567408559923-0').addService(googletag.pubads());
    } else if (!wi_ismobile && (!wi_isinbound || (wi_isinbound && wi_group !== "N"))) {
        googletag.defineSlot('/19033742/WIKIWIKI_PC_BOTTOM_LEFT',[[336,280],[300,250]],
        'div-gpt-ad-1567408559923-0').addService(googletag.pubads());
        googletag.defineSlot('/19033742/WIKIWIKI_PC_BOTTOM_RIGHT',[[336,280],[300,250]],
        'div-gpt-ad-1658912377789-0').addService(googletag.pubads());
    }
    if (wi_ismobile && wi_isportrait) {
        googletag.defineSlot('/19033742/WIKIWIKI_SP_OVERLAY',[[320,100],[320,50],[1,1]],'div-gpt-ad-1563441919648-0').addService(googletag.pubads());
    }
  if (window.innerWidth >= 1000 && wi_group === 'N' && wi_agreement === 'false') {
    googletag.defineOutOfPageSlot('/19033742/WIKIWIKI_SP_OVERLAY_ANCHOR', googletag.enums.OutOfPageFormat.BOTTOM_ANCHOR).addService(googletag.pubads());
  }
    googletag.pubads().setTargeting("gpolicy","sunny");
    googletag.pubads().setTargeting("site","splatoon3mix");
    googletag.pubads().collapseEmptyDivs();
    googletag.pubads().enableSingleRequest();
    googletag.pubads().addEventListener('slotRenderEnded', function(event) {
        var slot = event.slot;
        if (document.getElementById(slot.getSlotElementId()) != null){
            var slotElm = document.getElementById(slot.getSlotElementId());
            if (slotElm && slotElm.className === 'overlay-ad-wrapper') {
                var overlayRenderedEvent = document.createEvent('Event');
                overlayRenderedEvent.initEvent('overlay-ad-rendered', true, true);
                slotElm.dispatchEvent(overlayRenderedEvent);
            }
        }
    })
    googletag.pubads().enableLazyLoad({
        fetchMarginPercent: 50,   // 0.5画面分まできたらリクエスト
        renderMarginPercent: 50,  // 0.5画面分まできたら描画
        mobileScaling: 1.0        // モバイルもPCと同じ倍率（0.5画面分）にする
    });
    if (defineSlotFlux.length) {googletag.pubads().disableInitialLoad();};
    googletag.enableServices();
    if (defineSlotFlux.length) {
        pbjs.que.push(function () {
            pbFlux.prebidBidder();
        });
    }
});
</script>


<script type="text/javascript">
if (defineSlotFlux.length) {
    // set failsafe timeout
    setTimeout(function () {
        requestAdServer();
    }, failSafeTimeout);
}
</script>

<script>
googletag.cmd.push(function() {
  googletag.pubads()
    .setTargeting("wi_agreement",     String(wi_data.agreementStatus || "false"))
    .setTargeting("wi_group",     String(wi_data.group || "N"))
    .setTargeting("wi_comment",   wi_comment.length.toString())
    .setTargeting("wi_edit",      wi_edit.length.toString())
    .setTargeting("wi_freeze",    wi_freeze.length.toString())
    .setTargeting("wi_smsAuth",   String(wi_data.smsAuth || false))
    .setTargeting("wi_hasPosted", String(wi_data.hasPosted || false))
    .setTargeting("wi_referer",   String(wi_referer || "unknown"))
    .setTargeting("wi_random110", String(wi_random110 || "0"));
});
</script>

<style>
.pc-caption-ad-default {
    margin-top:20px;
    display:flex;
    justify-content:flex-start;
    gap: 10px 5px;
    min-height:280px;
    position: sticky;
    z-index: 3;
    top: 45px;
}

.pc-caption-ad-center{
    margin-top:20px;
    display:flex;
    justify-content:center;
    gap: 10px 5px;
    min-height:280px;
    position: sticky;
    z-index: 3;
    top: 45px;
}
.pc-caption-ad-mobile{
    margin-top:20px;
    margin-bottom:20px;
    display:flex;
    justify-content:center;
    min-height:331px;
    position: sticky;
    z-index: 3;
    top: 45px;
}
.pc-caption-ad-mobile-300x600{
    margin-top:20px;
    margin-bottom:20px;
    display:flex;
    justify-content:center;
    min-height:331px;
}
.default-advertisement {
    background-color: transparent;
    background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 576 512'%3E%3C!--!Font Awesome Pro 6.6.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2024 Fonticons, Inc.--%3E%3Cpath d='M16 48l0 416 544 0 0-416L16 48zM0 32l16 0 544 0 16 0 0 16 0 416 0 16-16 0L16 480 0 480l0-16L0 48 0 32zM320 280a56 56 0 1 0 112 0 56 56 0 1 0 -112 0zm56-72c22.6 0 42.8 10.4 56 26.7l0-66.7 0-8 16 0 0 8 0 112 0 64 0 8-16 0 0-8 0-18.7c-13.2 16.3-33.4 26.7-56 26.7c-39.8 0-72-32.2-72-72s32.2-72 72-72zM183.1 160l5.2 0 7.3 0 5.2 0 2.1 4.8L284.2 352l-17.4 0-20.8-48-107.8 0-20.8 48-17.4 0L181 164.8l2.1-4.8zM145 288l94 0L192 179.7 145 288z' fill='%23BBB'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: center;
    background-size: 25px 25px;
}

@media (max-width: 500px) {
  .caption-flybox:has(iframe[id^="google_ads_iframe_"]) {
    position: relative;
    min-height: 450px;
  }
}
</style>


<script>
googletag.cmd.push(function() {
    const pcCaptionPaths = [
        '/19033742/WIKIWIKI_PC_CAPTION',
        '/19033742/WIKIWIKI_PC_CAPTION_SIDE_BY',
        '/19033742/WIKIWIKI_PC_CAPTION_20TH',
        '/19033742/WIKIWIKI_CAPTION_B'
    ];

    const spCaptionPaths = [
        '/19033742/WIKIWIKI_SP_CAPTION',
        '/19033742/WIKIWIKI_SP_CAPTION_300x600'
    ];

    googletag.pubads().addEventListener('slotRenderEnded', function(event) {
        const slotElement = document.getElementById(event.slot.getSlotElementId());
        const parent = slotElement?.parentNode;

        if (parent && !event.isEmpty) {
            if (pcCaptionPaths.includes(event.slot.getAdUnitPath())) {
                parent.classList.add(parent.clientWidth < 769 ? "pc-caption-ad-center" : "pc-caption-ad-default");
            } else if (spCaptionPaths.includes(event.slot.getAdUnitPath())) {
                if (event.slot.getAdUnitPath() === '/19033742/WIKIWIKI_SP_CAPTION_300x600') {
                    parent.classList.add("pc-caption-ad-mobile-300x600");
                } else {
                    parent.classList.add("pc-caption-ad-mobile");
                }
            } else if (event.slot.getAdUnitPath() === '/19033742/WIKIWIKI_SP_OVERLAY') {
                document.querySelector('#pc-overlay-ad-close-button svg').style.fill =
                `rgba(${getComputedStyle(document.body).backgroundColor.match(/\d+/g).map(c => 255 - c).join(",")}, 0.5)`;
                document.getElementById('pc-overlay-ad-parent-container').style.visibility = 'visible';
                document.getElementById('pc-overlay-ad-close-button').style.visibility = 'visible';
                document.getElementById('pc-overlay-ad-close-button').classList.add('hidden-switch-class');
            }
        }
    });

    googletag.pubads().addEventListener('slotOnload', function(event) {
        const slotElement = document.getElementById(event.slot.getSlotElementId());
        slotElement?.parentNode?.classList.remove("default-advertisement");
    });
});
</script>

<link rel="preload" as="script" href="https://pdn.adingo.jp/p.js">
<link rel="preconnect" href="https://sh.adingo.jp" crossorigin="use-credentials">
    <link rel="canonical" href="https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF">
    <style>
@media screen and (min-width: 820px) {
  .container-wrapper {
    min-width: 1030px;
    max-width: 1030px;
  }
}
</style>
<style>
  .columns-container.has-left-column:not(.has-right-column).three-columns-container {
      grid-template-columns: 260px 1fr;
  }
  .columns-container.has-left-column.has-right-column.three-columns-container {
      grid-template-columns: 260px 1fr 170px;
  }
  .columns-container.has-left-column.two-columns-container {
    grid-template-columns: 260px 20px 1fr;
  }
</style>
<style>
  body {
      font-family: Verdana, Arial, "Hiragino Kaku Gothic ProN", "Hiragino Sans", Meiryo, sans-serif;
      font-size: 12px;
  }
</style>
<style>
  @media screen and (max-width: 819px), print and (max-width: 180mm) {
    body {
        font-size: 13px;
    }
  }
</style>
        <script>
        window.globalParamsContainer = {"smsAuthParams":{"actionTrollingDefenceCheck":"\/splatoon3mix\/::cmd\/trolling_defence_pass","actionSubmitNumber":"\/p\/sms-auth\/code\/request","actionSubmitCode":"\/p\/sms-auth\/code\/activate","cookieName":"authkey"},"editAssistantImgSrc":{"face_smile":"https:\/\/cdn.wikiwiki.jp\/to\/w\/common\/image\/face\/smile.png?v=4","face_bigsmile":"https:\/\/cdn.wikiwiki.jp\/to\/w\/common\/image\/face\/bigsmile.png?v=4","face_huh":"https:\/\/cdn.wikiwiki.jp\/to\/w\/common\/image\/face\/huh.png?v=4","face_oh":"https:\/\/cdn.wikiwiki.jp\/to\/w\/common\/image\/face\/oh.png?v=4","face_wink":"https:\/\/cdn.wikiwiki.jp\/to\/w\/common\/image\/face\/wink.png?v=4","face_sad":"https:\/\/cdn.wikiwiki.jp\/to\/w\/common\/image\/face\/sad.png?v=4","face_worried":"https:\/\/cdn.wikiwiki.jp\/to\/w\/common\/image\/face\/worried.png?v=4","face_tear":"https:\/\/cdn.wikiwiki.jp\/to\/w\/common\/image\/face\/tear.png?v=4","face_tere":"https:\/\/cdn.wikiwiki.jp\/to\/w\/common\/image\/face\/tere.png?v=4","face_shock":"https:\/\/cdn.wikiwiki.jp\/to\/w\/common\/image\/face\/shock.png?v=4","face_heart":"https:\/\/cdn.wikiwiki.jp\/to\/w\/common\/image\/face\/heart.png?v=4","face_star":"https:\/\/cdn.wikiwiki.jp\/to\/w\/common\/image\/face\/star.gif?v=4","face_hatena":"https:\/\/cdn.wikiwiki.jp\/to\/w\/common\/image\/face\/hatena.gif?v=4","face_tip":"https:\/\/cdn.wikiwiki.jp\/to\/w\/common\/image\/face\/tip.gif?v=4"},"experimentalFeature":false};
    </script>
</head>
<body class="">
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KQ52VZ3"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) --><noscript>
    <div class="noscript-alert">
        <i class="fa fa-exclamation-triangle"></i>
        ブラウザの JavaScript がオフ（ブロックまたは許可しない）に設定されているため、このページは正常に機能しません。
    </div>
</noscript>
<div class="container-wrapper">

    <div class="container clearfix">
                    <div id="header" class="default-header">
                <a href="/splatoon3mix/" title="Splatoon3 - スプラトゥーン3 攻略＆検証  Wiki*">
                    <span class="title2">Splatoon3 - スプラトゥーン3 攻略＆検証  Wiki*</span>
                </a>
            </div>
                <div class="toolbox-container system-ui clearfix" id="naviframe">
            <div class="toolbox toolbox-desktop navibar-container">
                <div id="navigator">[ <a href="/splatoon3mix/">ホーム</a> | <a href="/splatoon3mix/::cmd/newpage?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF" rel="nofollow">新規</a> | <a href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF" rel="nofollow">編集</a> | <a href="/splatoon3mix/::cmd/attach?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF" rel="nofollow">添付</a> ]</div>            </div>
            <div class="toolbox toolbox-desktop toolbar-container">
                <div class="toolbar"><a href="/splatoon3mix/::cmd/list" title="一覧" rel="nofollow"><span class="system-icon toolbar list"></span></a>
<a href="/splatoon3mix/RecentChanges" title="最終更新" rel="nofollow"><span class="system-icon toolbar recent"></span></a>
<a href="/splatoon3mix/::cmd/diff?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF" title="差分" rel="nofollow"><span class="system-icon toolbar diff"></span></a>
<a href="/splatoon3mix/::cmd/backup?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF" title="バックアップ" rel="nofollow"><span class="system-icon toolbar backup"></span></a>
<a href="/splatoon3mix/::cmd/freeze?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF" title="凍結" rel="nofollow"><span class="system-icon toolbar freeze"></span></a>
<a href="/splatoon3mix/::cmd/template?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF" title="複製" rel="nofollow"><span class="system-icon toolbar copy"></span></a>
<a href="/splatoon3mix/::cmd/rename?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF" title="名前変更" rel="nofollow"><span class="system-icon toolbar rename"></span></a>
<a href="/splatoon3mix/::cmd/help" title="ヘルプ" rel="nofollow"><span class="system-icon toolbar help"></span></a></div>            </div>
            <div class="toolbox toolbox-mobile toolbar-container">
                <div class="toolbar"><a href="/splatoon3mix/" title="ホーム"><span class="system-icon toolbar top"></span></a>
<a href="/splatoon3mix/RecentChanges" title="最終更新" rel="nofollow"><span class="system-icon toolbar recent"></span></a>
<a id="menu-in-nav" href="#menubar" class="menu-in-nav">Menu<i class="fas fa-arrow-alt-down"></i></a></div>            </div>
            <div class="toolbox toolbox-searchbar">
                <form action="/splatoon3mix/::cmd/search" method="get">
                    <input type="search"  name="word" value="" size="16" placeholder="サイト内検索">
                    <input type="hidden" name="type" value="AND">
                    <input type="submit" value="検索">
                </form>
            </div>
        </div>
            <div id="responsive-navigation"></div>
    <div style="display: none;">
        <div id="edit-menu" class="system-ui">
            <div id="edit-menu-items">
                <ul><li><a href="/splatoon3mix/::cmd/newpage?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF" rel="nofollow"><span class='system-icon toolbar new'></span> 新規</a></li><li><a href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF" rel="nofollow"><span class='system-icon toolbar edit'></span> 編集</a></li><li><a href="/splatoon3mix/::cmd/attach?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF" rel="nofollow"><span class='system-icon toolbar upload'></span> 添付</a></li></ul>
<ul><li><a href="/splatoon3mix/::cmd/list" rel="nofollow"><span class='system-icon toolbar list'></span> 一覧</a></li><li><a href="/splatoon3mix/RecentChanges" rel="nofollow"><span class='system-icon toolbar recent'></span> 最終更新</a></li><li><a href="/splatoon3mix/::cmd/diff?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF" rel="nofollow"><span class='system-icon toolbar diff'></span> 差分</a></li><li><a href="/splatoon3mix/::cmd/backup?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF" rel="nofollow"><span class='system-icon toolbar backup'></span> バックアップ</a></li></ul>
<ul><li><a href="/splatoon3mix/::cmd/freeze?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF" rel="nofollow"><span class='system-icon toolbar freeze'></span> 凍結</a></li><li><a href="/splatoon3mix/::cmd/template?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF" rel="nofollow"><span class='system-icon toolbar copy'></span> 複製</a></li><li><a href="/splatoon3mix/::cmd/rename?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF" rel="nofollow"><span class='system-icon toolbar rename'></span> 名前変更</a></li></ul>
<ul><li><a href="/splatoon3mix/::cmd/help" rel="nofollow"><span class='system-icon toolbar help'></span> ヘルプ</a></li></ul>

            </div>
        </div>
    </div>    </div>

    <div class="container">
        <div class="clearfix">
            <div id="breadcrumbs" class="system-ui">
                <div id="topicpath"><a href="/splatoon3mix/" title="FrontPage"><i class="fa fa-home" style="margin-left: 6px; display: inline-block; min-width: 1.2em;"></i></a> &gt; <a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン">サーモンラン</a> &gt; <a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8" title="サーモンラン/ステージ">ステージ</a> &gt; トキシラズいぶし工房</div>            </div>
            <div id="system-icon-container" class="system-ui">
                                <span id="share-button-root"></span>                <span id="admin-contact-root" class="single-system-icon"></span>
                <div id="load-panel-root"></div>
                <span id="admin-login" class="single-system-icon">
                    
<a class="admin-login-status" href="/splatoon3mix/::cmd/admin_login?return_to=%2Fsplatoon3mix%2F%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF" title="未ログイン">
    <i class="fa-solid fa-cog"></i>
</a>
                </span>
            </div>
        </div>
        <hr />
    </div>

    <div id="contents" class="columns-container three-columns-container container clearfix has-left-column">

        <div class="column-center clearfix">
            <div id="body">
                                                <div id="title">
                                            <h1 class="title">トキシラズいぶし工房</h1>
                                                                <div id="lastmodified">
                            Last-modified: 2026-01-13 (火) 09:25:24                                                            <span class="lastmodified-file-itself tooltip" data-tippy-content="このページ自体の更新: 2025-08-10 (日) 20:21:33"><i class="fas fa-file-signature"></i></span>
                                                    </div>
                                    </div>

                
<div id="inbound-ad-container">
  <!-- /19033742/WIKIWIKI_PC_INBOUND -->
  <div id='div-gpt-ad-1567409776345-0'></div>
  <!-- /19033742/WIKIWIKI_PC_INBOUND_RIGHT -->
  <div id='div-gpt-ad-1658802281376-0'></div>
  <!-- /19033742/WIKIWIKI_SP_INBOUND -->
  <div id='div-gpt-ad-1563430750445-0' class="hidden-switch-class"></div>
</div>

<style>
.pc-inbound-ad-default {
    margin-top:40px;
    margin-bottom:40px;
    display:flex;
    justify-content:flex-start;
    gap: 10px 5px;
    min-height:280px;
}
.pc-inbound-ad-center{
    margin-top:40px;
    margin-bottom:40px;
    display:flex;
    justify-content:center;
    gap: 10px 5px;
    min-height:280px;
    position: relative;
}
.pc-inbound-ad-mobile{
    margin-top:20px;
    margin-bottom:20px;
    display:flex;
    justify-content:center;
    min-height:280px;
}
.pc-inbound-ad-close-button {
    position: absolute;
    top: -25px;
    left: 50%;
    transform: translateX(-50%);
    width: 20px;
    height: 20px;
    background: url('data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"%3E%3C!--! Font Awesome Pro 6.6.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2024 Fonticons, Inc. --%3E%3Cpath class="fa-secondary" opacity=".4" d="M281.4 390.6L304 413.3 349.3 368l-22.6-22.6L237.3 256l89.4-89.4L349.3 144 304 98.7l-22.6 22.6L192 210.7l-89.4-89.4L80 98.7 34.7 144l22.6 22.6L146.7 256 57.4 345.4 34.7 368 80 413.3l22.6-22.6L192 301.3l89.4 89.4z" fill="%23888"/%3E%3C/svg%3E') no-repeat center;
    background-size: contain;
    cursor: pointer;
}
</style>

<script>
(function () {
    const co = document.getElementById('inbound-ad-container');
    const inboundPaths = [
        '/19033742/WIKIWIKI_PC_INBOUND',
        '/19033742/WIKIWIKI_PC_INBOUND_RIGHT'
    ];

    if (wi_isinbound && wi_group === "N" && wi_agreement === "false") {
        if (wi_ismobile) {
            co.classList.add("pc-inbound-ad-mobile","default-advertisement");
        } else {
            const width = co.clientWidth;
            const adClass = width < 683 || (width >= 683 && width < 900) ? ["pc-inbound-ad-center","default-advertisement"] : ["pc-inbound-ad-default"];
            co.classList.add(...adClass);

            if (adClass.includes("pc-inbound-ad-center")) {
                googletag.cmd.push(function() {
                    googletag.pubads().addEventListener('slotOnload', function(event) {
                        if (inboundPaths.includes(event.slot.getAdUnitPath())) {
                            let closeButton = co.querySelector(".pc-inbound-ad-close-button");
                            if (!closeButton) {
                                closeButton = document.createElement("div");
                                closeButton.classList.add("pc-inbound-ad-close-button");
                                closeButton.onclick = () => co.style.display = "none";
                                co.appendChild(closeButton);
                            }
                        }
                    });
                });
            }
        }
    }
})();
</script>

                <div class="search-words small" style="display: none;">
    <div class="small">これらのキーワードがハイライトされています：<ul class="search-words-words"></ul></div>
    <hr class="full_hr">
</div>
                <div id="content">
                                        <p>関連ページ:</p>
<div class="includex" style="padding:0;margin:0;"> <a class="anchor_super" id="zd9ae70791647ec99eddce02a03328fa6" href="#zd9ae70791647ec99eddce02a03328fa6" title="zd9ae70791647ec99eddce02a03328fa6"></a></div>
<form action="/splatoon3mix/::cmd/jumplist?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%82%A2%E3%83%A9%E3%83%9E%E3%82%AD%E7%A0%A6" method="post">
 <div>
  <select name="select"><option value="サーモンラン/ステージ/アラマキ砦">サーモンラン/ステージ/アラマキ砦</option>
<option value="サーモンラン/ステージ/ムニ・エール海洋発電所">サーモンラン/ステージ/ムニ・エール海洋発電所</option>
<option value="サーモンラン/ステージ/シェケナダム">サーモンラン/ステージ/シェケナダム</option>
<option value="サーモンラン/ステージ/難破船ドン・ブラコ">サーモンラン/ステージ/難破船ドン・ブラコ</option>
<option value="サーモンラン/ステージ/すじこジャンクション跡">サーモンラン/ステージ/すじこジャンクション跡</option>
<option value="サーモンラン/ステージ/トキシラズいぶし工房">サーモンラン/ステージ/トキシラズいぶし工房</option>
<option value="サーモンラン/ステージ/どんぴこ闘技場">サーモンラン/ステージ/どんぴこ闘技場</option>
</select>
  <input type="submit" name="jump" value="GO" />
 </div>
</form>

<hr class="full_hr" />
<div class="contents">
<a id="contents-index"></a>
<ul class="list1"><li><a href="#maininfo">攻略情報 </a>
<ul class="list2"><li><a href="#dad90fad">通常時 </a></li>
<li><a href="#vaf48d9d">満潮時 </a></li>
<li><a href="#k9b63705">干潮時 </a></li></ul></li>
<li><a href="#j5ba0c26">特殊な状況 </a>
<ul class="list3"><li><a href="#jf8fd397">ラッシュ </a></li>
<li><a href="#wfe25596">グリル発進 </a></li>
<li><a href="#w4e258f5">ドスコイ大量発生 </a></li>
<li><a href="#g9e0beff">キンシャケ探し </a></li></ul></li>
<li><a href="#a35cfd39">覚えておくと役立つ事 </a></li>
<li><a href="#commment">コメント</a></li></ul>
</div>
<hr class="full_hr" />
<p><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF/::ref/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF.jpg?rev=55c018df572f223f78f2966990864ea0&amp;t=20230920121604" alt="トキシラズいぶし工房" title="トキシラズいぶし工房" width="480" height="270"  loading="lazy"><br />
<img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF/::ref/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E5%85%A8%E4%BD%93%E3%83%9E%E3%83%83%E3%83%97.png.webp?rev=7d7f9ad991997d9261ff29ede97a9a97&amp;t=20230905075225" alt="トキシラズ全体マップ.png" title="トキシラズ全体マップ.png" width="614" height="381"  loading="lazy"></p>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">ブイとエリアの対応</div>
    <div class="fold-content visible-on-open"><div class="h-scrollable"><table><thead><tr><th>ブイ</th><th><strong>ウインナー</strong></th><th><strong>アスパラ</strong></th><th><strong>コーン</strong></th></tr></thead><tbody><tr><th>画像</th><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF/::ref/%E3%83%96%E3%82%A4_%E3%82%A6%E3%82%A4%E3%83%B3%E3%83%8A%E3%83%BC.png.webp?rev=fab1ab61f817b2267227d9cf8d0c659a&amp;t=20230920174859" alt="ブイ_ウインナー.png" title="ブイ_ウインナー.png" width="156" height="225"  loading="lazy"></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF/::ref/%E3%83%96%E3%82%A4_%E3%82%A2%E3%82%B9%E3%83%91%E3%83%A9.png.webp?rev=88817202d7cc8894faa40da7129e4753&amp;t=20230920174907" alt="ブイ_アスパラ.png" title="ブイ_アスパラ.png" width="156" height="225"  loading="lazy"></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF/::ref/%E3%83%96%E3%82%A4_%E3%82%B3%E3%83%BC%E3%83%B3.png.webp?rev=28d917cfb1f53cd2355703af4542b465&amp;t=20230920174914" alt="ブイ_コーン.png" title="ブイ_コーン.png" width="156" height="225"  loading="lazy"></td></tr><tr><th>方角</th><td>カゴ側左<br class="spacer">(簡易マップ左下側)</td><td>対岸側左<br class="spacer">(簡易マップ左上側)</td><td>カゴ側右下<br class="spacer">(簡易マップ右下側)</td></tr></tbody></table></div>
</div>
</div>
<h2 id="h2_content_1_0" >攻略情報  <a class="anchor_super" name ="maininfo"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF&id=maininfo" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<p>空中を水平に可動するプロペラリフトでつながれたふたつの施設跡と、それらを分かつ中央通路、主にコンテナの置かれた側の施設を中心に分布し、周囲を取り巻く砂浜から構成される。<br />
他ステージに比べると、外向きに長く伸びた地形がないためか、あるいは視界がよく通るためだろうか、幾分手狭な印象を受ける。</p>
<p>詳細は後述するが通常時・干潮と満潮の難易度差が最も激しいステージと言える。<br />
総合的に見ると見渡しが良く、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>の発見が遅れる事は少ない。また厄介な地点そのものが少ない。<br />
満潮こそ難易度が高く対岸という要注意ポイントもあるものの長居しなければいいので、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>の処理、カオスになった際の緊急退避など、上手く使いこなすといい。<br />
前作ではシャケの上陸地点が近く、金イクラを集めやすいことから難易度は低めと見られていたが、今作ではシャケの物量が増したことにより、気を抜くとシャケが溢れかえって打開が困難となるキケンなマップとなっている。</p>
<p>また、通常時と満潮時ではリフトに乗ろうとして転落する事故が発生しやすい。事故を防ぐ為に、<strong>リフトに乗る際は手前ではなく奥の方にジャンプして乗るように。</strong></p>
<p>なお以下では通常・満潮の方角を示す際、便宜上コンテナ付近から対岸を向いて右側・左側・後方と表記する。</p>
<h3 id="h3_content_1_1" class="heading-after-first">通常時  <a class="anchor_super" name ="dad90fad"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF&id=dad90fad" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<p>主戦場はコンテナ側施設周辺としたい。この施設自体が堅牢な要塞として活用できるためである。<br />
シャケの侵攻ルートである砂浜に対し、各方向に用意された高台からは見通しがよく利き、撃ち下ろしが有効に機能する。リフト直下の金属壁を除いたほとんどの壁も塗ることができるため、砂浜に落ちた金イクラの納品も容易かつ高速で、塗り状況の良い前半は有利に展開できるだろう。<br />
他ステージ満潮のような格闘戦に経験と自信があるなら、ここで存分に生かすことができるだろう。<br />
一方で、リフトを渡って向こう側の施設や、その周辺の砂浜などは基本的に敵陣となる。<br />
コンテナ側を中心に戦闘が展開されるため対岸は少し滞在する程度では比較的安全。しかし湧きポイントから距離が近いため長居しすぎると押し負けやすい。<br />
またコンテナ側以上に狭く距離が遠いので支援や救助も受けづらい点にも留意。<br />
ただし沿岸三銃士が出現した場合は別。その場合も素早く殲滅して速やかに帰還しよう。砂浜にシャケが多すぎるならば対岸を経由してピンポイントで遠征・帰還を行うのも1つの手。<strong>特に対岸施設には塗れる壁が多く、[巨大鉄塔]方向では中央通路や砂浜から直接屋上に登れる。ここはその近辺の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>に対して取り巻きをかわせる絶好の攻撃地点。</strong><br />
その他<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA" title="サーモンラン/シャケの種類/コウモリ" class="rel-wiki-page">コウモリ</a>を1ターンキルが容易なブキでは反射ではなく直接殴りに行くのも良い。<br />
どのような状況でも対岸は敵で溢れたコンテナ付近からの優秀な緊急退避施設として役立つ。</p>
<p>更なる応用として、対岸までやってきた<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a>をリフト上に止めてそのままコンテナ側までお持ち帰りしたり、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a>から放たれたボムを対岸にどかすテクニックがあり前者は干潮側リフト、後者は左側リフトで可能。覚えておくと役に立つだろう。</p>
<p>その他難度を引き上げる要因の1つに<strong><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%82%AD%E3%83%A5%E3%82%A6" title="サーモンラン/シャケの種類/テッキュウ" class="rel-wiki-page">テッキュウ</a>の往復経路が極めて短い</strong>ことが挙げられる。距離がそのまま攻撃速度に直結するため脅威度が跳ね上がり、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%82%AD%E3%83%A5%E3%82%A6" title="サーモンラン/シャケの種類/テッキュウ" class="rel-wiki-page">テッキュウ</a>2体でも他のステージの3体に匹敵しかねないスパンでコンテナ側の高台全域を攻撃するため非常に危険。</p>
<h4 id="h4_content_5_0" >地形の利用</h4>

<p><strong>移動ルート</strong></p>
<ul class="list1"><li>このステージでの<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a>はマップ中央の水場に建設することがある。<br />
<img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF/::ref/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF_%E9%80%9A%E5%B8%B8%E4%B8%AD%E5%A4%AE%E3%83%8F%E3%82%B7%E3%83%A9.webp.webp?rev=3e135f6767bc83b7da6e8c4a546f02b0&amp;t=20230920175708" alt="トキシラズいぶし工房_通常中央ハシラ.webp" title="トキシラズいぶし工房_通常中央ハシラ.webp" width="480" height="240"  loading="lazy">
<ul class="list2"><li>そこにある<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a>を利用すればプロペラリフト無しで対岸へ素早くアクセス可能。<br />
何故か満潮時はここに刺さる<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a>が高くなる。移動経路として使うには側面の塗りが必須になるので注意。<br />
<span class="wikicolor" style="color:red">Wave終了時にここにとどまるのは絶対にやってはならない。</span><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a>のてっぺんが「最後に立っていた地面」となり、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a>が消えると落下→水没→ウキワ→落下→水没→ウキワ...を繰り返してしまう。</li></ul></li></ul>
<p><strong><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>にボムを投げ込める場所</strong><br />
イクラコンテナ周辺の広場・高台から大概のスポットに投擲可能。</p>
<ul class="list1"><li>対岸右側[コーン]1体目・2回目の射撃時（右奥の個体）<br />
2ポイントあり、<strong>スロープ横をさらに一段登った高台</strong>か、<strong>スロープ手前から助走をつけ</strong>つつ投げ込む。<br />
後者の地点でそのまま下に飛び降りると前線移動が速い。そのまま戦闘に入る際はインク切れには注意すること。<br />
一方前者は飛び降りまでは至りづらく、安全策の趣が強い。<strong>スロープを登ってくる<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>越しにコンテナを落とせる</strong>ので、中盤以降戦果まで手が出しづらい局面で。<br />
前作ではここが1回目の射撃地点だったが、今作では1回目の射撃地点が奥側となり、出現直後にボムを投げ込むには対岸に渡る必要性が高くなった。</li>
<li>対岸左側[アスパラ]1体目・1回目の射撃時（左奥の個体<a id="notetext_1"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;前作と出現順が変更&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_1&quot;&gt;脚注 *1 へ&lt;/a&gt;&lt;/div&gt;">*1</a>）<br />
金網上から助走投げでぎりぎり届く。</li></ul>
<p><strong>高台にボムを置くことで<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>の両翼を壊せる場所</strong><br />
左後方<a id="notetext_2"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;左側3体目として出現する場合と後方3体目として出現する場合がある&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_2&quot;&gt;脚注 *2 へ&lt;/a&gt;&lt;/div&gt;">*2</a>の個体を除くすべての<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>で可能。</p>
<ul class="list1"><li>対岸右側[コーン]1体目・1、2回目の射撃時（右奥の個体、対岸の金網に接近）<br />
1回目は足場の角を狙うと届く<br />
<img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF/::ref/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF_%E3%82%AB%E3%82%BF%E3%83%91%E3%83%AF%E3%83%B3%E3%83%91%E3%83%B3_%E9%80%9A%E5%B8%B8%E5%AF%BE%E5%B2%B8%E3%82%B3%E3%83%BC%E3%83%B3_1%E4%BD%93%E7%9B%AE2%E5%9B%9E%E7%9B%AE.jpg.webp?rev=6fc5dea639bbe09228aa19dd37549382&amp;t=20240228153900" alt="トキシラズいぶし工房_カタパワンパン_通常対岸コーン_1体目2回目.jpg" title="トキシラズいぶし工房_カタパワンパン_通常対岸コーン_1体目2回目.jpg" width="480" height="240"  loading="lazy"><br />
2回目は金網側に向かせ金網上に置くと届く</li>
<li>右後方・2回目の射撃時（右後方高台に接近、右側2体目として出現する場合と後方2体目として出現する場合がある）<br />
<img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF/::ref/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF_%E3%82%AB%E3%82%BF%E3%83%91%E3%83%AF%E3%83%B3%E3%83%91%E3%83%B3_%E9%80%9A%E5%B8%B8%E5%BE%8C%E6%96%B9%E3%82%B3%E3%83%BC%E3%83%B3n%E4%BD%93%E7%9B%AE2%E5%9B%9E%E7%9B%AE.jpg.webp?rev=a580d596cfdce005516e47299911f2fa&amp;t=20240228153915" alt="トキシラズいぶし工房_カタパワンパン_通常後方コーンn体目2回目.jpg" title="トキシラズいぶし工房_カタパワンパン_通常後方コーンn体目2回目.jpg" width="480" height="240"  loading="lazy"><br />
地形になるべく正対させ高台上に置くと届く</li>
<li>後方[ウインナー]1体目（コンテナ後方の個体、左後方高台に接近<a id="notetext_3"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;前作にない射撃位置&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_3&quot;&gt;脚注 *3 へ&lt;/a&gt;&lt;/div&gt;">*3</a>）<br />
<img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF/::ref/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF_%E3%82%AB%E3%82%BF%E3%83%91%E3%83%AF%E3%83%B3%E3%83%91%E3%83%B3_%E9%80%9A%E5%B8%B8%E3%82%A6%E3%82%A4%E3%83%B3%E3%83%8A%E3%83%BC.webp.webp?rev=401dd83012b63dbf3ec27274da8da99e&amp;t=20230920175622" alt="トキシラズいぶし工房_カタパワンパン_通常ウインナー.webp" title="トキシラズいぶし工房_カタパワンパン_通常ウインナー.webp" width="480" height="240"  loading="lazy"><br />
高台角に置くと届く</li>
<li>対岸左側[アスパラ]1体目・1回目の射撃時（対岸高台頂上に接近）<br />
<img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF/::ref/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF_%E3%82%AB%E3%82%BF%E3%83%91%E3%83%AF%E3%83%B3%E3%83%91%E3%83%B3_%E9%80%9A%E5%B8%B8%E3%82%A2%E3%82%B9%E3%83%91%E3%83%A9_1%E4%BD%93%E7%9B%AE1%E5%9B%9E%E7%9B%AE.jpg.webp?rev=de2efdf48d8f5152874a987234c3551f&amp;t=20240114135931" alt="トキシラズいぶし工房_カタパワンパン_通常アスパラ_1体目1回目.jpg" title="トキシラズいぶし工房_カタパワンパン_通常アスパラ_1体目1回目.jpg" width="480" height="240"  loading="lazy"><br />
対岸高台頂上側に向かせ高台上に置くと届く。出現確認してすぐに向かわないと向き調整が間に合わない</li>
<li>対岸左側[アスパラ]2体目・2回目の射撃時（左手前の個体、金網のある高台カンケツセンAに接近）<br />
高台に正対させ高台上に置くと届く</li></ul>
<p><strong><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%80%E3%82%A4%E3%83%90%E3%83%BC" title="サーモンラン/シャケの種類/ダイバー" class="rel-wiki-page">ダイバー</a>の誘導に有効な場所</strong></p>
<ul class="list1"><li>金網およびリフト</li></ul>
<p><strong>イクラ投げ</strong></p>
<ul class="list1"><li>対岸からおおざっぱに投げてもコンテナ側に届くほか、中央の張り出した足場からイカダッシュ＋イクラ投げジャンプでコンテナまでぎりぎり届き、対岸金網上からイクラ投げジャンプでコンテナまで届く。</li>
<li>対岸に向かうリフトと金網の間の低地からイクラ投げジャンプでコンテナまで届く。</li></ul>
<p><strong>屋根状の地形</strong></p>
<ul class="list1"><li>コンテナ側金網に至る床面はひさし状に突き出ているため、その真下にいることで<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%A2%E3%83%A1%E3%83%95%E3%83%A9%E3%82%B7" title="ブキ/スペシャルウェポン/アメフラシ" class="rel-wiki-page">アメフラシ</a>やミサイルを遮る屋根として利用できる。壁面を塗って<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="主に&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;&lt;strong&gt;壁に塗られたインクに潜る様子のこと&lt;/strong&gt;。&lt;br class=&quot;spacer&quot;&gt;&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;では自分をターゲットとしているシャケらをしばらくの間釘付けにできるが、あまり長くやりすぎると&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB&quot; title=&quot;サーモンラン/シャケの種類/グリル&quot; class=&quot;rel-wiki-page&quot;&gt;グリル&lt;/a&gt;のターゲット変更や&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1&quot; title=&quot;サーモンラン/シャケの種類/ザコシャケ&quot; class=&quot;rel-wiki-page&quot;&gt;ザコシャケ&lt;/a&gt;の大ジャンプにより痛い目にあう。&lt;br class=&quot;spacer&quot;&gt;また、セミ中は攻撃できないため、自軍の火力が減るという重大な欠点もある。&lt;br class=&quot;spacer&quot;&gt;「金イクラが大量だが敵の勢いが激しく納品が捗らない状況で、自分が離れた地点でセミをし敵を誘導し、その隙に味方に納品をしてもらう」「デスした味方がウキワになるまでのタイムラグを凌ぐ」など、場面や使いようによっては非常に有用。&lt;br class=&quot;spacer&quot;&gt;&lt;br class=&quot;spacer&quot;&gt;&lt;a href=&quot;/splatoon3mix/%E7%94%A8%E8%AA%9E%E9%9B%86/%E5%AF%BE%E6%88%A6%E9%96%A2%E9%80%A3%E7%94%A8%E8%AA%9E#k58821ab&quot; title=&quot;用語集/対戦関連用語&quot; class=&quot;rel-wiki-page&quot;&gt;&lt;span class=&quot;wikicolor&quot; style=&quot;color:#808080&quot;&gt;[詳細]&lt;/span&gt;&lt;/a&gt;">セミ</span>をしてもよい。</li></ul>
<h3 id="h3_content_1_2" class="heading-after-first">満潮時  <a class="anchor_super" name ="vaf48d9d"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF&id=vaf48d9d" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<p>中央通路を含む施設外領域がほぼすべて水没し、コンテナ側と対岸施設の2つの小さなステージに分断される。<br />
中央の水没と分断に伴い、行動可能な面積は非常に狭く、その上あろうことかコンテナ至近まで<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>がつけてくるようなとんでもない上陸地点までも設定されており、waveを通じてシャケと文字通りに殴り合うような超近接戦闘の連続が避けられない。他ステージ満潮と比べても熾烈な戦闘を覚悟しなければならないだろう。<br />
対岸は納品的に原則不利とは述べたが、満潮時はコンテナ側だけではかなり狭くシビアなので、高危険度になるにつれ状況次第で臨機応変に対岸を活用していく必要がある。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>やカタパが対岸に湧いた時も、早めに渡って倒しにいかないと、通常時より更に狭いコンテナ側の足場があっという間に制圧されてしまう。でんせつ帯の場合、角笛の音がなったときに対岸の湧きを確認していないと、いつの間にか<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>が何体も対岸に湧いてカオス一直線ということが十分にありえる。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#snatcher" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">タマヒロイ</a>が有効活用出来る場合がありコンテナ側の後方2箇所、対岸側中央の1箇所で3パターンあり、コンテナ側から出現するパターンの場合は対岸である程度処理をしてしまっても納品は間に合うことが多い、対岸出現のパターンは対岸での処理のし過ぎに注意。</p>
<p>対岸へ渡る手段はリフト以外になく、この扱いが重要になる。</p>
<p>リフトを動かす前には、同乗しようとしている者がいないか必ず確認すること。乗り遅れが発生すると下は水面なのでドンブラコのリフトと違い即死する。特に対岸→コンテナ側に金イクラを持って移動する場合には、動かす前に「カモン！」で呼び寄せると良い。<strong>同僚と意思疎通が取れないならば、リスクヘッジ的に、対岸に2人以上いるのはかなり危険。</strong>というのも、帰りのリフトで全員が乗るまで待つのは、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%A2%E3%82%B0%E3%83%A9" title="サーモンラン/シャケの種類/モグラ" class="rel-wiki-page">モグラ</a>の襲撃・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>の空襲・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a>ボムのリフトへの投擲のリスクがあり、かと言って複数回に分けてリフトを利用するのは、後で利用するイカが対岸に長居するということになり、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>以外のオオモノやザコの攻撃を凌ぎながらリフトを待たないといけないためである。<br />
既にリフトが動かされている場合には、（コンテナ側、対岸側のどちらも）向かって左に伸びた金網の先端、および対岸側なら両リフトの中央からイカジャンプをすれば逆側のリフトまで飛び移れる。<br />
また、プロペラの裏から撃ってもリフトは動作するため、対岸のリフトを引き寄せることも可能。</p>
<p>なお、リフトには上に乗るだけで<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>の狙いを自分から逸らし、それらから最も近い他人に移してしまう性質があることは覚えておきたい<a id="notetext_4"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;なお、通常のシャケや&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3&quot; title=&quot;サーモンラン/シャケの種類/テッパン&quot; class=&quot;rel-wiki-page&quot;&gt;テッパン&lt;/a&gt;に対してはこの性質は働かず、飛び移れる場合は飛び移り、そうでない場合は反対側へ先回りしようとする。定点維持も困難で、&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5&quot; title=&quot;サーモンラン/特殊な状況/ラッシュ&quot; class=&quot;rel-wiki-page&quot;&gt;ラッシュ&lt;/a&gt;時に安全地帯として活用することは極めて難しいと思われる&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_4&quot;&gt;脚注 *4 へ&lt;/a&gt;&lt;/div&gt;">*4</a>。<br />
唐突な<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>のターゲット変更は味方の混乱やデスを招くため、狭くて敵との距離が近い満潮では安易にリフトに乗ってターゲット変更を行うべきではない。</p>
<p>ちなみに、満潮時はリフトだけが唯一対岸との移動手段になるが、ウキワになっていると弾が出せない為、<span class="wikicolor" style="color:Red"><strong>満潮時は対岸で死亡すると自力では絶対に帰還できない。</strong></span>この場合カモンで呼んでもどうしようもないので、多量のインクを消費するボム・長射程メイン・<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>で救助するしか無い。救助される側もそのような状況にならないよう、対岸に渡る際は死亡に対して細心の注意を払う事。また、リフトで帰還する場合、此岸側の足場に足をつけられずに死亡すると対岸でウキワになることにも注意。</p>
<p>たまに対岸にボムを投げるイカが見られるが、やめた方がよい。対岸にイカがいた場合、対岸から帰還しようとリフトを目指す→ボムの爆風でリフトが起動→反応が間に合わず水没　といったことになりかねないからだ。そもそもボムは１回でインクタンクの70%をも消費するが、前述の通りトキシラズの満潮は非常に狭く、投げた直後に敵が上陸してきてはジリ貧になること必至だ。例えインクが余っていたとしても、やたらと投げるべきではないのだ。</p>
<p>対岸<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>の金イクラを回収したはいいが、たちまちシャケに取り囲まれて死亡するアルバイターがかなり多い。すぐ横の壁が塗られていないと、死亡リスクがかなり上がる。<a id="notetext_5"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;対岸右の砂浜の坂道は出現直後の&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#chum&quot; title=&quot;サーモンラン/シャケの種類/ザコシャケ&quot; class=&quot;rel-wiki-page&quot;&gt;中シャケ&lt;/a&gt;に退路を断たれる。&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_5&quot;&gt;脚注 *5 へ&lt;/a&gt;&lt;/div&gt;">*5</a><strong>この壁が塗られていると確信できない場合は、対岸<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>を上の足場から倒したら、金イクラを拾いに行かずにすぐにリフトに乗ってコンテナ側に帰ることを強く推奨する。</strong><br />
ちなみに、左側の突き出した金網から、対岸の目の前にいる<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>は、射程があれば倒すことができる。</p>
<p>狙ったかのように対岸に悠々と陣を敷いた<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA" title="サーモンラン/シャケの種類/コウモリ" class="rel-wiki-page">コウモリ</a>が水上へ放った<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%A2%E3%83%A1%E3%83%95%E3%83%A9%E3%82%B7" title="ブキ/スペシャルウェポン/アメフラシ" class="rel-wiki-page">アメフラシ</a>弾に、短～中射程ブキが一切インクを当てられず、眼前で撃ち上がる雲を茫然と眺めて<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%A2%E3%83%A1%E3%83%95%E3%83%A9%E3%82%B7" title="ブキ/スペシャルウェポン/アメフラシ" class="rel-wiki-page">アメフラシ</a>に降られる、といった場面が多く見られた。<br />
<strong>長射程ブキの担当であれば、対岸から撃ち出される<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA" title="サーモンラン/シャケの種類/コウモリ" class="rel-wiki-page">コウモリ</a>の<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%A2%E3%83%A1%E3%83%95%E3%83%A9%E3%82%B7" title="ブキ/スペシャルウェポン/アメフラシ" class="rel-wiki-page">アメフラシ</a>弾は特に見逃さないようにしたい。</strong></p>
<p>高危険度になるほどシャケたちの強化や有利な<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#snatcher" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">タマヒロイ</a>などもあり前作ほど対岸に居続けるプレイヤーがクリアを遠のかせる要因にはなりにくい。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>処理、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>などを間引くことでコンテナ側の安全を高めることができクリアしやすくなるが、<strong>対岸に居続けるのであれば絶対に死なないこと</strong>。</p>
<p>満潮時に夜WAVEの予兆が発生し、カンケツセン・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B3%E3%83%93%E3%83%A4%E3%81%9F%E3%81%A1#mothership" title="サーモンラン/シャケの種類/ハコビヤたち" class="rel-wiki-page">ハコビヤ</a>・霧などの演出が確認できない場合は、WAVE開始の瞬間に通路部付近にいてはいけない。<br />
次のWAVEが<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%82%B0%E3%83%AA%E3%83%AB%E7%99%BA%E9%80%B2" title="サーモンラン/特殊な状況/グリル発進" class="rel-wiki-page">グリル発進</a>だった場合開幕と同時に<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>が乗り込んできて暴れ出すため、<strong>「<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>が現れた」というクマサンのアナウンスを脳で認識した時にはもう死んでいる</strong>…などということになりかねないからだ。<br />
(<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81#i106dbf9" title="サーモンラン/特殊な状況" class="rel-wiki-page">グリル発進が発生する場合にもグリルのカラカラ音が聞こえるという予兆はある</a>が、音が小さくわかりづらい)<br />
他のステージの満潮にも言えることではあるが、対岸を除いたステージ面積が極めて狭いこのステージでは<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>の開幕事故に特に注意が必要である。</p>
<h4 id="h4_content_6_0" >地形の利用</h4>

<p><strong><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>にボムを投げ込める場所</strong></p>
<ul class="list1"><li>対岸左側[アスパラ]1体目（対岸向かって左の個体）</li>
<li>対岸左側[アスパラ]3体目<br />
いずれもコンテナ側金網上から届く。</li></ul>
<p><strong>高台にボムを置くことで<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>の両翼を壊せる場所</strong><br />
位置的にできる可能性があるが、確認できていない場所</p>
<ul class="list1"><li>対岸右側[コーン]1体目</li></ul>
<p><strong><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャルウェポン</a></strong></p>
<ul class="list1"><li>対岸の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>にコンテナ側から<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%88%E3%83%AA%E3%83%97%E3%83%AB%E3%83%88%E3%83%AB%E3%83%8D%E3%83%BC%E3%83%89" title="ブキ/スペシャルウェポン/トリプルトルネード" class="rel-wiki-page">トリプルトルネード</a>・<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%8A%E3%82%A4%E3%82%B9%E3%83%80%E3%83%9E" title="ブキ/スペシャルウェポン/ナイスダマ" class="rel-wiki-page">ナイスダマ</a>が届く。</li>
<li>リフトを稼働させ対岸に足をつける前に<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88%E3%83%91%E3%83%83%E3%82%AF" title="ブキ/スペシャルウェポン/ジェットパック" class="rel-wiki-page">ジェットパック</a>を起動する、またはコンテナ側で起動し左右の海上を飛行して対岸に向かうなどすれば、帰還位置がコンテナ側となり、対岸で仕事をした後でも比較的安全に帰還できる。</li></ul>
<h3 id="h3_content_1_3" class="heading-after-first">干潮時  <a class="anchor_super" name ="k9b63705"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF&id=k9b63705" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<p>通路が広く大きく左右に分かれているという点ですじこ干潮に似たステージ。<br />
他の干潮時ステージとは異なる点として、以下の点が挙げられる。</p>
<ul class="list1"><li>ステージの形がほぼ正方形に近いために非常に横幅が広く、かつコンテナ周辺から上陸地点までその幅が変わらない。</li>
<li>細い道は殆ど存在せず、かつステージの周囲に柵があるために転落の危険が小さく、金網も上陸地点近辺にしかない。</li>
<li>まばらだが遮蔽となる物があり、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a>の爆発などを防ぐことができるほか、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>を遮蔽物に巻き付かせるようにして誘導すると単独でも処理がしやすくなる。</li>
<li>敵の上陸地点は金網通路で繋がれているが、ここはシャケの集団や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a>で封鎖されやすく、敵側にとってのみ左右の連絡や合流がしやすい構造。</li></ul>
<p>このため機動力に優れ、また転落におびえる必要もなくなったイカ側がより強い恩恵を受ける結果となっているように思われる。逃げやすく攻めやすいため、できる限りコンテナまでオオモノシャケを引き寄せて倒し、イクラを稼ぎたい所である。</p>
<div class="caption-flybox" >
  <div id="pc-caption-ad-container">
    <!-- /19033742/WIKIWIKI_PC_CAPTION -->
    <div id='div-gpt-ad-1565253136679-0'></div>
    <!-- /19033742/WIKIWIKI_PC_CAPTION_SIDE_BY -->
    <div id='div-gpt-ad-1719748039754-0' style='max-width: 300px;'></div>
    <!-- /19033742/WIKIWIKI_SP_CAPTION -->
    <div id='div-gpt-ad-1562925510696-0' class="hidden-switch-class"></div>
  </div>
</div>

<script>
if (wi_ismobile && !wi_isinbound) {
    document.getElementById("pc-caption-ad-container").classList.add("default-advertisement","pc-caption-ad-mobile");
    googletag.cmd.push(function() {googletag.display('div-gpt-ad-1562925510696-0');});
    if (window.wikiFq.checkWikifqDisplay('wi_fqgroup1',1,60,0.5) && wi_isread_yet ||wi_location_hash === '##gliaplayer') {
        googletag.cmd.push(function() {googletag.pubads().setTargeting('wi_fqgroup1', 'true');});
        sessionStorage.setItem('wi_pip', false);
        wi_isread_yet = false;
    } else if (sessionStorage.getItem('wi_pip') === 'false') {
        if (window.wikiFq.checkWikifqDisplay('wi_pip',10,60,1.0) && wi_isread_yet) {
            googletag.cmd.push(function() {googletag.pubads().setTargeting('wi_fqgroup1', 'true');});
            wi_isread_yet = false;
        }
    }
} else if (!wi_ismobile && wi_group === 'N' && wi_agreement === 'false' && !wi_isinbound) {
    (function () {
        var gi = document.getElementById("pc-caption-ad-container");
        gi.classList.add("default-advertisement");
        if (gi.clientWidth > 610) {
            if (gi.clientWidth < 769) {
                gi.classList.add("pc-caption-ad-center");
            } else {
                gi.classList.add("pc-caption-ad-default");
            }
            if (window.wikiFq.checkWikifqDisplay('wi_fqgroup1',1,60,1.0) && wi_recref && (wi_recref.includes("google") || wi_recref.includes("yahoo")) || window.wikiFq.checkWikifqDisplay('wi_fqgroup2',1,60,0.2)) {
                googletag.cmd.push(function() {googletag.pubads().setTargeting('wi_fqgroup1', 'true');});
                sessionStorage.setItem('wi_pip', false);
            } else if (sessionStorage.getItem('wi_pip') === 'false') {
                if (window.wikiFq.checkWikifqDisplay('wi_pip',10,60,1.0)) {
                    googletag.cmd.push(function() {googletag.pubads().setTargeting('wi_fqgroup1', 'true');});
                }
            }
            defineSlotFlux.push({"slotID": "div-gpt-ad-1719748039754-0", "sizes": [[300,250]], "slotName":"WIKIWIKI_PC_CAPTION_SIDE_BY"});
            googletag.cmd.push(function() {googletag.display('div-gpt-ad-1565253136679-0');});
            googletag.cmd.push(function() {
                googletag.defineSlot('/19033742/WIKIWIKI_PC_CAPTION_SIDE_BY',[[300,250],[1,1]],'div-gpt-ad-1719748039754-0').addService(googletag.pubads());
                googletag.display('div-gpt-ad-1719748039754-0');});
        }
    })();
}
</script>
<h2 id="h2_content_1_4" class="heading-after-first">特殊な状況  <a class="anchor_super" name ="j5ba0c26"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF&id=j5ba0c26" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<h4 id="h4_content_1_5" class="heading-after-first"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>  <a class="anchor_super" name ="jf8fd397"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF&id=jf8fd397" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h4>
<div class="includex" style="padding:0;margin:0;"> <a class="anchor_super" id="zf21d520005fe9127f6b4eb7822983d9f" href="#zf21d520005fe9127f6b4eb7822983d9f" title="zf21d520005fe9127f6b4eb7822983d9f"></a></div>
<div style="text-align:right"><a class="ext" href="/splatoon3mix/?cmd=edit&amp;page=サーモンラン/特殊な状況/ラッシュ&amp;id=v5bcb7bd" title="部分編集:サーモンラン/特殊な状況/ラッシュ&amp;id=v5bcb7bd"  rel="nofollow">[編集]<span class="system-icon ext pukiwiki-open-uri" data-href="/splatoon3mix/?cmd=edit&amp;page=サーモンラン/特殊な状況/ラッシュ&amp;id=v5bcb7bd" data-frame="_blank"></span></a></div>
<p>対岸に向かって右後方の高台が主な定位置。<br />
壁役は1段目のスロープ付近で狂シャケを防ぎ、長射程ブキは最上段から<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/キンシャケ" class="rel-wiki-page">キンシャケ</a>を削るとよい。</p>
<p>外壁のほとんどが塗れる壁のため、適宜<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="主に&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;&lt;strong&gt;壁に塗られたインクに潜る様子のこと&lt;/strong&gt;。&lt;br class=&quot;spacer&quot;&gt;&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;では自分をターゲットとしているシャケらをしばらくの間釘付けにできるが、あまり長くやりすぎると&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB&quot; title=&quot;サーモンラン/シャケの種類/グリル&quot; class=&quot;rel-wiki-page&quot;&gt;グリル&lt;/a&gt;のターゲット変更や&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1&quot; title=&quot;サーモンラン/シャケの種類/ザコシャケ&quot; class=&quot;rel-wiki-page&quot;&gt;ザコシャケ&lt;/a&gt;の大ジャンプにより痛い目にあう。&lt;br class=&quot;spacer&quot;&gt;また、セミ中は攻撃できないため、自軍の火力が減るという重大な欠点もある。&lt;br class=&quot;spacer&quot;&gt;「金イクラが大量だが敵の勢いが激しく納品が捗らない状況で、自分が離れた地点でセミをし敵を誘導し、その隙に味方に納品をしてもらう」「デスした味方がウキワになるまでのタイムラグを凌ぐ」など、場面や使いようによっては非常に有用。&lt;br class=&quot;spacer&quot;&gt;&lt;br class=&quot;spacer&quot;&gt;&lt;a href=&quot;/splatoon3mix/%E7%94%A8%E8%AA%9E%E9%9B%86/%E5%AF%BE%E6%88%A6%E9%96%A2%E9%80%A3%E7%94%A8%E8%AA%9E#k58821ab&quot; title=&quot;用語集/対戦関連用語&quot; class=&quot;rel-wiki-page&quot;&gt;&lt;span class=&quot;wikicolor&quot; style=&quot;color:#808080&quot;&gt;[詳細]&lt;/span&gt;&lt;/a&gt;">セミ</span>をして納品・立て直しの時間を稼ぐことができる。<br />
これらの壁は<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>のほか<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>でも使用することがあるため、WAVE開始前に優先的に塗っておきたい。<br />
納品中にハエに集られた場合はリフト横の塗れる壁でも<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="主に&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;&lt;strong&gt;壁に塗られたインクに潜る様子のこと&lt;/strong&gt;。&lt;br class=&quot;spacer&quot;&gt;&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;では自分をターゲットとしているシャケらをしばらくの間釘付けにできるが、あまり長くやりすぎると&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB&quot; title=&quot;サーモンラン/シャケの種類/グリル&quot; class=&quot;rel-wiki-page&quot;&gt;グリル&lt;/a&gt;のターゲット変更や&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1&quot; title=&quot;サーモンラン/シャケの種類/ザコシャケ&quot; class=&quot;rel-wiki-page&quot;&gt;ザコシャケ&lt;/a&gt;の大ジャンプにより痛い目にあう。&lt;br class=&quot;spacer&quot;&gt;また、セミ中は攻撃できないため、自軍の火力が減るという重大な欠点もある。&lt;br class=&quot;spacer&quot;&gt;「金イクラが大量だが敵の勢いが激しく納品が捗らない状況で、自分が離れた地点でセミをし敵を誘導し、その隙に味方に納品をしてもらう」「デスした味方がウキワになるまでのタイムラグを凌ぐ」など、場面や使いようによっては非常に有用。&lt;br class=&quot;spacer&quot;&gt;&lt;br class=&quot;spacer&quot;&gt;&lt;a href=&quot;/splatoon3mix/%E7%94%A8%E8%AA%9E%E9%9B%86/%E5%AF%BE%E6%88%A6%E9%96%A2%E9%80%A3%E7%94%A8%E8%AA%9E#k58821ab&quot; title=&quot;用語集/対戦関連用語&quot; class=&quot;rel-wiki-page&quot;&gt;&lt;span class=&quot;wikicolor&quot; style=&quot;color:#808080&quot;&gt;[詳細]&lt;/span&gt;&lt;/a&gt;">セミ</span>ができることを覚えておこう。<br />
満潮時は周囲が海になるため水没に注意。</p>

<h4 id="h4_content_1_6" class="heading-after-first"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%82%B0%E3%83%AA%E3%83%AB%E7%99%BA%E9%80%B2" title="サーモンラン/特殊な状況/グリル発進" class="rel-wiki-page">グリル発進</a>  <a class="anchor_super" name ="wfe25596"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF&id=wfe25596" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h4>
<div class="includex" style="padding:0;margin:0;"> <a class="anchor_super" id="zd156a9e919fe63f74b2bc418ad27637e" href="#zd156a9e919fe63f74b2bc418ad27637e" title="zd156a9e919fe63f74b2bc418ad27637e"></a></div>
<p><strong><span class="wikicolor" style="color:blue">青↑：誘導ルート</span></strong><br />
<strong><span class="wikicolor" style="color:red">赤↑：誘導すると危険なルート</span></strong><br />
<strong><span class="wikicolor" style="color:yellow; background-color:black">黄★：<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page"><span class="wikicolor" style="color:yellow">グリル</span></a>を攻撃して足止めする位置</span></strong><br />
<strong><span class="wikicolor" style="color:orange; background-color:black">橙●：味方が<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page"><span class="wikicolor" style="color:orange">グリル</span></a>を攻撃する位置</span></strong></p>

<div class="includex" style="padding:0;margin:0;"> <a class="anchor_super" id="zd156a9e919fe63f74b2bc418ad27637e" href="#zd156a9e919fe63f74b2bc418ad27637e" title="zd156a9e919fe63f74b2bc418ad27637e"></a></div>
<div style="text-align:right"><a class="ext" href="/splatoon3mix/?cmd=edit&amp;page=サーモンラン/特殊な状況/グリル発進&amp;id=fdf2c014" title="部分編集:サーモンラン/特殊な状況/グリル発進&amp;id=fdf2c014"  rel="nofollow">[編集]<span class="system-icon ext pukiwiki-open-uri" data-href="/splatoon3mix/?cmd=edit&amp;page=サーモンラン/特殊な状況/グリル発進&amp;id=fdf2c014" data-frame="_blank"></span></a></div>
<p><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%82%B0%E3%83%AA%E3%83%AB%E7%99%BA%E9%80%B2/::ref/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF_%E3%82%B0%E3%83%AA%E3%83%AB%E3%83%AB%E3%83%BC%E3%83%88.png.webp?rev=ea9b050eaf815553b9794067ed631a4f&amp;t=20230920180233" alt="トキシラズいぶし工房_グリルルート.png" title="トキシラズいぶし工房_グリルルート.png" width="720" height="135"  loading="lazy"><br />
誘導場所は主に次の2か所。</p>
<ol class="list1"><li>対岸に向かって右後方の高台で待機し、全方位からやってくる<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>を高台に上がる前にスタンさせる。</li>
<li>対岸に向かって左後方の高台で待機し、後方および右方向からやってくる<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>をコンテナ横でスタンさせる。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>が左方向からやってくる場合は一旦コンテナ後方のスロープに降り、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>がコンテナ付近に到達してから高台に戻りスタンさせる。</li></ol>
<p>ある程度の射程があれば互いのスタン位置に攻撃が届くため、息が合っていれば分散していても対処は可能。</p>
<p>満潮時は出現場所と主戦場までの距離が短く、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>撃破後に次の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>が来るスピードが非常に速いので、素早い対応が求められる高難易度ステージとなる。<br />
納品中でも<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>の駆動音がしたらすぐに高台に退避しよう。でないと轢かれてしまう。</p>
<p>自分が<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>に狙われている時にリフトに乗ると<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>のターゲットを外すことができる。<br />
これを利用して一時的な避難場所としたり、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>処理役がコンテナ付近で<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>を捌き続けるといった戦法が可能。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>をコンテナ付近に近づけたくない場合は、後ろ側の壁に張り付いて左右に往復したり、高台に戻ったり張り付いたりを繰り返すことで時間稼ぎが可能。<br />
ただし満潮時、特にWAVE1時には予めきれいに塗っておかなければならず、張り付きに失敗して溺れるリスクもある。</p>

<h4 id="h4_content_1_7" class="heading-after-first"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%89%E3%82%B9%E3%82%B3%E3%82%A4%E5%A4%A7%E9%87%8F%E7%99%BA%E7%94%9F" title="サーモンラン/特殊な状況/ドスコイ大量発生" class="rel-wiki-page">ドスコイ大量発生</a>  <a class="anchor_super" name ="w4e258f5"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF&id=w4e258f5" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h4>
<div class="includex" style="padding:0;margin:0;"> <a class="anchor_super" id="z09595c432907372020dbec42bf9a12cf" href="#z09595c432907372020dbec42bf9a12cf" title="z09595c432907372020dbec42bf9a12cf"></a></div>
<div style="text-align:right"><a class="ext" href="/splatoon3mix/?cmd=edit&amp;page=サーモンラン/特殊な状況/ドスコイ大量発生&amp;id=ld12c89c" title="部分編集:サーモンラン/特殊な状況/ドスコイ大量発生&amp;id=ld12c89c"  rel="nofollow">[編集]<span class="system-icon ext pukiwiki-open-uri" data-href="/splatoon3mix/?cmd=edit&amp;page=サーモンラン/特殊な状況/ドスコイ大量発生&amp;id=ld12c89c" data-frame="_blank"></span></a></div>
<p>コンテナ後ろの丘の左右両端に1基ずつある。<br />
両砲門とも上陸地点から十分離れ、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%A2%E3%82%B0%E3%83%A9" title="サーモンラン/シャケの種類/モグラ" class="rel-wiki-page">モグラ</a>強襲の心配はまずないものの、対角線になる上陸地点には砲弾が届きにくい。<br />
途中に障害物が多く奥のオオモノが狙いづらい。<br />
ただし前作と比較すると遮蔽物の当たり判定の高さが低くなっている(?)こと、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>のフタ部分に命中してもコンテナを破壊できるようになったことなどから、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>を1回目の射撃時に撃破することが容易になっている。<br />
弾の爆風範囲はかなり広いので、地上の敵相手なら多少ズレても有効打になる。障害物が邪魔で後ろの<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>に攻撃できない、といった場合も落ち着いて障害物の左右から弾を通して爆風攻撃を狙えばきちんと倒すことができる。床撃ちの爆風で<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%A2%E3%83%A1%E3%83%95%E3%83%A9%E3%82%B7" title="ブキ/スペシャルウェポン/アメフラシ" class="rel-wiki-page">アメフラシ</a>弾を撃ち落とすことさえある程度現実的。<span class="wikicolor" style="color:Silver">手前向きのはずの爆風を受けて奥に撃ち返されていくのは相当奇怪な光景だが</span><br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>はわざと遮蔽物に当てて爆風ダメージを入れることも考えよう。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a>は砲台の目の前に立つことがあり、射線を制限されてしまうため、空中分解を狙う優先度が高い。</p>

<h4 id="h4_content_1_8" class="heading-after-first"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1%E6%8E%A2%E3%81%97" title="サーモンラン/特殊な状況/キンシャケ探し" class="rel-wiki-page">キンシャケ探し</a>  <a class="anchor_super" name ="g9e0beff"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF&id=g9e0beff" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h4>
<div class="includex" style="padding:0;margin:0;"> <a class="anchor_super" id="z9e831ca05ca3941d74b4c7a7cf6755a8" href="#z9e831ca05ca3941d74b4c7a7cf6755a8" title="z9e831ca05ca3941d74b4c7a7cf6755a8"></a></div>
<div style="text-align:right"><a class="ext" href="/splatoon3mix/?cmd=edit&amp;page=サーモンラン/特殊な状況/キンシャケ探し&amp;id=zd13316d" title="部分編集:サーモンラン/特殊な状況/キンシャケ探し&amp;id=zd13316d"  rel="nofollow">[編集]<span class="system-icon ext pukiwiki-open-uri" data-href="/splatoon3mix/?cmd=edit&amp;page=サーモンラン/特殊な状況/キンシャケ探し&amp;id=zd13316d" data-frame="_blank"></span></a></div>
<p><strong>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF" title="サーモンラン/ステージ/トキシラズいぶし工房" class="rel-wiki-page">トキシラズいぶし工房</a>　通常時 7箇所</strong><br />
<img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1%E6%8E%A2%E3%81%97/::ref/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E6%B0%B4%E8%84%88%28%E9%80%9A%E5%B8%B8%29.png.webp?rev=9cd8d76aa4a0e1e5024dcf5343d463ef&amp;t=20230920190033" alt="トキシラズ水脈(通常).png" title="トキシラズ水脈(通常).png" width="1024" height="636"  loading="lazy"></p>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/キンシャケ" class="rel-wiki-page">キンシャケ</a>の移動ルート</div>
    <div class="fold-content visible-on-open"><div class="h-scrollable"><table><thead><tr><th>出現したカンケツセン</th><th>逃げこむ可能性のあるカンケツセン</th></tr></thead><tbody><tr><td style="text-align:center;">A</td><td style="text-align:center;">E,G</td></tr><tr><td style="text-align:center;">B</td><td style="text-align:center;">D,E,G</td></tr><tr><td style="text-align:center;">C</td><td style="text-align:center;">D,F</td></tr><tr><td style="text-align:center;">D</td><td rowspan="4" style="text-align:center;">A,B,C</td></tr><tr><td style="text-align:center;">E</td></tr><tr><td style="text-align:center;">F</td></tr><tr><td style="text-align:center;">G</td></tr></tbody></table></div>
</div>
</div>
<ul class="list1"><li>カンケツセンが少なく、他のカンケツセンとのつながりも少ないので(理屈が分かっているなら)当てるのはかなり楽。</li>
<li>覚えやすい(さらに満潮時と共通化可能な)手法は次の通り。まずは<strong>AとC</strong>の2ヶ所を開ける。
<ul class="list2"><li><strong>両方とも大ならBで確定</strong>。</li>
<li>片方が強い場合はそちら側の高台または浜辺。<strong>Aが大ならD・F</strong>、<strong>Cが大ならE・G</strong>。</li></ul></li></ul>
<ul class="list1"><li>最小手数で当てられる手法は次の通り。まずDを開ける。
<ul class="list2"><li>Dが大ならFを開け、Fが大ならA・小ならEに<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/キンシャケ" class="rel-wiki-page">キンシャケ</a>。</li>
<li>Dが小ならGを開け、Gが大ならC・小ならBに<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/キンシャケ" class="rel-wiki-page">キンシャケ</a>。</li>
<li>Eを開けに行く時に、Dを通らないといけないのが弱点。</li>
<li>Gで待機するとDを開けた味方の代わりにE・Gを開けられる。</li></ul></li></ul>
<hr class="full_hr" />
<p><strong>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF" title="サーモンラン/ステージ/トキシラズいぶし工房" class="rel-wiki-page">トキシラズいぶし工房</a>　満潮時 5箇所</strong><br />
<img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1%E6%8E%A2%E3%81%97/::ref/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E6%B0%B4%E8%84%88%28%E6%BA%80%E6%BD%AE%29.png.webp?rev=c6fe0b9dcdb31378a81f865d3d63ced1&amp;t=20230920190040" alt="トキシラズ水脈(満潮).png" title="トキシラズ水脈(満潮).png" width="1024" height="636"  loading="lazy"></p>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/キンシャケ" class="rel-wiki-page">キンシャケ</a>の移動ルート</div>
    <div class="fold-content visible-on-open"><div class="h-scrollable"><table><thead><tr><th>出現したカンケツセン</th><th>逃げこむ可能性のあるカンケツセン</th></tr></thead><tbody><tr><td style="text-align:center;">A</td><td style="text-align:center;">E</td></tr><tr><td style="text-align:center;">B</td><td style="text-align:center;">D,E</td></tr><tr><td style="text-align:center;">C</td><td style="text-align:center;">D</td></tr><tr><td style="text-align:center;">D</td><td rowspan="2" style="text-align:center;">A,B,C</td></tr><tr><td style="text-align:center;">E</td></tr></tbody></table></div>
</div>
</div>
<ul class="list1"><li>通常潮と同じく、まずは<strong>AとC</strong>の2ヶ所を開ける。
<ul class="list2"><li><strong>両方とも大ならBで確定</strong>。</li>
<li>片方だけ大の場合は勢いが強い方の対岸カンケツセンを開けよう。<strong>Aだけ大ならD確定</strong>、<strong>Cだけ大ならE確定</strong>。</li></ul></li>
<li>満潮時には対岸に出た金シャケは必ずコンテナ側まで渡ってくるため、対岸では自分が運ぶ分だけ金イクラを出させれば十分で、コンテナ側で見守っていた人は無理に対岸に渡って攻撃しに行かなくてもよい。コンテナ側で集中砲火すれば回収やイクラ番も楽である。</li></ul>

<h2 id="h2_content_1_9" class="heading-after-first">覚えておくと役立つ事  <a class="anchor_super" name ="a35cfd39"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF&id=a35cfd39" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<ul class="list1"><li>リフトによるターゲット切り<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>のターゲットにされている際にリフトに乗ることでターゲットが強制的に別プレイヤーへ変更される。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%82%B0%E3%83%AA%E3%83%AB%E7%99%BA%E9%80%B2" title="サーモンラン/特殊な状況/グリル発進" class="rel-wiki-page">グリル発進</a>においてリフト側から&#12467;ジャケを処理している最中、不意に自分がターゲットにされてしまった場合に有効(場合によっては崩壊の原因になってしまう)。<br />
また、リフトに乗っている間は<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%80%E3%82%A4%E3%83%90%E3%83%BC" title="サーモンラン/シャケの種類/ダイバー" class="rel-wiki-page">ダイバー</a>のターゲットにされることはない。</li>
<li>金網からリフトへの飛び移り、リフトから金網への飛び移り<br />
インクが尽きて<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>を処理できない状況や、リフトで着岸するとそのまま浮き輪になりそうな状況で有効。
<div class="spacer">&nbsp;</div></li></ul>
<h2 id="h2_content_1_10" class="heading-after-first">コメント <a class="anchor_super" name ="commment"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF&id=commment" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>攻略と統一。</p>
    <iframe id="zawazawa-embed-13fd257c805cef4ff4270df69a9cc11f-12" class="zawazawa-embed" src="https://z.wikiwiki.jp/em/spla3/topic/31?size=10&style=default"
        frameborder="0" scrolling="no" marginheight="0" marginwidth="0"
        style="width:100%; min-width: 100%; max-width: 100%; *width: 100%; min-height: 350px; height: 200px;"
        sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-modals allow-popups allow-popups-to-escape-sandbox allow-forms allow-top-navigation"
    ></iframe>
                </div>
                <div id="main-contents-bottom">
                    <div class="caption-flybox" >
<div id="pc-bottom-parent-ad-container" style="min-height:250px;">
<div id="pc-bottom-left-ad-container">
    <!-- /19033742/WIKIWIKI_PC_BOTTOM_LEFT or /19033742/WIKIWIKI_SP_SECOND -->
    <div id='div-gpt-ad-1567408559923-0' class="hidden-switch-class"></div>
</div>
<div id="pc-bottom-right-ad-container">
    <!-- /19033742/WIKIWIKI_PC_BOTTOM_RIGHT -->
    <div id='div-gpt-ad-1658912377789-0'></div>
</div>
</div>
</div>

<style>
.pc-bottom-ad-default {
    margin-top:120px;
    margin-bottom:20px;
    display:flex;
    justify-content:flex-start;
    gap: 10px 5px;
}
.pc-bottom-ad-center{
    margin-top:120px;
    margin-bottom:20px;
    display:flex;
    justify-content:center;
    flex-wrap:wrap;
    gap: 10px 5px;
}
.pc-bottom-ad-mobile{
    margin-top:20px;
    margin-bottom:20px;
    display:flex;
    align-items: center;
    flex-direction:column;
    position:sticky;
    z-index: 3;
    top:45px;
}
</style>

<script>
(function() {
    var body = document.getElementById('body');
    var co = document.getElementById("pc-bottom-parent-ad-container");
    var fh = 50;
    if (!wi_ismobile && body.clientHeight < 620) {
        co.style.marginTop = '200px';
    }
    if (wi_ismobile && body.clientWidth < 400){
        co.classList.add("pc-bottom-ad-mobile");
    } else if (co.clientWidth < 769) {
        co.classList.add("pc-bottom-ad-center");
    } else {
        co.classList.add("pc-bottom-ad-default");
    }
}());
</script>

<style>
@media (max-width: 430px) {
    body {
        margin-bottom: 100px !important;
    }
}

@keyframes fadeInOverlay {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

#pc-overlay-ad-parent-container {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  width: 100%;
  z-index: 99998;
  background: rgba(0, 0, 0, .5);
  opacity: 0;
  animation: fadeInOverlay 1s ease-in-out 0.5s forwards;
}

.overlay-ad-container {
  display: flex;
  justify-content: center;
}

#pc-overlay-ad-close-button {
    position: absolute;
    top: -21px;
    right: 10px;
    width: 21px;
    height: 21px;
    background: none;
    border: none;
    padding: 0;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    visibility:hidden;
}

#pc-overlay-ad-close-button svg {
    width: 100%;
    height: 100%;
    fill: rgba(0, 0, 0, .5);
}
</style>

<div id="pc-overlay-ad-parent-container" class="hidden-switch-class" style="overflow-anchor: none;">
    <button id="pc-overlay-ad-close-button" onclick="document.getElementById(
        'pc-overlay-ad-parent-container').style.visibility = 'hidden';
            document.getElementById('pc-overlay-ad-close-button').style.visibility = 'hidden'">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512">
        <!--!Font Awesome Pro 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2024 Fonticons, Inc.-->
        <path d="M326.6 166.6L349.3 144 304 98.7l-22.6 22.6L192 210.7l-89.4-89.4L80 98.7 34.7 144l22.6 22.6L146.7 256 57.4 345.4 34.7 368 80 413.3l22.6-22.6L192 301.3l89.4 89.4L304 413.3 349.3 368l-22.6-22.6L237.3 256l89.4-89.4z"/></svg>
    </button>
    <div id="pc-overlay-ad-container-hidden" class="overlay-ad-container">
        <div id="pc-overlay-ad-container">
            <div id='div-gpt-ad-1563441919648-0' class="overlay-ad-wrapper"></div>
        </div>
    </div>
</div>
                </div>

            </div>
        </div>

        
                    <div class="column-left">
                <div id="menubar">
                                        <h2 id="h2_content_1_0" >サイト内検索</h2>
<form action="/splatoon3mix/::cmd/lookup?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%2F%E3%83%96%E3%83%A9%E3%82%B3" method="post">
 <div>
  <input type="hidden" name="inter"  value="サイト内検索(by Google)" />
  <label for="_p_lookup_1">サイト内検索(by Google):</label>
  <input type="text" name="page" id="_p_lookup_1" size="20" value="" />
  <input type="submit" value="検索"/>
 </div>
</form>
<hr class="full_hr" />
<div class="flex-container" style="justify-content: center;">
    <div class="flex-box" style="">
    <div class="flex-box-inner">
        <div class="h-scrollable"><table><tbody><tr><th colspan="2" style="text-align:center; color:white; background-color:#333333;"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B9%E3%83%BC%E3%83%91%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%B3%E3%83%97%E6%99%82%E9%96%93%E7%9F%AD%E7%B8%AE_%E3%83%95%E3%83%81.webp?rev=11b687ecf13512a13ce5a8a42736290e&amp;t=20240306075605" alt="スーパージャンプ時間短縮_フチ.webp" title="スーパージャンプ時間短縮_フチ.webp" width="16" height="16"  loading="lazy"> ショートカット</th></tr><tr><td style="text-align:center; background-color:#f5f5f5;"><a href="#a_battle_mode_online"><strong><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%AC%E3%82%AE%E3%83%A5%E3%83%A9%E3%83%BC%E3%83%9E%E3%83%83%E3%83%81_%E3%83%95%E3%83%81.webp?rev=e571edbd801ab0ac77170b6912e4554d&amp;t=20240306075733" alt="レギュラーマッチ_フチ.webp" title="レギュラーマッチ_フチ.webp" width="16" height="16"  loading="lazy"> オンライン対戦</strong></a></td><td style="text-align:center; background-color:#f5f5f5;"><a href="#a_stage"><strong><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%AB%E3%83%BC%E3%83%AB_%E3%82%AC%E3%83%81%E3%82%A8%E3%83%AA%E3%82%A2_%E3%83%95%E3%83%81.webp?rev=ce0dd192b3e400ad34d5273a131c8771&amp;t=20240306075725" alt="ルール_ガチエリア_フチ.webp" title="ルール_ガチエリア_フチ.webp" width="16" height="16"  loading="lazy"> ステージ</strong></a></td></tr><tr><td style="text-align:center; background-color:#f5f5f5;"><a href="#a_salmon_run"><strong><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3_%E3%83%95%E3%83%81.webp?rev=5e0025880d4bdb3a8ceb64134e867ad2&amp;t=20240306075536" alt="サーモンラン_フチ.webp" title="サーモンラン_フチ.webp" width="16" height="16"  loading="lazy"> サーモンラン</strong></a></td><td style="text-align:center; background-color:#f5f5f5;"><a href="#a_offline_mode"><strong><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AA%E3%82%AF%E3%82%BF%E3%83%AA%E3%82%A2%E3%83%B3_%E3%83%95%E3%83%81.webp?rev=038229cd3377b292e979febcd2c79138&amp;t=20240306075506" alt="オクタリアン_フチ.webp" title="オクタリアン_フチ.webp" width="16" height="16"  loading="lazy"> オフラインモード</strong></a></td></tr><tr><td style="text-align:center; background-color:#f5f5f5;"><a href="#a_weapon"><strong><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%96%E3%82%AD%E3%83%81_%E3%83%95%E3%83%81.webp?rev=5c142d28a0514797b7383944306324bc&amp;t=20240306075706" alt="ブキチ_フチ.webp" title="ブキチ_フチ.webp" width="16" height="16"  loading="lazy"> ブキ</strong></a></td><td style="text-align:center; background-color:#f5f5f5;"><a href="#a_gear"><strong><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AE%E3%82%A2_%E3%83%95%E3%83%81.webp?rev=becb29e73442cb011fc78285d7aab13e&amp;t=20240306075517" alt="ギア_フチ.webp" title="ギア_フチ.webp" width="16" height="16"  loading="lazy"> ギア</strong></a></td></tr><tr><td style="text-align:center; background-color:#f5f5f5;"><a href="#a_event"><strong><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%95%E3%82%A7%E3%82%B9.png.webp?rev=f25948ce192ea0351191ea1fac2dc82c&amp;t=20230804112333" alt="フェス.png" title="フェス.png" width="16" height="16"  loading="lazy"> イベント</strong></a></td><td style="text-align:center; background-color:#f5f5f5;"><a href="#a_gamedata"><strong><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B9%E3%82%BF%E3%83%83%E3%83%95%E3%81%95%E3%82%93_%E3%83%95%E3%83%81.webp?rev=32c6f3464eea352db95bce9f18d0d0a7&amp;t=20240306075545" alt="スタッフさん_フチ.webp" title="スタッフさん_フチ.webp" width="16" height="16"  loading="lazy"> ゲームデータ</strong></a></td></tr><tr><td style="text-align:center; background-color:#f5f5f5;"><a href="#a_others"><strong><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%9F%E3%82%B9%E3%83%86%E3%83%AA%E3%83%BC%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB_%E3%83%95%E3%83%81.webp?rev=ab0ade7b50490be853c261433360b7ac&amp;t=20240306075715" alt="ミステリーファイル_フチ.webp" title="ミステリーファイル_フチ.webp" width="16" height="16"  loading="lazy"> その他</strong></a></td><td style="text-align:center; background-color:#f5f5f5;"><a href="#a_wiki_info"><strong><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3_%E3%83%95%E3%83%81.webp?rev=9629bce342202e344fbfa7610832f366&amp;t=20240306075527" alt="クマサン_フチ.webp" title="クマサン_フチ.webp" width="16" height="16"  loading="lazy"> 当Wikiについて</strong></a></td></tr></tbody></table></div>

    </div>
</div>

</div>
<div style="min-height:105px;border:1px solid #d5d5d5;margin:0.5em 1em;padding:0 1em;text-align:center"><p>本日のおすすめ記事 <img alt="[star]" src="https://cdn.wikiwiki.jp/to/w/common/image/face/star.gif?v=4" /></p>
<div><span class="plugin-randommes" data-page="データ/本日のおすすめ記事" data-mode="daily" data-stack-json="[&quot;\u30c7\u30fc\u30bf\/\u672c\u65e5\u306e\u304a\u3059\u3059\u3081\u8a18\u4e8b&quot;]">&nbsp;</span></div>
</div>
<div style="min-height:67px;border:1px solid #d5d5d5;margin:0.5em 1em;padding:0 1em;text-align:center"><p>本日のおすすめブキ <img alt="[heart]" src="https://cdn.wikiwiki.jp/to/w/common/image/face/heart.png?v=4" /></p>
<div><span class="plugin-randommes" data-page="データ/本日のおすすめブキ" data-mode="daily" data-stack-json="[&quot;\u30c7\u30fc\u30bf\/\u672c\u65e5\u306e\u304a\u3059\u3059\u3081\u30d6\u30ad&quot;]">&nbsp;</span></div>
</div>
<h2 id="h2_content_1_1" class="heading-after-first"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%A4%E3%83%B3%E3%82%AF%E3%83%AA%E3%83%B3%E3%82%B0_%E3%83%95%E3%83%81.webp?rev=fe5057e8f0f273ee1134a186e3b0a073&amp;t=20240306075427" alt="インクリング_フチ.webp" title="インクリング_フチ.webp" width="16" height="16"  loading="lazy"> 基本情報</h2>
<ul class="list1"><li><a href="/splatoon3mix/Splatoon3%E3%81%A8%E3%81%AF" title="Splatoon3とは" class="rel-wiki-page">Splatoon3とは</a></li>
<li><a href="/splatoon3mix/%E5%89%8D%E4%BD%9C%E3%81%A8%E3%81%AE%E7%9B%B8%E9%81%95%E7%82%B9" title="前作との相違点" class="rel-wiki-page">前作との相違点</a></li>
<li><a href="/splatoon3mix/%E8%A3%BD%E5%93%81%E3%83%A9%E3%82%A4%E3%83%B3%E3%83%8A%E3%83%83%E3%83%97" title="製品ラインナップ" class="rel-wiki-page">製品ラインナップ</a></li>
<li><a href="/splatoon3mix/%E3%82%AA%E3%83%B3%E3%83%A9%E3%82%A4%E3%83%B3%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6" title="オンラインサービスについて" class="rel-wiki-page">オンラインサービスについて</a></li>
<li><a href="/splatoon3mix/%E5%88%9D%E3%82%81%E3%81%A6%E3%81%AESplatoon" title="初めてのSplatoon" class="rel-wiki-page">初めてのSplatoon</a></li>
<li><a href="/splatoon3mix/%E6%93%8D%E4%BD%9C%E6%96%B9%E6%B3%95" title="操作方法" class="rel-wiki-page">操作方法</a></li>
<li><a href="/splatoon3mix/%E3%82%A2%E3%83%83%E3%83%97%E3%83%87%E3%83%BC%E3%83%88%E5%B1%A5%E6%AD%B4" title="アップデート履歴" class="rel-wiki-page">アップデート履歴</a>
<ul class="list2"><li><a href="/splatoon3mix/%E3%82%A2%E3%83%83%E3%83%97%E3%83%87%E3%83%BC%E3%83%88%E5%B1%A5%E6%AD%B4/%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3%E3%83%BB%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC%E3%81%94%E3%81%A8%E3%81%AE%E3%82%A2%E3%83%83%E3%83%97%E3%83%87%E3%83%BC%E3%83%88" title="アップデート履歴/ウェポン・ギアパワーごとのアップデート" class="rel-wiki-page">ウェポン・ギアパワー別履歴</a></li>
<li><a href="/splatoon3mix/%E3%82%B7%E3%83%BC%E3%82%BA%E3%83%B3%E3%81%94%E3%81%A8%E3%81%AE%E8%BF%BD%E5%8A%A0%E8%A6%81%E7%B4%A0" title="シーズンごとの追加要素" class="rel-wiki-page">シーズンごとの追加要素</a></li></ul></li>
<li><a href="/splatoon3mix/FAQ" title="FAQ" class="rel-wiki-page">FAQ</a></li>
<li><a href="/splatoon3mix/%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E8%A9%B3%E7%B4%B0%E4%BB%95%E6%A7%98" title="システム詳細仕様" class="rel-wiki-page">システム詳細仕様</a></li></ul>
<p><a class="anchor" name ="a_battle_mode_online"></a></p>
<h2 id="h2_content_1_2" class="heading-after-first">オンラインモード</h2>
<h3 id="h3_content_1_3" class="heading-after-first"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%AC%E3%82%AE%E3%83%A5%E3%83%A9%E3%83%BC%E3%83%9E%E3%83%83%E3%83%81_%E3%83%95%E3%83%81.webp?rev=e571edbd801ab0ac77170b6912e4554d&amp;t=20240306075733" alt="レギュラーマッチ_フチ.webp" title="レギュラーマッチ_フチ.webp" width="16" height="16"  loading="lazy"> オンライン対戦</h3>
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%AA%E3%83%B3%E3%83%A9%E3%82%A4%E3%83%B3%E5%AF%BE%E6%88%A6" title="オンライン対戦" class="rel-wiki-page">概要</a></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%AC%E3%82%AE%E3%83%A5%E3%83%A9%E3%83%BC%E3%83%9E%E3%83%83%E3%83%81" title="レギュラーマッチ" class="rel-wiki-page">レギュラーマッチ</a>
<ul class="list2"><li><a href="/splatoon3mix/%E3%83%8A%E3%83%AF%E3%83%90%E3%83%AA%E3%83%90%E3%83%88%E3%83%AB" title="ナワバリバトル" class="rel-wiki-page">ナワバリバトル</a></li></ul></li>
<li><a href="/splatoon3mix/%E3%83%95%E3%82%A7%E3%82%B9" title="フェス" class="rel-wiki-page">フェスマッチ</a>
<ul class="list2"><li><a href="/splatoon3mix/%E3%83%88%E3%83%AA%E3%82%AB%E3%83%A9%E3%83%90%E3%83%88%E3%83%AB%E6%8C%87%E5%8D%97" title="トリカラバトル指南" class="rel-wiki-page">トリカラバトル</a></li></ul></li>
<li><a href="/splatoon3mix/%E3%83%90%E3%83%B3%E3%82%AB%E3%83%A9%E3%83%9E%E3%83%83%E3%83%81" title="バンカラマッチ" class="rel-wiki-page">バンカラマッチ</a>
<ul class="list2"><li><a href="/splatoon3mix/%E3%82%AC%E3%83%81%E3%82%A8%E3%83%AA%E3%82%A2" title="ガチエリア" class="rel-wiki-page">ガチエリア</a></li>
<li><a href="/splatoon3mix/%E3%82%AC%E3%83%81%E3%83%A4%E3%82%B0%E3%83%A9" title="ガチヤグラ" class="rel-wiki-page">ガチヤグラ</a></li>
<li><a href="/splatoon3mix/%E3%82%AC%E3%83%81%E3%83%9B%E3%82%B3%E3%83%90%E3%83%88%E3%83%AB" title="ガチホコバトル" class="rel-wiki-page">ガチホコバトル</a></li>
<li><a href="/splatoon3mix/%E3%82%AC%E3%83%81%E3%82%A2%E3%82%B5%E3%83%AA" title="ガチアサリ" class="rel-wiki-page">ガチアサリ</a></li></ul></li>
<li><a href="/splatoon3mix/X%E3%83%9E%E3%83%83%E3%83%81" title="Xマッチ" class="rel-wiki-page">Xマッチ</a></li>
<li><a href="/splatoon3mix/%E3%83%97%E3%83%A9%E3%82%A4%E3%83%99%E3%83%BC%E3%83%88%E3%83%9E%E3%83%83%E3%83%81" title="プライベートマッチ" class="rel-wiki-page">プライベートマッチ</a></li>
<li><a href="/splatoon3mix/%E3%83%81%E3%83%A3%E3%83%B3%E3%83%8D%E3%83%AB" title="チャンネル" class="rel-wiki-page">チャンネル</a>
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins>リアルタイムコメントフォーム</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E3%83%81%E3%83%A3%E3%83%B3%E3%83%8D%E3%83%AB/%E3%83%AA%E3%82%A2%E3%83%AB%E3%82%BF%E3%82%A4%E3%83%A0%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%88%E3%83%95%E3%82%A9%E3%83%BC%E3%83%A01" title="チャンネル/リアルタイムコメントフォーム1" class="rel-wiki-page">チャットルーム1</a> / <a href="/splatoon3mix/%E3%83%81%E3%83%A3%E3%83%B3%E3%83%8D%E3%83%AB/%E3%83%AA%E3%82%A2%E3%83%AB%E3%82%BF%E3%82%A4%E3%83%A0%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%88%E3%83%95%E3%82%A9%E3%83%BC%E3%83%A02" title="チャンネル/リアルタイムコメントフォーム2" class="rel-wiki-page">2</a></li></ul>
</div>
</div>
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins>抽選機</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E3%83%81%E3%83%A3%E3%83%B3%E3%83%8D%E3%83%AB/%E6%8A%BD%E9%81%B8%E6%A9%9F" title="チャンネル/抽選機" class="rel-wiki-page">抽選機</a>
<ul class="list2"><li><a href="/splatoon3mix/%E3%83%81%E3%83%A3%E3%83%B3%E3%83%8D%E3%83%AB/%E6%8A%BD%E9%81%B8%E6%A9%9F/%E3%81%8F%E3%81%98%E7%AE%B1" title="チャンネル/抽選機/くじ箱" class="rel-wiki-page">くじ箱</a> / <a href="/splatoon3mix/%E3%83%81%E3%83%A3%E3%83%B3%E3%83%8D%E3%83%AB/%E6%8A%BD%E9%81%B8%E6%A9%9F/%E3%81%8F%E3%81%98%E7%AE%B12" title="チャンネル/抽選機/くじ箱2" class="rel-wiki-page">2</a></li></ul></li></ul>
</div>
</div></li></ul>
<p><a class="anchor" name ="a_stage"></a></p>
<h4 id="h4_content_191_0" ><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%AB%E3%83%BC%E3%83%AB_%E3%82%AC%E3%83%81%E3%82%A8%E3%83%AA%E3%82%A2_%E3%83%95%E3%83%81.webp?rev=ce0dd192b3e400ad34d5273a131c8771&amp;t=20240306075725" alt="ルール_ガチエリア_フチ.webp" title="ルール_ガチエリア_フチ.webp" width="16" height="16"  loading="lazy"><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8" title="ステージ" class="rel-wiki-page">ステージ</a></h4>

<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins>ステージ一覧</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8" title="ステージ" class="rel-wiki-page">概要</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%A6%E3%83%8E%E3%83%8F%E3%83%8A%E5%A4%A7%E6%B8%93%E8%B0%B7" title="ステージ/ユノハナ大渓谷" class="rel-wiki-page">ユノハナ大渓谷</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%B4%E3%83%B3%E3%82%BA%E3%82%A4%E5%9C%B0%E5%8C%BA" title="ステージ/ゴンズイ地区" class="rel-wiki-page">ゴンズイ地区</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%A4%E3%82%AC%E3%83%A9%E5%B8%82%E5%A0%B4" title="ステージ/ヤガラ市場" class="rel-wiki-page">ヤガラ市場</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%9E%E3%83%86%E3%82%AC%E3%82%A4%E6%94%BE%E6%B0%B4%E8%B7%AF" title="ステージ/マテガイ放水路" class="rel-wiki-page">マテガイ放水路</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%8A%E3%83%A1%E3%83%AD%E3%82%A6%E9%87%91%E5%B1%9E" title="ステージ/ナメロウ金属" class="rel-wiki-page">ナメロウ金属</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%9E%E3%82%B5%E3%83%90%E6%B5%B7%E5%B3%A1%E5%A4%A7%E6%A9%8B" title="ステージ/マサバ海峡大橋" class="rel-wiki-page">マサバ海峡大橋</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%AD%E3%83%B3%E3%83%A1%E3%83%80%E3%82%A4%E7%BE%8E%E8%A1%93%E9%A4%A8" title="ステージ/キンメダイ美術館" class="rel-wiki-page">キンメダイ美術館</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%9E%E3%83%92%E3%83%9E%E3%83%92%E3%83%AA%E3%82%BE%E3%83%BC%E3%83%88%EF%BC%86%E3%82%B9%E3%83%91" title="ステージ/マヒマヒリゾート＆スパ" class="rel-wiki-page">マヒマヒリゾート＆スパ</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E6%B5%B7%E5%A5%B3%E7%BE%8E%E8%A1%93%E5%A4%A7%E5%AD%A6" title="ステージ/海女美術大学" class="rel-wiki-page">海女美術大学</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%81%E3%83%A7%E3%82%A6%E3%82%B6%E3%83%A1%E9%80%A0%E8%88%B9" title="ステージ/チョウザメ造船" class="rel-wiki-page">チョウザメ造船</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%B6%E3%83%88%E3%82%A6%E3%83%9E%E3%83%BC%E3%82%B1%E3%83%83%E3%83%88" title="ステージ/ザトウマーケット" class="rel-wiki-page">ザトウマーケット</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%B9%E3%83%A1%E3%83%BC%E3%82%B7%E3%83%BC%E3%83%AF%E3%83%BC%E3%83%AB%E3%83%89" title="ステージ/スメーシーワールド" class="rel-wiki-page">スメーシーワールド</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%AF%E3%82%B5%E3%83%A4%E6%B8%A9%E6%B3%89" title="ステージ/クサヤ温泉" class="rel-wiki-page">クサヤ温泉</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%92%E3%83%A9%E3%83%A1%E3%81%8C%E4%B8%98%E5%9B%A3%E5%9C%B0" title="ステージ/ヒラメが丘団地" class="rel-wiki-page">ヒラメが丘団地</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%8A%E3%83%B3%E3%83%97%E3%83%A9%E3%83%BC%E9%81%BA%E8%B7%A1" title="ステージ/ナンプラー遺跡" class="rel-wiki-page">ナンプラー遺跡</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%9E%E3%83%B3%E3%82%BF%E3%83%9E%E3%83%AA%E3%82%A2%E5%8F%B7" title="ステージ/マンタマリア号" class="rel-wiki-page">マンタマリア号</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%BF%E3%83%A9%E3%83%9D%E3%83%BC%E3%83%88%E3%82%B7%E3%83%A7%E3%83%83%E3%83%94%E3%83%B3%E3%82%B0%E3%83%91%E3%83%BC%E3%82%AF" title="ステージ/タラポートショッピングパーク" class="rel-wiki-page">タラポートショッピングパーク</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%B3%E3%83%B3%E3%83%96%E3%83%88%E3%83%A9%E3%83%83%E3%82%AF" title="ステージ/コンブトラック" class="rel-wiki-page">コンブトラック</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%BF%E3%82%AB%E3%82%A2%E3%82%B7%E7%B5%8C%E6%B8%88%E7%89%B9%E5%8C%BA" title="ステージ/タカアシ経済特区" class="rel-wiki-page">タカアシ経済特区</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%AA%E3%83%92%E3%83%A7%E3%82%A6%E6%B5%B7%E9%81%8B" title="ステージ/オヒョウ海運" class="rel-wiki-page">オヒョウ海運</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%90%E3%82%A4%E3%82%AC%E3%82%A4%E4%BA%AD" title="ステージ/バイガイ亭" class="rel-wiki-page">バイガイ亭</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%8D%E3%82%AE%E3%83%88%E3%83%AD%E7%82%AD%E9%89%B1" title="ステージ/ネギトロ炭鉱" class="rel-wiki-page">ネギトロ炭鉱</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%AB%E3%82%B8%E3%82%AD%E7%A9%BA%E6%B8%AF" title="ステージ/カジキ空港" class="rel-wiki-page">カジキ空港</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%AA%E3%83%A5%E3%82%A6%E3%82%B0%E3%82%A6%E3%82%BF%E3%83%BC%E3%83%9F%E3%83%8A%E3%83%AB" title="ステージ/リュウグウターミナル" class="rel-wiki-page">リュウグウターミナル</a></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%87%E3%82%AB%E3%83%A9%E3%82%A4%E3%83%B3%E9%AB%98%E6%9E%B6%E4%B8%8B" title="ステージ/デカライン高架下" class="rel-wiki-page">デカライン高架下</a>
<div class="spacer">&nbsp;</div></li>
<li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%B0%E3%83%A9%E3%83%B3%E3%83%89%E3%83%90%E3%83%B3%E3%82%AB%E3%83%A9%E3%82%A2%E3%83%AA%E3%83%BC%E3%83%8A" title="ステージ/グランドバンカラアリーナ" class="rel-wiki-page">グランドバンカラアリーナ</a></li></ul>
<hr class="full_hr" />
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E9%9D%A2%E7%A9%8D%E3%81%82%E3%82%8C%E3%81%93%E3%82%8C" title="ステージ/面積あれこれ" class="rel-wiki-page">面積あれこれ</a></li></ul>
</div>
</div>
<h4 id="h4_content_193_0" >対戦指南</h4>

<ul class="list1"><li><a href="/splatoon3mix/%E5%88%9D%E3%82%81%E3%81%A6%E3%81%AESplatoon" title="初めてのSplatoon" class="rel-wiki-page">初めてのSplatoon</a>
<ul class="list2"><li><a href="/splatoon3mix/%E3%82%B8%E3%83%A3%E3%83%83%E3%82%B8%E3%81%8F%E3%82%93%E3%81%AE%E3%82%A2%E3%83%89%E3%83%90%E3%82%A4%E3%82%B9" title="ジャッジくんのアドバイス" class="rel-wiki-page">ジャッジくんのアドバイス</a></li>
<li><a href="/splatoon3mix/%E3%83%97%E3%83%AC%E3%82%A4%E3%83%9E%E3%83%8A%E3%83%BC" title="プレイマナー" class="rel-wiki-page">プレイマナー</a></li></ul></li>
<li><a href="/splatoon3mix/%E5%88%9D%E5%BF%83%E8%80%85%E5%90%91%E3%81%91%E6%8C%87%E5%8D%97" title="初心者向け指南" class="rel-wiki-page">初心者向け指南</a>
<ul class="list2"><li><a href="/splatoon3mix/%E6%88%A6%E9%97%98%E6%8C%87%E5%8D%97%E3%83%BB%E5%9F%BA%E7%A4%8E" title="戦闘指南・基礎" class="rel-wiki-page">戦闘指南・基礎</a></li>
<li><a href="/splatoon3mix/%E3%82%88%E3%81%8F%E3%81%82%E3%82%8B%E5%A4%B1%E6%95%97" title="よくある失敗" class="rel-wiki-page">よくある失敗</a></li></ul></li>
<li><a href="/splatoon3mix/%E4%B8%8A%E7%B4%9A%E8%80%85%E3%81%AB%E3%81%AA%E3%82%8B%E3%81%9F%E3%82%81%E3%81%AB" title="上級者になるために" class="rel-wiki-page">上級者になるために</a>
<ul class="list2"><li><a href="/splatoon3mix/%E3%83%A1%E3%83%B3%E3%82%BF%E3%83%AB%E6%8C%87%E5%8D%97" title="メンタル指南" class="rel-wiki-page">メンタル指南</a></li>
<li><a href="/splatoon3mix/%E5%B0%8F%E3%83%86%E3%82%AF%E3%83%8B%E3%83%83%E3%82%AF" title="小テクニック" class="rel-wiki-page">小テクニック</a></li>
<li><a href="/splatoon3mix/%E3%83%90%E3%83%88%E3%83%AB%E3%83%A1%E3%83%A2%E3%83%AA%E3%83%BC" title="バトルメモリー" class="rel-wiki-page">バトルメモリー</a></li></ul></li></ul>
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins>モード・ルール別指南</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E3%83%8A%E3%83%AF%E3%83%90%E3%83%AA%E3%83%90%E3%83%88%E3%83%AB%E6%8C%87%E5%8D%97" title="ナワバリバトル指南" class="rel-wiki-page">ナワバリバトル</a></li>
<li><a href="/splatoon3mix/%E3%83%88%E3%83%AA%E3%82%AB%E3%83%A9%E3%83%90%E3%83%88%E3%83%AB%E6%8C%87%E5%8D%97" title="トリカラバトル指南" class="rel-wiki-page">トリカラバトル</a></li></ul>
<hr class="full_hr" />
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%90%E3%83%B3%E3%82%AB%E3%83%A9%E3%83%9E%E3%83%83%E3%83%81%E6%8C%87%E5%8D%97" title="バンカラマッチ指南" class="rel-wiki-page">バンカラマッチ全般</a>
<ul class="list2"><li><a href="/splatoon3mix/%E3%83%90%E3%83%B3%E3%82%AB%E3%83%A9%E3%83%9E%E3%83%83%E3%83%81%E6%8C%87%E5%8D%97/%E3%82%AC%E3%83%81%E3%82%A8%E3%83%AA%E3%82%A2%E6%8C%87%E5%8D%97" title="バンカラマッチ指南/ガチエリア指南" class="rel-wiki-page">ガチエリア</a></li>
<li><a href="/splatoon3mix/%E3%83%90%E3%83%B3%E3%82%AB%E3%83%A9%E3%83%9E%E3%83%83%E3%83%81%E6%8C%87%E5%8D%97/%E3%82%AC%E3%83%81%E3%83%A4%E3%82%B0%E3%83%A9%E6%8C%87%E5%8D%97" title="バンカラマッチ指南/ガチヤグラ指南" class="rel-wiki-page">ガチヤグラ</a></li>
<li><a href="/splatoon3mix/%E3%83%90%E3%83%B3%E3%82%AB%E3%83%A9%E3%83%9E%E3%83%83%E3%83%81%E6%8C%87%E5%8D%97/%E3%82%AC%E3%83%81%E3%83%9B%E3%82%B3%E3%83%90%E3%83%88%E3%83%AB%E6%8C%87%E5%8D%97" title="バンカラマッチ指南/ガチホコバトル指南" class="rel-wiki-page">ガチホコバトル</a></li>
<li><a href="/splatoon3mix/%E3%83%90%E3%83%B3%E3%82%AB%E3%83%A9%E3%83%9E%E3%83%83%E3%83%81%E6%8C%87%E5%8D%97/%E3%82%AC%E3%83%81%E3%82%A2%E3%82%B5%E3%83%AA%E6%8C%87%E5%8D%97" title="バンカラマッチ指南/ガチアサリ指南" class="rel-wiki-page">ガチアサリ</a></li></ul></li></ul>
<hr class="full_hr" />
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%A9%E3%83%B3%E3%82%AF%E5%88%A5%E6%98%87%E6%A0%BC%E6%88%A6%E6%8C%87%E5%8D%97" title="ランク別昇格戦指南" class="rel-wiki-page">ランク別昇格戦指南</a>
<ul class="list2"><li><a href="/splatoon3mix/%E3%83%A9%E3%83%B3%E3%82%AF%E5%88%A5%E6%98%87%E6%A0%BC%E6%88%A6%E6%8C%87%E5%8D%97%EF%BD%9EC%E5%B8%AF%E3%81%8B%E3%82%89B%E5%B8%AF%E3%81%B8%E7%B7%A8" title="ランク別昇格戦指南～C帯からB帯へ編" class="rel-wiki-page">C帯からB帯へ編</a></li>
<li><a href="/splatoon3mix/%E3%83%A9%E3%83%B3%E3%82%AF%E5%88%A5%E6%98%87%E6%A0%BC%E6%88%A6%E6%8C%87%E5%8D%97%EF%BD%9EB%E5%B8%AF%E3%81%8B%E3%82%89A%E5%B8%AF%E3%81%B8%E7%B7%A8" title="ランク別昇格戦指南～B帯からA帯へ編" class="rel-wiki-page">B帯からA帯へ編</a></li>
<li><a href="/splatoon3mix/%E3%83%A9%E3%83%B3%E3%82%AF%E5%88%A5%E6%98%87%E6%A0%BC%E6%88%A6%E6%8C%87%E5%8D%97%EF%BD%9EA%E5%B8%AF%E3%81%8B%E3%82%89S%E5%B8%AF%E3%81%B8%E7%B7%A8" title="ランク別昇格戦指南～A帯からS帯へ編" class="rel-wiki-page">A帯からS帯へ編</a></li></ul></li></ul>
</div>
</div>
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins>ブキ別対策</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E5%90%84%E3%83%96%E3%82%AD%E5%AF%BE%E7%AD%961" title="各ブキ対策1" class="rel-wiki-page">シューター・ローラー・チャージャー対策</a></li>
<li><a href="/splatoon3mix/%E5%90%84%E3%83%96%E3%82%AD%E5%AF%BE%E7%AD%962" title="各ブキ対策2" class="rel-wiki-page">他メイン対策</a></li>
<li><a href="/splatoon3mix/%E5%90%84%E3%83%96%E3%82%AD%E5%AF%BE%E7%AD%963" title="各ブキ対策3" class="rel-wiki-page">サブ・スペシャル対策</a></li></ul>
</div>
</div>
<p><a class="anchor" name ="a_salmon_run"></a></p>
<h3 id="h3_content_1_4" class="heading-after-first"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3_%E3%83%95%E3%83%81.webp?rev=5e0025880d4bdb3a8ceb64134e867ad2&amp;t=20240306075536" alt="サーモンラン_フチ.webp" title="サーモンラン_フチ.webp" width="16" height="16"  loading="lazy"> <a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン NEXT WAVE</a></h3>
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">概要</a></li></ul>
<hr class="full_hr" />
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins>ステージ</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8" title="サーモンラン/ステージ" class="rel-wiki-page">ステージ一覧</a></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%A2%E3%83%A9%E3%83%9E%E3%82%AD%E7%A0%A6" title="サーモンラン/ステージ/アラマキ砦" class="rel-wiki-page">アラマキ砦</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%A0%E3%83%8B%E3%83%BB%E3%82%A8%E3%83%BC%E3%83%AB%E6%B5%B7%E6%B4%8B%E7%99%BA%E9%9B%BB%E6%89%80" title="サーモンラン/ステージ/ムニ・エール海洋発電所" class="rel-wiki-page">ムニ・エール海洋発電所</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%B7%E3%82%A7%E3%82%B1%E3%83%8A%E3%83%80%E3%83%A0" title="サーモンラン/ステージ/シェケナダム" class="rel-wiki-page">シェケナダム</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3" title="サーモンラン/ステージ/難破船ドン・ブラコ" class="rel-wiki-page">難破船ドン・ブラコ</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%81%99%E3%81%98%E3%81%93%E3%82%B8%E3%83%A3%E3%83%B3%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E8%B7%A1" title="サーモンラン/ステージ/すじこジャンクション跡" class="rel-wiki-page">すじこジャンクション跡</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF" title="サーモンラン/ステージ/トキシラズいぶし工房" class="rel-wiki-page">トキシラズいぶし工房</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%81%A9%E3%82%93%E3%81%B4%E3%81%93%E9%97%98%E6%8A%80%E5%A0%B4" title="サーモンラン/ステージ/どんぴこ闘技場" class="rel-wiki-page">どんぴこ闘技場</a></li></ul>
</div>
</div>
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins>シャケの種類</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E" title="サーモンラン/シャケの種類" class="rel-wiki-page">シャケについて</a></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>
<ul class="list2"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#chum" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">シャケ</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#cohock" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ドスコイ</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#snatcher" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">タマヒロイ</a></li></ul></li></ul>
<hr class="full_hr" />
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%A2%E3%82%B0%E3%83%A9" title="サーモンラン/シャケの種類/モグラ" class="rel-wiki-page">モグラ</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA" title="サーモンラン/シャケの種類/コウモリ" class="rel-wiki-page">コウモリ</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%80%E3%82%A4%E3%83%90%E3%83%BC" title="サーモンラン/シャケの種類/ダイバー" class="rel-wiki-page">ダイバー</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%82%AD%E3%83%A5%E3%82%A6" title="サーモンラン/シャケの種類/テッキュウ" class="rel-wiki-page">テッキュウ</a></li></ul>
<hr class="full_hr" />
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/キンシャケ" class="rel-wiki-page">キンシャケ</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B3%E3%83%93%E3%83%A4%E3%81%9F%E3%81%A1#mothership" title="サーモンラン/シャケの種類/ハコビヤたち" class="rel-wiki-page">ハコビヤ</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B3%E3%83%93%E3%83%A4%E3%81%9F%E3%81%A1#chinooks" title="サーモンラン/シャケの種類/ハコビヤたち" class="rel-wiki-page">シャケコプター</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%89%E3%83%AD%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ドロシャケ" class="rel-wiki-page">ドロシャケ</a></li></ul>
<hr class="full_hr" />
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%A8%E3%82%B3%E3%83%85%E3%83%8A" title="サーモンラン/シャケの種類/ヨコヅナ" class="rel-wiki-page">ヨコヅナ</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%84" title="サーモンラン/シャケの種類/タツ" class="rel-wiki-page">タツ</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B8%E3%83%A7%E3%83%BC" title="サーモンラン/シャケの種類/ジョー" class="rel-wiki-page">ジョー</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AA%E3%82%AB%E3%82%B7%E3%83%A9%E9%80%A3%E5%90%88" title="サーモンラン/シャケの種類/オカシラ連合" class="rel-wiki-page">オカシラ連合</a></li></ul>
</div>
</div>
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins>特殊な状況</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81" title="サーモンラン/特殊な状況" class="rel-wiki-page">特殊な状況について</a></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E9%9C%A7" title="サーモンラン/特殊な状況/霧" class="rel-wiki-page">霧</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%82%B0%E3%83%AA%E3%83%AB%E7%99%BA%E9%80%B2" title="サーモンラン/特殊な状況/グリル発進" class="rel-wiki-page">グリル発進</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%89%E3%82%B9%E3%82%B3%E3%82%A4%E5%A4%A7%E9%87%8F%E7%99%BA%E7%94%9F" title="サーモンラン/特殊な状況/ドスコイ大量発生" class="rel-wiki-page">ドスコイ大量発生</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1%E6%8E%A2%E3%81%97" title="サーモンラン/特殊な状況/キンシャケ探し" class="rel-wiki-page">キンシャケ探し</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%8F%E3%82%B3%E3%83%93%E3%83%A4%E8%A5%B2%E6%9D%A5" title="サーモンラン/特殊な状況/ハコビヤ襲来" class="rel-wiki-page">ハコビヤ襲来</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%89%E3%83%AD%E3%82%B7%E3%83%A3%E3%82%B1%E5%99%B4%E5%87%BA" title="サーモンラン/特殊な状況/ドロシャケ噴出" class="rel-wiki-page">ドロシャケ噴出</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E5%B7%A8%E5%A4%A7%E3%82%BF%E3%83%84%E3%83%9E%E3%82%AD" title="サーモンラン/特殊な状況/巨大タツマキ" class="rel-wiki-page">巨大タツマキ</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/Extra%20Wave" title="サーモンラン/特殊な状況/Extra Wave" class="rel-wiki-page">Extra Wave</a></li></ul>
</div>
</div>
<hr class="full_hr" />
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E9%96%8B%E5%82%AC%E5%B1%A5%E6%AD%B4" title="サーモンラン/開催履歴" class="rel-wiki-page">開催履歴</a>
<ul class="list2"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%B7%A8%E6%88%90%E8%A9%95%E4%BE%A1" title="サーモンラン/編成評価" class="rel-wiki-page">編成評価</a></li></ul></li>
<li><a href="/splatoon3mix/%E3%83%90%E3%82%A4%E3%83%88%E3%82%B7%E3%83%8A%E3%83%AA%E3%82%AA" title="バイトシナリオ" class="rel-wiki-page">バイトシナリオ</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%90%E3%82%A4%E3%83%88%E5%B0%82%E7%94%A8%E3%83%96%E3%82%AD%E3%81%AE%E8%A3%9C%E6%AD%A3" title="サーモンラン/バイト専用ブキの補正" class="rel-wiki-page">ブキの補正・シャケ達の攻撃力</a></li></ul>
<h4 id="h4_content_199_0" ><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>指南</h4>

<ul class="list1"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E5%88%9D%E3%82%81%E3%81%A6%E3%81%AE%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン/初めてのサーモンラン" class="rel-wiki-page">初めてのサーモンラン</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%E5%88%9D%E5%BF%83%E8%80%85%E5%90%91%E3%81%91" title="サーモンラン/サーモンラン初心者向け" class="rel-wiki-page">初心者向け</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%E6%8C%87%E5%8D%97" title="サーモンラン/サーモンラン指南" class="rel-wiki-page">中級者向け</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B5%E3%83%90%E3%82%A4%E3%83%90%E3%83%AB%E6%8C%87%E5%8D%97" title="サーモンラン/サバイバル指南" class="rel-wiki-page">サバイバル指南</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%E4%B8%8A%E7%B4%9A%E8%80%85%E5%90%91%E3%81%91%E6%8C%87%E5%8D%97" title="サーモンラン/サーモンラン上級者向け指南" class="rel-wiki-page">上級者向け・立ち回り指南</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%E3%83%8F%E3%83%83%E3%82%AF" title="サーモンラン/サーモンランハック" class="rel-wiki-page">上級者向け・テクニック集</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%88%E3%81%8F%E3%81%82%E3%82%8B%E5%A4%B1%E6%95%97" title="サーモンラン/よくある失敗" class="rel-wiki-page">よくある失敗</a></li></ul>
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins>ブキ別指南</ins></span></button>
    <div class="navfold-content"><ul class="list2"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A" title="サーモンラン/ブキ別立ち回り" class="rel-wiki-page">ブキ別立ち回り</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC%E3%83%BB%E3%83%9E%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%90%E3%83%BC%E5%B1%9E" title="サーモンラン/ブキ別立ち回り/シューター・マニューバー属" class="rel-wiki-page">シューター・マニューバー属</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC%E5%B1%9E" title="サーモンラン/ブキ別立ち回り/ブラスター属" class="rel-wiki-page">ブラスター属</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC%E5%B1%9E" title="サーモンラン/ブキ別立ち回り/ローラー属" class="rel-wiki-page">ローラー属</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%83%95%E3%83%87%E5%B1%9E" title="サーモンラン/ブキ別立ち回り/フデ属" class="rel-wiki-page">フデ属</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC%E5%B1%9E" title="サーモンラン/ブキ別立ち回り/チャージャー属" class="rel-wiki-page">チャージャー属</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%82%B9%E3%83%94%E3%83%8A%E3%83%BC%E5%B1%9E" title="サーモンラン/ブキ別立ち回り/スピナー属" class="rel-wiki-page">スピナー属</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%82%B9%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC%E5%B1%9E" title="サーモンラン/ブキ別立ち回り/スロッシャー属" class="rel-wiki-page">スロッシャー属</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%BF%E3%83%BC%E5%B1%9E" title="サーモンラン/ブキ別立ち回り/シェルター属" class="rel-wiki-page">シェルター属</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%82%B9%E3%83%88%E3%83%AA%E3%83%B3%E3%82%AC%E3%83%BC%E5%B1%9E" title="サーモンラン/ブキ別立ち回り/ストリンガー属" class="rel-wiki-page">ストリンガー属</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC%E5%B1%9E" title="サーモンラン/ブキ別立ち回り/ワイパー属" class="rel-wiki-page">ワイパー属</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%82%B5%E3%83%96%E3%83%BB%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%83%BB%E3%82%A4%E3%82%AF%E3%83%A9%E6%8A%95%E3%81%92" title="サーモンラン/ブキ別立ち回り/サブ・スペシャル・イクラ投げ" class="rel-wiki-page">サブ・スペシャル・イクラ投げ</a></li></ul>
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins>レアブ&#12461;個別解説</ins></span></button>
    <div class="navfold-content"><ul class="list3"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%82%B9%E3%83%88%E3%83%AA%E3%83%B3%E3%82%AC%E3%83%BC" title="ブキ/クマサン印のストリンガー" class="rel-wiki-page">クマサン印のストリンガー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC" title="ブキ/クマサン印のブラスター" class="rel-wiki-page">クマサン印のブラスター</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%BF%E3%83%BC" title="ブキ/クマサン印のシェルター" class="rel-wiki-page">クマサン印のシェルター</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC" title="ブキ/クマサン印のワイパー" class="rel-wiki-page">クマサン印のワイパー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%82%B9%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC" title="ブキ/クマサン印のスロッシャー" class="rel-wiki-page">クマサン印のスロッシャー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC" title="ブキ/クマサン印のチャージャー" class="rel-wiki-page">クマサン印のチャージャー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%83%9E%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%90%E3%83%BC" title="ブキ/クマサン印のマニューバー" class="rel-wiki-page">クマサン印のマニューバー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC" title="ブキ/クマサン印のローラー" class="rel-wiki-page">クマサン印のローラー</a></li></ul>
</div>
</div>
</div>
</div>
<p><a class="anchor" name ="a_offline_mode"></a></p>
<h2 id="h2_content_1_5" class="heading-after-first">オフラインモード</h2>
<h3 id="h3_content_1_6" class="heading-after-first"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AA%E3%82%AF%E3%82%BF%E3%83%AA%E3%82%A2%E3%83%B3_%E3%83%95%E3%83%81.webp?rev=038229cd3377b292e979febcd2c79138&amp;t=20240306075506" alt="オクタリアン_フチ.webp" title="オクタリアン_フチ.webp" width="20" height="20"  loading="lazy"> <a href="/splatoon3mix/%E3%83%92%E3%83%BC%E3%83%AD%E3%83%BC%E3%83%A2%E3%83%BC%E3%83%89" title="ヒーローモード" class="rel-wiki-page">ヒーローモード</a></h3>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%92%E3%83%BC%E3%83%AD%E3%83%BC%E3%83%A2%E3%83%BC%E3%83%89" title="ヒーローモード" class="rel-wiki-page">概要</a></li>
<li><a href="/splatoon3mix/%E3%82%AA%E3%82%AF%E3%82%BF%E3%83%AA%E3%82%A2%E3%83%B3" title="オクタリアン" class="rel-wiki-page">オクタリアン</a>
<ul class="list2"><li><a href="/splatoon3mix/%E6%95%B5%E3%82%AD%E3%83%A3%E3%83%A9%E4%B8%80%E8%A6%A7" title="敵キャラ一覧" class="rel-wiki-page">敵キャラ一覧</a></li></ul></li>
<li><a href="/splatoon3mix/%E3%83%92%E3%83%BC%E3%83%AD%E3%83%BC%E3%83%A2%E3%83%BC%E3%83%89/%E3%83%A4%E3%82%AB%E3%83%B3%E4%B8%80%E8%A6%A7" title="ヒーローモード/ヤカン一覧" class="rel-wiki-page">ヤカン一覧</a>
<ul class="list2"><li><a href="/splatoon3mix/%E3%83%92%E3%83%BC%E3%83%AD%E3%83%BC%E3%83%A2%E3%83%BC%E3%83%89/%E9%9B%A3%E9%96%A2%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%E6%94%BB%E7%95%A5" title="ヒーローモード/難関ステージ攻略" class="rel-wiki-page">難関ステージ攻略</a></li></ul></li>
<li><a href="/splatoon3mix/%E3%83%92%E3%83%BC%E3%83%AD%E3%83%BC%E3%83%A2%E3%83%BC%E3%83%89/%E3%82%AA%E3%83%AB%E3%82%BF%E3%83%8A%E3%83%AD%E3%82%B0%E4%B8%80%E8%A6%A7" title="ヒーローモード/オルタナログ一覧" class="rel-wiki-page">オルタナログ一覧</a></li>
<li><a href="/splatoon3mix/%E3%83%92%E3%83%BC%E3%83%AD%E3%83%BC%E3%83%A2%E3%83%BC%E3%83%89/%E3%83%9F%E3%82%B9%E3%83%86%E3%83%AA%E3%83%BC%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%83%BC%E8%A6%A7" title="ヒーローモード/ミステリーファイルー覧" class="rel-wiki-page">ミステリーファイル一覧</a></li></ul>
<h3 id="h3_content_1_7" class="heading-after-first"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%92%E3%83%A1%E3%83%89%E3%83%AD%E3%83%BC%E3%83%B3%28%E3%83%90%E3%83%83%E3%82%B8%29_%E3%83%95%E3%83%81.webp?rev=5403d6d76ff2a440ac6113d1b852d08e&amp;t=20240306075633" alt="ヒメドローン(バッジ)_フチ.webp" title="ヒメドローン(バッジ)_フチ.webp" width="20" height="20"  loading="lazy"> <a href="/splatoon3mix/%E3%82%B5%E3%82%A4%E3%83%89%E3%83%BB%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC" title="サイド・オーダー" class="rel-wiki-page">サイド・オーダー</a></h3>
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%B5%E3%82%A4%E3%83%89%E3%83%BB%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC" title="サイド・オーダー" class="rel-wiki-page">概要</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%82%A4%E3%83%89%E3%83%BB%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC/%E3%83%91%E3%83%AC%E3%83%83%E3%83%88" title="サイド・オーダー/パレット" class="rel-wiki-page">パレット</a>
<ul class="list2"><li><a href="/splatoon3mix/%E3%82%B5%E3%82%A4%E3%83%89%E3%83%BB%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC/%E3%82%AB%E3%83%A9%E3%83%BC%E3%83%81%E3%83%83%E3%83%97" title="サイド・オーダー/カラーチップ" class="rel-wiki-page">カラーチップ</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%82%A4%E3%83%89%E3%83%BB%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC/%E5%90%84%E7%A8%AE%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="サイド・オーダー/各種ウェポン" class="rel-wiki-page">各種ウェポン</a></li></ul></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%82%A4%E3%83%89%E3%83%BB%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC/%E3%83%8F%E3%83%83%E3%82%AD%E3%83%B3%E3%82%B0" title="サイド・オーダー/ハッキング" class="rel-wiki-page">ハッキング</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%82%A4%E3%83%89%E3%83%BB%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC/%E6%95%B5%E3%82%AD%E3%83%A3%E3%83%A9%E4%B8%80%E8%A6%A7" title="サイド・オーダー/敵キャラ一覧" class="rel-wiki-page">敵キャラ一覧</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%82%A4%E3%83%89%E3%83%BB%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC/%E3%83%95%E3%83%AD%E3%82%A2%E4%B8%80%E8%A6%A7" title="サイド・オーダー/フロア一覧" class="rel-wiki-page">フロア一覧</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%82%A4%E3%83%89%E3%83%BB%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC/%E3%83%91%E3%83%AC%E3%83%83%E3%83%88%E3%81%AE%E3%83%A1%E3%83%A2%E4%B8%80%E8%A6%A7" title="サイド・オーダー/パレットのメモ一覧" class="rel-wiki-page">パレットのメモ一覧</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%82%A4%E3%83%89%E3%83%BB%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC/%E3%82%A4%E3%82%A4%E3%83%80%E3%81%AE%E9%96%8B%E7%99%BA%E6%97%A5%E8%A8%98%E4%B8%80%E8%A6%A7" title="サイド・オーダー/イイダの開発日記一覧" class="rel-wiki-page">イイダの開発日記一覧</a></li></ul>
<h3 id="h3_content_1_8" class="heading-after-first"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%8A%E3%83%AF%E3%83%90%E3%83%88%E3%83%A9%E3%83%BC_%E3%83%95%E3%83%81.webp?rev=6ce502f7850901b86898b0f7d9cc8eb0&amp;t=20240306075614" alt="ナワバトラー_フチ.webp" title="ナワバトラー_フチ.webp" width="16" height="16"  loading="lazy"> <a href="/splatoon3mix/%E9%99%A3%E5%8F%96%E5%A4%A7%E6%88%A6%E3%83%8A%E3%83%AF%E3%83%90%E3%83%88%E3%83%A9%E3%83%BC" title="陣取大戦ナワバトラー" class="rel-wiki-page">陣取大戦ナワバトラー</a></h3>
<ul class="list1"><li><a href="/splatoon3mix/%E9%99%A3%E5%8F%96%E5%A4%A7%E6%88%A6%E3%83%8A%E3%83%AF%E3%83%90%E3%83%88%E3%83%A9%E3%83%BC" title="陣取大戦ナワバトラー" class="rel-wiki-page">概要</a></li>
<li><a href="/splatoon3mix/%E9%99%A3%E5%8F%96%E5%A4%A7%E6%88%A6%E3%83%8A%E3%83%AF%E3%83%90%E3%83%88%E3%83%A9%E3%83%BC/%E3%82%AB%E3%83%BC%E3%83%89%E4%B8%80%E8%A6%A7" title="陣取大戦ナワバトラー/カード一覧" class="rel-wiki-page">カード一覧</a></li>
<li><a href="/splatoon3mix/%E9%99%A3%E5%8F%96%E5%A4%A7%E6%88%A6%E3%83%8A%E3%83%AF%E3%83%90%E3%83%88%E3%83%A9%E3%83%BC/%E5%AF%BE%E6%88%A6%E7%9B%B8%E6%89%8B" title="陣取大戦ナワバトラー/対戦相手" class="rel-wiki-page">対戦相手</a></li></ul>
<h3 id="h3_content_1_9" class="heading-after-first">その他</h3>
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%A4%E3%82%AB%E3%83%83%E3%83%81%E3%83%A3" title="イカッチャ" class="rel-wiki-page">イカッチャ</a></li>
<li><a href="/splatoon3mix/%E6%92%AE%E5%BD%B1%E3%83%BB%E3%83%95%E3%82%A9%E3%83%88%E3%82%A2%E3%83%AB%E3%83%90%E3%83%A0" title="撮影・フォトアルバム" class="rel-wiki-page">撮影・フォトアルバム</a></li>
<li><a href="/splatoon3mix/amiibo" title="amiibo" class="rel-wiki-page">amiibo</a></li></ul>
<p><a class="anchor" name ="a_weapon"></a></p>
<h2 id="h2_content_1_10" class="heading-after-first"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%96%E3%82%AD%E3%83%81_%E3%83%95%E3%83%81.webp?rev=5c142d28a0514797b7383944306324bc&amp;t=20240306075706" alt="ブキチ_フチ.webp" title="ブキチ_フチ.webp" width="20" height="20"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD" title="ブキ" class="rel-wiki-page"><span class="wikicolor" style="color:white">ブキ</span></a></h2>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD" title="ブキ" class="rel-wiki-page">概要</a>
<ul class="list2"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%96%E3%82%AD%E6%80%A7%E8%83%BD" title="ブキ/ブキ性能" class="rel-wiki-page">ブキ性能</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E6%AF%94%E8%BC%83" title="ブキ/比較" class="rel-wiki-page">比較</a></li></ul></li></ul>
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC_%E3%83%95%E3%83%81.png.webp?rev=63e120a039050700802c2a596889b45b&amp;t=20230119180047" alt="シューター_フチ.png" title="シューター_フチ.png" width="15" height="15"  loading="lazy">シュータ&#12540;</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC%E5%B1%9E" title="ブキ/シューター属" class="rel-wiki-page">シューター属</a></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%9C%E3%83%BC%E3%83%AB%E3%83%89%E3%83%9E%E3%83%BC%E3%82%AB%E3%83%BC" title="ブキ/ボールドマーカー" class="rel-wiki-page">ボールドマーカー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%9C%E3%83%BC%E3%83%AB%E3%83%89%E3%83%9E%E3%83%BC%E3%82%AB%E3%83%BC%E3%83%8D%E3%82%AA" title="ブキ/ボールドマーカーネオ" class="rel-wiki-page">ネオ</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%8F%E3%81%8B%E3%81%B0%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC" title="ブキ/わかばシューター" class="rel-wiki-page">わかばシューター</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%82%E3%81%BF%E3%81%98%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC" title="ブキ/もみじシューター" class="rel-wiki-page">もみじ</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B7%E3%83%A3%E3%83%BC%E3%83%97%E3%83%9E%E3%83%BC%E3%82%AB%E3%83%BC" title="ブキ/シャープマーカー" class="rel-wiki-page">シャープマーカー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B7%E3%83%A3%E3%83%BC%E3%83%97%E3%83%9E%E3%83%BC%E3%82%AB%E3%83%BC%E3%83%8D%E3%82%AA" title="ブキ/シャープマーカーネオ" class="rel-wiki-page">ネオ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B7%E3%83%A3%E3%83%BC%E3%83%97%E3%83%9E%E3%83%BC%E3%82%AB%E3%83%BCGECK" title="ブキ/シャープマーカーGECK" class="rel-wiki-page">GECK</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%97%E3%83%AD%E3%83%A2%E3%83%87%E3%83%A9%E3%83%BCMG" title="ブキ/プロモデラーMG" class="rel-wiki-page">プロモデラーMG</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%97%E3%83%AD%E3%83%A2%E3%83%87%E3%83%A9%E3%83%BCRG" title="ブキ/プロモデラーRG" class="rel-wiki-page">RG</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%97%E3%83%AD%E3%83%A2%E3%83%87%E3%83%A9%E3%83%BC%E5%BD%A9" title="ブキ/プロモデラー彩" class="rel-wiki-page">彩</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC" title="ブキ/スプラシューター" class="rel-wiki-page">スプラシューター</a> /  <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC%E3%82%B3%E3%83%A9%E3%83%9C" title="ブキ/スプラシューターコラボ" class="rel-wiki-page">コラボ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC%E7%85%8C" title="ブキ/スプラシューター煌" class="rel-wiki-page">煌</a><br class="spacer">　　<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%92%E3%83%BC%E3%83%AD%E3%83%BC%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC%20%E3%83%AC%E3%83%97%E3%83%AA%E3%82%AB" title="ブキ/ヒーローシューター レプリカ" class="rel-wiki-page">ヒーロー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AA%E3%82%AF%E3%82%BF%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC%20%E3%83%AC%E3%83%97%E3%83%AA%E3%82%AB" title="ブキ/オクタシューター レプリカ" class="rel-wiki-page">オクタ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC%20%E3%83%AC%E3%83%97%E3%83%AA%E3%82%AB" title="ブキ/オーダーシューター レプリカ" class="rel-wiki-page">オーダー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/.52%E3%82%AC%E3%83%AD%E3%83%B3" title="ブキ/.52ガロン" class="rel-wiki-page">.52ガロン</a>/<a href="/splatoon3mix/%E3%83%96%E3%82%AD/.52%E3%82%AC%E3%83%AD%E3%83%B3%E3%83%87%E3%82%B3" title="ブキ/.52ガロンデコ" class="rel-wiki-page">デコ</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/N-ZAP85" title="ブキ/N-ZAP85" class="rel-wiki-page">N-ZAP85</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/N-ZAP89" title="ブキ/N-ZAP89" class="rel-wiki-page">89</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%97%E3%83%A9%E3%82%A4%E3%83%A0%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC" title="ブキ/プライムシューター" class="rel-wiki-page">プライムシューター</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%97%E3%83%A9%E3%82%A4%E3%83%A0%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC%E3%82%B3%E3%83%A9%E3%83%9C" title="ブキ/プライムシューターコラボ" class="rel-wiki-page">コラボ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%97%E3%83%A9%E3%82%A4%E3%83%A0%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BCFRZN" title="ブキ/プライムシューターFRZN" class="rel-wiki-page">FRZN</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/.96%E3%82%AC%E3%83%AD%E3%83%B3" title="ブキ/.96ガロン" class="rel-wiki-page">.96ガロン</a> /  <a href="/splatoon3mix/%E3%83%96%E3%82%AD/.96%E3%82%AC%E3%83%AD%E3%83%B3%E3%83%87%E3%82%B3" title="ブキ/.96ガロンデコ" class="rel-wiki-page">デコ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/.96%E3%82%AC%E3%83%AD%E3%83%B3%E7%88%AA" title="ブキ/.96ガロン爪" class="rel-wiki-page">爪</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88%E3%82%B9%E3%82%A4%E3%83%BC%E3%83%91%E3%83%BC" title="ブキ/ジェットスイーパー" class="rel-wiki-page">ジェットスイーパー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88%E3%82%B9%E3%82%A4%E3%83%BC%E3%83%91%E3%83%BC%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%A0" title="ブキ/ジェットスイーパーカスタム" class="rel-wiki-page">カスタム</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88%E3%82%B9%E3%82%A4%E3%83%BC%E3%83%91%E3%83%BCCOBR" title="ブキ/ジェットスイーパーCOBR" class="rel-wiki-page">COBR</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%83%BC%E3%82%B9%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC" title="ブキ/スペースシューター" class="rel-wiki-page">スペースシューター</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%83%BC%E3%82%B9%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC%E3%82%B3%E3%83%A9%E3%83%9C" title="ブキ/スペースシューターコラボ" class="rel-wiki-page">コラボ</a></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/L3%E3%83%AA%E3%83%BC%E3%83%AB%E3%82%AC%E3%83%B3" title="ブキ/L3リールガン" class="rel-wiki-page">L3リールガン</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/L3%E3%83%AA%E3%83%BC%E3%83%AB%E3%82%AC%E3%83%B3D" title="ブキ/L3リールガンD" class="rel-wiki-page">D</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/L3%E3%83%AA%E3%83%BC%E3%83%AB%E3%82%AC%E3%83%B3%E7%AE%94" title="ブキ/L3リールガン箔" class="rel-wiki-page">箔</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/H3%E3%83%AA%E3%83%BC%E3%83%AB%E3%82%AC%E3%83%B3" title="ブキ/H3リールガン" class="rel-wiki-page">H3リールガン</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/H3%E3%83%AA%E3%83%BC%E3%83%AB%E3%82%AC%E3%83%B3D" title="ブキ/H3リールガンD" class="rel-wiki-page">D</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/H3%E3%83%AA%E3%83%BC%E3%83%AB%E3%82%AC%E3%83%B3SNAK" title="ブキ/H3リールガンSNAK" class="rel-wiki-page">SNAK</a></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%9C%E3%83%88%E3%83%AB%E3%82%AC%E3%82%A4%E3%82%B6%E3%83%BC" title="ブキ/ボトルガイザー" class="rel-wiki-page">ボトルガイザー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%9C%E3%83%88%E3%83%AB%E3%82%AC%E3%82%A4%E3%82%B6%E3%83%BC%E3%83%95%E3%82%A9%E3%82%A4%E3%83%AB" title="ブキ/ボトルガイザーフォイル" class="rel-wiki-page">フォイル</a></li></ul>
</div>
</div>
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC_%E3%83%95%E3%83%81.png.webp?rev=b269f5bddc65f747cecb8475261c73a3&amp;t=20230119180112" alt="ローラー_フチ.png" title="ローラー_フチ.png" width="15" height="15"  loading="lazy">ローラ&#12540;</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC%E5%B1%9E" title="ブキ/ローラー属" class="rel-wiki-page">ローラー属</a></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AB%E3%83%BC%E3%83%9C%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC" title="ブキ/カーボンローラー" class="rel-wiki-page">カーボンローラー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AB%E3%83%BC%E3%83%9C%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC%E3%83%87%E3%82%B3" title="ブキ/カーボンローラーデコ" class="rel-wiki-page">デコ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AB%E3%83%BC%E3%83%9C%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BCANGL" title="ブキ/カーボンローラーANGL" class="rel-wiki-page">ANGL</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC" title="ブキ/スプラローラー" class="rel-wiki-page">スプラローラー</a> /  <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC%E3%82%B3%E3%83%A9%E3%83%9C" title="ブキ/スプラローラーコラボ" class="rel-wiki-page">コラボ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC%20%E3%83%AC%E3%83%97%E3%83%AA%E3%82%AB" title="ブキ/オーダーローラー レプリカ" class="rel-wiki-page">オーダー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%80%E3%82%A4%E3%83%8A%E3%83%A2%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC" title="ブキ/ダイナモローラー" class="rel-wiki-page">ダイナモローラー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%80%E3%82%A4%E3%83%8A%E3%83%A2%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC%E3%83%86%E3%82%B9%E3%83%A9" title="ブキ/ダイナモローラーテスラ" class="rel-wiki-page">テスラ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%80%E3%82%A4%E3%83%8A%E3%83%A2%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC%E5%86%A5" title="ブキ/ダイナモローラー冥" class="rel-wiki-page">冥</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%B4%E3%82%A1%E3%83%AA%E3%82%A2%E3%83%96%E3%83%AB%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC" title="ブキ/ヴァリアブルローラー" class="rel-wiki-page">ヴァリアブルローラー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%B4%E3%82%A1%E3%83%AA%E3%82%A2%E3%83%96%E3%83%AB%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC%E3%83%95%E3%82%A9%E3%82%A4%E3%83%AB" title="ブキ/ヴァリアブルローラーフォイル" class="rel-wiki-page">フォイル</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%AF%E3%82%A4%E3%83%89%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC" title="ブキ/ワイドローラー" class="rel-wiki-page">ワイドローラー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%AF%E3%82%A4%E3%83%89%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC%E3%82%B3%E3%83%A9%E3%83%9C" title="ブキ/ワイドローラーコラボ" class="rel-wiki-page">コラボ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%AF%E3%82%A4%E3%83%89%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC%E6%83%91" title="ブキ/ワイドローラー惑" class="rel-wiki-page">惑</a></li></ul>
</div>
</div>
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC_%E3%83%95%E3%83%81.png?rev=e07a09c76973bc647c928ea0a3a475ee&amp;t=20230119180100" alt="チャージャー_フチ.png" title="チャージャー_フチ.png" width="15" height="15"  loading="lazy">チャージャ&#12540;</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC%E5%B1%9E" title="ブキ/チャージャー属" class="rel-wiki-page">チャージャー属</a></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%82%AF%E3%82%A4%E3%83%83%E3%82%AF%E3%83%AA%E3%83%B3%CE%B1" title="ブキ/スクイックリンα" class="rel-wiki-page">スクイックリンα</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%82%AF%E3%82%A4%E3%83%83%E3%82%AF%E3%83%AA%E3%83%B3%CE%B2" title="ブキ/スクイックリンβ" class="rel-wiki-page">β</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC" title="ブキ/スプラチャージャー" class="rel-wiki-page">スプラチャージャー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC%E3%82%B3%E3%83%A9%E3%83%9C" title="ブキ/スプラチャージャーコラボ" class="rel-wiki-page">コラボ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BCFRST" title="ブキ/スプラチャージャーFRST" class="rel-wiki-page">FRST</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC%20%E3%83%AC%E3%83%97%E3%83%AA%E3%82%AB" title="ブキ/オーダーチャージャー レプリカ" class="rel-wiki-page">オーダー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%97" title="ブキ/スプラスコープ" class="rel-wiki-page">スプラスコープ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%97%E3%82%B3%E3%83%A9%E3%83%9C" title="ブキ/スプラスコープコラボ" class="rel-wiki-page">コラボ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%97FRST" title="ブキ/スプラスコープFRST" class="rel-wiki-page">FRST</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%AA%E3%83%83%E3%82%BF%E3%83%BC4K" title="ブキ/リッター4K" class="rel-wiki-page">リッター4K</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%AA%E3%83%83%E3%82%BF%E3%83%BC4K%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%A0" title="ブキ/リッター4Kカスタム" class="rel-wiki-page">カスタム</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/4K%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%97" title="ブキ/4Kスコープ" class="rel-wiki-page">4Kスコープ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/4K%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%97%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%A0" title="ブキ/4Kスコープカスタム" class="rel-wiki-page">カスタム</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/14%E5%BC%8F%E7%AB%B9%E7%AD%92%E9%8A%83%E3%83%BB%E7%94%B2" title="ブキ/14式竹筒銃・甲" class="rel-wiki-page">14式竹筒銃・甲</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/14%E5%BC%8F%E7%AB%B9%E7%AD%92%E9%8A%83%E3%83%BB%E4%B9%99" title="ブキ/14式竹筒銃・乙" class="rel-wiki-page">乙</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%BD%E3%82%A4%E3%83%81%E3%83%A5%E3%83%BC%E3%83%90%E3%83%BC" title="ブキ/ソイチューバー" class="rel-wiki-page">ソイチューバー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%BD%E3%82%A4%E3%83%81%E3%83%A5%E3%83%BC%E3%83%90%E3%83%BC%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%A0" title="ブキ/ソイチューバーカスタム" class="rel-wiki-page">カスタム</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/R-PEN%EF%BC%8F5H" title="ブキ/R-PEN／5H" class="rel-wiki-page">R-PEN/5H</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/R-PEN%EF%BC%8F5B" title="ブキ/R-PEN／5B" class="rel-wiki-page">5B</a></li></ul>
</div>
</div>
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B9%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC_%E3%83%95%E3%83%81.png.webp?rev=4403304ed3d9baaf9a8f8f850d2708cf&amp;t=20230119180056" alt="スロッシャー_フチ.png" title="スロッシャー_フチ.png" width="15" height="15"  loading="lazy">スロッシャ&#12540;</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC%E5%B1%9E" title="ブキ/スロッシャー属" class="rel-wiki-page">スロッシャー属</a></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%90%E3%82%B1%E3%83%83%E3%83%88%E3%82%B9%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC" title="ブキ/バケットスロッシャー" class="rel-wiki-page">バケットスロッシャー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%90%E3%82%B1%E3%83%83%E3%83%88%E3%82%B9%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC%E3%83%87%E3%82%B3" title="ブキ/バケットスロッシャーデコ" class="rel-wiki-page">デコ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC%E3%82%B9%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC%20%E3%83%AC%E3%83%97%E3%83%AA%E3%82%AB" title="ブキ/オーダースロッシャー レプリカ" class="rel-wiki-page">オーダー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%92%E3%83%83%E3%82%BB%E3%83%B3" title="ブキ/ヒッセン" class="rel-wiki-page">ヒッセン</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%92%E3%83%83%E3%82%BB%E3%83%B3%E3%83%BB%E3%83%92%E3%83%A5%E3%83%BC" title="ブキ/ヒッセン・ヒュー" class="rel-wiki-page">ヒュー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%92%E3%83%83%E3%82%BB%E3%83%B3ASH" title="ブキ/ヒッセンASH" class="rel-wiki-page">ASH</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%A5%E3%83%BC%E3%82%B9%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC" title="ブキ/スクリュースロッシャー" class="rel-wiki-page">スクリュースロッシャー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%A5%E3%83%BC%E3%82%B9%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC%E3%83%8D%E3%82%AA" title="ブキ/スクリュースロッシャーネオ" class="rel-wiki-page">ネオ</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AA%E3%83%BC%E3%83%90%E3%83%BC%E3%83%95%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC" title="ブキ/オーバーフロッシャー" class="rel-wiki-page">オーバーフロッシャー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AA%E3%83%BC%E3%83%90%E3%83%BC%E3%83%95%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC%E3%83%87%E3%82%B3" title="ブキ/オーバーフロッシャーデコ" class="rel-wiki-page">デコ</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%A8%E3%82%AF%E3%82%B9%E3%83%97%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC" title="ブキ/エクスプロッシャー" class="rel-wiki-page">エクスプロッシャー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%A8%E3%82%AF%E3%82%B9%E3%83%97%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%A0" title="ブキ/エクスプロッシャーカスタム" class="rel-wiki-page">カスタム</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%A2%E3%83%83%E3%83%97%E3%83%AA%E3%83%B3" title="ブキ/モップリン" class="rel-wiki-page">モップリン</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%A2%E3%83%83%E3%83%97%E3%83%AA%E3%83%B3D" title="ブキ/モップリンD" class="rel-wiki-page">D</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%A2%E3%83%83%E3%83%97%E3%83%AA%E3%83%B3%E8%A7%92" title="ブキ/モップリン角" class="rel-wiki-page">角</a></li></ul>
</div>
</div>
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B9%E3%83%94%E3%83%8A%E3%83%BC_%E3%83%95%E3%83%81.png.webp?rev=8a1baa079887e97058720b09634b4094&amp;t=20230119180053" alt="スピナー_フチ.png" title="スピナー_フチ.png" width="15" height="15"  loading="lazy">スピナ&#12540;</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%94%E3%83%8A%E3%83%BC%E5%B1%9E" title="ブキ/スピナー属" class="rel-wiki-page">スピナー属</a></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%82%B9%E3%83%94%E3%83%8A%E3%83%BC" title="ブキ/スプラスピナー" class="rel-wiki-page">スプラスピナー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%82%B9%E3%83%94%E3%83%8A%E3%83%BC%E3%82%B3%E3%83%A9%E3%83%9C" title="ブキ/スプラスピナーコラボ" class="rel-wiki-page">コラボ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%82%B9%E3%83%94%E3%83%8A%E3%83%BCPYTN" title="ブキ/スプラスピナーPYTN" class="rel-wiki-page">PYTN</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%90%E3%83%AC%E3%83%AB%E3%82%B9%E3%83%94%E3%83%8A%E3%83%BC" title="ブキ/バレルスピナー" class="rel-wiki-page">バレルスピナー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%90%E3%83%AC%E3%83%AB%E3%82%B9%E3%83%94%E3%83%8A%E3%83%BC%E3%83%87%E3%82%B3" title="ブキ/バレルスピナーデコ" class="rel-wiki-page">デコ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC%E3%82%B9%E3%83%94%E3%83%8A%E3%83%BC%20%E3%83%AC%E3%83%97%E3%83%AA%E3%82%AB" title="ブキ/オーダースピナー レプリカ" class="rel-wiki-page">オーダー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%8F%E3%82%A4%E3%83%89%E3%83%A9%E3%83%B3%E3%83%88" title="ブキ/ハイドラント" class="rel-wiki-page">ハイドラント</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%8F%E3%82%A4%E3%83%89%E3%83%A9%E3%83%B3%E3%83%88%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%A0" title="ブキ/ハイドラントカスタム" class="rel-wiki-page">カスタム</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%8F%E3%82%A4%E3%83%89%E3%83%A9%E3%83%B3%E3%83%88%E5%9C%A7" title="ブキ/ハイドラント圧" class="rel-wiki-page">圧</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%BC%E3%82%B2%E3%83%AB%E3%82%B7%E3%83%A5%E3%83%A9%E3%82%A4%E3%83%90%E3%83%BC" title="ブキ/クーゲルシュライバー" class="rel-wiki-page">クーゲルシュライバー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%BC%E3%82%B2%E3%83%AB%E3%82%B7%E3%83%A5%E3%83%A9%E3%82%A4%E3%83%90%E3%83%BC%E3%83%BB%E3%83%92%E3%83%A5%E3%83%BC" title="ブキ/クーゲルシュライバー・ヒュー" class="rel-wiki-page">ヒュー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%8E%E3%83%BC%E3%83%81%E3%83%A9%E3%82%B947" title="ブキ/ノーチラス47" class="rel-wiki-page">ノーチラス47</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%8E%E3%83%BC%E3%83%81%E3%83%A9%E3%82%B979" title="ブキ/ノーチラス79" class="rel-wiki-page">79</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%A4%E3%82%B0%E3%82%B6%E3%83%9F%E3%83%8A%E3%83%BC" title="ブキ/イグザミナー" class="rel-wiki-page">イグザミナー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%A4%E3%82%B0%E3%82%B6%E3%83%9F%E3%83%8A%E3%83%BC%E3%83%BB%E3%83%92%E3%83%A5%E3%83%BC" title="ブキ/イグザミナー・ヒュー" class="rel-wiki-page">ヒュー</a></li></ul>
</div>
</div>
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%9E%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%90%E3%83%BC_%E3%83%95%E3%83%81.png.webp?rev=7e38bfc9d55b8f00cbf4120c5d77f342&amp;t=20230119180110" alt="マニューバー_フチ.png" title="マニューバー_フチ.png" width="15" height="15"  loading="lazy">マニューバ&#12540;</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%9E%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%90%E3%83%BC%E5%B1%9E" title="ブキ/マニューバー属" class="rel-wiki-page">マニューバー属</a></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%91%E3%83%83%E3%82%BF%E3%83%AA%E3%83%BC" title="ブキ/スパッタリー" class="rel-wiki-page">スパッタリー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%91%E3%83%83%E3%82%BF%E3%83%AA%E3%83%BC%E3%83%BB%E3%83%92%E3%83%A5%E3%83%BC" title="ブキ/スパッタリー・ヒュー" class="rel-wiki-page">ヒュー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%91%E3%83%83%E3%82%BF%E3%83%AA%E3%83%BCOWL" title="ブキ/スパッタリーOWL" class="rel-wiki-page">OWL</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%9E%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%90%E3%83%BC" title="ブキ/スプラマニューバー" class="rel-wiki-page">スプラマニューバー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%9E%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%90%E3%83%BC%E3%82%B3%E3%83%A9%E3%83%9C" title="ブキ/スプラマニューバーコラボ" class="rel-wiki-page">コラボ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%9E%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%90%E3%83%BC%E8%80%80" title="ブキ/スプラマニューバー耀" class="rel-wiki-page">耀</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC%E3%83%9E%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%90%E3%83%BC%20%E3%83%AC%E3%83%97%E3%83%AA%E3%82%AB" title="ブキ/オーダーマニューバー レプリカ" class="rel-wiki-page">オーダー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B1%E3%83%AB%E3%83%93%E3%83%B3525" title="ブキ/ケルビン525" class="rel-wiki-page">ケルビン525</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B1%E3%83%AB%E3%83%93%E3%83%B3525%E3%83%87%E3%82%B3" title="ブキ/ケルビン525デコ" class="rel-wiki-page">デコ</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%87%E3%83%A5%E3%82%A2%E3%83%AB%E3%82%B9%E3%82%A4%E3%83%BC%E3%83%91%E3%83%BC" title="ブキ/デュアルスイーパー" class="rel-wiki-page">デュアルスイーパー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%87%E3%83%A5%E3%82%A2%E3%83%AB%E3%82%B9%E3%82%A4%E3%83%BC%E3%83%91%E3%83%BC%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%A0" title="ブキ/デュアルスイーパーカスタム" class="rel-wiki-page">カスタム</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%87%E3%83%A5%E3%82%A2%E3%83%AB%E3%82%B9%E3%82%A4%E3%83%BC%E3%83%91%E3%83%BC%E8%B9%84" title="ブキ/デュアルスイーパー蹄" class="rel-wiki-page">蹄</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%82%A2%E3%83%83%E3%83%89%E3%83%9B%E3%83%83%E3%83%91%E3%83%BC%E3%83%96%E3%83%A9%E3%83%83%E3%82%AF" title="ブキ/クアッドホッパーブラック" class="rel-wiki-page">クアッドホッパーブラック</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%82%A2%E3%83%83%E3%83%89%E3%83%9B%E3%83%83%E3%83%91%E3%83%BC%E3%83%9B%E3%83%AF%E3%82%A4%E3%83%88" title="ブキ/クアッドホッパーホワイト" class="rel-wiki-page">ホワイト</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AC%E3%82%A8%E3%83%B3FF" title="ブキ/ガエンFF" class="rel-wiki-page">ガエンFF</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AC%E3%82%A8%E3%83%B3FF%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%A0" title="ブキ/ガエンFFカスタム" class="rel-wiki-page">カスタム</a></li></ul>
</div>
</div>
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%BF%E3%83%BC_%E3%83%95%E3%83%81.png?rev=5fa6649af23c0ffb404e4eb544f40c99&amp;t=20230119180044" alt="シェルター_フチ.png" title="シェルター_フチ.png" width="15" height="15"  loading="lazy">シェルタ&#12540;</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%BF%E3%83%BC%E5%B1%9E" title="ブキ/シェルター属" class="rel-wiki-page">シェルター属</a></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%91%E3%83%A9%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%BF%E3%83%BC" title="ブキ/パラシェルター" class="rel-wiki-page">パラシェルター</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%91%E3%83%A9%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%BF%E3%83%BC%E3%82%BD%E3%83%AC%E3%83%BC%E3%83%A9" title="ブキ/パラシェルターソレーラ" class="rel-wiki-page">ソレーラ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%BF%E3%83%BC%20%E3%83%AC%E3%83%97%E3%83%AA%E3%82%AB" title="ブキ/オーダーシェルター レプリカ" class="rel-wiki-page">オーダー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%94%E3%83%B3%E3%82%B0%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%BF%E3%83%BC" title="ブキ/キャンピングシェルター" class="rel-wiki-page">キャンピングシェルター</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%94%E3%83%B3%E3%82%B0%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%BF%E3%83%BC%E3%82%BD%E3%83%AC%E3%83%BC%E3%83%A9" title="ブキ/キャンピングシェルターソレーラ" class="rel-wiki-page">ソレーラ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%94%E3%83%B3%E3%82%B0%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%BF%E3%83%BCCREM" title="ブキ/キャンピングシェルターCREM" class="rel-wiki-page">CREM</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%91%E3%82%A4%E3%82%AC%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88" title="ブキ/スパイガジェット" class="rel-wiki-page">スパイガジェット</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%91%E3%82%A4%E3%82%AC%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88%E3%82%BD%E3%83%AC%E3%83%BC%E3%83%A9" title="ブキ/スパイガジェットソレーラ" class="rel-wiki-page">ソレーラ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%91%E3%82%A4%E3%82%AC%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88%E7%B9%9A" title="ブキ/スパイガジェット繚" class="rel-wiki-page">繚</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/24%E5%BC%8F%E5%BC%B5%E6%9B%BF%E5%82%98%E3%83%BB%E7%94%B2" title="ブキ/24式張替傘・甲" class="rel-wiki-page">24式張替傘・甲</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/24%E5%BC%8F%E5%BC%B5%E6%9B%BF%E5%82%98%E3%83%BB%E4%B9%99" title="ブキ/24式張替傘・乙" class="rel-wiki-page">乙</a></li></ul>
</div>
</div>
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC_%E3%83%95%E3%83%81.png.webp?rev=b53b476517e64b9fb269c537eef53348&amp;t=20230119180106" alt="ブラスター_フチ.png" title="ブラスター_フチ.png" width="15" height="15"  loading="lazy">ブラスタ&#12540;</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC%E5%B1%9E" title="ブキ/ブラスター属" class="rel-wiki-page">ブラスター属</a></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%8E%E3%83%B4%E3%82%A1%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC" title="ブキ/ノヴァブラスター" class="rel-wiki-page">ノヴァブラスター</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%8E%E3%83%B4%E3%82%A1%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%8D%E3%82%AA" title="ブキ/ノヴァブラスターネオ" class="rel-wiki-page">ネオ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC%20%E3%83%AC%E3%83%97%E3%83%AA%E3%82%AB" title="ブキ/オーダーブラスター レプリカ" class="rel-wiki-page">オーダー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%9B%E3%83%83%E3%83%88%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC" title="ブキ/ホットブラスター" class="rel-wiki-page">ホットブラスター</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%9B%E3%83%83%E3%83%88%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%A0" title="ブキ/ホットブラスターカスタム" class="rel-wiki-page">カスタム</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%9B%E3%83%83%E3%83%88%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC%E8%89%B6" title="ブキ/ホットブラスター艶" class="rel-wiki-page">艶</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%AD%E3%83%B3%E3%82%B0%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC" title="ブキ/ロングブラスター" class="rel-wiki-page">ロングブラスター</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%AD%E3%83%B3%E3%82%B0%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%A0" title="ブキ/ロングブラスターカスタム" class="rel-wiki-page">カスタム</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC" title="ブキ/クラッシュブラスター" class="rel-wiki-page">クラッシュブラスター</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%8D%E3%82%AA" title="ブキ/クラッシュブラスターネオ" class="rel-wiki-page">ネオ</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%A9%E3%83%94%E3%83%83%E3%83%89%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC" title="ブキ/ラピッドブラスター" class="rel-wiki-page">ラピッドブラスター</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%A9%E3%83%94%E3%83%83%E3%83%89%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%87%E3%82%B3" title="ブキ/ラピッドブラスターデコ" class="rel-wiki-page">デコ</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/R%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC%E3%82%A8%E3%83%AA%E3%83%BC%E3%83%88" title="ブキ/Rブラスターエリート" class="rel-wiki-page">Rブラスターエリート</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/R%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC%E3%82%A8%E3%83%AA%E3%83%BC%E3%83%88%E3%83%87%E3%82%B3" title="ブキ/Rブラスターエリートデコ" class="rel-wiki-page">デコ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/R%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC%E3%82%A8%E3%83%AA%E3%83%BC%E3%83%88WNTR" title="ブキ/RブラスターエリートWNTR" class="rel-wiki-page">WNTR</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/S-BLAST92" title="ブキ/S-BLAST92" class="rel-wiki-page">S-BLAST92</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/S-BLAST91" title="ブキ/S-BLAST91" class="rel-wiki-page">91</a></li></ul>
</div>
</div>
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%95%E3%83%87_%E3%83%95%E3%83%81.png?rev=4af8c4131c3b6a3b90c8afe2904cd24a&amp;t=20230119180103" alt="フデ_フチ.png" title="フデ_フチ.png" width="15" height="15"  loading="lazy">フ&#12487;</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%95%E3%83%87%E5%B1%9E" title="ブキ/フデ属" class="rel-wiki-page">フデ属</a></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%91%E3%83%96%E3%83%AD" title="ブキ/パブロ" class="rel-wiki-page">パブロ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%91%E3%83%96%E3%83%AD%E3%83%BB%E3%83%92%E3%83%A5%E3%83%BC" title="ブキ/パブロ・ヒュー" class="rel-wiki-page">ヒュー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%9B%E3%82%AF%E3%82%B5%E3%82%A4" title="ブキ/ホクサイ" class="rel-wiki-page">ホクサイ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%9B%E3%82%AF%E3%82%B5%E3%82%A4%E3%83%BB%E3%83%92%E3%83%A5%E3%83%BC" title="ブキ/ホクサイ・ヒュー" class="rel-wiki-page">ヒュー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%9B%E3%82%AF%E3%82%B5%E3%82%A4%E5%BD%97" title="ブキ/ホクサイ彗" class="rel-wiki-page">彗</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC%E3%83%96%E3%83%A9%E3%82%B7%20%E3%83%AC%E3%83%97%E3%83%AA%E3%82%AB" title="ブキ/オーダーブラシ レプリカ" class="rel-wiki-page">オーダー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%95%E3%82%A3%E3%83%B3%E3%82%BB%E3%83%B3%E3%83%88" title="ブキ/フィンセント" class="rel-wiki-page">フィンセント</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%95%E3%82%A3%E3%83%B3%E3%82%BB%E3%83%B3%E3%83%88%E3%83%BB%E3%83%92%E3%83%A5%E3%83%BC" title="ブキ/フィンセント・ヒュー" class="rel-wiki-page">ヒュー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%95%E3%82%A3%E3%83%B3%E3%82%BB%E3%83%B3%E3%83%88BRNZ" title="ブキ/フィンセントBRNZ" class="rel-wiki-page">BRNZ</a></li></ul>
</div>
</div>
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B9%E3%83%88%E3%83%AA%E3%83%B3%E3%82%AC%E3%83%BC_%E3%83%95%E3%83%81.png.webp?rev=7e43dcbc7cad5e34b98c99155bb188cd&amp;t=20230119180050" alt="ストリンガー_フチ.png" title="ストリンガー_フチ.png" width="15" height="15"  loading="lazy">ストリンガ&#12540;</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%88%E3%83%AA%E3%83%B3%E3%82%AC%E3%83%BC%E5%B1%9E" title="ブキ/ストリンガー属" class="rel-wiki-page">ストリンガー属</a></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%88%E3%83%A9%E3%82%A4%E3%82%B9%E3%83%88%E3%83%AA%E3%83%B3%E3%82%AC%E3%83%BC" title="ブキ/トライストリンガー" class="rel-wiki-page">トライストリンガー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%88%E3%83%A9%E3%82%A4%E3%82%B9%E3%83%88%E3%83%AA%E3%83%B3%E3%82%AC%E3%83%BC%E3%82%B3%E3%83%A9%E3%83%9C" title="ブキ/トライストリンガーコラボ" class="rel-wiki-page">コラボ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%88%E3%83%A9%E3%82%A4%E3%82%B9%E3%83%88%E3%83%AA%E3%83%B3%E3%82%AC%E3%83%BC%E7%87%88" title="ブキ/トライストリンガー燈" class="rel-wiki-page">燈</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC%E3%82%B9%E3%83%88%E3%83%AA%E3%83%B3%E3%82%AC%E3%83%BC%20%E3%83%AC%E3%83%97%E3%83%AA%E3%82%AB" title="ブキ/オーダーストリンガー レプリカ" class="rel-wiki-page">オーダー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/LACT-450" title="ブキ/LACT-450" class="rel-wiki-page">LACT-450</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/LACT-450%E3%83%87%E3%82%B3" title="ブキ/LACT-450デコ" class="rel-wiki-page">デコ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/LACT-450MILK" title="ブキ/LACT-450MILK" class="rel-wiki-page">MILK</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%95%E3%83%AB%E3%82%A4%E3%83%89V" title="ブキ/フルイドV" class="rel-wiki-page">フルイドV</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%95%E3%83%AB%E3%82%A4%E3%83%89V%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%A0" title="ブキ/フルイドVカスタム" class="rel-wiki-page">カスタム</a></li></ul>
</div>
</div>
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC_%E3%83%95%E3%83%81.png.webp?rev=bc7f9b35220c1001fabc9eca91930d3f&amp;t=20230119180115" alt="ワイパー_フチ.png" title="ワイパー_フチ.png" width="15" height="15"  loading="lazy">ワイパ&#12540;</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC%E5%B1%9E" title="ブキ/ワイパー属" class="rel-wiki-page">ワイパー属</a></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B8%E3%83%A0%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC" title="ブキ/ジムワイパー" class="rel-wiki-page">ジムワイパー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B8%E3%83%A0%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC%E3%83%BB%E3%83%92%E3%83%A5%E3%83%BC" title="ブキ/ジムワイパー・ヒュー" class="rel-wiki-page">ヒュー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B8%E3%83%A0%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC%E5%B0%81" title="ブキ/ジムワイパー封" class="rel-wiki-page">封</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC%20%E3%83%AC%E3%83%97%E3%83%AA%E3%82%AB" title="ブキ/オーダーワイパー レプリカ" class="rel-wiki-page">オーダー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%89%E3%83%A9%E3%82%A4%E3%83%96%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC" title="ブキ/ドライブワイパー" class="rel-wiki-page">ドライブワイパー</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%89%E3%83%A9%E3%82%A4%E3%83%96%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC%E3%83%87%E3%82%B3" title="ブキ/ドライブワイパーデコ" class="rel-wiki-page">デコ</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%89%E3%83%A9%E3%82%A4%E3%83%96%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BCRUST" title="ブキ/ドライブワイパーRUST" class="rel-wiki-page">RUST</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%87%E3%83%B3%E3%82%BF%E3%83%AB%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC%E3%83%9F%E3%83%B3%E3%83%88" title="ブキ/デンタルワイパーミント" class="rel-wiki-page">デンタルワイパーミント</a> / <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%87%E3%83%B3%E3%82%BF%E3%83%AB%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC%E3%82%B9%E3%83%9F" title="ブキ/デンタルワイパースミ" class="rel-wiki-page">スミ</a></li></ul>
</div>
</div>
<hr class="full_hr" />
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5%E3%83%9C%E3%83%A0.webp?rev=99f57bdaa53bb33b9e13415be067e13e&amp;t=20230312235050" alt="スプラッシュボム.webp" title="スプラッシュボム.webp" width="15" height="15"  loading="lazy">&#12469;ブウェポン</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/サブウェポン" class="rel-wiki-page">サブウェポン</a></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5%E3%83%9C%E3%83%A0" title="ブキ/サブウェポン/スプラッシュボム" class="rel-wiki-page">スプラッシュボム</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%AD%E3%83%A5%E3%83%BC%E3%83%90%E3%83%B3%E3%83%9C%E3%83%A0" title="ブキ/サブウェポン/キューバンボム" class="rel-wiki-page">キューバンボム</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%AF%E3%82%A4%E3%83%83%E3%82%AF%E3%83%9C%E3%83%A0" title="ブキ/サブウェポン/クイックボム" class="rel-wiki-page">クイックボム</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%B9%E3%83%97%E3%83%AA%E3%83%B3%E3%82%AF%E3%83%A9%E3%83%BC" title="ブキ/サブウェポン/スプリンクラー" class="rel-wiki-page">スプリンクラー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5%E3%82%B7%E3%83%BC%E3%83%AB%E3%83%89" title="ブキ/サブウェポン/スプラッシュシールド" class="rel-wiki-page">スプラッシュシールド</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%BF%E3%83%B3%E3%82%B5%E3%83%B3%E3%83%9C%E3%83%A0" title="ブキ/サブウェポン/タンサンボム" class="rel-wiki-page">タンサンボム</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%AB%E3%83%BC%E3%83%AA%E3%83%B3%E3%82%B0%E3%83%9C%E3%83%A0" title="ブキ/サブウェポン/カーリングボム" class="rel-wiki-page">カーリングボム</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%AD%E3%83%9C%E3%83%83%E3%83%88%E3%83%9C%E3%83%A0" title="ブキ/サブウェポン/ロボットボム" class="rel-wiki-page">ロボットボム</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%B8%E3%83%A3%E3%83%B3%E3%83%97%E3%83%93%E3%83%BC%E3%82%B3%E3%83%B3" title="ブキ/サブウェポン/ジャンプビーコン" class="rel-wiki-page">ジャンプビーコン</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88%E3%82%BB%E3%83%B3%E3%82%B5%E3%83%BC" title="ブキ/サブウェポン/ポイントセンサー" class="rel-wiki-page">ポイントセンサー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%88%E3%83%A9%E3%83%83%E3%83%97" title="ブキ/サブウェポン/トラップ" class="rel-wiki-page">トラップ</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%9D%E3%82%A4%E3%82%BA%E3%83%B3%E3%83%9F%E3%82%B9%E3%83%88" title="ブキ/サブウェポン/ポイズンミスト" class="rel-wiki-page">ポイズンミスト</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%A9%E3%82%A4%E3%83%B3%E3%83%9E%E3%83%BC%E3%82%AB%E3%83%BC" title="ブキ/サブウェポン/ラインマーカー" class="rel-wiki-page">ラインマーカー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%88%E3%83%BC%E3%83%94%E3%83%BC%E3%83%89" title="ブキ/サブウェポン/トーピード" class="rel-wiki-page">トーピード</a></li></ul>
</div>
</div>
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%88%E3%83%AA%E3%83%97%E3%83%AB%E3%83%88%E3%83%AB%E3%83%8D%E3%83%BC%E3%83%89.webp?rev=175f2542fbbb8aa5e3203caaebebc4fb&amp;t=20230312234857" alt="トリプルトルネード.webp" title="トリプルトルネード.webp" width="15" height="15"  loading="lazy">&#12473;ペシャルウェポン</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャルウェポン</a></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%A6%E3%83%AB%E3%83%88%E3%83%A9%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88" title="ブキ/スペシャルウェポン/ウルトラショット" class="rel-wiki-page">ウルトラショット</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%B0%E3%83%AC%E3%83%BC%E3%83%88%E3%83%90%E3%83%AA%E3%82%A2" title="ブキ/スペシャルウェポン/グレートバリア" class="rel-wiki-page">グレートバリア</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%B7%E3%83%A7%E3%82%AF%E3%83%AF%E3%83%B3%E3%83%80%E3%83%BC" title="ブキ/スペシャルウェポン/ショクワンダー" class="rel-wiki-page">ショクワンダー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%9E%E3%83%AB%E3%83%81%E3%83%9F%E3%82%B5%E3%82%A4%E3%83%AB" title="ブキ/スペシャルウェポン/マルチミサイル" class="rel-wiki-page">マルチミサイル</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%A2%E3%83%A1%E3%83%95%E3%83%A9%E3%82%B7" title="ブキ/スペシャルウェポン/アメフラシ" class="rel-wiki-page">アメフラシ</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%8A%E3%82%A4%E3%82%B9%E3%83%80%E3%83%9E" title="ブキ/スペシャルウェポン/ナイスダマ" class="rel-wiki-page">ナイスダマ</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%9B%E3%83%83%E3%83%97%E3%82%BD%E3%83%8A%E3%83%BC" title="ブキ/スペシャルウェポン/ホップソナー" class="rel-wiki-page">ホップソナー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%AD%E3%83%A5%E3%83%BC%E3%82%A4%E3%83%B3%E3%82%AD" title="ブキ/スペシャルウェポン/キューインキ" class="rel-wiki-page">キューインキ</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%A1%E3%82%AC%E3%83%9B%E3%83%B3%E3%83%AC%E3%83%BC%E3%82%B6%E3%83%BC5.1ch" title="ブキ/スペシャルウェポン/メガホンレーザー5.1ch" class="rel-wiki-page">メガホンレーザー5.1ch</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88%E3%83%91%E3%83%83%E3%82%AF" title="ブキ/スペシャルウェポン/ジェットパック" class="rel-wiki-page">ジェットパック</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%A6%E3%83%AB%E3%83%88%E3%83%A9%E3%83%8F%E3%83%B3%E3%82%B3" title="ブキ/スペシャルウェポン/ウルトラハンコ" class="rel-wiki-page">ウルトラハンコ</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%AB%E3%83%8B%E3%82%BF%E3%83%B3%E3%82%AF" title="ブキ/スペシャルウェポン/カニタンク" class="rel-wiki-page">カニタンク</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%B5%E3%83%A1%E3%83%A9%E3%82%A4%E3%83%89" title="ブキ/スペシャルウェポン/サメライド" class="rel-wiki-page">サメライド</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%88%E3%83%AA%E3%83%97%E3%83%AB%E3%83%88%E3%83%AB%E3%83%8D%E3%83%BC%E3%83%89" title="ブキ/スペシャルウェポン/トリプルトルネード" class="rel-wiki-page">トリプルトルネード</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%A8%E3%83%8A%E3%82%B8%E3%83%BC%E3%82%B9%E3%82%BF%E3%83%B3%E3%83%89" title="ブキ/スペシャルウェポン/エナジースタンド" class="rel-wiki-page">エナジースタンド</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%87%E3%82%B3%E3%82%A4%E3%83%81%E3%83%A9%E3%82%B7" title="ブキ/スペシャルウェポン/デコイチラシ" class="rel-wiki-page">デコイチラシ</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%86%E3%82%A4%E3%82%AA%E3%82%A6%E3%82%A4%E3%82%AB" title="ブキ/スペシャルウェポン/テイオウイカ" class="rel-wiki-page">テイオウイカ</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%A6%E3%83%AB%E3%83%88%E3%83%A9%E3%83%81%E3%83%A3%E3%82%AF%E3%83%81" title="ブキ/スペシャルウェポン/ウルトラチャクチ" class="rel-wiki-page">ウルトラチャクチ</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%B9%E3%83%9F%E3%83%8A%E3%82%AC%E3%82%B7%E3%83%BC%E3%83%88" title="ブキ/スペシャルウェポン/スミナガシート" class="rel-wiki-page">スミナガシート</a></li></ul>
<hr class="full_hr" />
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%AC%E3%83%81%E3%83%9B%E3%82%B3%E3%83%90%E3%83%88%E3%83%AB#rainmaker_stats" title="ガチホコバトル" class="rel-wiki-page">ガチホコ</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%B9%E3%83%BC%E3%83%91%E3%83%BC%E3%83%81%E3%83%A3%E3%82%AF%E3%83%81" title="ブキ/スペシャルウェポン/スーパーチャクチ" class="rel-wiki-page">スーパーチャクチ</a></li></ul>
</div>
</div>
<hr class="full_hr" />
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%95%86%E4%BC%9A.webp?rev=1794256dab1e329c1662ea42a7d35a82&amp;t=20250906191543" alt="クマサン商会.webp" title="クマサン商会.webp" width="15" height="15"  loading="lazy">&#12469;ーモンラン専用ブキ</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3#grizzco_weapons" title="サーモンラン" class="rel-wiki-page">サーモンラン専用ブキ</a></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%82%B9%E3%83%88%E3%83%AA%E3%83%B3%E3%82%AC%E3%83%BC" title="ブキ/クマサン印のストリンガー" class="rel-wiki-page">クマサン印のストリンガー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC" title="ブキ/クマサン印のブラスター" class="rel-wiki-page">クマサン印のブラスター</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%BF%E3%83%BC" title="ブキ/クマサン印のシェルター" class="rel-wiki-page">クマサン印のシェルター</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC" title="ブキ/クマサン印のワイパー" class="rel-wiki-page">クマサン印のワイパー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%82%B9%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC" title="ブキ/クマサン印のスロッシャー" class="rel-wiki-page">クマサン印のスロッシャー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC" title="ブキ/クマサン印のチャージャー" class="rel-wiki-page">クマサン印のチャージャー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%83%9E%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%90%E3%83%BC" title="ブキ/クマサン印のマニューバー" class="rel-wiki-page">クマサン印のマニューバー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC" title="ブキ/クマサン印のローラー" class="rel-wiki-page">クマサン印のローラー</a></li></ul>
</div>
</div>
<hr class="full_hr" />
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD%E3%83%A1%E3%83%BC%E3%82%AB%E3%83%BC" title="ブキメーカー" class="rel-wiki-page">ブキメーカー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD%E3%83%81%E3%81%AE%E8%AA%AC%E6%98%8E%E4%B8%80%E8%A6%A7" title="ブキチの説明一覧" class="rel-wiki-page">ブキチの説明一覧</a></li></ul>
<p><a class="anchor" name ="a_gear"></a></p>
<h2 id="h2_content_1_11" class="heading-after-first"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AE%E3%82%A2_%E3%83%95%E3%83%81.webp?rev=becb29e73442cb011fc78285d7aab13e&amp;t=20240306075517" alt="ギア_フチ.webp" title="ギア_フチ.webp" width="20" height="20"  loading="lazy"> <a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page"><span class="wikicolor" style="color:white">ギア</span></a></h2>
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">概要</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC" title="ギア/ギアパワー" class="rel-wiki-page">ギアパワー</a>
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label">一覧</span></button>
    <div class="navfold-content"><ul class="list1"><li>通常<a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC" title="ギア/ギアパワー" class="rel-wiki-page">ギアパワー</a>
<ul class="list2"><li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#ink_saver_main" title="ギア/ギアパワー" class="rel-wiki-page">インク効率アップ(メイン)</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#ink_saver_sub" title="ギア/ギアパワー" class="rel-wiki-page">インク効率アップ(サブ)</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#ink_recovery_up" title="ギア/ギアパワー" class="rel-wiki-page">インク回復力アップ</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#run_speed_up" title="ギア/ギアパワー" class="rel-wiki-page">ヒト移動速度アップ</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#swim_speed_up" title="ギア/ギアパワー" class="rel-wiki-page">イカダッシュ速度アップ</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#special_charge_up" title="ギア/ギアパワー" class="rel-wiki-page">スペシャル増加量アップ</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#special_saver" title="ギア/ギアパワー" class="rel-wiki-page">スペシャル減少量ダウン</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#special_power_up" title="ギア/ギアパワー" class="rel-wiki-page">スペシャル性能アップ</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#quick_respawn" title="ギア/ギアパワー" class="rel-wiki-page">復活時間短縮</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#quick_super_jump" title="ギア/ギアパワー" class="rel-wiki-page">スーパージャンプ時間短縮</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#sub_power_up" title="ギア/ギアパワー" class="rel-wiki-page">サブ性能アップ</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#ink_resist" title="ギア/ギアパワー" class="rel-wiki-page">相手インク影響軽減</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#sub_resist" title="ギア/ギアパワー" class="rel-wiki-page">サブ影響軽減</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#action_enhance" title="ギア/ギアパワー" class="rel-wiki-page">アクション強化</a></li></ul></li>
<li>アタマ専用<a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC" title="ギア/ギアパワー" class="rel-wiki-page">ギアパワー</a>
<ul class="list2"><li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#opening_gambit" title="ギア/ギアパワー" class="rel-wiki-page">スタートダッシュ</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#last-ditch_effort" title="ギア/ギアパワー" class="rel-wiki-page">ラストスパート</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#tenacity" title="ギア/ギアパワー" class="rel-wiki-page">逆境強化</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#comeback" title="ギア/ギアパワー" class="rel-wiki-page">カムバック</a></li></ul></li>
<li>フク専用<a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC" title="ギア/ギアパワー" class="rel-wiki-page">ギアパワー</a>
<ul class="list2"><li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#ninja_squid" title="ギア/ギアパワー" class="rel-wiki-page">イカニンジャ</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#haunt" title="ギア/ギアパワー" class="rel-wiki-page">リベンジ</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#thermal_ink" title="ギア/ギアパワー" class="rel-wiki-page">サーマルインク</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#respawn_punisher" title="ギア/ギアパワー" class="rel-wiki-page">復活ペナルティアップ</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#ability_doubler" title="ギア/ギアパワー" class="rel-wiki-page">追加ギアパワー倍化</a></li></ul></li>
<li>クツ専用<a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC" title="ギア/ギアパワー" class="rel-wiki-page">ギアパワー</a>
<ul class="list2"><li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#stealth_jump" title="ギア/ギアパワー" class="rel-wiki-page">ステルスジャンプ</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#object_shredder" title="ギア/ギアパワー" class="rel-wiki-page">対物攻撃力アップ</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#drop_roller" title="ギア/ギアパワー" class="rel-wiki-page">受け身術</a></li></ul></li></ul>
</div>
</div></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2%E3%83%AA%E3%82%B9%E3%83%88" title="ギアリスト" class="rel-wiki-page">ギアリスト</a></li>
<li><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%83%96%E3%83%A9%E3%83%B3%E3%83%89" title="ギア/ブランド" class="rel-wiki-page">ブランド</a></li></ul>
<p><a class="anchor" name ="a_event"></a></p>
<h2 id="h2_content_1_12" class="heading-after-first"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%95%E3%82%A7%E3%82%B9_%E3%83%95%E3%83%81.webp?rev=c40f73401d8c9f6b238049421c4401a7&amp;t=20240306075651" alt="フェス_フチ.webp" title="フェス_フチ.webp" width="16" height="16"  loading="lazy"> イベント</h2>
<ul class="list1"><li><a href="/splatoon3mix/%E5%89%8D%E5%A4%9C%E7%A5%AD" title="前夜祭" class="rel-wiki-page"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E5%89%8D%E5%A4%9C%E7%A5%AD_%E3%83%95%E3%83%81.webp?rev=f10514608b2ac596285aba18c0fbfaf3&amp;t=20240306075742" alt="前夜祭_フチ.webp" title="前夜祭_フチ.webp" width="16" height="16"  loading="lazy">前夜祭</a></li>
<li><a href="/splatoon3mix/%E3%83%95%E3%82%A7%E3%82%B9" title="フェス" class="rel-wiki-page"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%95%E3%82%A7%E3%82%B9_%E3%83%95%E3%83%81.webp?rev=c40f73401d8c9f6b238049421c4401a7&amp;t=20240306075651" alt="フェス_フチ.webp" title="フェス_フチ.webp" width="16" height="16"  loading="lazy">フェス</a></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%83%9E%E3%83%83%E3%83%81" title="イベントマッチ" class="rel-wiki-page"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%83%9E%E3%83%83%E3%83%81_%E3%83%95%E3%83%81.webp?rev=dc001b752bc33311c420df6645b4743f&amp;t=20240306075415" alt="イベントマッチ_フチ.webp" title="イベントマッチ_フチ.webp" width="16" height="16"  loading="lazy">イベントマッチ</a> / <a href="/splatoon3mix/%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%83%9E%E3%83%83%E3%83%81/%E6%94%BB%E7%95%A5" title="イベントマッチ/攻略" class="rel-wiki-page">攻略</a></li></ul>
<hr class="full_hr" />
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3_%E3%83%95%E3%83%81.webp?rev=c4dc0112b8a81f92aefd659bcb1fcc2b&amp;t=20240306075641" alt="ビッグラン_フチ.webp" title="ビッグラン_フチ.webp" width="16" height="16"  loading="lazy">ビッグラン</a> / <a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3/%E6%94%BB%E7%95%A5" title="サーモンラン/ビッグラン/攻略" class="rel-wiki-page">攻略</a></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%90%E3%82%A4%E3%83%88%E3%83%81%E3%83%BC%E3%83%A0%E3%82%B3%E3%83%B3%E3%83%86%E3%82%B9%E3%83%88" title="サーモンラン/バイトチームコンテスト" class="rel-wiki-page"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%90%E3%82%A4%E3%83%88%E3%83%81%E3%83%BC%E3%83%A0%E3%82%B3%E3%83%B3%E3%83%86%E3%82%B9%E3%83%88_%E3%83%95%E3%83%81.webp?rev=faf3a2d324ddd64b2398ab1d32a6ab10&amp;t=20240306075624" alt="バイトチームコンテスト_フチ.webp" title="バイトチームコンテスト_フチ.webp" width="16" height="16"  loading="lazy">バイトチームコンテスト</a> / <a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%90%E3%82%A4%E3%83%88%E3%83%81%E3%83%BC%E3%83%A0%E3%82%B3%E3%83%B3%E3%83%86%E3%82%B9%E3%83%88/%E6%94%BB%E7%95%A5" title="サーモンラン/バイトチームコンテスト/攻略" class="rel-wiki-page">攻略</a></li></ul>
<hr class="full_hr" />
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%88%E3%82%A5%E3%83%BC%E3%83%B3%E7%94%B2%E5%AD%90%E5%9C%922023" title="スプラトゥーン甲子園2023" class="rel-wiki-page"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%88%E3%82%A5%E3%83%BC%E3%83%B3%E7%94%B2%E5%AD%90%E5%9C%922023_%E3%83%95%E3%83%81.webp?rev=a8fb1c3658a7f4080ff51dcc39261a23&amp;t=20240306075555" alt="スプラトゥーン甲子園2023_フチ.webp" title="スプラトゥーン甲子園2023_フチ.webp" width="16" height="16"  loading="lazy">スプラトゥーン甲子園2023</a></li></ul>
<p><a class="anchor" name ="a_gamedata"></a></p>
<h2 id="h2_content_1_13" class="heading-after-first"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B9%E3%82%BF%E3%83%83%E3%83%95%E3%81%95%E3%82%93_%E3%83%95%E3%83%81.webp?rev=32c6f3464eea352db95bce9f18d0d0a7&amp;t=20240306075545" alt="スタッフさん_フチ.webp" title="スタッフさん_フチ.webp" width="20" height="20"  loading="lazy"> ゲームデータ</h2>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%90%E3%83%B3%E3%82%AB%E3%83%A9%E8%A1%97" title="バンカラ街" class="rel-wiki-page">バンカラ街</a> / <a href="/splatoon3mix/%E3%83%8F%E3%82%A4%E3%82%AB%E3%83%A9%E3%82%B7%E3%83%86%E3%82%A3" title="ハイカラシティ" class="rel-wiki-page">ハイカラシティ</a> / <a href="/splatoon3mix/%E3%83%8F%E3%82%A4%E3%82%AB%E3%83%A9%E3%82%B9%E3%82%AF%E3%82%A8%E3%82%A2" title="ハイカラスクエア" class="rel-wiki-page">ハイカラスクエア</a></li>
<li><a href="/splatoon3mix/%E3%82%AD%E3%83%A3%E3%83%A9%E3%83%A1%E3%82%A4%E3%82%AF" title="キャラメイク" class="rel-wiki-page">キャラメイク</a></li>
<li><a href="/splatoon3mix/%E3%82%AD%E3%83%A3%E3%83%A9%E3%82%AF%E3%82%BF%E3%83%BC%E7%B4%B9%E4%BB%8B" title="キャラクター紹介" class="rel-wiki-page">キャラクター紹介</a></li>
<li><a href="/splatoon3mix/%E9%9F%B3%E6%A5%BD" title="音楽" class="rel-wiki-page">音楽</a></li>
<li><a href="/splatoon3mix/%E3%83%90%E3%83%B3%E3%82%AB%E3%83%A9%E3%82%B8%E3%82%AA" title="バンカラジオ" class="rel-wiki-page">バンカラジオ</a></li>
<li><a href="/splatoon3mix/%E3%82%B8%E3%83%A3%E3%83%83%E3%82%B8%E3%81%8F%E3%82%93%E3%81%AE%E3%82%A2%E3%83%89%E3%83%90%E3%82%A4%E3%82%B9" title="ジャッジくんのアドバイス" class="rel-wiki-page">ジャッジくんのアドバイス</a></li>
<li><a href="/splatoon3mix/%E3%83%A9%E3%83%B3%E3%82%AF" title="ランク" class="rel-wiki-page">ランク</a></li>
<li><a href="/splatoon3mix/%E8%A1%A8%E5%BD%B0" title="表彰" class="rel-wiki-page">表彰</a></li>
<li><a href="/splatoon3mix/%E6%B6%88%E8%B2%BB%E7%89%A9%E4%B8%80%E8%A6%A7" title="消費物一覧" class="rel-wiki-page">消費物</a></li></ul>
<hr class="full_hr" />
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%AB%E3%82%BF%E3%83%AD%E3%82%B0%28%E3%82%B2%E3%83%BC%E3%83%A0%E5%86%85%29" title="カタログ(ゲーム内)" class="rel-wiki-page">カタログ</a></li>
<li><a href="/splatoon3mix/%E3%81%8F%E3%81%98%E5%BC%95%E3%81%8D" title="くじ引き" class="rel-wiki-page">くじ引き</a></li>
<li><a href="/splatoon3mix/%E6%97%A5%E3%80%85%E3%81%AE%E3%83%AB%E3%83%BC%E3%83%86%E3%82%A3%E3%83%BC%E3%83%B3" title="日々のルーティーン" class="rel-wiki-page">日々のルーティーン</a></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88" title="ネームプレート" class="rel-wiki-page">ネームプレート</a>
<ul class="list2"><li><a href="/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88" title="ネームプレート/プレート" class="rel-wiki-page">プレート</a> / <a href="/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%90%E3%83%83%E3%82%B8" title="ネームプレート/バッジ" class="rel-wiki-page">バッジ</a> / <a href="/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E4%BA%8C%E3%81%A4%E5%90%8D" title="ネームプレート/二つ名" class="rel-wiki-page">二つ名</a></li></ul></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC" title="ロッカー" class="rel-wiki-page">ロッカー</a>
<ul class="list2"><li><a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E" title="ロッカー/オキモノ" class="rel-wiki-page">オキモノ</a> / <a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/%E3%82%B9%E3%83%86%E3%83%83%E3%82%AB%E3%83%BC" title="ロッカー/ステッカー" class="rel-wiki-page">ステッカー</a></li></ul></li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%A8%E3%83%A2%E3%83%BC%E3%83%88" title="エモート" class="rel-wiki-page">エモート</a></li></ul>
<hr class="full_hr" />
<ul class="list1"><li><a href="/splatoon3mix/%E6%92%AE%E5%BD%B1%E3%83%BB%E3%83%95%E3%82%A9%E3%83%88%E3%82%A2%E3%83%AB%E3%83%90%E3%83%A0" title="撮影・フォトアルバム" class="rel-wiki-page">撮影・フォトアルバム</a></li>
<li><a href="/splatoon3mix/%E3%82%A4%E3%82%AB%E3%83%83%E3%83%81%E3%83%A3" title="イカッチャ" class="rel-wiki-page">イカッチャ</a></li>
<li><a href="/splatoon3mix/%E3%82%A4%E3%82%AB%E3%83%AA%E3%83%B3%E3%82%B03" title="イカリング3" class="rel-wiki-page">イカリング3</a> / <a href="/splatoon3mix/%E3%83%AD%E3%83%96%E3%82%A4%E3%83%81%E5%A0%B1%E9%85%AC%E4%B8%80%E8%A6%A7" title="ロブイチ報酬一覧" class="rel-wiki-page">ロブイチ</a> / <a href="/splatoon3mix/QR%E3%82%B3%E3%83%BC%E3%83%89%E3%83%BB%E3%82%B3%E3%83%BC%E3%83%89%E4%B8%80%E8%A6%A7" title="QRコード・コード一覧" class="rel-wiki-page">QRコード</a></li>
<li><a href="/splatoon3mix/amiibo" title="amiibo" class="rel-wiki-page">amiibo</a></li></ul>
<p><a class="anchor" name ="a_others"></a></p>
<h2 id="h2_content_1_14" class="heading-after-first"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%9F%E3%82%B9%E3%83%86%E3%83%AA%E3%83%BC%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB_%E3%83%95%E3%83%81.webp?rev=ab0ade7b50490be853c261433360b7ac&amp;t=20240306075715" alt="ミステリーファイル_フチ.webp" title="ミステリーファイル_フチ.webp" width="20" height="20"  loading="lazy"> その他</h2>
<ul class="list1"><li><a href="/splatoon3mix/%E9%9B%91%E8%AB%87%E6%8E%B2%E7%A4%BA%E6%9D%BF" title="雑談掲示板" class="rel-wiki-page">雑談掲示板</a></li>
<li><a href="/splatoon3mix/%E5%B0%8F%E3%83%8D%E3%82%BF" title="小ネタ" class="rel-wiki-page">小ネタ</a></li>
<li><a href="/splatoon3mix/%E5%85%83%E3%83%8D%E3%82%BF%E4%B8%80%E8%A6%A7" title="元ネタ一覧" class="rel-wiki-page">元ネタ一覧</a>
<ul class="list2"><li><a href="/splatoon3mix/%E5%85%83%E3%83%8D%E3%82%BF%E4%B8%80%E8%A6%A7/%E3%82%AE%E3%82%A2" title="元ネタ一覧/ギア" class="rel-wiki-page">ギア元ネタ</a></li></ul></li></ul>
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins>ブキの環境変遷</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD%E3%81%AE%E7%92%B0%E5%A2%83%E5%A4%89%E9%81%B73" title="ブキの環境変遷3" class="rel-wiki-page">前夜祭～シーズン4</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD%E3%81%AE%E7%92%B0%E5%A2%83%E5%A4%89%E9%81%B72" title="ブキの環境変遷2" class="rel-wiki-page">シーズン5～8</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD%E3%81%AE%E7%92%B0%E5%A2%83%E5%A4%89%E9%81%B7" title="ブキの環境変遷" class="rel-wiki-page">シーズン9～</a></li></ul>
</div>
</div>
<hr class="full_hr" />
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins>用語集</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E7%94%A8%E8%AA%9E%E9%9B%86" title="用語集" class="rel-wiki-page">用語集</a>
<ul class="list2"><li><a href="/splatoon3mix/%E7%94%A8%E8%AA%9E%E9%9B%86/%E5%AF%BE%E6%88%A6%E9%96%A2%E9%80%A3%E7%94%A8%E8%AA%9E" title="用語集/対戦関連用語" class="rel-wiki-page">対戦関連</a></li>
<li><a href="/splatoon3mix/%E7%94%A8%E8%AA%9E%E9%9B%86/%E5%AF%BE%E6%88%A6%E4%BB%A5%E5%A4%96%E3%81%AETPS%E9%96%A2%E9%80%A3%E7%94%A8%E8%AA%9E" title="用語集/対戦以外のTPS関連用語" class="rel-wiki-page">対戦以外TPS</a></li>
<li><a href="/splatoon3mix/%E7%94%A8%E8%AA%9E%E9%9B%86/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%88%E3%82%A5%E3%83%BC%E3%83%B3%E4%B8%96%E7%95%8C%E3%81%AE%E7%94%A8%E8%AA%9E" title="用語集/スプラトゥーン世界の用語" class="rel-wiki-page">スプラ世界</a></li>
<li><a href="/splatoon3mix/%E7%94%A8%E8%AA%9E%E9%9B%86/%E3%82%B2%E3%83%BC%E3%83%A0%E5%86%85%E7%94%A8%E8%AA%9E%E3%81%AE%E7%95%A5%E7%A7%B0%E4%B8%80%E8%A6%A7" title="用語集/ゲーム内用語の略称一覧" class="rel-wiki-page">略称一覧</a></li>
<li><a href="/splatoon3mix/%E7%94%A8%E8%AA%9E%E9%9B%86/%E6%B3%A8%E6%84%8F%E3%81%99%E3%81%B9%E3%81%8D%E7%94%A8%E8%AA%9E" title="用語集/注意すべき用語" class="rel-wiki-page">注意すべき用語</a></li></ul></li></ul>
</div>
</div>
<ul class="list1"><li><a href="/splatoon3mix/%E8%A8%80%E8%AA%9E%E5%88%A5%E5%AF%BE%E5%BF%9C%E8%A1%A8" title="言語別対応表" class="rel-wiki-page">言語別対応表</a> / <a href="/splatoon3mix/10%E8%A8%80%E8%AA%9E%E5%AF%BE%E5%BF%9C%E8%A1%A8" title="10言語対応表" class="rel-wiki-page">10言語対応表</a></li></ul>
<hr class="full_hr" />
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins>関連リンク</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="https://wikiwiki.jp/p/cushion?to=https%3A%2F%2Fwww.nintendo.co.jp%2Fswitch%2Fav5ja%2Findex.html"  rel="nofollow">公式ホームページ</a></li>
<li><a href="https://wikiwiki.jp/p/cushion?to=https%3A%2F%2Fwww.nintendo.co.jp%2Fsupport%2Fswitch%2Fsoftware_support%2Fav5ja%2Findex.html"  rel="nofollow">公式アップデート情報</a></li>
<li><a href="https://wikiwiki.jp/p/cushion?to=https%3A%2F%2Fwww.nintendo.co.jp%2Fcharacter%2Fsplatoon%2Findex.html"  rel="nofollow">スプラトゥーンベース</a></li>
<li><a href="https://wikiwiki.jp/splatoon2ch/"  rel="nofollow">スプラトゥーン(Splatoon) for 2ch Wiki</a></li>
<li><a href="https://wikiwiki.jp/splatoon2mix/"  rel="nofollow">スプラトゥーン2 攻略＆検証 Wiki</a></li>
<li><a href="https://wikiwiki.jp/p/cushion?to=https%3A%2F%2Fwww.famitsu.com%2Fnews%2F201907%2F21179901.html"  rel="nofollow">ファミ通インタビュー記事まとめ</a></li></ul>
</div>
</div>
<ul class="list1"><li><a href="/splatoon3mix/%E5%85%AC%E5%BC%8F%E5%8B%95%E7%94%BB%E9%9B%86" title="公式動画集" class="rel-wiki-page">公式動画集</a></li></ul>
<hr class="full_hr" />
<ul class="list1"><li><a href="/splatoon3mix/%E6%9C%AA%E6%95%B4%E7%90%86%EF%BD%A5%E6%9C%AA%E7%A2%BA%E8%AA%8D%E6%83%85%E5%A0%B1" title="未整理･未確認情報" class="rel-wiki-page">未整理･未確認情報</a></li>
<li><a href="/splatoon3mix/%E3%83%90%E3%82%B0%E3%83%BB%E4%B8%8D%E5%85%B7%E5%90%88%E6%83%85%E5%A0%B1" title="バグ・不具合情報" class="rel-wiki-page">バグ・不具合情報</a></li>
<li><a href="/splatoon3mix/%E4%BA%88%E6%83%B3%E3%83%BB%E8%80%83%E5%AF%9F" title="予想・考察" class="rel-wiki-page">予想・考察</a></li>
<li><a href="/splatoon3mix/%E6%A4%9C%E8%A8%BC" title="検証" class="rel-wiki-page">検証</a></li>
<li><a href="/splatoon3mix/%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E8%A9%B3%E7%B4%B0%E4%BB%95%E6%A7%98" title="システム詳細仕様" class="rel-wiki-page">システム詳細仕様</a></li></ul>
<p><a class="anchor" name ="a_wiki_info"></a></p>
<h2 id="h2_content_1_15" class="heading-after-first"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3_%E3%83%95%E3%83%81.webp?rev=9629bce342202e344fbfa7610832f366&amp;t=20240306075527" alt="クマサン_フチ.webp" title="クマサン_フチ.webp" width="20" height="20"  loading="lazy"> 当wikiについて</h2>
<p>この<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="ここにヘルプがでます"> <img alt="[hatena]" src="https://cdn.wikiwiki.jp/to/w/common/image/face/hatena.gif?v=4" /></span>に触れるとヘルプが表示されます</p>
<hr class="full_hr" />
<p><strong>Wiki運営</strong></p>
<ul class="list1"><li><a href="/splatoon3mix/%E7%B7%A8%E9%9B%86%E9%80%A3%E7%B5%A1%E6%8E%B2%E7%A4%BA%E6%9D%BF" title="編集連絡掲示板" class="rel-wiki-page">編集連絡掲示板</a> <span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="編集の相談はこちら"> <img alt="[hatena]" src="https://cdn.wikiwiki.jp/to/w/common/image/face/hatena.gif?v=4" /></span></li>
<li><a href="/splatoon3mix/%E7%AE%A1%E7%90%86%E6%8E%B2%E7%A4%BA%E6%9D%BF" title="管理掲示板" class="rel-wiki-page">管理掲示板</a> <span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="管理人への連絡はこちら"> <img alt="[hatena]" src="https://cdn.wikiwiki.jp/to/w/common/image/face/hatena.gif?v=4" /></span></li>
<li><a href="/splatoon3mix/Wiki%E7%B7%A8%E9%9B%86%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6" title="Wiki編集について" class="rel-wiki-page">Wiki編集について</a> <span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="編集のルールについて"> <img alt="[hatena]" src="https://cdn.wikiwiki.jp/to/w/common/image/face/hatena.gif?v=4" /></span></li>
<li><a href="/splatoon3mix/Wiki%E7%AE%A1%E7%90%86%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6" title="Wiki管理について" class="rel-wiki-page">Wiki管理について</a> <span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="wikiご利用にあたって"> <img alt="[hatena]" src="https://cdn.wikiwiki.jp/to/w/common/image/face/hatena.gif?v=4" /></span></li>
<li><a href="/splatoon3mix/%E7%B7%B4%E7%BF%92%E3%83%9A%E3%83%BC%E3%82%B8" title="練習ページ" class="rel-wiki-page">練習ページ</a> <span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="おためしで編集ができる"> <img alt="[hatena]" src="https://cdn.wikiwiki.jp/to/w/common/image/face/hatena.gif?v=4" /></span></li></ul>
<hr class="full_hr" />
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins>共有スペース</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E9%9B%91%E8%AB%87%E6%8E%B2%E7%A4%BA%E6%9D%BF" title="雑談掲示板" class="rel-wiki-page">雑談掲示板</a></li>
<li><a href="/splatoon3mix/%E4%BA%88%E6%83%B3%E3%83%BB%E8%80%83%E5%AF%9F" title="予想・考察" class="rel-wiki-page">予想・考察</a></li>
<li><a href="/splatoon3mix/%E3%83%90%E3%82%B0%E3%83%BB%E4%B8%8D%E5%85%B7%E5%90%88%E6%83%85%E5%A0%B1" title="バグ・不具合情報" class="rel-wiki-page">バグ・不具合情報</a></li>
<li><a href="/splatoon3mix/%E6%9C%AA%E6%95%B4%E7%90%86%EF%BD%A5%E6%9C%AA%E7%A2%BA%E8%AA%8D%E6%83%85%E5%A0%B1" title="未整理･未確認情報" class="rel-wiki-page">未整理･未確認情報</a></li>
<li><a href="/splatoon3mix/%E3%83%90%E3%83%88%E3%83%AB%E3%83%A1%E3%83%A2%E3%83%AA%E3%83%BC" title="バトルメモリー" class="rel-wiki-page">バトルメモリー</a></li>
<li><a href="/splatoon3mix/%E3%83%81%E3%83%A3%E3%83%B3%E3%83%8D%E3%83%AB" title="チャンネル" class="rel-wiki-page">チャンネル</a></li>
<li><a href="https://wikiwiki.jp/splatoon3mix/%E9%9B%91%E8%AB%87%E6%8E%B2%E7%A4%BA%E6%9D%BF#comment"  rel="nofollow">チャンネル雑談板</a></li>
<li><a href="/splatoon3mix/%E3%83%90%E3%82%A4%E3%83%88%E3%82%B7%E3%83%8A%E3%83%AA%E3%82%AA" title="バイトシナリオ" class="rel-wiki-page">バイトシナリオ</a></li>
<li><a href="/splatoon3mix/%E4%BB%8A%E6%97%A5100" title="今日100" class="rel-wiki-page">今日100</a></li>
<li><a href="/splatoon3mix/%E4%BA%BA%E6%B0%97100" title="人気100" class="rel-wiki-page">人気100</a></li></ul>
</div>
</div>
<hr class="full_hr" />
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins>編集お役立ち</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E6%95%B4%E5%BD%A2%E3%83%AB%E3%83%BC%E3%83%AB" title="整形ルール" class="rel-wiki-page">整形ルール</a> <span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="wikiのかきかた"> <img alt="[hatena]" src="https://cdn.wikiwiki.jp/to/w/common/image/face/hatena.gif?v=4" /></span>
<ul class="list2"><li><a href="/splatoon3mix/%E3%83%97%E3%83%A9%E3%82%B0%E3%82%A4%E3%83%B3%E8%A7%A3%E8%AA%AC" title="プラグイン解説" class="rel-wiki-page">プラグイン解説</a> <span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="wikiの書き方をもっとくわしく"> <img alt="[hatena]" src="https://cdn.wikiwiki.jp/to/w/common/image/face/hatena.gif?v=4" /></span></li>
<li><a href="/splatoon3mix/%E7%B7%A8%E9%9B%86%E3%81%AE%E3%82%B3%E3%83%84" title="編集のコツ" class="rel-wiki-page">編集のコツ</a> <span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="もっと上手に編集できるかも？"> <img alt="[hatena]" src="https://cdn.wikiwiki.jp/to/w/common/image/face/hatena.gif?v=4" /></span></li>
<li><a href="/splatoon3mix/%E3%82%AB%E3%83%A9%E3%83%BC%E3%82%B3%E3%83%BC%E3%83%89" title="カラーコード" class="rel-wiki-page">カラーコード</a> <span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="文字に色をつけてみよう"> <img alt="[hatena]" src="https://cdn.wikiwiki.jp/to/w/common/image/face/hatena.gif?v=4" /></span></li></ul></li></ul>
<hr class="full_hr" />
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%96%E3%82%AD" title="テンプレート/ブキ" class="rel-wiki-page">ブキページのテンプレート</a> <span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="新規「ブキ/」ページを作るときのひな形"> <img alt="[hatena]" src="https://cdn.wikiwiki.jp/to/w/common/image/face/hatena.gif?v=4" /></span></li>
<li><a href="/splatoon3mix/%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%82%B5%E3%83%96%E3%83%BB%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB" title="テンプレート/サブ・スペシャル" class="rel-wiki-page">サブ・スペシャルページのテンプレート</a> <span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="新規「&lt;a href=&quot;/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3&quot; title=&quot;ブキ/サブウェポン&quot; class=&quot;rel-wiki-page&quot;&gt;サブ&lt;/a&gt;/」「&lt;a href=&quot;/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3&quot; title=&quot;ブキ/スペシャルウェポン&quot; class=&quot;rel-wiki-page&quot;&gt;スペシャル&lt;/a&gt;/」ページを作るときのひな形"> <img alt="[hatena]" src="https://cdn.wikiwiki.jp/to/w/common/image/face/hatena.gif?v=4" /></span></li>
<li><a href="/splatoon3mix/%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8" title="テンプレート/ステージ" class="rel-wiki-page">ステージページのテンプレート</a> <span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="新規「ステージ/」ページを作るときのひな形"> <img alt="[hatena]" src="https://cdn.wikiwiki.jp/to/w/common/image/face/hatena.gif?v=4" /></span></li></ul>
<hr class="full_hr" />
<ul class="list1"><li><a href="/splatoon3mix/AutoAliasName" title="AutoAliasName" class="rel-wiki-page">AutoAliasName</a> <span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="指定した単語にリンクをはる"> <img alt="[hatena]" src="https://cdn.wikiwiki.jp/to/w/common/image/face/hatena.gif?v=4" /></span></li>
<li><a href="/splatoon3mix/Glossary" title="Glossary" class="rel-wiki-page">Glossary</a> <span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="指定した単語に説明文をつける"> <img alt="[hatena]" src="https://cdn.wikiwiki.jp/to/w/common/image/face/hatena.gif?v=4" /></span></li>
<li><a href="/splatoon3mix/icon" title="icon" class="rel-wiki-page">画像置き場(icon)</a> <span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="いろんなアイコンが置いてある"> <img alt="[hatena]" src="https://cdn.wikiwiki.jp/to/w/common/image/face/hatena.gif?v=4" /></span>
<div class="navfold-container clearfix ">
    <button class="navfold-summary"><span class="navfold-summary-icon navfold-icon-close"><i class="fa-solid fa-fw fa-xs fa-chevron-right"></i></span><span class="navfold-summary-icon navfold-icon-open"><i class="fa-solid fa-fw fa-xs fa-chevron-down"></i></span><span class="navfold-summary-label"><ins>ブキ使用イメージ</ins></span></button>
    <div class="navfold-content"><ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC1/%E4%BD%BF%E7%94%A8%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8" title="ブキ/シューター1/使用イメージ" class="rel-wiki-page">シューター①</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC2/%E4%BD%BF%E7%94%A8%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8" title="ブキ/シューター2/使用イメージ" class="rel-wiki-page">シューター②</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC%E3%80%81%E3%82%B9%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC/%E4%BD%BF%E7%94%A8%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8" title="ブキ/ローラー、スロッシャー/使用イメージ" class="rel-wiki-page">ローラー・スロッシャー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC/%E4%BD%BF%E7%94%A8%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8" title="ブキ/チャージャー/使用イメージ" class="rel-wiki-page">チャージャー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%94%E3%83%8A%E3%83%BC%E3%80%81%E3%82%B9%E3%83%88%E3%83%AA%E3%83%B3%E3%82%AC%E3%83%BC/%E4%BD%BF%E7%94%A8%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8" title="ブキ/スピナー、ストリンガー/使用イメージ" class="rel-wiki-page">スピナー・ストリンガー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%9E%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%90%E3%83%BC/%E4%BD%BF%E7%94%A8%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8" title="ブキ/マニューバー/使用イメージ" class="rel-wiki-page">マニューバー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%BF%E3%83%BC%E3%80%81%E3%83%95%E3%83%87/%E4%BD%BF%E7%94%A8%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8" title="ブキ/シェルター、フデ/使用イメージ" class="rel-wiki-page">シェルター・フデ</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC/%E4%BD%BF%E7%94%A8%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8" title="ブキ/ブラスター/使用イメージ" class="rel-wiki-page">ブラスター</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC/%E4%BD%BF%E7%94%A8%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8" title="ブキ/ワイパー/使用イメージ" class="rel-wiki-page">ワイパー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E4%BD%BF%E7%94%A8%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8" title="ブキ/サブウェポン/使用イメージ" class="rel-wiki-page">サブウェポン</a></li></ul>
</div>
</div></li>
<li><a href="/splatoon3mix/%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88" title="テンプレート" class="rel-wiki-page">モジュール置き場</a><span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="いろんな看板が置いてある"> <img alt="[hatena]" src="https://cdn.wikiwiki.jp/to/w/common/image/face/hatena.gif?v=4" /></span></li>
<li><a href="/splatoon3mix/%E3%83%87%E3%83%BC%E3%82%BF" title="データ" class="rel-wiki-page">データ</a><span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="いろんな情報を置いたり使ったり"> <img alt="[hatena]" src="https://cdn.wikiwiki.jp/to/w/common/image/face/hatena.gif?v=4" /></span></li></ul>
</div>
</div>
<h2 id="h2_content_1_16" class="heading-after-first">コメント 最新20件</h2>
<div class="wikicolor" style="color:#08e">
<div class="zawazawa-recent" data-zrecent-hash="3a684b0a43f138bd34882058ed488b0c" data-zrecent-data="{&quot;topics&quot;:[{&quot;embeddedSites&quot;:{&quot;wikiwiki&quot;:{&quot;name&quot;:&quot;サメライド&quot;,&quot;url&quot;:&quot;https://wikiwiki.jp/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%B5%E3%83%A1%E3%83%A9%E3%82%A4%E3%83%89#comment&quot;}},&quot;forumSlug&quot;:&quot;spla3&quot;,&quot;forumTitle&quot;:&quot;Splatoon3 - スプラトゥーン3 攻略&amp;検証 Wiki&quot;,&quot;lastCommentNumber&quot;:7026,&quot;lastCommentedAt&quot;:&quot;Fri, 16 Jan 2026 19:24:48 +0900&quot;,&quot;topicNumber&quot;:104,&quot;topicTitle&quot;:&quot;サメライド&quot;,&quot;url&quot;:&quot;https://z.wikiwiki.jp/spla3/topic/104&quot;},{&quot;embeddedSites&quot;:{&quot;wikiwiki&quot;:{&quot;name&quot;:&quot;雑談掲示板/ログ3&quot;,&quot;url&quot;:&quot;https://wikiwiki.jp/splatoon3mix/%E9%9B%91%E8%AB%87%E6%8E%B2%E7%A4%BA%E6%9D%BF#comment&quot;}},&quot;forumSlug&quot;:&quot;spla3&quot;,&quot;forumTitle&quot;:&quot;Splatoon3 - スプラトゥーン3 攻略&amp;検証 Wiki&quot;,&quot;lastCommentNumber&quot;:82120,&quot;lastCommentedAt&quot;:&quot;Fri, 16 Jan 2026 19:19:44 +0900&quot;,&quot;topicNumber&quot;:280,&quot;topicTitle&quot;:&quot;雑談掲示板/ログ3&quot;,&quot;url&quot;:&quot;https://z.wikiwiki.jp/spla3/topic/280&quot;},{&quot;embeddedSites&quot;:{&quot;wikiwiki&quot;:{&quot;name&quot;:&quot;スパイガジェット繚&quot;,&quot;url&quot;:&quot;https://wikiwiki.jp/splatoon3mix/ブキ/スパイガジェット繚#comment&quot;}},&quot;forumSlug&quot;:&quot;spla3&quot;,&quot;forumTitle&quot;:&quot;Splatoon3 - スプラトゥーン3 攻略&amp;検証 Wiki&quot;,&quot;lastCommentNumber&quot;:244,&quot;lastCommentedAt&quot;:&quot;Fri, 16 Jan 2026 19:02:17 +0900&quot;,&quot;topicNumber&quot;:326,&quot;topicTitle&quot;:&quot;スパイガジェット繚&quot;,&quot;url&quot;:&quot;https://z.wikiwiki.jp/spla3/topic/326&quot;},{&quot;embeddedSites&quot;:{&quot;wikiwiki&quot;:{&quot;name&quot;:&quot;カーボンローラーデコ&quot;,&quot;url&quot;:&quot;https://wikiwiki.jp/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AB%E3%83%BC%E3%83%9C%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC%E3%83%87%E3%82%B3#comment&quot;}},&quot;forumSlug&quot;:&quot;spla3&quot;,&quot;forumTitle&quot;:&quot;Splatoon3 - スプラトゥーン3 攻略&amp;検証 Wiki&quot;,&quot;lastCommentNumber&quot;:807,&quot;lastCommentedAt&quot;:&quot;Fri, 16 Jan 2026 18:29:15 +0900&quot;,&quot;topicNumber&quot;:171,&quot;topicTitle&quot;:&quot;カーボンローラーデコ&quot;,&quot;url&quot;:&quot;https://z.wikiwiki.jp/spla3/topic/171&quot;},{&quot;embeddedSites&quot;:{&quot;wikiwiki&quot;:{&quot;name&quot;:&quot;スペースシューター&quot;,&quot;url&quot;:&quot;https://wikiwiki.jp/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%83%BC%E3%82%B9%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC#comment&quot;}},&quot;forumSlug&quot;:&quot;spla3&quot;,&quot;forumTitle&quot;:&quot;Splatoon3 - スプラトゥーン3 攻略&amp;検証 Wiki&quot;,&quot;lastCommentNumber&quot;:6019,&quot;lastCommentedAt&quot;:&quot;Fri, 16 Jan 2026 18:15:20 +0900&quot;,&quot;topicNumber&quot;:157,&quot;topicTitle&quot;:&quot;スペースシューター&quot;,&quot;url&quot;:&quot;https://z.wikiwiki.jp/spla3/topic/157&quot;},{&quot;embeddedSites&quot;:{&quot;wikiwiki&quot;:{&quot;name&quot;:&quot;フデ属&quot;,&quot;url&quot;:&quot;https://wikiwiki.jp/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%95%E3%83%87%E5%B1%9E#comment&quot;}},&quot;forumSlug&quot;:&quot;spla3&quot;,&quot;forumTitle&quot;:&quot;Splatoon3 - スプラトゥーン3 攻略&amp;検証 Wiki&quot;,&quot;lastCommentNumber&quot;:280,&quot;lastCommentedAt&quot;:&quot;Fri, 16 Jan 2026 17:08:52 +0900&quot;,&quot;topicNumber&quot;:127,&quot;topicTitle&quot;:&quot;フデ属&quot;,&quot;url&quot;:&quot;https://z.wikiwiki.jp/spla3/topic/127&quot;},{&quot;embeddedSites&quot;:{&quot;wikiwiki&quot;:{&quot;name&quot;:&quot;14式竹筒銃・甲&quot;,&quot;url&quot;:&quot;https://wikiwiki.jp/splatoon3mix/%E3%83%96%E3%82%AD/14%E5%BC%8F%E7%AB%B9%E7%AD%92%E9%8A%83%E3%83%BB%E7%94%B2#comment&quot;}},&quot;forumSlug&quot;:&quot;spla3&quot;,&quot;forumTitle&quot;:&quot;Splatoon3 - スプラトゥーン3 攻略&amp;検証 Wiki&quot;,&quot;lastCommentNumber&quot;:2307,&quot;lastCommentedAt&quot;:&quot;Fri, 16 Jan 2026 16:19:34 +0900&quot;,&quot;topicNumber&quot;:81,&quot;topicTitle&quot;:&quot;14式竹筒銃・甲&quot;,&quot;url&quot;:&quot;https://z.wikiwiki.jp/spla3/topic/81&quot;},{&quot;embeddedSites&quot;:{&quot;wikiwiki&quot;:{&quot;name&quot;:&quot;サーモンラン雑談/ログ2&quot;,&quot;url&quot;:&quot;https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3#commentA&quot;}},&quot;forumSlug&quot;:&quot;spla3&quot;,&quot;forumTitle&quot;:&quot;Splatoon3 - スプラトゥーン3 攻略&amp;検証 Wiki&quot;,&quot;lastCommentNumber&quot;:41197,&quot;lastCommentedAt&quot;:&quot;Fri, 16 Jan 2026 15:54:40 +0900&quot;,&quot;topicNumber&quot;:244,&quot;topicTitle&quot;:&quot;サーモンラン雑談/ログ2&quot;,&quot;url&quot;:&quot;https://z.wikiwiki.jp/spla3/topic/244&quot;},{&quot;embeddedSites&quot;:{&quot;wikiwiki&quot;:{&quot;name&quot;:&quot;ブラスター属&quot;,&quot;url&quot;:&quot;https://wikiwiki.jp/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC%E5%B1%9E#comment&quot;}},&quot;forumSlug&quot;:&quot;spla3&quot;,&quot;forumTitle&quot;:&quot;Splatoon3 - スプラトゥーン3 攻略&amp;検証 Wiki&quot;,&quot;lastCommentNumber&quot;:205,&quot;lastCommentedAt&quot;:&quot;Fri, 16 Jan 2026 15:54:08 +0900&quot;,&quot;topicNumber&quot;:59,&quot;topicTitle&quot;:&quot;ブラスター属&quot;,&quot;url&quot;:&quot;https://z.wikiwiki.jp/spla3/topic/59&quot;},{&quot;embeddedSites&quot;:{&quot;wikiwiki&quot;:{&quot;name&quot;:&quot;S-BLAST92&quot;,&quot;url&quot;:&quot;https://wikiwiki.jp/splatoon3mix/%E3%83%96%E3%82%AD/S-BLAST92#comment&quot;}},&quot;forumSlug&quot;:&quot;spla3&quot;,&quot;forumTitle&quot;:&quot;Splatoon3 - スプラトゥーン3 攻略&amp;検証 Wiki&quot;,&quot;lastCommentNumber&quot;:1133,&quot;lastCommentedAt&quot;:&quot;Fri, 16 Jan 2026 14:54:32 +0900&quot;,&quot;topicNumber&quot;:211,&quot;topicTitle&quot;:&quot;S-BLAST92&quot;,&quot;url&quot;:&quot;https://z.wikiwiki.jp/spla3/topic/211&quot;},{&quot;embeddedSites&quot;:{&quot;wikiwiki&quot;:{&quot;name&quot;:&quot;オーバーフロッシャー&quot;,&quot;url&quot;:&quot;https://wikiwiki.jp/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AA%E3%83%BC%E3%83%90%E3%83%BC%E3%83%95%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC#comment&quot;}},&quot;forumSlug&quot;:&quot;spla3&quot;,&quot;forumTitle&quot;:&quot;Splatoon3 - スプラトゥーン3 攻略&amp;検証 Wiki&quot;,&quot;lastCommentNumber&quot;:2603,&quot;lastCommentedAt&quot;:&quot;Fri, 16 Jan 2026 14:49:41 +0900&quot;,&quot;topicNumber&quot;:93,&quot;topicTitle&quot;:&quot;オーバーフロッシャー&quot;,&quot;url&quot;:&quot;https://z.wikiwiki.jp/spla3/topic/93&quot;},{&quot;embeddedSites&quot;:{&quot;wikiwiki&quot;:{&quot;name&quot;:&quot;スパッタリー&quot;,&quot;url&quot;:&quot;https://wikiwiki.jp/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%91%E3%83%83%E3%82%BF%E3%83%AA%E3%83%BC#comment&quot;}},&quot;forumSlug&quot;:&quot;spla3&quot;,&quot;forumTitle&quot;:&quot;Splatoon3 - スプラトゥーン3 攻略&amp;検証 Wiki&quot;,&quot;lastCommentNumber&quot;:1298,&quot;lastCommentedAt&quot;:&quot;Fri, 16 Jan 2026 14:47:34 +0900&quot;,&quot;topicNumber&quot;:67,&quot;topicTitle&quot;:&quot;スパッタリー&quot;,&quot;url&quot;:&quot;https://z.wikiwiki.jp/spla3/topic/67&quot;},{&quot;embeddedSites&quot;:{&quot;wikiwiki&quot;:{&quot;name&quot;:&quot;ヴァリアブルローラー&quot;,&quot;url&quot;:&quot;https://wikiwiki.jp/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%B4%E3%82%A1%E3%83%AA%E3%82%A2%E3%83%96%E3%83%AB%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC#comment&quot;}},&quot;forumSlug&quot;:&quot;spla3&quot;,&quot;forumTitle&quot;:&quot;Splatoon3 - スプラトゥーン3 攻略&amp;検証 Wiki&quot;,&quot;lastCommentNumber&quot;:1785,&quot;lastCommentedAt&quot;:&quot;Fri, 16 Jan 2026 14:01:38 +0900&quot;,&quot;topicNumber&quot;:79,&quot;topicTitle&quot;:&quot;ヴァリアブルローラー&quot;,&quot;url&quot;:&quot;https://z.wikiwiki.jp/spla3/topic/79&quot;},{&quot;embeddedSites&quot;:{&quot;wikiwiki&quot;:{&quot;name&quot;:&quot;ジャンプビーコン&quot;,&quot;url&quot;:&quot;https://wikiwiki.jp/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%B8%E3%83%A3%E3%83%B3%E3%83%97%E3%83%93%E3%83%BC%E3%82%B3%E3%83%B3#comment&quot;}},&quot;forumSlug&quot;:&quot;spla3&quot;,&quot;forumTitle&quot;:&quot;Splatoon3 - スプラトゥーン3 攻略&amp;検証 Wiki&quot;,&quot;lastCommentNumber&quot;:2637,&quot;lastCommentedAt&quot;:&quot;Fri, 16 Jan 2026 13:04:56 +0900&quot;,&quot;topicNumber&quot;:120,&quot;topicTitle&quot;:&quot;ジャンプビーコン&quot;,&quot;url&quot;:&quot;https://z.wikiwiki.jp/spla3/topic/120&quot;},{&quot;embeddedSites&quot;:{&quot;wikiwiki&quot;:{&quot;name&quot;:&quot;フィンセント&quot;,&quot;url&quot;:&quot;https://wikiwiki.jp/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%95%E3%82%A3%E3%83%B3%E3%82%BB%E3%83%B3%E3%83%88#comment&quot;}},&quot;forumSlug&quot;:&quot;spla3&quot;,&quot;forumTitle&quot;:&quot;Splatoon3 - スプラトゥーン3 攻略&amp;検証 Wiki&quot;,&quot;lastCommentNumber&quot;:2061,&quot;lastCommentedAt&quot;:&quot;Fri, 16 Jan 2026 11:41:13 +0900&quot;,&quot;topicNumber&quot;:210,&quot;topicTitle&quot;:&quot;フィンセント&quot;,&quot;url&quot;:&quot;https://z.wikiwiki.jp/spla3/topic/210&quot;},{&quot;embeddedSites&quot;:{&quot;wikiwiki&quot;:{&quot;name&quot;:&quot;クイックボム&quot;,&quot;url&quot;:&quot;https://wikiwiki.jp/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%AF%E3%82%A4%E3%83%83%E3%82%AF%E3%83%9C%E3%83%A0#comment&quot;}},&quot;forumSlug&quot;:&quot;spla3&quot;,&quot;forumTitle&quot;:&quot;Splatoon3 - スプラトゥーン3 攻略&amp;検証 Wiki&quot;,&quot;lastCommentNumber&quot;:934,&quot;lastCommentedAt&quot;:&quot;Fri, 16 Jan 2026 11:31:45 +0900&quot;,&quot;topicNumber&quot;:112,&quot;topicTitle&quot;:&quot;クイックボム&quot;,&quot;url&quot;:&quot;https://z.wikiwiki.jp/spla3/topic/112&quot;},{&quot;embeddedSites&quot;:{&quot;wikiwiki&quot;:{&quot;name&quot;:&quot;クアッドホッパーブラック&quot;,&quot;url&quot;:&quot;https://wikiwiki.jp/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%82%A2%E3%83%83%E3%83%89%E3%83%9B%E3%83%83%E3%83%91%E3%83%BC%E3%83%96%E3%83%A9%E3%83%83%E3%82%AF#comment&quot;}},&quot;forumSlug&quot;:&quot;spla3&quot;,&quot;forumTitle&quot;:&quot;Splatoon3 - スプラトゥーン3 攻略&amp;検証 Wiki&quot;,&quot;lastCommentNumber&quot;:1239,&quot;lastCommentedAt&quot;:&quot;Fri, 16 Jan 2026 11:02:48 +0900&quot;,&quot;topicNumber&quot;:99,&quot;topicTitle&quot;:&quot;クアッドホッパーブラック&quot;,&quot;url&quot;:&quot;https://z.wikiwiki.jp/spla3/topic/99&quot;},{&quot;embeddedSites&quot;:{&quot;wikiwiki&quot;:{&quot;name&quot;:&quot;H3リールガンD&quot;,&quot;url&quot;:&quot;https://wikiwiki.jp/splatoon3mix/%E3%83%96%E3%82%AD/H3%E3%83%AA%E3%83%BC%E3%83%AB%E3%82%AC%E3%83%B3D#comment&quot;}},&quot;forumSlug&quot;:&quot;spla3&quot;,&quot;forumTitle&quot;:&quot;Splatoon3 - スプラトゥーン3 攻略&amp;検証 Wiki&quot;,&quot;lastCommentNumber&quot;:534,&quot;lastCommentedAt&quot;:&quot;Fri, 16 Jan 2026 10:50:58 +0900&quot;,&quot;topicNumber&quot;:216,&quot;topicTitle&quot;:&quot;H3リールガンD&quot;,&quot;url&quot;:&quot;https://z.wikiwiki.jp/spla3/topic/216&quot;},{&quot;embeddedSites&quot;:{&quot;wikiwiki&quot;:{&quot;name&quot;:&quot;S-BLAST91&quot;,&quot;url&quot;:&quot;https://wikiwiki.jp/splatoon3mix/%E3%83%96%E3%82%AD/S-BLAST91#comment&quot;}},&quot;forumSlug&quot;:&quot;spla3&quot;,&quot;forumTitle&quot;:&quot;Splatoon3 - スプラトゥーン3 攻略&amp;検証 Wiki&quot;,&quot;lastCommentNumber&quot;:1231,&quot;lastCommentedAt&quot;:&quot;Fri, 16 Jan 2026 09:16:49 +0900&quot;,&quot;topicNumber&quot;:260,&quot;topicTitle&quot;:&quot;S-BLAST91&quot;,&quot;url&quot;:&quot;https://z.wikiwiki.jp/spla3/topic/260&quot;},{&quot;embeddedSites&quot;:{&quot;wikiwiki&quot;:{&quot;name&quot;:&quot;ギアパワー&quot;,&quot;url&quot;:&quot;https://wikiwiki.jp/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC#comment&quot;}},&quot;forumSlug&quot;:&quot;spla3&quot;,&quot;forumTitle&quot;:&quot;Splatoon3 - スプラトゥーン3 攻略&amp;検証 Wiki&quot;,&quot;lastCommentNumber&quot;:2702,&quot;lastCommentedAt&quot;:&quot;Fri, 16 Jan 2026 08:16:26 +0900&quot;,&quot;topicNumber&quot;:128,&quot;topicTitle&quot;:&quot;ギアパワー&quot;,&quot;url&quot;:&quot;https://z.wikiwiki.jp/spla3/topic/128&quot;}]}"></div>

</div>
<div style="text-align:center">〔<a href="https://z.wikiwiki.jp/spla3/"  rel="nofollow"><strong>zawazawaで見る</strong></a>〕</div>
<div class="wikicolor" style="color:#f80">
<div class="recentdetail-container" data-recent-hash="42fcba72d9a4528fa69e938bf99900df"></div>

</div>
<div style="text-align:center">〔<a href="/splatoon3mix/%E4%BA%BA%E6%B0%97100" title="人気100" class="rel-wiki-page"><strong>人気</strong></a>/<a href="/splatoon3mix/%E4%BB%8A%E6%97%A5100" title="今日100" class="rel-wiki-page"><strong>今日人気</strong></a>〕〔<a href="/splatoon3mix/RecentChanges" title="RecentChanges" class="rel-wiki-page"><strong>最新</strong></a>〕</div>
<hr class="full_hr" />
<div style="text-align:right">〔<a href="https://wikiwiki.jp/splatoon3mix/?cmd=edit&amp;page=MenuBar"  rel="nofollow">MENU編集</a>〕<br />
今日.<span class="wikiwiki-counter wikiwiki-counter-today">?</span>　昨日.<span class="wikiwiki-counter wikiwiki-counter-yesterday">?</span><br />
同接.<span class="wikiwiki-online">?</span> 総合.<span class="wikiwiki-counter wikiwiki-counter-total">?</span></div>                </div>
                <div class="admenu-sticky">
<!-- /19033742/WIKIWIKI_PC_MENU_STICKY -->
<div id='div-gpt-ad-1567834179057-0'></div>
</div>
<script>
if (document.documentElement.clientWidth > 805 && !wi_ismobile && wi_group === 'N' && wi_agreement === 'false' && !wi_isinbound &&
    document.getElementById('body').clientHeight - document.getElementById('menubar').clientHeight > 1000) {
    googletag.cmd.push(() => {
        googletag.display(
            googletag.defineSlot('/19033742/WIKIWIKI_PC_MENU_STICKY', [[120,600],[160,600],[1,1]], 'div-gpt-ad-1567834179057-0').addService(googletag.pubads())
        );
    });
    defineSlotFlux.push({"slotID": "div-gpt-ad-1567834179057-0", "sizes": [[160,600]], "slotName":"WIKIWIKI_PC_MENU_STICKY"});
}
</script>
<style>
.admenu-sticky {
    display: flex;
    justify-content: center;
    position: -webkit-sticky;
    position: sticky;
    margin-top: 50px;
    top: 50px;
    max-width: 160px;
    margin-left: auto;
    margin-right: auto;
}
</style>

            </div>
            </div>

            <div class="container">
            <div id="note">
                <hr class="note_hr" /><a id="notefoot_1" href="#notetext_1" class="note_super">*1</a>
<span class="small">前作と出現順が変更</span><br>
<a id="notefoot_2" href="#notetext_2" class="note_super">*2</a>
<span class="small">左側3体目として出現する場合と後方3体目として出現する場合がある</span><br>
<a id="notefoot_3" href="#notetext_3" class="note_super">*3</a>
<span class="small">前作にない射撃位置</span><br>
<a id="notefoot_4" href="#notetext_4" class="note_super">*4</a>
<span class="small">なお、通常のシャケや<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a>に対してはこの性質は働かず、飛び移れる場合は飛び移り、そうでない場合は反対側へ先回りしようとする。定点維持も困難で、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>時に安全地帯として活用することは極めて難しいと思われる</span><br>
<a id="notefoot_5" href="#notetext_5" class="note_super">*5</a>
<span class="small">対岸右の砂浜の坂道は出現直後の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#chum" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">中シャケ</a>に退路を断たれる。</span><br>            </div>
        </div>
    
    <div id="footer">
                <div class="container">
            <hr />
            <div class="footer-block clearfix">
                <div class="footer-block-item-left" id="signature">
                    <!-- google_ad_section_start(weight=ignore) -->
                    レンタルWIKI by <a href="https://wikiwiki.jp/" title="無料レンタルWIKIサービス">WIKIWIKI.jp*</a>&nbsp;/&nbsp;
                    Designed by <a href="https://wikiwiki.jp/pp/skin-design-policy" title="スキンデザインのご利用についてのお願い">Olivia</a>&nbsp;/&nbsp;
                    <a href="https://wikiwiki.jp/pp/aboutad" title="広告について">広告について</a>&nbsp;/&nbsp;
                    無料レンタル掲示板 <a href="https://z.wikiwiki.jp/" title="zawazawa">zawazawa</a>
                    <!-- google_ad_section_end -->
                </div>
                <div class="footer-block-item-right">
                    <div class="footer-mixirss">
                        <div class="toolbar"><a href="/splatoon3mix/::cmd/mixirss" title="最終更新のRSS" rel="nofollow"><span class="system-icon rss"></span></a></div>                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
html:has(
  body[style*="position: fixed"], 
  #im_interstitial_pc[style*="display: flex"]
) #gpt_unit_\/19033742\/WIKIWIKI_SP_OVERLAY_ANCHOR_0 {
  display: none !important;
}
</style><div id="pageload" style="display: none" data-pageload="{&quot;time&quot;:{&quot;all&quot;:{&quot;real&quot;:0.015039205551147461,&quot;cost&quot;:0.15909314155578613},&quot;body&quot;:{&quot;real&quot;:0.003092050552368164,&quot;cost&quot;:0.049736976623535156},&quot;main&quot;:{&quot;real&quot;:0.04664492607116699,&quot;cost&quot;:0.04664492607116699},&quot;menu&quot;:{&quot;real&quot;:0.09711790084838867,&quot;cost&quot;:0.09711790084838867},&quot;head&quot;:{&quot;real&quot;:0.0001780986785888672,&quot;cost&quot;:0.0001780986785888672},&quot;foot&quot;:{&quot;real&quot;:0.00011301040649414062,&quot;cost&quot;:0.00011301040649414062}},&quot;include&quot;:8,&quot;memory&quot;:1774176,&quot;io&quot;:{&quot;read&quot;:{&quot;files&quot;:1,&quot;bytes&quot;:8,&quot;locks&quot;:1},&quot;write&quot;:{&quot;files&quot;:0,&quot;bytes&quot;:0,&quot;locks&quot;:0},&quot;directory&quot;:{&quot;traversals&quot;:0,&quot;files&quot;:0},&quot;misc&quot;:57},&quot;contentSize&quot;:{&quot;all&quot;:260503,&quot;body&quot;:84480},&quot;timestamp&quot;:&quot;2026-01-16 19:26:28&quot;}"></div>

<script type="text/javascript" src="https://cdn.wikiwiki.jp/to/w/common/assets/dist/wikiwiki-2ee375d6199d21f58b1a.min.js"></script>
<script type="text/javascript">
    bootLazy.addJqPluginInit('.fold-container', function() {
        this.fold({
            buttonSelector: '.fold-toggle-button',
            openClassName: 'fold-open'
        });
    });
</script>
<script>
    bootLazy.addJqPluginInit('.zawazawa-embed', function() {
        this.zcommentResize();
    });
</script>
<div id="wikiwiki-pageview-counter" data-endpoint="https://counter.wikiwiki.jp/c/splatoon3mix/pv/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF" style="display: none;"></div>
<script>
    $('#wikiwiki-pageview-counter').pageview();
</script>
<script>
bootLazy.addJqPluginInit('.plugin-randommes', function() {
    this.randommes({
        url: '/splatoon3mix/::cmd/randommes',
        stackName: 'lazy_fetch_stack'
    });
});
</script>
<script type="text/javascript">
    bootLazy.addJqPluginInit('.navfold-container', function() {
        this.navfold({
            wiki: "splatoon3mix",
            persistence: {
                'menubar': '#menubar'
            }
        });
    });
</script>
    <script type="text/javascript">
        bootLazy.addJqPluginInit('.zawazawa-recent', function() {
            this.zrecent();
        });
    </script>
<script type="text/javascript">
    bootLazy.addJqPluginInit('.recentdetail-container[data-recent-hash="42fcba72d9a4528fa69e938bf99900df"]', function() {
        this.recentdetail({"timestamp":1768555677,"groupBoundary":["5m","10m","15m","30m","1h","3h","6h","12h","24h"],"list":[{"time":1768555677,"page":"Xマッチ","link":"/splatoon3mix/X%E3%83%9E%E3%83%83%E3%83%81"},{"time":1768547776,"page":"トリカラバトル指南","link":"/splatoon3mix/%E3%83%88%E3%83%AA%E3%82%AB%E3%83%A9%E3%83%90%E3%83%88%E3%83%AB%E6%8C%87%E5%8D%97"},{"time":1768543334,"page":"ブキ/スプラチャージャー","link":"/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC"},{"time":1768543169,"page":"ブキ/スプラチャージャーFRST","link":"/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BCFRST"},{"time":1768532665,"page":"サーモンラン/開催履歴","link":"/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E9%96%8B%E5%82%AC%E5%B1%A5%E6%AD%B4"},{"time":1768528861,"page":"ブキ/クアッドホッパーブラック","link":"/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%82%A2%E3%83%83%E3%83%89%E3%83%9B%E3%83%83%E3%83%91%E3%83%BC%E3%83%96%E3%83%A9%E3%83%83%E3%82%AF"},{"time":1768528011,"page":"ブキ/H3リールガンD","link":"/splatoon3mix/%E3%83%96%E3%82%AD/H3%E3%83%AA%E3%83%BC%E3%83%AB%E3%82%AC%E3%83%B3D"},{"time":1768526021,"page":"ブキ/.52ガロン","link":"/splatoon3mix/%E3%83%96%E3%82%AD/.52%E3%82%AC%E3%83%AD%E3%83%B3"},{"time":1768522261,"page":"フェス","link":"/splatoon3mix/%E3%83%95%E3%82%A7%E3%82%B9"},{"time":1768519142,"page":"ブキ/H3リールガン","link":"/splatoon3mix/%E3%83%96%E3%82%AD/H3%E3%83%AA%E3%83%BC%E3%83%AB%E3%82%AC%E3%83%B3"}]});
    });
</script>
    <script>
        bootLazy.addJqPluginInit('#responsive-navigation', function() {
            this.responsiveNavigation({
                menuBarSelector: '#menubar',
                editMenuSelector: '#edit-menu',

                mainContentsBottomElement: '#main-contents-bottom',
                sidebarBottomElement: '#sidebar-bottom',
                menuBarContainerElement: '#contents .column-left',
                footerElement: '#footer',

                overlayAdRenderedEventName: 'overlay-ad-rendered',
                overlayAdMarginTop: 25
            });
        });
    </script>
    <script>
        $('#share-button-root').sharePanel({
            title: "トキシラズいぶし工房 - Splatoon3 - スプラトゥーン3 攻略＆検証  Wiki*",
            controlPanelUrl: "https:\/\/c.wikiwiki.jp\/wiki\/splatoon3mix\/design",
            imageUrl: "https:\/\/icon.wikiwiki.jp\/symbolicon\/splatoon3mix\/ogImage\/f1fa837847c5.png",
            description: "このサイトは、スプラトゥーン3の攻略・検証を目的とした非公式wikiです。",
            shareUrl: "https:\/\/wikiwiki.jp\/splatoon3mix\/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3\/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8\/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF",
            shortUrlRequestUrl: "\/splatoon3mix\/::cmd\/short_url?mode=json&page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF",
            hasOgSettings: true,
        })
    </script>
<script>
    $('#admin-contact-root').adminContact({
        logoImgUrl: "https:\/\/icon.wikiwiki.jp\/symbolicon\/splatoon3mix\/appleTouchIcon\/dbed77543aea.png",
        pageTitle: "Splatoon3 - スプラトゥーン3 攻略＆検証  Wiki*",
        controlPanelUrl: "https:\/\/c.wikiwiki.jp\/wiki\/splatoon3mix\/settings",
        contact: "管理掲示板：https:\/\/zawazawa.jp\/spla3\/topic\/191",
        helpLink: 'https://wikiwiki.jp/pp/admin_contact',
    });
</script>
<script>
$("#load-panel-root").loadpanel({
    dataSelector: "#pageload",
    helpLink: 'https://wikiwiki.jp/pp/page_load_panel'
});
</script>
<script>
    $('.admin-login-status').adminLoginStatus({
        cookieName: 'login_session',
    });
</script>
<script>
    $(function() {
        $('.search-words').searchWordHighlight({
            paramName: 'word',
            selector: "#content,#note",
            limit: 10,
            markedClassResolver: function (i) { return "word" + i; }
        });
    });
</script>
<script>$(".realtime-date").realtimeDate();</script>
<script>
    $("body").notificationBar();
</script>
<script>
$("#contents").anchorLink({
    url: '/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF',
});
</script>
    <script>
        bootLazy.addPlainScript(function() {
            tippy('.tooltip');
        });
    </script>
    <script>
        bootLazy.addPlainScript(function() {
            lightbox.option({
                resizeDuration: 0
            });
        });
    </script>
<script>
    $(function() {
        window.bootLazy.bootOn(document);
    });
</script>
<script>
    $(document).pukiwiki();
</script>

<script>
jQuery(function() {
    $('form').usageStatistics({"keyName":"usageStatistics","smsAuth":false,"hasPosted":false});
    $(document).browsingStatistics({
        keyName: 'browsingStatistics'
    });
});
</script>
</body>
</html>
