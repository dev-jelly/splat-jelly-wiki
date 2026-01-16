<!DOCTYPE html>
<html lang="ja">
<head prefix="og: https://ogp.me/ns# fb: https://ogp.me/ns/fb# article: https://ogp.me/ns/article#">
    <meta charset="utf-8">
    <meta name="viewport" content="width=980">

    <meta name="description" content="このサイトは、スプラトゥーン3の攻略・検証を目的とした非公式wikiです。">
        <meta property="og:url" content="https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3/%E6%94%BB%E7%95%A5" />
    <meta property="og:type" content="article" />
    <meta property="og:title" content="サーモンラン/ビッグラン/攻略 - Splatoon3 - スプラトゥーン3 攻略＆検証  Wiki*" />
    <meta property="og:description" content="このサイトは、スプラトゥーン3の攻略・検証を目的とした非公式wikiです。" />
    <meta property="og:site_name" content="Splatoon3 - スプラトゥーン3 攻略＆検証  Wiki*" />
    <meta property="og:image" content="https://icon.wikiwiki.jp/symbolicon/splatoon3mix/ogImage/f1fa837847c5.png" />
    <title>サーモンラン/ビッグラン/攻略 - Splatoon3 - スプラトゥーン3 攻略＆検証  Wiki*</title>

    <link rel="alternate" href="/splatoon3mix/::cmd/mixirss" type="application/rss+xml" title="RSS" />
        <link rel="icon" href="https://icon.wikiwiki.jp/symbolicon/splatoon3mix/favicon/fcb0de74bdf2.png" />
    <link rel="apple-touch-icon" href="https://icon.wikiwiki.jp/symbolicon/splatoon3mix/appleTouchIcon/dbed77543aea.png" />
    <link rel="manifest" href="https://icon.wikiwiki.jp/symbolicon/splatoon3mix/manifest.webmanifest">
    <link rel="stylesheet" href="https://cdn.wikiwiki.jp/to/w/common/assets/dist/wikiwiki-ad217af191780b21c7f8.min.css" type="text/css">
<link rel="stylesheet" href="https://cdn.wikiwiki.jp/to/w/common/assets/dist/wikiwiki-ex1-ca7abd155d2d8393da00.min.css" type="text/css">
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
    <link rel="canonical" href="https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3/%E6%94%BB%E7%95%A5">
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
                <div id="navigator">[ <a href="/splatoon3mix/">ホーム</a> | <a href="/splatoon3mix/::cmd/newpage?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5" rel="nofollow">新規</a> | <a href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5" rel="nofollow">編集</a> | <a href="/splatoon3mix/::cmd/attach?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5" rel="nofollow">添付</a> ]</div>            </div>
            <div class="toolbox toolbox-desktop toolbar-container">
                <div class="toolbar"><a href="/splatoon3mix/::cmd/list" title="一覧" rel="nofollow"><span class="system-icon toolbar list"></span></a>
<a href="/splatoon3mix/RecentChanges" title="最終更新" rel="nofollow"><span class="system-icon toolbar recent"></span></a>
<a href="/splatoon3mix/::cmd/diff?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5" title="差分" rel="nofollow"><span class="system-icon toolbar diff"></span></a>
<a href="/splatoon3mix/::cmd/backup?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5" title="バックアップ" rel="nofollow"><span class="system-icon toolbar backup"></span></a>
<a href="/splatoon3mix/::cmd/freeze?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5" title="凍結" rel="nofollow"><span class="system-icon toolbar freeze"></span></a>
<a href="/splatoon3mix/::cmd/template?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5" title="複製" rel="nofollow"><span class="system-icon toolbar copy"></span></a>
<a href="/splatoon3mix/::cmd/rename?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5" title="名前変更" rel="nofollow"><span class="system-icon toolbar rename"></span></a>
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
                <ul><li><a href="/splatoon3mix/::cmd/newpage?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5" rel="nofollow"><span class='system-icon toolbar new'></span> 新規</a></li><li><a href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5" rel="nofollow"><span class='system-icon toolbar edit'></span> 編集</a></li><li><a href="/splatoon3mix/::cmd/attach?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5" rel="nofollow"><span class='system-icon toolbar upload'></span> 添付</a></li></ul>
<ul><li><a href="/splatoon3mix/::cmd/list" rel="nofollow"><span class='system-icon toolbar list'></span> 一覧</a></li><li><a href="/splatoon3mix/RecentChanges" rel="nofollow"><span class='system-icon toolbar recent'></span> 最終更新</a></li><li><a href="/splatoon3mix/::cmd/diff?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5" rel="nofollow"><span class='system-icon toolbar diff'></span> 差分</a></li><li><a href="/splatoon3mix/::cmd/backup?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5" rel="nofollow"><span class='system-icon toolbar backup'></span> バックアップ</a></li></ul>
<ul><li><a href="/splatoon3mix/::cmd/freeze?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5" rel="nofollow"><span class='system-icon toolbar freeze'></span> 凍結</a></li><li><a href="/splatoon3mix/::cmd/template?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5" rel="nofollow"><span class='system-icon toolbar copy'></span> 複製</a></li><li><a href="/splatoon3mix/::cmd/rename?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5" rel="nofollow"><span class='system-icon toolbar rename'></span> 名前変更</a></li></ul>
<ul><li><a href="/splatoon3mix/::cmd/help" rel="nofollow"><span class='system-icon toolbar help'></span> ヘルプ</a></li></ul>

            </div>
        </div>
    </div>    </div>

    <div class="container">
        <div class="clearfix">
            <div id="breadcrumbs" class="system-ui">
                <div id="topicpath"><a href="/splatoon3mix/" title="FrontPage"><i class="fa fa-home" style="margin-left: 6px; display: inline-block; min-width: 1.2em;"></i></a> &gt; <a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン">サーモンラン</a> &gt; <a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン">ビッグラン</a> &gt; 攻略</div>            </div>
            <div id="system-icon-container" class="system-ui">
                                <span id="share-button-root"></span>                <span id="admin-contact-root" class="single-system-icon"></span>
                <div id="load-panel-root"></div>
                <span id="admin-login" class="single-system-icon">
                    
<a class="admin-login-status" href="/splatoon3mix/::cmd/admin_login?return_to=%2Fsplatoon3mix%2F%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5" title="未ログイン">
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
                                            <h1 class="title">サーモンラン/ビッグラン/攻略</h1>
                                                                <div id="lastmodified">
                            Last-modified: 2025-12-15 (月) 15:45:14                                                    </div>
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
                                        <div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">目次</div>
    <div class="fold-content visible-on-open"><div class="contents">
<a id="contents-index"></a>
<ul class="list1"><li><a href="#ic6ae55f">はじめに </a>
<ul class="list2"><li><a href="#Wahoo_World">スメーシーワールド </a></li>
<li><a href="#Inkblot_Art_Academy">海女美術大学 </a></li>
<li><a href="#Undertow_Spillway">マテガイ放水路 </a></li>
<li><a href="#Umami_Ruins">ナンプラー遺跡 </a></li>
<li><a href="#Barnacle_and_Dime">タラポートショッピングパーク </a></li>
<li><a href="#Eeltail_Alley">ゴンズイ地区 </a></li>
<li><a href="#BIG_Big_run">各地で同時発生 </a></li>
<li><a href="#Grand_Splatlands_Bowl">グランドバンカラアリーナ </a></li></ul></li>
<li><a href="#comment">コメント</a></li></ul>
</div>
</div>
</div>
<h2 id="h2_content_1_0" >はじめに  <a class="anchor_super" name ="ic6ae55f"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5&id=ic6ae55f" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<p>このページでは、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>のステージ別の攻略情報をまとめている。<br />
シャケの侵攻を食い止め、ハイスコア達成を目指すアルバイターの皆様に役立てば幸いだ。<br />
また、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>の発生は短期間である事から、通常のバイトに比べて攻略情報が集まり辛い。<br />
有用な情報をご存知の方は、ぜひ編集・追記をお願いしたい。</p>
<h3 id="h3_content_1_1" class="heading-after-first"><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%B9%E3%83%A1%E3%83%BC%E3%82%B7%E3%83%BC%E3%83%AF%E3%83%BC%E3%83%AB%E3%83%89" title="ステージ/スメーシーワールド" class="rel-wiki-page">スメーシーワールド</a>  <a class="anchor_super" name ="Wahoo_World"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5&id=Wahoo_World" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">クリックで展開</div>
    <div class="fold-content visible-on-open"><p><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3/%E6%94%BB%E7%95%A5/::ref/%E3%82%B9%E3%83%A1%E3%83%BC%E3%82%B7%E3%83%BC%E3%83%AF%E3%83%BC%E3%83%AB%E3%83%89_%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3.webp.webp?rev=16b564c3377e49a256ecbe9bcaf0e971&amp;t=20230903163719" alt="スメーシーワールド_ビッグラン.webp" title="スメーシーワールド_ビッグラン.webp" width="1075" height="570"  loading="lazy"></p>
<h4 id="h4_content_4_0" >概要</h4>

<p><span class="wikicolor" style="color:silver">記念すべき</span>第1回、第9回<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>の発生地。<br />
バトルステージの<a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%B9%E3%83%A1%E3%83%BC%E3%82%B7%E3%83%BC%E3%83%AF%E3%83%BC%E3%83%AB%E3%83%89" title="ステージ/スメーシーワールド" class="rel-wiki-page">スメーシーワールド</a>が<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>用に改装されたステージ。</p>
<p>ステージ中に配置されたクマサン商会のロゴの入った壁は塗ることができる。<br />
他のステージと違い、シャケが登って来ることのできない段差が存在している。<br />
通常時や干潮では海岸からだけでなく、ステージ中に配置されたカンケツセンからもシャケが湧き出てくる。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E5%B7%A8%E5%A4%A7%E3%82%BF%E3%83%84%E3%83%9E%E3%82%AD" title="サーモンラン/特殊な状況/巨大タツマキ" class="rel-wiki-page">巨大タツマキ</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%89%E3%82%B9%E3%82%B3%E3%82%A4%E5%A4%A7%E9%87%8F%E7%99%BA%E7%94%9F" title="サーモンラン/特殊な状況/ドスコイ大量発生" class="rel-wiki-page">ドスコイ大量発生</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1%E6%8E%A2%E3%81%97" title="サーモンラン/特殊な状況/キンシャケ探し" class="rel-wiki-page">キンシャケ探し</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%89%E3%83%AD%E3%82%B7%E3%83%A3%E3%82%B1%E5%99%B4%E5%87%BA" title="サーモンラン/特殊な状況/ドロシャケ噴出" class="rel-wiki-page">ドロシャケ噴出</a>の4つのイベントが発生しない。</p>
<p>ステージ全体はとても広く、湧きポイントから遠く離れた場所にも行くことができる。しかし、湧きポイントからコンテナまでの距離は通常のステージとあまり変わらないので、普通にプレイする分にはむしろ狭く感じるほどだろう。</p>
<h4 id="h4_content_5_0" >通常時</h4>

<p>イクラコンテナの位置と開始地点は通常のリスポーン地点付近。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>ステージの満潮より少し広い程度なのである程度は勝手に寄ってくる。<br />
プレイヤー側に有利な高台がいくつもあり、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a>の処理が楽。<br />
シャケたちの発生する場所がさほど遠くないこと、イクラ投げでコンテナのすぐ近くまで運べるため、海岸マンがそこまで害悪というわけでもない。<br />
ただし、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#snatcher" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">タマヒロイ</a>の発生位置がコンテナ裏のため<strong>遠くのイクラを運ぶ意味は薄い</strong>。イクラを運んできてくれた<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#snatcher" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">タマヒロイ</a>をコンテナ近くで倒すことで大量納品が期待できる。むしろ、<strong>帰宅中の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#snatcher" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">タマヒロイ</a>を見逃さない</strong>ことに注力したい。<br />
DPSが高いブキはできるだけオオモノシャケを<strong>坂の上まで寄せて</strong>倒し、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>や起動した<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a>等は存分にリスキルすると良い。<span class="wikicolor" style="color:silver"><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%8F%E3%82%A4%E3%83%89%E3%83%A9%E3%83%B3%E3%83%88" title="ブキ/ハイドラント" class="rel-wiki-page">ハイドラント</a>が適任であるが、機動力に難があるため注意。</span></p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>は左右の高台で迎撃する。どちらを使っても良いのでうまく集合したい。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>は反対側の高台で納品の時間稼ぎ可。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>に接触しやすく位置がややシビアだが、高台奥の追加ブロック(塗れる壁の上部)の外側寄りに立つと<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>が完全に静止する。外側すぎて落ちても壁が塗れるので戻ってこられる。</p>
<p><strong>高台にボムを置くことで<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>の両翼を壊せる場所</strong></p>
<ul class="list1"><li>正面・2回目の発射時・左高台に置くと届く。</li></ul>
<h4 id="h4_content_6_0" >満潮時</h4>

<p>満潮、干潮時は中央に移動する。ジャンプ先の位置でどちらか見分けることが可能。満潮だとカゴの周囲を囲むような形。<br />
満潮時は狭い中央に向かって4方向からシャケがやってくる。難易度は高くなるが稼ぐチャンス。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a>がコンテナ横に刺さると身動きが取れず非常にキケンなので最優先で撃破したい。<br />
霧が起きてしまうとバラバラにやってくるため、運よく<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a>＆高火力<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%94%E3%83%8A%E3%83%BC%E5%B1%9E" title="ブキ/スピナー属" class="rel-wiki-page">スピナー</a>が来ないと詰む可能性が高い。平坦な場所が多いため、<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%9B%E3%83%83%E3%83%97%E3%82%BD%E3%83%8A%E3%83%BC" title="ブキ/スペシャルウェポン/ホップソナー" class="rel-wiki-page">ホップソナー</a>が通常以上に有効。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>時は地獄を見ることになる。4方向からシャケが猛スピードでやってくる上、ステージが狭いため、少しでも崩れると終わってしまう。<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC%E5%B1%9E" title="ブキ/ローラー属" class="rel-wiki-page">ローラー</a>が2人以上いないと安心できないかもしれない。<br />
納品が厳しくなるが塗れない床を渡った先の高台が安地。納品の時間稼ぎ用に。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>は正面高台を使えば単騎で止められる。<br />
ほか、カゴ近くの塗れない床の僅かな段差のうち下の方(ナワバリでいう回転床の方)でも良い。</p>
<h4 id="h4_content_7_0" >干潮時</h4>

<p>同じく中央に移動する。ジャンプ先は片側に寄る。<br />
干潮時は片方からしか湧かないため、高台を取り、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>を一掃しよう。<br />
コンテナまではやや遠いが、イクラ投げですぐ近くまで投げられるため、さほど問題にならない。</p>
<p>遠征後、通常ルートが左右とも詰まっている時はカゴ下の空間を通って中央まで帰ることもできる。<br />
実用性は無いが、下の空間に居ても<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a>は真下通過に反応して落下する。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>の攻略法は満潮時と同様。<br />
ナワバリでインクレールの根元がある部分も安地だが、更に納品が厳しい。こちらの実用性は無い。</p>
<p><strong>高台にボムを置くことで<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>の両翼を壊せる場所</strong></p>
<ul class="list1"><li>左側・1回目の発射時・高台の隅に置くと届く。</li>
<li>右側2体目?・2回目の発射時・奥に向け段差上に置くと届く。</li></ul>
</div>
</div>
<h3 id="h3_content_1_2" class="heading-after-first"><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E6%B5%B7%E5%A5%B3%E7%BE%8E%E8%A1%93%E5%A4%A7%E5%AD%A6" title="ステージ/海女美術大学" class="rel-wiki-page">海女美術大学</a>  <a class="anchor_super" name ="Inkblot_Art_Academy"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5&id=Inkblot_Art_Academy" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">クリックで展開</div>
    <div class="fold-content visible-on-open"><p><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3/%E6%94%BB%E7%95%A5/::attach/00B3056E-EC8F-4584-9E40-07C8FCDBCB58.jpeg?rev=d02495f336a324ab516c2a416ade3496&amp;t=20230903163739" title="00B3056E-EC8F-4584-9E40-07C8FCDBCB58.jpeg" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3/%E6%94%BB%E7%95%A5/::ref/00B3056E-EC8F-4584-9E40-07C8FCDBCB58.jpeg?rev=d02495f336a324ab516c2a416ade3496&amp;t=20230903163739" alt="00B3056E-EC8F-4584-9E40-07C8FCDBCB58.jpeg" title="00B3056E-EC8F-4584-9E40-07C8FCDBCB58.jpeg" width="310" height="163"  loading="lazy"></a><br />
<a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3/%E6%94%BB%E7%95%A5/::attach/54FF238E-2E81-4D3A-A561-B08086B5311F.png?rev=789a5e1b137f40862b58e00eb642cdc1&amp;t=20230903163729" title="54FF238E-2E81-4D3A-A561-B08086B5311F.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3/%E6%94%BB%E7%95%A5/::ref/54FF238E-2E81-4D3A-A561-B08086B5311F.png.webp?rev=789a5e1b137f40862b58e00eb642cdc1&amp;t=20230903163729" alt="54FF238E-2E81-4D3A-A561-B08086B5311F.png" title="54FF238E-2E81-4D3A-A561-B08086B5311F.png" width="511" height="285"  loading="lazy"></a></p>
<h4 id="h4_content_9_0" >概要</h4>

<div style="margin:0 0 0 auto;text-align:right;">
  <a href="/splatoon3mix/::cmd/areaedit?areaedit_no=0&inline_plugin=0&page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5&digest=db5098d9724ebaa8013fd8140c271818" title="0" name="areaedit_block_0" rel="nofollow"
     class="security-check-interrupt" data-trolling-defence="on" data-page="サーモンラン/ビッグラン/攻略"
     data-interrupt="none" data-unfreeze-url=""
  >[編集]</a>
</div>
<p>第2回、第10回<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>の発生地。バトルステージの<a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E6%B5%B7%E5%A5%B3%E7%BE%8E%E8%A1%93%E5%A4%A7%E5%AD%A6" title="ステージ/海女美術大学" class="rel-wiki-page">海女美術大学</a>が<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>用に改装されたステージ。なお、ビッグ<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>以降は地形の一部が変更されている。</p>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">ステージ改修(ビッグ<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>以降)</div>
    <div class="fold-content visible-on-open"><p>通常時コンテナ左前方が<a href="/splatoon3mix/%E3%82%AC%E3%83%81%E3%82%A2%E3%82%B5%E3%83%AA" title="ガチアサリ" class="rel-wiki-page">ガチアサリ</a>用のスロープ→<a href="/splatoon3mix/%E3%82%AC%E3%83%81%E3%83%A4%E3%82%B0%E3%83%A9" title="ガチヤグラ" class="rel-wiki-page">ガチヤグラ</a>用の段差に。一部は古い攻略も含まれているので注意。</p>
</div>
</div>
<p>ステージ中に配置されたクマサン商会のロゴの入った(<a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/%E3%82%B9%E3%83%86%E3%83%83%E3%82%AB%E3%83%BC" title="ロッカー/ステッカー" class="rel-wiki-page">ステッカー</a>が貼られた)壁は塗ることができる。<br />
他のステージと違い、シャケが登って来ることのできない段差が存在している。<br />
通常時や干潮では海岸からだけでなく、ステージ中に配置されたカンケツセンからもシャケが湧き出てくる。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E5%B7%A8%E5%A4%A7%E3%82%BF%E3%83%84%E3%83%9E%E3%82%AD" title="サーモンラン/特殊な状況/巨大タツマキ" class="rel-wiki-page">巨大タツマキ</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%89%E3%82%B9%E3%82%B3%E3%82%A4%E5%A4%A7%E9%87%8F%E7%99%BA%E7%94%9F" title="サーモンラン/特殊な状況/ドスコイ大量発生" class="rel-wiki-page">ドスコイ大量発生</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1%E6%8E%A2%E3%81%97" title="サーモンラン/特殊な状況/キンシャケ探し" class="rel-wiki-page">キンシャケ探し</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%89%E3%83%AD%E3%82%B7%E3%83%A3%E3%82%B1%E5%99%B4%E5%87%BA" title="サーモンラン/特殊な状況/ドロシャケ噴出" class="rel-wiki-page">ドロシャケ噴出</a>の4つのイベントが発生しない。</p>
<p>ルールによって変わる特徴的な中央高台・中央左右の高台は撤去され、代わりに中央左右には塗れるブロックが置かれている。<br />
ステージ全体はかなり狭く、段差を登るルートが限られる。潮位を問わず、<strong><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>がかなりの脅威</strong>となる。<br />
寄せている余裕は無いので<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>は即撃破を心がけたい。</p>
<div></div>
<h4 id="h4_content_11_0" >通常時</h4>

<div style="margin:0 0 0 auto;text-align:right;">
  <a href="/splatoon3mix/::cmd/areaedit?areaedit_no=2&inline_plugin=0&page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5&digest=db5098d9724ebaa8013fd8140c271818" title="1" name="areaedit_block_2" rel="nofollow"
     class="security-check-interrupt" data-trolling-defence="on" data-page="サーモンラン/ビッグラン/攻略"
     data-interrupt="none" data-unfreeze-url=""
  >[編集]</a>
</div>
<p>イクラコンテナは通常の自陣高台付近。開始地点はもう一段手前の高台となる。<br />
敵陣高台にはカンケツセンがありそこからもシャケが湧く。<br />
中央低地は左右が海岸なので居座り続けると危険。<br />
塗れるブロックや干潮コンテナ台の上は対<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>等の安置だがオオモノの攻撃には無力なので一時しのぎ用となる。<br />
だからといって自陣に引き篭もると<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%B7%E3%82%A7%E3%82%B1%E3%83%8A%E3%83%80%E3%83%A0" title="サーモンラン/ステージ/シェケナダム" class="rel-wiki-page">シェケナダム</a>やドンブラコの満潮時のように圧殺される。自陣奥・時には敵陣も含めてステージを広く使いたい。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>はもちろん、<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="※初回は左側の部分が段差ではなく坂になっていた">左側</span>に居座る<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a>の脅威度も高い。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a>は<del>壁にめり込んで半身撃ちをしてきやすいので通常よりも狙い辛いが、</del>シャケを巻き込みやすい位置で止まることが多く、倒した時のリターンは大きめ。積極的に狙いたい。<br />
開催2回目以降は左側が段差になったためこちらに有利に。雑魚に囲まれた際の退避ルートやインク回復や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a>狙い時に。<br />
また、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a>が複数詰まっている時は上を渡ってゼンメツさせたい。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a>は高台の近くに来るものが多く比較的下から処理しやすいが、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>はその高台が遮蔽になる位置に陣取るので要警戒。</p>
<p><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%9B%E3%83%83%E3%83%97%E3%82%BD%E3%83%8A%E3%83%BC" title="ブキ/スペシャルウェポン/ホップソナー" class="rel-wiki-page">ホップソナー</a>を早めに使う場合はカゴ横に置くか中央低地に投げ込むと良いだろう。干潮コンテナ台の上にソナーを置くと通常コンテナのある高さまで届く。<br />
逆に<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%82%AD%E3%83%A5%E3%82%A6" title="サーモンラン/シャケの種類/テッキュウ" class="rel-wiki-page">テッキュウ</a>の衝撃波も干潮コンテナ台近くまで届くので注意。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>は<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC%E5%B1%9E" title="ブキ/チャージャー属" class="rel-wiki-page">チャージャー</a>がよく居座る&quot; 「  &quot;型の高台が安置。<br />
狭いので味方と射線が被らないように。納品を兼ねてカゴ横にも何名か居ると良いだろう。改修により一本道になったため<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC%E5%B1%9E" title="ブキ/ローラー属" class="rel-wiki-page">ローラー</a>等の壁役が得意なブキが居れば全員カゴ横の方が稼ぎやすい。<br />
居座る位置で誘導先が変わるのでイクラ生産と納品タイムを使い分けたい。<br />
カゴから見て左の高台も安置となるが、シャケに回り込まれ納品が難しいので常用はできない。こちらは立て直し用に。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>も同じ場所が安置。<br />
高台が非常に狭く、高台上からはみ出た体が<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>に接触すると即死なので前に出過ぎないよう注意したい。<br />
右後方の高台も塗れるブロック側寄りに立つと<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>が停止するため安全性が高い。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>には注意する必要があるが立て直し用やタゲ分散用に使える。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B3%E3%83%93%E3%83%A4%E3%81%9F%E3%81%A1#mothership" title="サーモンラン/シャケの種類/ハコビヤたち" class="rel-wiki-page">ハコビヤ</a>では自陣奥にもかなりの<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B3%E3%83%93%E3%83%A4%E3%81%9F%E3%81%A1#chinooks" title="サーモンラン/シャケの種類/ハコビヤたち" class="rel-wiki-page">シャケコプター</a>が飛来する。<br />
中央2人(左右)・自陣2人(奥高台とカゴ周囲)ぐらいでうまく分担したい。<br />
射程のあるブキなら奥高台から<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B3%E3%83%93%E3%83%A4%E3%81%9F%E3%81%A1#chinooks" title="サーモンラン/シャケの種類/ハコビヤたち" class="rel-wiki-page">シャケコプター</a>リスキルが可能。</p>
<ul class="list1"><li>オカシラシャケ・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%84" title="サーモンラン/シャケの種類/タツ" class="rel-wiki-page">タツ</a>について<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%84" title="サーモンラン/シャケの種類/タツ" class="rel-wiki-page">タツ</a>の周回ルートが各シャケの進行ルートや固定位置にかなり干渉するため、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a>や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>といった頭上の標的が<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%84" title="サーモンラン/シャケの種類/タツ" class="rel-wiki-page">タツ</a>に重なり保護されるケースが起こりやすい。</li></ul>
<ul class="list1"><li>地形の利用<br />
<strong>高台にボムを置くことで<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>の両翼を壊せる場所</strong>
<ul class="list2"><li>右側・2回目の発射時・狭い高台の隅に置けば届く。</li>
<li>正面・1回目の発射時・奥側の狭い高台に置けば届く。<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>遠征のついでに。
<div></div></li></ul></li></ul>
<h4 id="h4_content_12_0" >満潮時</h4>

<div style="margin:0 0 0 auto;text-align:right;">
  <a href="/splatoon3mix/::cmd/areaedit?areaedit_no=4&inline_plugin=0&page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5&digest=db5098d9724ebaa8013fd8140c271818" title="2" name="areaedit_block_4" rel="nofollow"
     class="security-check-interrupt" data-trolling-defence="on" data-page="サーモンラン/ビッグラン/攻略"
     data-interrupt="none" data-unfreeze-url=""
  >[編集]</a>
</div>
<p>イクラコンテナと開始地点は普段のリスポーン地点。<br />
コンテナのある左側に比べ、右側のほうは細く長い。長いスロープに塗れない壁もあり段差下は極めて窮屈。<br />
難易度は高くなるが稼ぐチャンス。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>は左後方の塗れない青い箱の上が安置となる。後ろの塗れる壁でインク回復も可能。<br />
狭くて射線が被る&amp;居座ると納品が出来ないのでうまく交代したい。<br />
イカロールを駆使してさらにその奥に乗ることも可能(ページ下部リンク先参照)。<br />
こちらはセンプクによる高速インク回復ができないので補助として。</p>
<p>高DPSブキ多数や<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC%E5%B1%9E" title="ブキ/ローラー属" class="rel-wiki-page">ローラー</a>が居る場合は普通にカゴ横の塗れない坂の頂上でも成立する。</p>
<p><span class="wikicolor" style="color:Silver">ちなみに掲示板の裏はクマサン端末や通常のステージ同様<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>や<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%A8%E3%82%AF%E3%82%B9%E3%83%97%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC" title="ブキ/エクスプロッシャー" class="rel-wiki-page">エクスプロッシャー</a>でしか塗れない壁。</span></p>
<div></div>
<h4 id="h4_content_13_0" >干潮時</h4>

<div style="margin:0 0 0 auto;text-align:right;">
  <a href="/splatoon3mix/::cmd/areaedit?areaedit_no=6&inline_plugin=0&page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5&digest=db5098d9724ebaa8013fd8140c271818" title="3" name="areaedit_block_6" rel="nofollow"
     class="security-check-interrupt" data-trolling-defence="on" data-page="サーモンラン/ビッグラン/攻略"
     data-interrupt="none" data-unfreeze-url=""
  >[編集]</a>
</div>
<p>イクラコンテナは中央。<br />
敵陣高台&amp;両サイドから攻められ難易度が高くなるが稼ぐチャンス。<br />
例によってカゴ前に拘ると<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>に詰まされやすいので自陣高台に避難したり、オオモノ・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>を処理しながらステージ内を駆け回ることも考えたい。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#snatcher" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">タマヒロイ</a>の向きも確認しておこう。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>の安置は通常潮と同じ。<br />
金イクラ生産用と納品タイム用の誘導場所は逆になる。<br />
塗れるブロックの上に長時間居座り、シャケの位置が変わらないと他ステージで不動<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="主に&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;&lt;strong&gt;壁に塗られたインクに潜る様子のこと&lt;/strong&gt;。&lt;br class=&quot;spacer&quot;&gt;&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;では自分をターゲットとしているシャケらをしばらくの間釘付けにできるが、あまり長くやりすぎると&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB&quot; title=&quot;サーモンラン/シャケの種類/グリル&quot; class=&quot;rel-wiki-page&quot;&gt;グリル&lt;/a&gt;のターゲット変更や&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1&quot; title=&quot;サーモンラン/シャケの種類/ザコシャケ&quot; class=&quot;rel-wiki-page&quot;&gt;ザコシャケ&lt;/a&gt;の大ジャンプにより痛い目にあう。&lt;br class=&quot;spacer&quot;&gt;また、セミ中は攻撃できないため、自軍の火力が減るという重大な欠点もある。&lt;br class=&quot;spacer&quot;&gt;「金イクラが大量だが敵の勢いが激しく納品が捗らない状況で、自分が離れた地点でセミをし敵を誘導し、その隙に味方に納品をしてもらう」「デスした味方がウキワになるまでのタイムラグを凌ぐ」など、場面や使いようによっては非常に有用。&lt;br class=&quot;spacer&quot;&gt;&lt;br class=&quot;spacer&quot;&gt;&lt;a href=&quot;/splatoon3mix/%E7%94%A8%E8%AA%9E%E9%9B%86/%E5%AF%BE%E6%88%A6%E9%96%A2%E9%80%A3%E7%94%A8%E8%AA%9E#k58821ab&quot; title=&quot;用語集/対戦関連用語&quot; class=&quot;rel-wiki-page&quot;&gt;&lt;span class=&quot;wikicolor&quot; style=&quot;color:#808080&quot;&gt;[詳細]&lt;/span&gt;&lt;/a&gt;">セミ</span>した時のようにジャンプして殴られる。<br />
処理が遅れているときは位置を変えてシャケを少し歩かせよう。</p>
<div></div>
<h4 id="h4_content_14_0" >コメント欄有益情報リンク</h4>

<p><a class="ext" href="https://zawazawa.jp/spla3/topic/30/59189"  rel="nofollow">タマヒロイマップ<span class="system-icon ext pukiwiki-open-uri" data-href="https://zawazawa.jp/spla3/topic/30/59189" data-frame="_blank"></span></a><br />
<a class="ext" href="https://zawazawa.jp/spla3/topic/30/59332"  rel="nofollow">満潮ラッシュ・グリル安置<span class="system-icon ext pukiwiki-open-uri" data-href="https://zawazawa.jp/spla3/topic/30/59332" data-frame="_blank"></span></a><br />
<a class="ext" href="https://zawazawa.jp/spla3/topic/30/59346"  rel="nofollow">満潮ラッシュ・グリル安置<span class="system-icon ext pukiwiki-open-uri" data-href="https://zawazawa.jp/spla3/topic/30/59346" data-frame="_blank"></span></a><br />
<a class="ext" href="https://zawazawa.jp/spla3/topic/30/59367"  rel="nofollow">マップ付き攻略<span class="system-icon ext pukiwiki-open-uri" data-href="https://zawazawa.jp/spla3/topic/30/59367" data-frame="_blank"></span></a></p>
</div>
</div>
<h3 id="h3_content_1_3" class="heading-after-first"><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%9E%E3%83%86%E3%82%AC%E3%82%A4%E6%94%BE%E6%B0%B4%E8%B7%AF" title="ステージ/マテガイ放水路" class="rel-wiki-page">マテガイ放水路</a>  <a class="anchor_super" name ="Undertow_Spillway"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5&id=Undertow_Spillway" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">クリックで展開</div>
    <div class="fold-content visible-on-open"><p><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3/%E6%94%BB%E7%95%A5/::ref/%E3%83%9E%E3%83%86%E3%82%AC%E3%82%A4%E6%94%BE%E6%B0%B4%E8%B7%AF.png.webp?rev=d9af1f082b1df2158ad12ed2b30708ae&amp;t=20230903163752" alt="マテガイ放水路.png" title="マテガイ放水路.png" width="512" height="288"  loading="lazy"></p>
<h4 id="h4_content_16_0" >概要</h4>

<p>第3回、第11回<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>の発生地。<br />
バトルステージの<a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%9E%E3%83%86%E3%82%AC%E3%82%A4%E6%94%BE%E6%B0%B4%E8%B7%AF" title="ステージ/マテガイ放水路" class="rel-wiki-page">マテガイ放水路</a>が<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>用に改装されたステージ。第11回の際には、地形に少し変化が見られる。</p>
<p>通常潮コンテナの左の坂道が広くなり、塗れるようになった。またコンテナに隣接している高台の下の通路(バトルのステージでは塗れないところ)も塗れるようになった。</p>
<p>ステージ中に配置されたクマサン商会のロゴの入った(<a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/%E3%82%B9%E3%83%86%E3%83%83%E3%82%AB%E3%83%BC" title="ロッカー/ステッカー" class="rel-wiki-page">ステッカー</a>が貼られた)壁は塗ることができる。<br />
他のステージと違い、シャケが登って来ることのできない段差が存在している。<br />
通常時や干潮では海岸からだけでなく、ステージ中に配置されたカンケツセンからもシャケが湧き出てくる。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E5%B7%A8%E5%A4%A7%E3%82%BF%E3%83%84%E3%83%9E%E3%82%AD" title="サーモンラン/特殊な状況/巨大タツマキ" class="rel-wiki-page">巨大タツマキ</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%89%E3%82%B9%E3%82%B3%E3%82%A4%E5%A4%A7%E9%87%8F%E7%99%BA%E7%94%9F" title="サーモンラン/特殊な状況/ドスコイ大量発生" class="rel-wiki-page">ドスコイ大量発生</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1%E6%8E%A2%E3%81%97" title="サーモンラン/特殊な状況/キンシャケ探し" class="rel-wiki-page">キンシャケ探し</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%89%E3%83%AD%E3%82%B7%E3%83%A3%E3%82%B1%E5%99%B4%E5%87%BA" title="サーモンラン/特殊な状況/ドロシャケ噴出" class="rel-wiki-page">ドロシャケ噴出</a>の4つのイベントが発生しない。<br />
さらに、今までの<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>と異なり、<strong><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%82%B0%E3%83%AA%E3%83%AB%E7%99%BA%E9%80%B2" title="サーモンラン/特殊な状況/グリル発進" class="rel-wiki-page">グリル発進</a>が発生しない。</strong><span class="wikicolor" style="color:silver">干潮のナナメの地形のせいだろうか……</span></p>
<p>第3回では、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/Extra%20Wave" title="サーモンラン/特殊な状況/Extra Wave" class="rel-wiki-page">Extra Wave</a>で登場するオカシラシャケの種類が<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>史上初のランダム(<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%A8%E3%82%B3%E3%83%85%E3%83%8A" title="サーモンラン/シャケの種類/ヨコヅナ" class="rel-wiki-page">ヨコヅナ</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%84" title="サーモンラン/シャケの種類/タツ" class="rel-wiki-page">タツ</a>)になっていた。</p>
<p>全体的に塗り面積はともかく<span class="wikicolor" style="color:red"><strong>道が非常に狭い</strong></span>。<br />
どの潮位でも<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>は大きな脅威になる。<span class="wikicolor" style="color:red"><strong><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>は見つけ次第即殺</strong></span>すること。<br />
高台の地形のせいで難しい事も多いが、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%80%E3%82%A4%E3%83%90%E3%83%BC" title="サーモンラン/シャケの種類/ダイバー" class="rel-wiki-page">ダイバー</a>は可能な限り塗ってから倒したい。狭い地形での貴重な安全地帯となる。<br />
コンテナ近辺に刺さった<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a>を放置しているとただでさえ狭い足場をあっという間に塗りつぶされる。<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC%E5%B1%9E" title="ブキ/シューター属" class="rel-wiki-page">シューター</a>、<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC%E5%B1%9E" title="ブキ/ブラスター属" class="rel-wiki-page">ブラスター</a>、<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC%E5%B1%9E" title="ブキ/スロッシャー属" class="rel-wiki-page">スロッシャー</a>などを持った時は出現を見逃さず速やかに処理したい。余裕が無さそうならSPを切ろう。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>の群れにも普段以上に注意。射程端で早めに倒すことを意識しておきたい。<br />
難しく感じる原因の殆どは処理不足に由来するはずなので前作ポラリス満潮のように片っ端からリスキルする意識を持とう。</p>
<p>今回のクマブキは<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC" title="ブキ/クマサン印のチャージャー" class="rel-wiki-page">クマサン印のチャージャー</a>。<br />
オオモノばかりではなく、最長射程の貫通を上手く使って<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#cohock" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ドスコイ</a>を殲滅する意識を持ちたい。<br />
多忙時は必ずしも倒し切る必要はなく、1発ずつ当てておくだけで良い。周りが格段に動きやすくなる。</p>
<h4 id="h4_content_17_0" >通常時</h4>

<p>開始位置は自陣高台周辺。<br />
難易度はやや高めだが(<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%B7%E3%82%A7%E3%82%B1%E3%83%8A%E3%83%80%E3%83%A0" title="サーモンラン/ステージ/シェケナダム" class="rel-wiki-page">シェケナダム</a>や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3" title="サーモンラン/ステージ/難破船ドン・ブラコ" class="rel-wiki-page">難破船ドン・ブラコ</a>と同程度との意見が多い)、非常に稼ぎやすい。<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#snatcher" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">タマヒロイ</a>がコンテナ周辺を通りやすいので、積極的に活用しよう。<br />
コンテナ周辺が自陣、低地が敵陣のようなもので分かりやすい構造。<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%A2%E3%82%B0%E3%83%A9" title="サーモンラン/シャケの種類/モグラ" class="rel-wiki-page">モグラ</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a>のみ寄せ、他オオモノや<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>はコンテナに近づけないようにしたい。</p>
<p>右方向の沸きポイントからコンテナまでがかなり近くなっており、湧きを見落とすとシャケに一気に制圧される。<br />
特に<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>はコンテナ周りだと回避しにくく非常にキケン。<br />
バトル時と同じくコンテナ横高台と金網で繋がっているため塗れない床方面が詰まっていても避難できるが、高台に<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>を連れて行くことになりやすいため常用は推奨しない。</p>
<p>コンテナ横の高台が見通しが良く納品もしやすいため基本的な<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC%E5%B1%9E" title="ブキ/チャージャー属" class="rel-wiki-page">チャージャー</a>ポジションとなる。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA" title="サーモンラン/シャケの種類/コウモリ" class="rel-wiki-page">コウモリ</a>の<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;&lt;strong&gt;&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA&quot; title=&quot;サーモンラン/シャケの種類/コウモリ&quot; class=&quot;rel-wiki-page&quot;&gt;コウモリ&lt;/a&gt;が撃ち出す砲弾&lt;/strong&gt;のこと。撃ち落さないと&lt;a href=&quot;/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%A2%E3%83%A1%E3%83%95%E3%83%A9%E3%82%B7&quot; title=&quot;ブキ/スペシャルウェポン/アメフラシ&quot; class=&quot;rel-wiki-page&quot;&gt;アメフラシ&lt;/a&gt;が発生する。">雨弾</span>も撃ち返しやすく、右側沸きや<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#snatcher" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">タマヒロイ</a>も見やすいため、長射程ブキを持った<strong>視野の広いプレイヤー</strong>が居座りたい。<br />
逆に短射程ブキはコンテナ横の高台に居座るべきではない。一時的に行く分にはOK。</p>
<p>コンテナ周辺が制圧されたとき、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>の接近を許してしまったときは右後方や左後方の高台を使って立て直しを図りたい。<br />
安全なため長射程ブキ向けの場所でもあるが、後方に居座ると納品に参加できないのでノルマに注意。</p>
<p>左前方に湧く<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>は左高台から回り込むと倒しやすい。追加ブロックもあるので下から<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>を倒した後の退避先にするのも良い。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>は2回目の発射位置なら金網端にボムコロでワンパンも可能。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>は右後方の高台(追加ブロック)が安置となり、高台上からボムで一気に狂シャケを倒せる。が、高台からは納品ができず、下で回収しようにもヒカリバエの切り替えタイミングを見誤ると即死するため納品不足に注意。<br />
キャラコンに自信があればコンテナ横高台から撃ちながらイクラ拾い→自分にヒカリバエが付いたらジャンプで安置の壁に飛び移る、といったことも可能。<br />
しっかりとボムを落とし続けて処理すればほぼ無いが、数秒で倒せないとシャケが大ジャンプで高台上に登ってくる。<br />
<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC%E5%B1%9E" title="ブキ/ローラー属" class="rel-wiki-page">ローラー</a>が居る場合は最初はコンテナ周辺でノルマの半分近く金イクラを出しておくと良いだろう。この場合でも<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC%E5%B1%9E" title="ブキ/チャージャー属" class="rel-wiki-page">チャージャー</a>1人が安置に居ると安心できる。</p>
<p><strong>高台にボムを置くことで<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>の両翼を壊せる場所</strong></p>
<ul class="list1"><li>左側・1回目の発射時・高台に置くと届く。</li></ul>
<h4 id="h4_content_18_0" >満潮時</h4>

<p>開始位置は自陣リスポーン地点。<br />
通常潮ほどではないが稼ぎやすい方。<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#snatcher" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">タマヒロイ</a>も活用しよう。</p>
<p>左正面すぐにカンケツセンがあり、納品の安全確保にはシャケを倒し続けてナワバリを確保しておく必要がある。納品するたびにここからシャケが湧いていないか確認しておきたい。<br />
地形が狭いため、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>の群れは縦一直線に並びやすい。<br />
<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC" title="ブキ/クマサン印のチャージャー" class="rel-wiki-page">クマサン印のチャージャー</a>がいれば、1人だけでも十分に対応できるだろう。ただし<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>には注意。<br />
右正面に<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a>が詰まっていたり<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a>が放置されると左湧き<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>からの逃げ場が無くなるため、こちらも早めに処理を。</p>
<p>やはり最奥(通常潮の右沸き)の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%82%AD%E3%83%A5%E3%82%A6" title="サーモンラン/シャケの種類/テッキュウ" class="rel-wiki-page">テッキュウ</a>にも悩まされる。特に<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>。<br />
複数湧いた時はSPで素早く片付けたい。<br />
遠すぎる&amp;イクラ回収困難なので<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>は<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;&lt;strong&gt;&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89&quot; title=&quot;サーモンラン/シャケの種類/カタパッド&quot; class=&quot;rel-wiki-page&quot;&gt;カタパッド&lt;/a&gt;のミサイルポッドを半分だけ破壊して倒さないでおくこと&lt;/strong&gt;。&lt;br class=&quot;spacer&quot;&gt;敢えて倒すのが面倒な&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89&quot; title=&quot;サーモンラン/シャケの種類/カタパッド&quot; class=&quot;rel-wiki-page&quot;&gt;カタパッド&lt;/a&gt;の被害を半減しつつ、他のオオモノシャケを狙う戦法。&lt;br class=&quot;spacer&quot;&gt;この戦法の代償として、&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89&quot; title=&quot;サーモンラン/シャケの種類/カタパッド&quot; class=&quot;rel-wiki-page&quot;&gt;カタパッド&lt;/a&gt;から金イクラを手に入れることができなくなる。&lt;br class=&quot;spacer&quot;&gt;他のオオモノをたくさん倒してカバーすることが必要。">片翼</span>放置も大いにアリ。両翼は絶対に許さないことが大事。<br />
ここに落ちた金イクラは<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#snatcher" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">タマヒロイ</a>任せで良いので速やかに退避することを心掛け、遠征先でデスしないようにしたい。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>は左前方の高台(追加ブロック)が安置。<br />
ただしコンテナ横を狂シャケが横切るため納品は難しめ。<br />
やや遠いが先に壁塗りを済ませてあれば通常潮側の安置で納品時の時間稼ぎができるので適宜活用したい。</p>
<h4 id="h4_content_19_0" >干潮時</h4>

<p>開始位置はステージ中央を囲む形。<br />
コンテナは中央の狭い高台のど真ん中に設置される。<span class="wikicolor" style="color:silver">すごく邪魔</span><br />
コンテナ周りの急斜面と近場の壁は開始直後に塗り切っておくこと。<br />
水没するため壁塗りする場合は<strong>満潮の次ならカウント4まで降りない</strong>ように。(通常潮の次ならカウント6まで)<br />
<span class="wikicolor" style="color:silver"><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC%E5%B1%9E" title="ブキ/シューター属" class="rel-wiki-page"><span class="wikicolor" style="color:silver">シューター</span></a>などで初動塗りをするつもりでLスティック+[ZR]長押しを不用意に入力すると、支給された<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%91%E3%83%96%E3%83%AD" title="ブキ/パブロ" class="rel-wiki-page"><span class="wikicolor" style="color:silver">パブロ</span></a>の塗り進みが暴発して開幕即水没してしまう恐れがあるので注意。</span><br />
急斜面の下から納品するにはイクラ投げが必要そうに見えるが、<span class="wikicolor" style="color:red"><strong>コンテナに十分近づけば下からでもインクを消費せず納品できる</strong></span>ので覚えておきたい。<br />
前後からシャケ湧くため対処が難しく、非常に狭い<strong>コンテナ周辺が危険地帯</strong>となっている。<br />
金イクラを稼ぎにくいどころかノルマ達成すら怪しくなるレベル。<br />
干潮が出た時点でハイスコア狙いは諦め、通常のバイト同様クリアを目指す方向にしたい。</p>
<p>コンテナ周りはシャケに囲まれやすいため、長射程ブキはバトルで使う高台が基本位置。納品難の潮位のため、湧き変更のタイミング等では積極的に納品に参加したい。<br />
沸きポイントは自陣・敵陣高台にもあり、特に<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>にはアクセスし辛いため、SP使用を考えたい。<br />
縦長&amp;ボトルネック地形のため脅威度が跳ね上がる<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>の討伐は迅速に。放置すると数秒ごとに味方や自分がデスすることになる。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a>は寄せる(放置する)と地形に引っかかり斜めになりやすいため乗りづらい。こちらも即殺安定。幸いにもエイム力があれば高台から狙いやすい。</p>
<ul class="list1"><li>自陣・敵陣の見分け方(通話向け)<br />
背景にクマサン商会のヘリが飛んでいる側・通常潮用のコンテナや塗れる追加ブロックがある側が自陣</li></ul>
<h4 id="h4_content_20_0" >コメント欄有益情報リンク</h4>

<p><a class="ext" href="https://zawazawa.jp/spla3/topic/30/78067"  rel="nofollow">攻略<span class="system-icon ext pukiwiki-open-uri" data-href="https://zawazawa.jp/spla3/topic/30/78067" data-frame="_blank"></span></a></p>
<h4 id="h4_content_21_0" >小ネタ</h4>

<ul class="list1"><li><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%9E%E3%83%86%E3%82%AC%E3%82%A4%E6%94%BE%E6%B0%B4%E8%B7%AF" title="ステージ/マテガイ放水路" class="rel-wiki-page">マテガイ放水路</a>はバンカラ街の地下にあるという設定だが、現場にはいつも通りヘリで出勤する。<br />
<span class="wikicolor" style="color:silver">どうやって入っているのだろうか…</span></li>
<li>wave1が干潮の場合、スーパージャンプで中央の柱を貫通する姿が見られる。<br />
<span class="wikicolor" style="color:silver">スーパージャンプ時の地形貫通は今に始まったことでは無いが、やっぱり不自然。</span></li>
<li>ヘリの扉が開いてから数秒後に警報音が聞こえる。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>が起こっていることへの警告か、もう使われていない放水路に水が入ってきているからかはわからない。</li></ul>
</div>
</div>
<h3 id="h3_content_1_4" class="heading-after-first"><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%8A%E3%83%B3%E3%83%97%E3%83%A9%E3%83%BC%E9%81%BA%E8%B7%A1" title="ステージ/ナンプラー遺跡" class="rel-wiki-page">ナンプラー遺跡</a>  <a class="anchor_super" name ="Umami_Ruins"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5&id=Umami_Ruins" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">クリックで展開</div>
    <div class="fold-content visible-on-open"><p><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3/%E6%94%BB%E7%95%A5/::ref/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3_%E3%83%8A%E3%83%B3%E3%83%97%E3%83%A9%E3%83%BC%E9%81%BA%E8%B7%A1.webp?rev=70933d7da9a7b22cb1fc1b8962f329ad&amp;t=20230903163759" alt="ビッグラン_ナンプラー遺跡.webp" title="ビッグラン_ナンプラー遺跡.webp" width="1280" height="720"  loading="lazy"></p>
<h4 id="h4_content_23_0" >概要</h4>

<p>第4回、第12回<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>の発生地。<br />
バトルステージの<a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%8A%E3%83%B3%E3%83%97%E3%83%A9%E3%83%BC%E9%81%BA%E8%B7%A1" title="ステージ/ナンプラー遺跡" class="rel-wiki-page">ナンプラー遺跡</a>が<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>用に改装されたステージ。<span class="wikicolor" style="color:silver">なぜ一瞬で水を張り巡らせられるのだろうか…</span><br />
バトルではいくつか点在していた中央地帯の遮蔽物が撤去されており、中央高台には坂道が設置されている。<br />
<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%83%9E%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%90%E3%83%BC" title="ブキ/クマサン印のマニューバー" class="rel-wiki-page">クマサン印のマニューバー</a>のお披露目回でもある。</p>
<p>ステージ中に配置されたクマサン商会のロゴの入った(<a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/%E3%82%B9%E3%83%86%E3%83%83%E3%82%AB%E3%83%BC" title="ロッカー/ステッカー" class="rel-wiki-page">ステッカー</a>が貼られた)壁は塗ることができる。<br />
他のステージと違い、シャケが登って来ることのできない段差が存在している。<br />
通常時や干潮では海岸からだけでなく、ステージ中に配置されたカンケツセンからもシャケが湧き出てくる。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E5%B7%A8%E5%A4%A7%E3%82%BF%E3%83%84%E3%83%9E%E3%82%AD" title="サーモンラン/特殊な状況/巨大タツマキ" class="rel-wiki-page">巨大タツマキ</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%89%E3%82%B9%E3%82%B3%E3%82%A4%E5%A4%A7%E9%87%8F%E7%99%BA%E7%94%9F" title="サーモンラン/特殊な状況/ドスコイ大量発生" class="rel-wiki-page">ドスコイ大量発生</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1%E6%8E%A2%E3%81%97" title="サーモンラン/特殊な状況/キンシャケ探し" class="rel-wiki-page">キンシャケ探し</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%89%E3%83%AD%E3%82%B7%E3%83%A3%E3%82%B1%E5%99%B4%E5%87%BA" title="サーモンラン/特殊な状況/ドロシャケ噴出" class="rel-wiki-page">ドロシャケ噴出</a>の4つのイベントが発生しない。</p>
<p>要注意オオモノは<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA" title="サーモンラン/シャケの種類/コウモリ" class="rel-wiki-page">コウモリ</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>。<del>後者2体はいつも通り。</del><br />
他の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>ステージと比べて高低差のある地形がやや控えめであり、射程の短いブキは<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a>処理に手こずりやすい。<br />
また中央高台(通常潮)やコンテナ付近(干潮)にアメやミサイルが降り注ぐと納品や進軍が困難になる。<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;&lt;strong&gt;&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA&quot; title=&quot;サーモンラン/シャケの種類/コウモリ&quot; class=&quot;rel-wiki-page&quot;&gt;コウモリ&lt;/a&gt;が撃ち出す砲弾&lt;/strong&gt;のこと。撃ち落さないと&lt;a href=&quot;/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%A2%E3%83%A1%E3%83%95%E3%83%A9%E3%82%B7&quot; title=&quot;ブキ/スペシャルウェポン/アメフラシ&quot; class=&quot;rel-wiki-page&quot;&gt;アメフラシ&lt;/a&gt;が発生する。">雨弾</span>は全て撃ち落とし、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>が数体湧いたら<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>を切りたい。</p>
<h4 id="h4_content_24_0" >通常時</h4>

<p>開始位置は中央。シャケの湧き位置は前後双方向にある。<br />
低地部分は狭く、オオモノを初動で撃破できないと一気にシャケ溜まりになる。オオモノ撃破自体は高台上から届く展開で（短射程でなければ）やりやすい方。<br />
円形高台周辺はシャケが密集する狭所で接近しづらく、その左奥金網に最奥<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>ポジもある要注意ポイント。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>(ヒカリバエ)集合場所は<span class="wikicolor" style="color:red"><strong>干潮側の</strong></span>円形高台(コンテナが近い方)。間違って反対側に集まってしまうと納品が非常に困難になるので注意。<br />
ヒカリバエに狙われたら高台上からボムコロ等の範囲攻撃をしよう。<br />
納品タイムが必要な場合、高台の奥に行くとそちら側に誘導できる。<br />
干潮コンテナを挟んで反対側の小高台も安置ではあるが、納品を考えるとこちらの活用機会は無い。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>はコンテナ付近下側に誘導して壁を登ると納品しやすい<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;「美味い金イクラ」の略で、&lt;strong&gt;コンテナ近くに落ちて納品しやすい金イクラのこと&lt;/strong&gt;を指す。&lt;br class=&quot;spacer&quot;&gt;ウマイクラをなるべく増やし、マズイクラをなるべく減らすように立ち回ることが、スムーズな金イクラの納品、ひいては円滑なノルマクリア、評価アップへの近道となる。&lt;br class=&quot;spacer&quot;&gt;&lt;br class=&quot;spacer&quot;&gt;&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%E6%8C%87%E5%8D%97#FarAndBasketEggs&quot; title=&quot;サーモンラン/サーモンラン指南&quot; class=&quot;rel-wiki-page&quot;&gt;&lt;span class=&quot;wikicolor&quot; style=&quot;color:#808080&quot;&gt;[詳細]&lt;/span&gt;&lt;/a&gt;">ウマイクラ</span>を作る事ができる。アラマキやムニエール右側の要領でイカノボリをしても良い。<br />
高台上に上げてしまうとグダりやすい。<br />
コンテナ横へ絶えず<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>本体や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>が来るため納品が難しいので、SP等で同時に2体撃破するか<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>安置へ誘導して納品タイムを作りたい。</p>
<h4 id="h4_content_25_0" >満潮時</h4>

<p>開始位置は普段のリスポーン付近。<br />
特筆すべき点としてシャケが湧く位置が1箇所しかなく<a id="notetext_1"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89&quot; title=&quot;サーモンラン/シャケの種類/カタパッド&quot; class=&quot;rel-wiki-page&quot;&gt;カタパッド&lt;/a&gt;の待機位置は複数あり、内部設定的な湧き方角は存在はするようだ。&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_1&quot;&gt;脚注 *1 へ&lt;/a&gt;&lt;/div&gt;">*1</a>、Waveを通して高台の下の海面から全てのシャケが湧き続ける。<br />
そのため海岸付近に金イクラがドロップするとザコの群れに阻まれて回収が困難になる。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#snatcher" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">タマヒロイ</a>が活用しやすいのでうっかり倒してしまわないようにしたい。</p>
<p>ややリスキーだが<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a>を倒さずにプレス工場にする手もある。<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>による押し出しに注意。</p>
<p>リスポーンの手前にもかなり大きな高台があり、壁を塗れば登れる。<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>では安全地帯として利用可能。</p>
<p>オオモノ全滅後は上陸地点すぐ奥の円形の高台上が安全地帯になるうえ、<ins>そこに登ってもシャケはこちらが高台にいることを感知できないかのようにターゲットを変えない</ins>ため、<strong>そこに取りつきさえすれば<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>は上陸のそばから高台にぴったりくっついて離れなくなり、残る3名による納品を完全にフリーにできる。</strong><a id="notetext_2"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;&lt;a class=&quot;ext&quot; href=&quot;https://twitter.com/mukukuzu/status/1697942044491366581&quot;  rel=&quot;nofollow&quot;&gt;https://twitter.com/mukukuzu/status/1697942044491366581&lt;span class=&quot;system-icon ext pukiwiki-open-uri&quot; data-href=&quot;https://twitter.com/mukukuzu/status/1697942044491366581&quot; data-frame=&quot;_blank&quot;&gt;&lt;/span&gt;&lt;/a&gt;&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_2&quot;&gt;脚注 *2 へ&lt;/a&gt;&lt;/div&gt;">*2</a>上り坂手前に金イクラ溜まりを作っておけば、ただ突っ立っているだけで同僚たちに30秒近い至福のひとときを提供できるだろう。<br />
飛び込まれて追い詰められた際は、通常潮位の地形まで前進することで避難も可能。</p>
<h4 id="h4_content_26_0" >干潮時</h4>

<p>開始位置は敵陣側円形高台。コンテナは低地の段差上、通常時の項で触れた狭所の位置。<br />
向かって左の低地には巨大な壁が設置され、全面塗れる。また低地からイクラコンテナ基部に密着すれば直納品も可能。<br />
しかし同平面にカンケツセンも設置され、奇襲を受ければほぼ助からない。<br />
低地から上がってくる坂には小さな高台も存在する。奥に<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>が立つこともあって、ついつい立ちたくなってしまうが、<ins>特に厚みの薄い先端部だと高台下の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>の頭部や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#cohock" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ドスコイ</a>のフライパンがめり込むことがある</ins>。突き飛ばされれば即海面であり、やはりまず助からない。<br />
低地カンケツセンから湧いた<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>はステージ中央に位置取る、散開していると背を向けられるケースも多く対処が難しい。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>安置は通常潮と同じ。<br />
納品中にヒカリバエが付いた場合、ステージ中央側に引っ張ってから(イカロールで)壁に貼り付くと良い。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>も同じ場所で迎え撃つ。</p>
</div>
</div>
<h3 id="h3_content_1_5" class="heading-after-first"><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%BF%E3%83%A9%E3%83%9D%E3%83%BC%E3%83%88%E3%82%B7%E3%83%A7%E3%83%83%E3%83%94%E3%83%B3%E3%82%B0%E3%83%91%E3%83%BC%E3%82%AF" title="ステージ/タラポートショッピングパーク" class="rel-wiki-page">タラポートショッピングパーク</a>  <a class="anchor_super" name ="Barnacle_and_Dime"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5&id=Barnacle_and_Dime" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">クリックで展開</div>
    <div class="fold-content visible-on-open"><p><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3/%E6%94%BB%E7%95%A5/::ref/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3_%E3%82%BF%E3%83%A9%E3%83%9D%E3%83%BC%E3%83%88%E3%82%B7%E3%83%A7%E3%83%83%E3%83%94%E3%83%B3%E3%82%B0%E3%83%91%E3%83%BC%E3%82%AF.webp?rev=26fd951f293c93cda98080687f89c203&amp;t=20231203110821" alt="ビッグラン_タラポートショッピングパーク.webp" title="ビッグラン_タラポートショッピングパーク.webp" width="1280" height="720"  loading="lazy"></p>
<h4 id="h4_content_28_0" >概要</h4>

<p>第5回、第13回<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>の発生地。<br />
バトルステージの<a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%BF%E3%83%A9%E3%83%9D%E3%83%BC%E3%83%88%E3%82%B7%E3%83%A7%E3%83%83%E3%83%94%E3%83%B3%E3%82%B0%E3%83%91%E3%83%BC%E3%82%AF" title="ステージ/タラポートショッピングパーク" class="rel-wiki-page">タラポートショッピングパーク</a>が<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>用に改装されたステージ。<br />
オカシラシャケ「<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B8%E3%83%A7%E3%83%BC" title="サーモンラン/シャケの種類/ジョー" class="rel-wiki-page">ジョー</a>」が初めて襲来したステージでもある。</p>
<p>ステージ中に配置されたクマサン商会のロゴの入った(<a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/%E3%82%B9%E3%83%86%E3%83%83%E3%82%AB%E3%83%BC" title="ロッカー/ステッカー" class="rel-wiki-page">ステッカー</a>が貼られた)壁は塗ることができる。<br />
他のステージと違い、シャケが登って来ることのできない段差が存在している。<br />
通常時や干潮では海岸からだけでなく、ステージ中に配置されたカンケツセンからもシャケが湧き出てくる。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E5%B7%A8%E5%A4%A7%E3%82%BF%E3%83%84%E3%83%9E%E3%82%AD" title="サーモンラン/特殊な状況/巨大タツマキ" class="rel-wiki-page">巨大タツマキ</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%89%E3%82%B9%E3%82%B3%E3%82%A4%E5%A4%A7%E9%87%8F%E7%99%BA%E7%94%9F" title="サーモンラン/特殊な状況/ドスコイ大量発生" class="rel-wiki-page">ドスコイ大量発生</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1%E6%8E%A2%E3%81%97" title="サーモンラン/特殊な状況/キンシャケ探し" class="rel-wiki-page">キンシャケ探し</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%89%E3%83%AD%E3%82%B7%E3%83%A3%E3%82%B1%E5%99%B4%E5%87%BA" title="サーモンラン/特殊な状況/ドロシャケ噴出" class="rel-wiki-page">ドロシャケ噴出</a>の4つのイベントが発生しない。</p>
<p>全体的に平坦で見晴らしの良いステージであり、特にコンテナ周辺は段差が少なく動きやすい。<br />
しかし、これはシャケ側にとっても侵攻が容易であることを意味する。<br />
押し込まれた後の打開が難しいケースが多いので、処理優先で動くのが吉だろう。<br />
<span class="wikicolor" style="color:silver"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page"><span class="wikicolor" style="color:silver">ビッグラン</span></a>では野良バイターの意識が納品数に向きがちだということも考えれば尚更である。</span></p>
<p>今回は通常のブキに加えて、<strong>クマサン印のブキ全種類が支給される可能性がある</strong>初のシフトである。<br />
<span class="wikicolor" style="color:silver">ちょっとしたクマフェス気分だ。</span><br />
普段のオールランダム以上に、味方のブキ編成に注意して挑む必要があるだろう。</p>
<h4 id="h4_content_29_0" >通常時</h4>

<p>コンテナはステージ中央、シャケはカンケツセンの吹き出した前方側(敵陣側・干潮の反対側)から湧く。高台左奥、右奥、右海岸の3箇所で右2つはすぐに合流する。</p>
<p>活動範囲としては左右が狭く縦長の構造。<br />
一般的なステージの干潮時のように、シャケの出現方角が似たような方角に固まっており、状況を俯瞰しやすい。<br />
また<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#snatcher" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">タマヒロイ</a>の出現方角もコンテナ後方へ集中しており、しかも大半でコンテナ上空を通過するようで、敵陣から金イクラを配達してもらいやすい。<br />
ただし、それはコンテナ周囲に寄せた金イクラを高速で持ち去られていくこととも表裏一体。要注意。</p>
<p>高台左奥から湧いた<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>にはコンテナ付近からボムを投げ込める。ほぼ同位置まで<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a>が来る(イカが近くに居てもこの位置までは確実に来る)ので<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a>プレスも狙いやすい。<br />
右海岸から湧いた<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%82%AD%E3%83%A5%E3%82%A6" title="サーモンラン/シャケの種類/テッキュウ" class="rel-wiki-page">テッキュウ</a>は右低地付近まで来るのである程度の寄せも可能。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>は各追加ブロック上に居るととぐろを巻いて倒しづらくなるので、大きく後方に誘導して味方に倒して貰うのがベスト。右湧きなら高台側から回り込んでリスキルしても良いだろう。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>の集合場所は左右の塗れない段差上の<span class="wikicolor" style="color:red">ごく小さな塗れるブロックの上</span>。<br />
このブロックの上に居ると<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>は<strong>完全に停止</strong>し、<strong>自分で弱点を狙うことができる</strong>。<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>も金イクラが最も納品しやすい位置に貯まる。<br />
左右それぞれにあるので納品時は上手く分かれよう。<br />
他にも安置の追加ブロックはあるがバラバラに動くと意思疎通や連携が難しいので補助用と思っておきたい。</p>
<h4 id="h4_content_30_0" >満潮時</h4>

<p>コンテナは通常時同様中央に設置される。<br />
開始前のジャンプマーカーが正方形の並びならこちら。<br />
こちらは通常時でいう後方にもカンケツセンが出現する。<br />
低地が水没し、元々狭いステージがもうちょっとだけ狭くなる。</p>
<p>満潮らしく<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>が大きな脅威となる。即撃破を心がけたい。<br />
特に海岸(通常潮の左右低地)から湧いた<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a>は最優先。後回しにするとすぐに動ける場所が無くなってしまう。<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>は高台側に回り込んで本体を狙うことができる。<br />
また、左右が狭いことから<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA" title="サーモンラン/シャケの種類/コウモリ" class="rel-wiki-page">コウモリ</a>も脅威。塗り状況維持のためにも<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;&lt;strong&gt;&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA&quot; title=&quot;サーモンラン/シャケの種類/コウモリ&quot; class=&quot;rel-wiki-page&quot;&gt;コウモリ&lt;/a&gt;が撃ち出す砲弾&lt;/strong&gt;のこと。撃ち落さないと&lt;a href=&quot;/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%A2%E3%83%A1%E3%83%95%E3%83%A9%E3%82%B7&quot; title=&quot;ブキ/スペシャルウェポン/アメフラシ&quot; class=&quot;rel-wiki-page&quot;&gt;アメフラシ&lt;/a&gt;が発生する。">雨弾</span>は撃ち落とそう。</p>
<h4 id="h4_content_31_0" >干潮時</h4>

<p>コンテナは普段のリスポーン地点付近。コンテナは後方高台に隣接し、やや背が高いが下部からでも直接の納品が可能。<br />
コンテナ後方がかなり広く、高台に塗れる壁が多数増設されている。<br />
しかし、一度後方まで押し込まれてしまうと<strong>打開は非常に厳しい</strong>。<br />
基本的にコンテナ前広場までで処理し、後方利用は<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>を苦手とする長射程ブキが一時的に退避するのみにしたい。<br />
コンテナ前まで迫った<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a>を放置すると一気に制圧されるため注意。</p>
<h4 id="h4_content_32_0" >コメント欄有益情報リンク</h4>

<p><a class="ext" href="https://zawazawa.jp/spla3/topic/177/700"  rel="nofollow">攻略<span class="system-icon ext pukiwiki-open-uri" data-href="https://zawazawa.jp/spla3/topic/177/700" data-frame="_blank"></span></a></p>
<h4 id="h4_content_33_0" >小ネタ</h4>

<ul class="list1"><li>なぜか干潮時高台のステージ外壁に水面に面する形で塗れるブロックが置かれ、通常潮位時でも干潮高台に登れるようになっている。</li></ul>
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>史上初、ステージの水没に留まらず、<strong>背景の建造物に具体的な損壊描写が存在する</strong>。
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">画像</div>
    <div class="fold-content visible-on-open"><p><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3/%E6%94%BB%E7%95%A5/::ref/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3_%E3%82%BF%E3%83%A9%E3%83%9D%E3%83%BC%E3%83%88_%E8%A2%AB%E5%AE%B3.webp?rev=205a8d65d6ea04578a03d8a954b69c16&amp;t=20231203110909" alt="ビッグラン_タラポート_被害.webp" title="ビッグラン_タラポート_被害.webp" width="1280" height="720"  loading="lazy"><br />
<span style="font-size:10px"><span class="wikicolor" style="color:Maroon">▲ 天井のガラスに大穴が空いている様子がわかる。</span></span></p>
<p><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3/%E6%94%BB%E7%95%A5/::ref/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3_%E3%82%BF%E3%83%A9%E3%83%9D%E3%83%BC%E3%83%88_%E8%A2%AB%E5%AE%B3_%E6%AF%94%E8%BC%83%E7%94%A8.webp?rev=98c308c29e5b123c5bb3a2e49d59470a&amp;t=20231203110915" alt="ビッグラン_タラポート_被害_比較用.webp" title="ビッグラン_タラポート_被害_比較用.webp" width="1280" height="720"  loading="lazy"><br />
<span style="font-size:10px"><span class="wikicolor" style="color:Maroon">▲ こちらは通常時の様子。上の画像と比較すると、被害の大きさがよく分かるだろう。</span></span></p>
</div>
</div>
天井の窓ガラスが直径数十メートルもの規模で破損し、そのすぐ下ではコンクリートも一部砕けているが、具体的に何がこの被害をもたらしたのかは不明。<br />
ガラスを突き破って<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B8%E3%83%A7%E3%83%BC" title="サーモンラン/シャケの種類/ジョー" class="rel-wiki-page">ジョー</a>が飛び込んででもきたのだろうか。</li></ul>
<ul class="list2"><li>クマサン商会のヘリコプターは、その開口部から侵入して施設内でホバリングしている。<br />
ショッピングモール内で滞空するヘリコプター、すさまじい建築規模と飛行技術である。</li></ul>
<ul class="list2"><li>なお、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>終了からわずか2時間後の12/4 11:00～13:00には<a href="/splatoon3mix/X%E3%83%9E%E3%83%83%E3%83%81" title="Xマッチ" class="rel-wiki-page">Xマッチ</a>のステージとして<a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%BF%E3%83%A9%E3%83%9D%E3%83%BC%E3%83%88%E3%82%B7%E3%83%A7%E3%83%83%E3%83%94%E3%83%B3%E3%82%B0%E3%83%91%E3%83%BC%E3%82%AF" title="ステージ/タラポートショッピングパーク" class="rel-wiki-page">タラポートショッピングパーク</a>が選出され、普段と全く変わらない様子でプレイできた。<br />
あの大穴をわずか2時間で修理したのだろうか…？</li></ul>
</div>
</div>
<h3 id="h3_content_1_6" class="heading-after-first"><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%B4%E3%83%B3%E3%82%BA%E3%82%A4%E5%9C%B0%E5%8C%BA" title="ステージ/ゴンズイ地区" class="rel-wiki-page">ゴンズイ地区</a>  <a class="anchor_super" name ="Eeltail_Alley"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5&id=Eeltail_Alley" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">クリックで展開</div>
    <div class="fold-content visible-on-open"><p><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3/%E6%94%BB%E7%95%A5/::ref/IMG_1807.jpeg.webp?rev=b9ebac111aa3c73a729900a941b522b8&amp;t=20240309171709" alt="IMG_1807.jpeg" title="IMG_1807.jpeg" width="1280" height="720"  loading="lazy"></p>
<h4 id="h4_content_36_0" >概要</h4>

<p>第6回、第14回<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>の発生地。<br />
バトルステージの<a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%B4%E3%83%B3%E3%82%BA%E3%82%A4%E5%9C%B0%E5%8C%BA" title="ステージ/ゴンズイ地区" class="rel-wiki-page">ゴンズイ地区</a>が<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>用に改装されたステージ。</p>
<p>ステージ中に配置されたクマサン商会のロゴの入った(<a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/%E3%82%B9%E3%83%86%E3%83%83%E3%82%AB%E3%83%BC" title="ロッカー/ステッカー" class="rel-wiki-page">ステッカー</a>が貼られた)壁は塗ることができる。<br />
他のステージと違い、シャケが登って来ることのできない段差が存在している。<br />
通常時や干潮ではステージ中に配置されたカンケツセンからもシャケが湧き出てくる。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E5%B7%A8%E5%A4%A7%E3%82%BF%E3%83%84%E3%83%9E%E3%82%AD" title="サーモンラン/特殊な状況/巨大タツマキ" class="rel-wiki-page">巨大タツマキ</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%89%E3%82%B9%E3%82%B3%E3%82%A4%E5%A4%A7%E9%87%8F%E7%99%BA%E7%94%9F" title="サーモンラン/特殊な状況/ドスコイ大量発生" class="rel-wiki-page">ドスコイ大量発生</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1%E6%8E%A2%E3%81%97" title="サーモンラン/特殊な状況/キンシャケ探し" class="rel-wiki-page">キンシャケ探し</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%89%E3%83%AD%E3%82%B7%E3%83%A3%E3%82%B1%E5%99%B4%E5%87%BA" title="サーモンラン/特殊な状況/ドロシャケ噴出" class="rel-wiki-page">ドロシャケ噴出</a>の4つのイベントが発生しない。<br />
また、どの潮位でもステージ内には水面がなく、変化するのはスタート位置とイクラコンテナの位置、シャケの出現地点となるカンケツセンの場所、それと場外に落ちて水面に接触して水没判定を受けるまでの時間のみである。<span class="wikicolor" style="color:silver">なぜ水が0の<a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%8A%E3%83%B3%E3%83%97%E3%83%A9%E3%83%BC%E9%81%BA%E8%B7%A1" title="ステージ/ナンプラー遺跡" class="rel-wiki-page">ナンプラー遺跡</a>に一瞬で水を大量に入れられるのに、ここでは満潮ですら水がステージ内にまったくないのだろうか…。WAVE開始までのカウントの水位変化が詐欺に思えてくる。</span><br />
自陣の左高台手前の足場が無くなっていたり、中央に左右の窪みがあったりするなど、<a href="/splatoon3mix/%E3%83%88%E3%83%AA%E3%82%AB%E3%83%A9%E3%83%90%E3%83%88%E3%83%AB%E6%8C%87%E5%8D%97" title="トリカラバトル指南" class="rel-wiki-page">トリカラバトル</a>の地形を彷彿とさせる。<br />
塗れない壁の大半に塗れるブロックが追加されており、他ルールと比べステージ全域を駆け回りやすい。<span class="wikicolor" style="color:silver">普段からこれにして……</span></p>
<h4 id="h4_content_37_0" >通常時</h4>

<p>コンテナはステージ中央。開始位置は中央高台に2・2で分かれる。<br />
シャケがやってくるのは片側(敵陣側・背景が荒野側)からのみ。<br />
ただし、右低地から湧いた<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA" title="サーモンラン/シャケの種類/コウモリ" class="rel-wiki-page">コウモリ</a>のみ初手で右後方に飛ぶため見落とすと<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%A2%E3%83%A1%E3%83%95%E3%83%A9%E3%82%B7" title="ブキ/スペシャルウェポン/アメフラシ" class="rel-wiki-page">アメフラシ</a>で挟撃されてしまう。主戦場に<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;&lt;strong&gt;&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA&quot; title=&quot;サーモンラン/シャケの種類/コウモリ&quot; class=&quot;rel-wiki-page&quot;&gt;コウモリ&lt;/a&gt;が撃ち出す砲弾&lt;/strong&gt;のこと。撃ち落さないと&lt;a href=&quot;/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%A2%E3%83%A1%E3%83%95%E3%83%A9%E3%82%B7&quot; title=&quot;ブキ/スペシャルウェポン/アメフラシ&quot; class=&quot;rel-wiki-page&quot;&gt;アメフラシ&lt;/a&gt;が発生する。">雨弾</span>が飛ばないように最優先で撃破したい。<br />
左側の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>には左側の追加ブロックからすぐに向かえる。<br />
高台の一部が金網になっており、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>の初期位置がこの付近になるため金網を利用したボムコロでワンパン可能。慣れていれば低地から金網へ山なりに乗せることもできる。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>ともに集合場所はコンテナ右後方の高台下。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>は壁役ブキならそのまま低地で戦い、低火力ブキならヒカリバエが付いたら<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="主に&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;&lt;strong&gt;壁に塗られたインクに潜る様子のこと&lt;/strong&gt;。&lt;br class=&quot;spacer&quot;&gt;&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;では自分をターゲットとしているシャケらをしばらくの間釘付けにできるが、あまり長くやりすぎると&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB&quot; title=&quot;サーモンラン/シャケの種類/グリル&quot; class=&quot;rel-wiki-page&quot;&gt;グリル&lt;/a&gt;のターゲット変更や&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1&quot; title=&quot;サーモンラン/シャケの種類/ザコシャケ&quot; class=&quot;rel-wiki-page&quot;&gt;ザコシャケ&lt;/a&gt;の大ジャンプにより痛い目にあう。&lt;br class=&quot;spacer&quot;&gt;また、セミ中は攻撃できないため、自軍の火力が減るという重大な欠点もある。&lt;br class=&quot;spacer&quot;&gt;「金イクラが大量だが敵の勢いが激しく納品が捗らない状況で、自分が離れた地点でセミをし敵を誘導し、その隙に味方に納品をしてもらう」「デスした味方がウキワになるまでのタイムラグを凌ぐ」など、場面や使いようによっては非常に有用。&lt;br class=&quot;spacer&quot;&gt;&lt;br class=&quot;spacer&quot;&gt;&lt;a href=&quot;/splatoon3mix/%E7%94%A8%E8%AA%9E%E9%9B%86/%E5%AF%BE%E6%88%A6%E9%96%A2%E9%80%A3%E7%94%A8%E8%AA%9E#k58821ab&quot; title=&quot;用語集/対戦関連用語&quot; class=&quot;rel-wiki-page&quot;&gt;&lt;span class=&quot;wikicolor&quot; style=&quot;color:#808080&quot;&gt;[詳細]&lt;/span&gt;&lt;/a&gt;">セミ</span>推奨。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>はムニエールのようにイカノボリ待機状態で誘導し、イカノボリ後弱点を叩こう。<br />
どちらもコンテナ左前方の塗れる追加ブロックの上が安置なので納品タイムを作るならここへ。</p>
<h4 id="h4_content_38_0" >満潮時</h4>

<p>コンテナは普段のリスポーン地点付近。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>の集合場所はコンテナ後方高台。シャケの進行方向が一つにまとまるので迎撃しやすい。<br />
一方で安全な退避場所が無いため納品が課題。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>は一旦コンテナ横へ誘導してから壁を登って背中を撃とう。</p>
<h4 id="h4_content_39_0" >干潮時</h4>

<p>コンテナは敵陣側の<a href="/splatoon3mix/%E3%82%AC%E3%83%81%E3%83%9B%E3%82%B3%E3%83%90%E3%83%88%E3%83%AB" title="ガチホコバトル" class="rel-wiki-page">ガチホコバトル</a>でいう左右カンモンのちょうど中間辺りに配置される。下からでも直接納品可能。<br />
シャケがやってくるのは敵陣側からのみ。<br />
他ルールで塗れない通路が塗れるようになっているため主要ルートとして機能するほか、塗れる追加ブロックから左高台へ直接登れる。左へ攻める際に活用したい。<br />
向かって左側、<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC%E5%B1%9E" title="ブキ/チャージャー属" class="rel-wiki-page">チャージャー</a>がよく居座る高台は<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>でも安置・長射程用高台として機能する。長居すると納品参加できなくなってしまうが、左側のオオモノを倒すのには便利なため適宜活用したい。<br />
それぞれの道が狭いため<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>には要注意。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>の集合場所Aはコンテナ後方の下層付近(仮)。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>は壁役ブキならそのまま低地(コンテナ横)で戦い、低火力ブキならヒカリバエが付いたら<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="主に&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;&lt;strong&gt;壁に塗られたインクに潜る様子のこと&lt;/strong&gt;。&lt;br class=&quot;spacer&quot;&gt;&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;では自分をターゲットとしているシャケらをしばらくの間釘付けにできるが、あまり長くやりすぎると&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB&quot; title=&quot;サーモンラン/シャケの種類/グリル&quot; class=&quot;rel-wiki-page&quot;&gt;グリル&lt;/a&gt;のターゲット変更や&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1&quot; title=&quot;サーモンラン/シャケの種類/ザコシャケ&quot; class=&quot;rel-wiki-page&quot;&gt;ザコシャケ&lt;/a&gt;の大ジャンプにより痛い目にあう。&lt;br class=&quot;spacer&quot;&gt;また、セミ中は攻撃できないため、自軍の火力が減るという重大な欠点もある。&lt;br class=&quot;spacer&quot;&gt;「金イクラが大量だが敵の勢いが激しく納品が捗らない状況で、自分が離れた地点でセミをし敵を誘導し、その隙に味方に納品をしてもらう」「デスした味方がウキワになるまでのタイムラグを凌ぐ」など、場面や使いようによっては非常に有用。&lt;br class=&quot;spacer&quot;&gt;&lt;br class=&quot;spacer&quot;&gt;&lt;a href=&quot;/splatoon3mix/%E7%94%A8%E8%AA%9E%E9%9B%86/%E5%AF%BE%E6%88%A6%E9%96%A2%E9%80%A3%E7%94%A8%E8%AA%9E#k58821ab&quot; title=&quot;用語集/対戦関連用語&quot; class=&quot;rel-wiki-page&quot;&gt;&lt;span class=&quot;wikicolor&quot; style=&quot;color:#808080&quot;&gt;[詳細]&lt;/span&gt;&lt;/a&gt;">セミ</span>推奨。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>集合場所Bは左側高台上の安置(仮)。投げ納品になるが安置から1投で届くため35個以上は納品可能。</p>
</div>
</div>
<h3 id="h3_content_1_7" class="heading-after-first">各地で同時発生  <a class="anchor_super" name ="BIG_Big_run"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5&id=BIG_Big_run" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">クリックで展開</div>
    <div class="fold-content visible-on-open"><h4 id="h4_content_41_0" >概要</h4>

<p>第7回<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>となるビッグ<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>でバイターたちが出動するステージは、過去に登場した<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>ステージ全6種の中から毎回ランダムに選ばれる。<br />
各ステージは初出時から一部地形が変更されている。古い地形を前提とした攻略情報の中にはそのまま使えないものもあるので注意。<br />
ランダムステージという<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>の常識を覆す仕様のため、通常のバイトや今までの<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>のように「何度も遊びながらステージを覚える」のがやや難しい。新鮮な気持ちで楽しみたいというこだわりが特にないのであれば、未プレイのステージについて予習してからプレイするとスムーズに攻略できるだろう。<br />
バイト専用ブキとして<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC" title="ブキ/クマサン印のローラー" class="rel-wiki-page">クマサン印のローラー</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/Extra%20Wave" title="サーモンラン/特殊な状況/Extra Wave" class="rel-wiki-page">Extra Wave</a>として<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AA%E3%82%AB%E3%82%B7%E3%83%A9%E9%80%A3%E5%90%88" title="サーモンラン/シャケの種類/オカシラ連合" class="rel-wiki-page">オカシラ連合</a>が初登場した。詳細はリンク先を参照されたし。</p>
</div>
</div>
<h3 id="h3_content_1_8" class="heading-after-first"><a href="/splatoon3mix/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%B0%E3%83%A9%E3%83%B3%E3%83%89%E3%83%90%E3%83%B3%E3%82%AB%E3%83%A9%E3%82%A2%E3%83%AA%E3%83%BC%E3%83%8A" title="ステージ/グランドバンカラアリーナ" class="rel-wiki-page">グランドバンカラアリーナ</a>  <a class="anchor_super" name ="Grand_Splatlands_Bowl"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5&id=Grand_Splatlands_Bowl" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">クリックで展開</div>
    <div class="fold-content visible-on-open"><h4 id="h4_content_43_0" >概要</h4>

<p>第8回<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>の発生地。<br />
グランドフェス用に特設されたステージ。クマサン商会の計らいでステージの随所に金イクラをコンテナ近くへ飛ばせる発射台が設置されている。<br />
今回の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>は全世界のアルバイターが集めた金イクラの数が表示され、世界中で驚愕の<strong>7億個</strong>のノルマをクリアすれば金7個、銀21個、銅210個のウロコがもらえるそうだ。<br />
→<span class="wikicolor" style="color:red"><strong>2024年9月8日午前0:14頃に達成!</strong></span>　今後1億個毎に金1、銀3、銅30が加算されていく模様。<br />
→期間中に全世界で1,535,611,351個もの金イクラが集まり、参加者には金15個、銀45個、銅450個のウロコが送付された。<br />
また、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>専用のバイトツナギも用意されており、ゲームニュースからゲットできる。</p>
<ul class="list1"><li>特別な仕様について
<ul class="list2"><li>最初からクマサン商会のロゴ入りの発射台（<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%82%AD%E3%83%A5%E3%82%A6" title="サーモンラン/シャケの種類/テッキュウ" class="rel-wiki-page">テッキュウ</a>が使うもの）が各地に設置されている。<br />
<strong>イクラコンテナに近いものは必ずコンテナに直接入る。</strong>水位が変化してイクラコンテナの位置が変わると、発射台の向きも自動で変わる。<br />
直接納品なら実質第2、第3のイクラコンテナとみなすことができるが、投げ入れようとすると海に投げたときのように弾かれてしまうので注意。</li>
<li><strong>通常Waveや<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/Extra%20Wave" title="サーモンラン/特殊な状況/Extra Wave" class="rel-wiki-page">Extra Wave</a>でも少数の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/キンシャケ" class="rel-wiki-page">キンシャケ</a>(霧仕様)が出現する。</strong><span class="wikicolor" style="color:silver">いつもでてこい</span></li>
<li>一部音楽が変更されており、ロビーは『カガヤクンデス・マーチ24h』、通常Waveは『過言』、リザルトは『ノット・バッド』がフェスを思わせるアレンジになっている。</li></ul></li></ul>
<h4 id="h4_content_44_0" >通常時</h4>

<p>コンテナは中央にある。シャケは、右、前方、左から攻めてくる。コンテナに直接入る発射台は右前方と左の2つ。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>はコンテナ横・左右発射台の横どちらでも対応可能。<br />
コンテナ横に居ると2方向からの襲撃を受けることになるが、クマブキのパワーで迎撃には困らないだろう。<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC" title="ブキ/クマサン印のローラー" class="rel-wiki-page">クマサン印のローラー</a>を引いたら高火力低消費の低速轢きを思う存分にイカそう。<br />
編成事故等でヒカリバエが付いたプレイヤーの安置が欲しければ中央のビニール床一帯か、コンテナに直接入る発射台の近くの高台に居座れる。どちらも狭いので処理を怠ってジャンプ<a id="notetext_3"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;狂シャケはターゲットが安置に居る等で一定時間同じ場所に留まるとジャンプしてくる&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_3&quot;&gt;脚注 *3 へ&lt;/a&gt;&lt;/div&gt;">*3</a>されるとすぐ叩き落されるので注意。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>は右前方高台(干潮と同じ場所)だと意図が伝わりやすい。<br />
コンテナ横でもOKで、左側の発射台近くで倒せるとスムーズに納品できる。右側から来た場合もアラマキと同じ要領で下段で待つことで左側に流すことができる。納品タイムが欲しければ左右の高台に分かれるのも手。<br />
中央のビニールの高台も安置だがインク回復ができないこと、コンテナ横に<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>を集めてしまうことから納品数は伸びづらい。</p>
<h4 id="h4_content_45_0" >満潮時</h4>

<p>コンテナは通常潮から見て左側の<a href="/splatoon3mix/%E3%83%88%E3%83%AA%E3%82%AB%E3%83%A9%E3%83%90%E3%83%88%E3%83%AB%E6%8C%87%E5%8D%97" title="トリカラバトル指南" class="rel-wiki-page">トリカラバトル</a>の攻撃チームのスタート地点周辺。シャケは右奥の海と通常潮コンテナ周辺から攻めてくる。<br />
コンテナに直接入る発射台は満潮時中央付近の1つのみ。<br />
一見満潮には見えないがそれは間違い。コンテナ後方には若干のスペースこそあるが逃げ場になる高台は一切無く、中央周辺まで侵攻されてしまうとドンブラコ満潮船首縛り・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%81%A9%E3%82%93%E3%81%B4%E3%81%93%E9%97%98%E6%8A%80%E5%A0%B4" title="サーモンラン/ステージ/どんぴこ闘技場" class="rel-wiki-page">どんぴこ闘技場</a>満潮高台縛りプレイくらいの狭さになってしまう。<br />
中央の直接入る発射台周辺が主戦場となる。開幕は中央発射台より<span class="wikicolor" style="color:red"><strong>前に出ないこと</strong></span>。<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a>や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a>を奥で反応させてしまうとスタートからグダグダになる。この辺りはアラマキ干潮やムニエール干潮に似ているか。<br />
<strong>奥に長時間居座るのは悪手</strong>。発射台があるが<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%82%AD%E3%83%A5%E3%82%A6" title="サーモンラン/シャケの種類/テッキュウ" class="rel-wiki-page">テッキュウ</a>砲台同様コンテナ付近に散らばってしまうため納品役が必須になり、常に1人欠けた状態でプレイする状態になってしまう。当然納品数も伸びない。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>が沸いたときや中央～奥の一本道を<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>に制圧されそうなときは左右のインクレールを使って倒しにいこう。<br />
インクレールは一方通行に見えるが奥高台からイカジャンプで飛び乗って戻れる。ただし奥高台自体は壁を塗る必要があるのでブキによっては高台から飛び降りると陸路でしか戻ってこれなくなる可能性がある。特にWAVE1満潮時は塗られていない状態でスタートするため注意。<br />
<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88%E3%83%91%E3%83%83%E3%82%AF" title="ブキ/スペシャルウェポン/ジェットパック" class="rel-wiki-page">ジェットパック</a>使用時はインクレール付近までは水没せず低空飛行することができる(干潮時に使用する地面がある)ため、奥に向かいたい時に活用できる。更に時間を節約したいならインクレール上からジャンプして使用するのも良いだろう。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>時はコンテナ近くのインクレールの根本付近に集まる。高台上は非常に狭いのでヒカリバエがついたプレイヤーだけにしたい。<br />
クマブキなので処理には困らないが、納品タイムが必要ならインクレールで奥高台まで行こう。インクレール上に居るとシャケは根本に集まるため意味が無い。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>も同様。弱点は反対側に向くので高台に居座るのはターゲットが付いたプレイヤーのみにしたい。</p>
<h4 id="h4_content_46_0" >干潮時</h4>

<p>コンテナはトリカラ守備チームスタート地点。通常潮から見て正面奥。スーパージャンプ先は左右高台上に2人ずつ。<br />
水位が下がるため満潮時のインクレールの下部分が通行可能になる。シャケは通常コンテナ高台、右手前低地、左奥低地から出現する。干潮ながら横に広いので乱獲しやすい。<br />
コンテナに直接入る発射台は干潮スタート地点から見て左前方の1つのみ。右奥は遠いので散らばってしまう。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>時の集合地点は、左前方の発射台周辺と付近の高台上。発射台からコンテナに直接入る。すぐ隣の小高台も安置。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>も同様。弱点が反対側に向くので狙われている人だけが登ろう。同じく小高台も安置。</p>
<h4 id="h4_content_47_0" >コメント欄有益情報リンク</h4>

<ul class="list1"><li><a class="ext" href="https://zawazawa.jp/spla3/topic/280/42098"  rel="nofollow">マップ<span class="system-icon ext pukiwiki-open-uri" data-href="https://zawazawa.jp/spla3/topic/280/42098" data-frame="_blank"></span></a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%8F%E3%82%B3%E3%83%93%E3%83%A4%E8%A5%B2%E6%9D%A5" title="サーモンラン/特殊な状況/ハコビヤ襲来" class="rel-wiki-page">ハコビヤ襲来</a>では、<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%82%B9%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC" title="ブキ/クマサン印のスロッシャー" class="rel-wiki-page">クマサン印のスロッシャー</a>で<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B3%E3%83%93%E3%83%A4%E3%81%9F%E3%81%A1#mothership" title="サーモンラン/シャケの種類/ハコビヤたち" class="rel-wiki-page">ハコビヤ</a>母艦上部を撃つことで、<strong>接近時のみならず滞空時でも</strong>母艦を貫通して<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B3%E3%83%93%E3%83%A4%E3%81%9F%E3%81%A1#chinooks" title="サーモンラン/シャケの種類/ハコビヤたち" class="rel-wiki-page">シャケコプター</a>をリスキルできる。通常潮、満潮、干潮全てで確認。<br />
参考:<a class="ext" href="https://zawazawa.jp/spla3/topic/280/42162"  rel="nofollow">雑談掲示板/ログ3#42162<span class="system-icon ext pukiwiki-open-uri" data-href="https://zawazawa.jp/spla3/topic/280/42162" data-frame="_blank"></span></a>、<a class="ext" href="https://zawazawa.jp/spla3/topic/244/34093"  rel="nofollow">サーモンラン雑談/ログ2#34093※動画含む<span class="system-icon ext pukiwiki-open-uri" data-href="https://zawazawa.jp/spla3/topic/244/34093" data-frame="_blank"></span></a>
<ul class="list2"><li>通常潮だとイクラ落下地点近くに赤砲台が置かれているわけではないので<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%84" title="サーモンラン/シャケの種類/タツ" class="rel-wiki-page">タツ</a>マキよろしくイクラリレーが必要になるため納品数は伸びない。1回イクラ投げするだけでコンテナ手前に落ちるので輸送ルートは短め。また、クマスロ一人で全ての<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B3%E3%83%93%E3%83%A4%E3%81%9F%E3%81%A1#chinooks" title="サーモンラン/シャケの種類/ハコビヤたち" class="rel-wiki-page">シャケコプター</a>をリスキルできるわけではないので、他の味方は<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%84" title="サーモンラン/シャケの種類/タツ" class="rel-wiki-page">タツ</a>マキ同様にイクラ輸送ルートに群がってきたザコたちを捌く必要がある。野良でやる場合味方がここまで動きを合わせてくれることは少ないので注意が必要。<br />
クマスロは燃費的に対<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B3%E3%83%93%E3%83%A4%E3%81%9F%E3%81%A1#chinooks" title="サーモンラン/シャケの種類/ハコビヤたち" class="rel-wiki-page">シャケコプター</a>が厳しい面もあるので、味方も同様に対<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B3%E3%83%93%E3%83%A4%E3%81%9F%E3%81%A1#chinooks" title="サーモンラン/シャケの種類/ハコビヤたち" class="rel-wiki-page">シャケコプター</a>が厳しいという場合はWAVE失敗を回避するため損切りでこの方法をとるのもアリ。<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B3%E3%83%93%E3%83%A4%E3%81%9F%E3%81%A1#chinooks" title="サーモンラン/シャケの種類/ハコビヤたち" class="rel-wiki-page">シャケコプター</a>を間引くことでザコで氾濫した盤面になることだけは回避できる。</li>
<li>満潮だとイクラ落下地点近くに赤砲台が置かれているので、通常潮ほど連携は要さない。味方の動きや編成にもよるがある程度有益。</li>
<li>干潮でも可能だが利用価値は無い。ビニール上から狙えるが、インク回復ができず発射台からも遠い。</li></ul></li></ul>
</div>
</div>
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
<h2 id="h2_content_1_9" class="heading-after-first">コメント <a class="anchor_super" name ="comment"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5&id=comment" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">サーモンラン/ビッグラン</a>と統一。</p>
    <iframe id="zawazawa-embed-2ad7bbfa461b312af9b11cc58b5a4a6d-56" class="zawazawa-embed" src="https://z.wikiwiki.jp/em/spla3/topic/177?style=default&size=10"
        frameborder="0" scrolling="no" marginheight="0" marginwidth="0"
        style="width:100%; min-width: 100%; max-width: 100%; *width: 100%; min-height: 350px; height: 350px;"
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
<span class="small"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>の待機位置は複数あり、内部設定的な湧き方角は存在はするようだ。</span><br>
<a id="notefoot_2" href="#notetext_2" class="note_super">*2</a>
<span class="small"><a class="ext" href="https://twitter.com/mukukuzu/status/1697942044491366581"  rel="nofollow">https://twitter.com/mukukuzu/status/1697942044491366581<span class="system-icon ext pukiwiki-open-uri" data-href="https://twitter.com/mukukuzu/status/1697942044491366581" data-frame="_blank"></span></a></span><br>
<a id="notefoot_3" href="#notetext_3" class="note_super">*3</a>
<span class="small">狂シャケはターゲットが安置に居る等で一定時間同じ場所に留まるとジャンプしてくる</span><br>            </div>
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
</style><div id="pageload" style="display: none" data-pageload="{&quot;time&quot;:{&quot;all&quot;:{&quot;real&quot;:0.06655621528625488,&quot;cost&quot;:0.16396522521972656},&quot;body&quot;:{&quot;real&quot;:0.05889391899108887,&quot;cost&quot;:0.05889391899108887},&quot;main&quot;:{&quot;real&quot;:0.05601215362548828,&quot;cost&quot;:0.05601215362548828},&quot;menu&quot;:{&quot;real&quot;:0.09711790084838867,&quot;cost&quot;:0.09711790084838867},&quot;head&quot;:{&quot;real&quot;:0.0001780986785888672,&quot;cost&quot;:0.0001780986785888672},&quot;foot&quot;:{&quot;real&quot;:0.00011301040649414062,&quot;cost&quot;:0.00011301040649414062}},&quot;include&quot;:2,&quot;memory&quot;:3044224,&quot;io&quot;:{&quot;read&quot;:{&quot;files&quot;:6,&quot;bytes&quot;:85480,&quot;locks&quot;:4},&quot;write&quot;:{&quot;files&quot;:0,&quot;bytes&quot;:0,&quot;locks&quot;:0},&quot;directory&quot;:{&quot;traversals&quot;:0,&quot;files&quot;:0},&quot;misc&quot;:829},&quot;contentSize&quot;:{&quot;all&quot;:336279,&quot;body&quot;:160256},&quot;timestamp&quot;:&quot;2026-01-16 19:26:33&quot;}"></div>

<script type="text/javascript" src="https://cdn.wikiwiki.jp/to/w/common/assets/dist/wikiwiki-2ee375d6199d21f58b1a.min.js"></script>
<script type="text/javascript" src="https://cdn.wikiwiki.jp/to/w/common/assets/dist/wikiwiki-ex1-5b2960938b353a08a472.min.js"></script>
<script type="text/javascript">
    bootLazy.addJqPluginInit('.fold-container', function() {
        this.fold({
            buttonSelector: '.fold-toggle-button',
            openClassName: 'fold-open'
        });
    });
</script>
    <script>
        bootLazy.addJqPluginInit('.security-check-interrupt', function() {
            this.securityCheckInterrupt({});
        });
    </script>
<script>
    bootLazy.addJqPluginInit('.zawazawa-embed', function() {
        this.zcommentResize();
    });
</script>
<div id="wikiwiki-pageview-counter" data-endpoint="https://counter.wikiwiki.jp/c/splatoon3mix/pv/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5" style="display: none;"></div>
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
            title: "サーモンラン\/ビッグラン\/攻略 - Splatoon3 - スプラトゥーン3 攻略＆検証  Wiki*",
            controlPanelUrl: "https:\/\/c.wikiwiki.jp\/wiki\/splatoon3mix\/design",
            imageUrl: "https:\/\/icon.wikiwiki.jp\/symbolicon\/splatoon3mix\/ogImage\/f1fa837847c5.png",
            description: "このサイトは、スプラトゥーン3の攻略・検証を目的とした非公式wikiです。",
            shareUrl: "https:\/\/wikiwiki.jp\/splatoon3mix\/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3\/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3\/%E6%94%BB%E7%95%A5",
            shortUrlRequestUrl: "\/splatoon3mix\/::cmd\/short_url?mode=json&page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3%2F%E6%94%BB%E7%95%A5",
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
    url: '/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3/%E6%94%BB%E7%95%A5',
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
