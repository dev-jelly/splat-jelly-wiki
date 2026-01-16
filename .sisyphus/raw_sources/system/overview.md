<!DOCTYPE html>
<html lang="ja">
<head prefix="og: https://ogp.me/ns# fb: https://ogp.me/ns/fb# article: https://ogp.me/ns/article#">
    <meta charset="utf-8">
    <meta name="viewport" content="width=980">

    <meta name="description" content="このサイトは、スプラトゥーン3の攻略・検証を目的とした非公式wikiです。">
        <meta property="og:url" content="https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" />
    <meta property="og:type" content="article" />
    <meta property="og:title" content="サーモンラン NEXT WAVE - Splatoon3 - スプラトゥーン3 攻略＆検証  Wiki*" />
    <meta property="og:description" content="このサイトは、スプラトゥーン3の攻略・検証を目的とした非公式wikiです。" />
    <meta property="og:site_name" content="Splatoon3 - スプラトゥーン3 攻略＆検証  Wiki*" />
    <meta property="og:image" content="https://icon.wikiwiki.jp/symbolicon/splatoon3mix/ogImage/f1fa837847c5.png" />
    <title>サーモンラン NEXT WAVE - Splatoon3 - スプラトゥーン3 攻略＆検証  Wiki*</title>

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
if (wi_ismobile && wi_group == "N" && wi_agreement === "false") {
      defineSlotFlux.push({"slotID": "div-gpt-ad-1731135777754-0", "sizes": [[300,600]], "slotName":"WIKIWIKI_SP_CAPTION_300x600"});
}
      defineSlotFlux.push({"slotID": "div-gpt-ad-1566473930452-0", "sizes": [[300,250]], "slotName":"WIKIWIKI_PC_CAPTION_20TH"});
      defineSlotFlux.push({"slotID": "div-gpt-ad-other", "sizes": [[300,250]], "slotName":"WIKIWIKI_CAPTION_B"});
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
if (wi_ismobile && wi_group == "N" && wi_agreement === "false") {
    googletag.defineSlot('/19033742/WIKIWIKI_SP_CAPTION_300x600',[[300,600],[1,1]],
        'div-gpt-ad-1731135777754-0').addService(googletag.pubads());
}
    googletag.defineSlot('/19033742/WIKIWIKI_PC_CAPTION_20TH',[[300,250],[1,1]],
        'div-gpt-ad-1566473930452-0').addService(googletag.pubads());
    googletag.defineSlot('/19033742/WIKIWIKI_CAPTION_B',[[300,250],[1,1]],
        'div-gpt-ad-other').addService(googletag.pubads());
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
    <link rel="canonical" href="https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3">
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
                <div id="navigator">[ <a href="/splatoon3mix/">ホーム</a> | <a href="/splatoon3mix/::cmd/newpage?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" rel="nofollow">新規</a> | <a href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" rel="nofollow">編集</a> | <a href="/splatoon3mix/::cmd/attach?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" rel="nofollow">添付</a> ]</div>            </div>
            <div class="toolbox toolbox-desktop toolbar-container">
                <div class="toolbar"><a href="/splatoon3mix/::cmd/list" title="一覧" rel="nofollow"><span class="system-icon toolbar list"></span></a>
<a href="/splatoon3mix/RecentChanges" title="最終更新" rel="nofollow"><span class="system-icon toolbar recent"></span></a>
<a href="/splatoon3mix/::cmd/diff?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="差分" rel="nofollow"><span class="system-icon toolbar diff"></span></a>
<a href="/splatoon3mix/::cmd/backup?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="バックアップ" rel="nofollow"><span class="system-icon toolbar backup"></span></a>
<a href="/splatoon3mix/::cmd/freeze?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="凍結" rel="nofollow"><span class="system-icon toolbar freeze"></span></a>
<a href="/splatoon3mix/::cmd/template?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="複製" rel="nofollow"><span class="system-icon toolbar copy"></span></a>
<a href="/splatoon3mix/::cmd/rename?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="名前変更" rel="nofollow"><span class="system-icon toolbar rename"></span></a>
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
                <ul><li><a href="/splatoon3mix/::cmd/newpage?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" rel="nofollow"><span class='system-icon toolbar new'></span> 新規</a></li><li><a href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" rel="nofollow"><span class='system-icon toolbar edit'></span> 編集</a></li><li><a href="/splatoon3mix/::cmd/attach?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" rel="nofollow"><span class='system-icon toolbar upload'></span> 添付</a></li></ul>
<ul><li><a href="/splatoon3mix/::cmd/list" rel="nofollow"><span class='system-icon toolbar list'></span> 一覧</a></li><li><a href="/splatoon3mix/RecentChanges" rel="nofollow"><span class='system-icon toolbar recent'></span> 最終更新</a></li><li><a href="/splatoon3mix/::cmd/diff?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" rel="nofollow"><span class='system-icon toolbar diff'></span> 差分</a></li><li><a href="/splatoon3mix/::cmd/backup?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" rel="nofollow"><span class='system-icon toolbar backup'></span> バックアップ</a></li></ul>
<ul><li><a href="/splatoon3mix/::cmd/freeze?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" rel="nofollow"><span class='system-icon toolbar freeze'></span> 凍結</a></li><li><a href="/splatoon3mix/::cmd/template?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" rel="nofollow"><span class='system-icon toolbar copy'></span> 複製</a></li><li><a href="/splatoon3mix/::cmd/rename?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" rel="nofollow"><span class='system-icon toolbar rename'></span> 名前変更</a></li></ul>
<ul><li><a href="/splatoon3mix/::cmd/help" rel="nofollow"><span class='system-icon toolbar help'></span> ヘルプ</a></li></ul>

            </div>
        </div>
    </div>    </div>

    <div class="container">
        <div class="clearfix">
            <div id="breadcrumbs" class="system-ui">
                <div id="topicpath"><a href="/splatoon3mix/" title="FrontPage"><i class="fa fa-home" style="margin-left: 6px; display: inline-block; min-width: 1.2em;"></i></a> &gt; サーモンラン</div>            </div>
            <div id="system-icon-container" class="system-ui">
                                <span id="share-button-root"></span>                <span id="admin-contact-root" class="single-system-icon"></span>
                <div id="load-panel-root"></div>
                <span id="admin-login" class="single-system-icon">
                    
<a class="admin-login-status" href="/splatoon3mix/::cmd/admin_login?return_to=%2Fsplatoon3mix%2F%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="未ログイン">
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
                                            <h1 class="title">サーモンラン NEXT WAVE</h1>
                                                                <div id="lastmodified">
                            Last-modified: 2025-12-19 (金) 20:13:35                                                            <span class="lastmodified-file-itself tooltip" data-tippy-content="このページ自体の更新: 2025-11-29 (土) 08:56:12"><i class="fas fa-file-signature"></i></span>
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
                                        <p><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3_%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8.webp?rev=3b065b35b470114485924d9254a1deda&amp;t=20221008104208" alt="サーモンラン_トップ" title="サーモンラン_トップ" width="614" height="345"  loading="lazy"><br />
<img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%E3%83%BB%E3%83%88%E3%83%83%E3%83%97.webp?rev=f1cc3dd670b0d398e16028ac19b6376c&amp;t=20221008104214" alt="終わりだよこのバイト" title="終わりだよこのバイト" width="614" height="345"  loading="lazy"></p>
<p>関連ページ:</p>
<form action="/splatoon3mix/::cmd/jumplist?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" method="post">
 <div>
  <select name="select"><option value="サーモンラン/開催履歴">サーモンラン/開催履歴</option>
<option value="サーモンラン/編成評価">サーモンラン/編成評価</option>
<option value="サーモンラン/サーモンラン初心者向け">サーモンラン/サーモンラン初心者向け</option>
<option value="サーモンラン/サーモンラン指南">サーモンラン/サーモンラン指南</option>
<option value="サーモンラン/ステージ">サーモンラン/ステージ</option>
<option value="サーモンラン/シャケの種類">サーモンラン/シャケの種類</option>
<option value="サーモンラン/特殊な状況">サーモンラン/特殊な状況</option>
</select>
  <input type="submit" name="jump" value="GO" />
 </div>
</form>
<hr class="full_hr" />
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">目次</div>
    <div class="fold-content visible-on-open"><div class="contents">
<a id="contents-index"></a>
<ul class="list1"><li><a href="#overview">概要 </a></li>
<li><a href="#tutorial">チュートリアル（けんしゅう） </a>
<ul class="list2"><li><a href="#tutorial_ki">キホンの「キ」 </a></li>
<li><a href="#tutorial_ho">キホンの「ホ」 </a></li></ul></li>
<li><a href="#cf35a330">試しうち場 </a></li>
<li><a href="#t183088b">ページマップ </a>
<ul class="list2"><li><a href="#stage">ステージ </a></li>
<li><a href="#salmon_type">シャケの種類 </a></li>
<li><a href="#special_condition">特殊な状況 </a></li>
<li><a href="#hacks">サーモンラン指南 </a>
<ul class="list3"><li><a href="#hacks_weapon">ブキ別指南 </a></li>
<li><a href="#weapon_correction">ブキ補正 </a></li></ul></li></ul></li>
<li><a href="#rule">ルール詳細 </a></li>
<li><a href="#weaponandgear">バイト専用のブキ・ギア・インクタンク </a></li>
<li><a href="#paygrade">評価</a></li>
<li><a href="#hazardlevel">キケン度 </a>
<ul class="list2"><li><a href="#r99a8579">キケン度による変化 </a>
<ul class="list3"><li><a href="#de6bdadb">ノルマ＆オオモノ出現数の表 </a></li>
<li><a href="#wea530d1">シャケの出現間隔の表 </a></li></ul></li></ul></li>
<li><a href="#w9c55236">報酬 </a>
<ul class="list2"><li><a href="#k0bdd097">クマサンポイントとプレゼント </a></li>
<li><a href="#a4a7708c">ウロコと限定品 </a></li></ul></li>
<li><a href="#mf0a5025">バッジ </a></li>
<li><a href="#c8dedbcc">イカリング3 </a></li>
<li><a href="#q451c880">開催履歴 </a></li>
<li><a href="#nff9673b">編成評価 </a></li>
<li><a href="#commentB">コメント(攻略・質問) </a></li>
<li><a href="#commentA">雑談用コメント </a></li></ul>
</div>
</div>
</div>
<hr class="full_hr" />
<h2 id="h2_content_1_0" >概要  <a class="anchor_super" name ="overview"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=overview" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<p>Splatoon3における協力型マルチプレイモード。<br />
たくさんやってくるシャケを仲間とともにシバき、金イクラを指定数以上納品することが目的。<br />
バンカラなイカたちの間で流行しているアルバイトらしい。<span class="wikicolor" style="color:silver">闇バイトというウワサも</span></p>
<p>このバイトを斡旋しているのは、「クマサン商会」という組織らしいが、詳細は謎に包まれている。<br />
バイトを始めたいなら、まずはクマサン商会を訪れよう。クマサン商会はバンカラ街のロビーに向かって右手、赤い門にある。<br />
中に入ってクマサンに話しかけ、初回の研修を受ければ、キミも今すぐにクマサン商会の一員として働く事ができるぞ！</p>
<p>商会の建物内部には、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>やオオモノシャケの弱点の体力丁度のマトや、イクラ投げなどの新アクションの練習ができる設備が整えられている。<br />
より良いアルバイターとなるべく、練習を重ねるのもいいだろう。</p>
<p>回収したイクラの量によってクマサンポイントを獲得できる。<br />
ポイントをたくさん稼げば、お金やバトルに役立つアイテムをゲットできる。<br />
具体的には<a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC" title="ギア/ギアパワー" class="rel-wiki-page">ギアパワー</a>のかけら、フードやドリンクのチケット、普段とは違った<span class="wikicolor" style="color:Silver">お洒落とは言い難い</span>デザインの限定<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>など。<br />
またノルマ達成で評価を上げれば、報酬アップやさらなる挑戦が用意されている。</p>
<p>舞台は、バンカラ街から大きく離れた位置にあるバンカラ湾の隔離海域<a id="notetext_1"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;任天堂公式サイトの「&lt;a class=&quot;ext&quot; href=&quot;https://www.nintendo.co.jp/interview/av5ja/index.html&quot;  rel=&quot;nofollow&quot;&gt;開発者に訊きました スプラトゥーン３&lt;span class=&quot;system-icon ext pukiwiki-open-uri&quot; data-href=&quot;https://www.nintendo.co.jp/interview/av5ja/index.html&quot; data-frame=&quot;_blank&quot;&gt;&lt;/span&gt;&lt;/a&gt;」にスプラトゥーン世界の地図が載っており、「バンカラ湾」と「ハイカラ湾」に「シャケのナワバリ」があることを確認できる。&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_1&quot;&gt;脚注 *1 へ&lt;/a&gt;&lt;/div&gt;">*1</a>。<br />
クマサン商会所有の専用ヘリでステージの近くまで来た後に、スーパージャンプでステージへと跳ぶ。<br />
島はインフラ不足・謎の磁気嵐のせいでリスポーンポイントもナワバリマップもない、過酷な環境となっている。<br />
ブキと<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>は、過酷な環境に耐えうるバイト専用のものが支給される。<br />
詳しくは<a href="#weaponandgear">ブキとギア</a>を参照されたし。</p>
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
<h2 id="h2_content_1_1" class="heading-after-first">チュートリアル（けんしゅう）  <a class="anchor_super" name ="tutorial"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=tutorial" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<p>チュートリアルでは、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>を遊ぶうえで不可欠なアクションを学ぶことができる。</p>
<div class="accordion-container ">
    <h3 class="accordion-header">
        <i class="fas fa-plus-square hidden-on-open"></i>
        <i class="fas fa-minus-square visible-on-open"></i>
        少し詳しく
    </h3>
    <div class="accordion-content"><p>初回のみ、チュートリアルを受けることをクマサンから勧められる。<br />
前作で<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>をプレイしたことがある場合、チュートリアル　キホンの「キ」はスキップすることができる。<br />
新オオモノの紹介を含むため、キホンの「ホ」はスキップできない。（ただしいつでも終了できる）<br />
また、ほうしゅう受け取り所向かって右の黄色いかごに乗った分厚いファイルから「キ」「ホ」両けんしゅうを何度でも受け直せるようになった。<br />
<strong><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>を遊んだことがない、操作を忘れてしまった！という方は絶対に受けておくように。</strong></p>
<h3 id="h3_content_4_0" >キホンの「キ」  <a class="anchor_super" name ="tutorial_ki"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=tutorial_ki" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<p>ここでは、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>とはどういうものなのか、何をすればいいのかという原点から<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>の遊び方を学ぶことができる。<br />
クマサンの指示に従いつつ進めていこう。<br />
シャケのインクでやられてしまってもクマサンが復活させてくれる。</p>
<h3 id="h3_content_4_1" class="heading-after-first">キホンの「ホ」  <a class="anchor_super" name ="tutorial_ho"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=tutorial_ho" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<p>ここでは、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>のすべきこと、金イクラを手に入れるための<strong>オオモノシャケのたおし方</strong>を学ぶことができる。<br />
しっかり頭に叩き込んで、実戦に備えよう。<br />
どのオオモノシャケと戦いたいか自由に選ぶことができ、任意のタイミングで終了できるので、苦手なオオモノシャケをたおす練習をするのも良いだろう。<br />
オオモノシャケの解説は<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E" title="サーモンラン/シャケの種類" class="rel-wiki-page">シャケの種類</a>を参照頂きたい。</p>
</div>
</div>
<h2 id="h2_content_1_2" class="heading-after-first">試しうち場  <a class="anchor_super" name ="cf35a330"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=cf35a330" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<p>クマサン商会の建物内部には試しうち場が設けられている。<br />
現場に臨む前に、支給されるブキの操作やダメージの確認をすると良いだろう。</p>
<p>また、ここにあるクマサン端末ではバイト履歴の確認と、マッチしたプレイヤーの通報、バイトシナリオの保存及びダウンロードが可能。</p>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">試しうち場詳細</div>
    <div class="fold-content visible-on-open"><p>ここにあるバルーンは各種シャケと同じ体力を持っている。<br />
左奥と左上のバルーンには、それが模しているオオモノシャケのシールが貼ってある。</p>
<ul class="list1"><li>大/中/小のバルーンは<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#cohock" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ドスコイ</a>(400)/<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#chum" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">中シャケ</a>(100)/<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>(40)の体力</li>
<li>左奥にある大きなバルーンは<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a>の体力(500)</li>
<li>左上にある大きなバルーンは<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a>の体力(300)＆高さとなっている。</li></ul>
<p>クマサン端末の右隣にある青い箱を調べると別のブキを選んで試しうちできる。<br />
選べるブキは現在のシフトで支給される4種類。</p>
<p>現在の支給ブキが全てランダムの「<strong><span class="wikicolor" style="color:springgreen; background-color:black">？</span></strong>」(または「<strong><span class="wikicolor" style="color:gold; background-color:black">？</span></strong>」)の場合、青い箱から選べるブキは<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC" title="ブキ/スプラシューター" class="rel-wiki-page">スプラシューター</a>のみとなる。<br />
その代わりに、バイトが終わると、手にしていたブキを試しうち場に持ち帰ることができる。<br />
クマサン印のブキはこの方法でのみ試しうち場に持ち込める。</p>
</div>
</div>
<hr class="full_hr" />
<h2 id="h2_content_1_3" class="heading-after-first">ページマップ  <a class="anchor_super" name ="t183088b"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=t183088b" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<h3 id="h3_content_1_4" class="heading-after-first">ステージ  <a class="anchor_super" name ="stage"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=stage" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8" title="サーモンラン/ステージ" class="rel-wiki-page">▼ステージ</a></p>
<ul class="list1"><li>開催ごとにどれかが選ばれる。<br />
各ステージにおいてとるべき行動や、特徴を理解することで効率的なバイトが実現できるぞ。</li></ul>
<h3 id="h3_content_1_5" class="heading-after-first">シャケの種類  <a class="anchor_super" name ="salmon_type"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=salmon_type" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E" title="サーモンラン/シャケの種類" class="rel-wiki-page">▼シャケの種類</a></p>
<ul class="list1"><li>敵となるシャケの紹介と攻略法が記されている。<br />
それぞれのシャケの適切な倒し方を知っていれば、現場で慌てることなく済む。<br />
ゲーム内のマニュアルと合わせて読んでおきたい。</li></ul>
<h3 id="h3_content_1_6" class="heading-after-first">特殊な状況  <a class="anchor_super" name ="special_condition"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=special_condition" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81" title="サーモンラン/特殊な状況" class="rel-wiki-page">▼特殊な状況</a></p>
<ul class="list1"><li>WAVE開始時に水位の変化が起こるタイミングがあり、加えて特殊な状況が起きることがある。<br />
背景が暗くなることが特殊な状況が始まる合図であり、通常waveとは全く異なる行動が要求される。<br />
そのルールは複雑だが、知っているだけで成功はグッと近くなるぞ。</li></ul>
<h3 id="h3_content_1_7" class="heading-after-first"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>指南  <a class="anchor_super" name ="hacks"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=hacks" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%E5%88%9D%E5%BF%83%E8%80%85%E5%90%91%E3%81%91" title="サーモンラン/サーモンラン初心者向け" class="rel-wiki-page">▼初心者向け</a></p>
<ul class="list1"><li>まずはここから。けんしゅうの内容をもう一度おさらいし、その上で知っておくべきことをなるべく簡単に解説するぞ。</li></ul>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%E6%8C%87%E5%8D%97" title="サーモンラン/サーモンラン指南" class="rel-wiki-page">▼中級者向け</a></p>
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>全体の基本的な戦略および立ち回りの考え方について記されている。参考にされたし。</li></ul>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%E3%83%8F%E3%83%83%E3%82%AF" title="サーモンラン/サーモンランハック" class="rel-wiki-page">▼上級者向け・テクニック集</a></p>
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>の小ネタやテクニックなど。知れば知るほどクマサンのために働きたくなる。</li></ul>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%E4%B8%8A%E7%B4%9A%E8%80%85%E5%90%91%E3%81%91%E6%8C%87%E5%8D%97" title="サーモンラン/サーモンラン上級者向け指南" class="rel-wiki-page">▼上級者向け・立ち回り指南</a></p>
<ul class="list1"><li>野良をさらに安定してクリアする上で重要な基礎となる立ち回りなどについて。</li></ul>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B5%E3%83%90%E3%82%A4%E3%83%90%E3%83%AB%E6%8C%87%E5%8D%97" title="サーモンラン/サバイバル指南" class="rel-wiki-page">▼サバイバル指南</a></p>
<ul class="list1"><li>業務成功のためにはより長く生き抜くことも重要だ。<br />
すぐウキワになってしまう、何度もウキワになってしまうことに悩んだら先輩たちのアドバイスを参考にしてみよう。</li></ul>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%88%E3%81%8F%E3%81%82%E3%82%8B%E5%A4%B1%E6%95%97" title="サーモンラン/よくある失敗" class="rel-wiki-page">▼よくある失敗</a></p>
<ul class="list1"><li>失敗扱いとなるのはゼンメツ、ノルマ不足のまま時間切れの2通りだが、そこへ至る原因は多岐にわたる。<br />
失敗が多いと感じたら、先輩たちの考察をもとに自らの行動を省みてみよう。<br />
また、失敗の原因を考察し書き込むことで、自らの意識改善やアルバイト全体の意識向上につながるだろう。</li></ul>
<h4 id="h4_content_1_8" class="heading-after-first">ブキ別指南  <a class="anchor_super" name ="hacks_weapon"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=hacks_weapon" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h4>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A" title="サーモンラン/ブキ別立ち回り" class="rel-wiki-page">▼ブキ別立ち回り</a><br />
　<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC%E3%83%BB%E3%83%9E%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%90%E3%83%BC%E5%B1%9E" title="サーモンラン/ブキ別立ち回り/シューター・マニューバー属" class="rel-wiki-page">▼シューター・マニューバー属</a><br />
　<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC%E5%B1%9E" title="サーモンラン/ブキ別立ち回り/ブラスター属" class="rel-wiki-page">▼ブラスター属</a><br />
　<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC%E5%B1%9E" title="サーモンラン/ブキ別立ち回り/ローラー属" class="rel-wiki-page">▼ローラー属</a><br />
　<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%83%95%E3%83%87%E5%B1%9E" title="サーモンラン/ブキ別立ち回り/フデ属" class="rel-wiki-page">▼フデ属</a><br />
　<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC%E5%B1%9E" title="サーモンラン/ブキ別立ち回り/チャージャー属" class="rel-wiki-page">▼チャージャー属</a><br />
　<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%82%B9%E3%83%94%E3%83%8A%E3%83%BC%E5%B1%9E" title="サーモンラン/ブキ別立ち回り/スピナー属" class="rel-wiki-page">▼スピナー属</a><br />
　<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%82%B9%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC%E5%B1%9E" title="サーモンラン/ブキ別立ち回り/スロッシャー属" class="rel-wiki-page">▼スロッシャー属</a><br />
　<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%BF%E3%83%BC%E5%B1%9E" title="サーモンラン/ブキ別立ち回り/シェルター属" class="rel-wiki-page">▼シェルター属</a><br />
　<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%82%B9%E3%83%88%E3%83%AA%E3%83%B3%E3%82%AC%E3%83%BC%E5%B1%9E" title="サーモンラン/ブキ別立ち回り/ストリンガー属" class="rel-wiki-page">▼ストリンガー属</a><br />
　<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC%E5%B1%9E" title="サーモンラン/ブキ別立ち回り/ワイパー属" class="rel-wiki-page">▼ワイパー属</a><br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%82%B5%E3%83%96%E3%83%BB%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%83%BB%E3%82%A4%E3%82%AF%E3%83%A9%E6%8A%95%E3%81%92" title="サーモンラン/ブキ別立ち回り/サブ・スペシャル・イクラ投げ" class="rel-wiki-page">▼サブ・スペ・イクラ投げ</a></p>
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>において、ブキの有効な扱い方は対人戦と大きく異なる。<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>特有の立ち回りを理解しておこう。</li></ul>
<h4 id="h4_content_1_9" class="heading-after-first">ブキ補正  <a class="anchor_super" name ="weapon_correction"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=weapon_correction" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h4>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%90%E3%82%A4%E3%83%88%E5%B0%82%E7%94%A8%E3%83%96%E3%82%AD%E3%81%AE%E8%A3%9C%E6%AD%A3" title="サーモンラン/バイト専用ブキの補正" class="rel-wiki-page">▼バイト専用ブキの補正</a></p>
<ul class="list1"><li>ブキによってはダメージやインク効率がバトルから変更されている場合がある。把握しておくと何かと便利だ。</li></ul>
<hr class="full_hr" />
<h2 id="h2_content_1_10" class="heading-after-first">ルール詳細  <a class="anchor_super" name ="rule"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=rule" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<p>目的は、制限時間内に「金イクラ」を既定のノルマ数「納品」すること。<br />
「納品」するイクラをあつめるためにシャケを「倒す」<br />
詳細は以下</p>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">ルール詳細</div>
    <div class="fold-content visible-on-open"><ul class="list1"><li>バイトの流れ
<ul class="list2"><li>マッチング後バイトが始まると各プレイヤーにバイト専用装備のセット（後述）が支給される。</li>
<li>シフトで決められたステージのスタート地点からゲームスタート</li>
<li>WAVE1がはじまり、成功条件を満たすと次のWAVE2がスタート、同様にWAVE3へ</li>
<li>最終WAVE3をクリアすることでバイトは成功。リザルト画面へ。</li>
<li>クリア条件が満たされなかった場合「Works Over!」となりバイト失敗。<br />
仮にWAVE1で失敗した場合も次のWAVEが始まると言ったことはなく、即リザルト画面へ。</li>
<li>リザルト画面では各種ポイントの入手、減算などが行われる（後述）</li></ul></li></ul>
<ul class="list1"><li>WAVEについて
<ul class="list2"><li>バイト1回のなかにWAVE（ウェーブ）と呼ばれる区切りが存在する。</li>
<li>ひとつのWAVEは10カウントの「準備時間」と100カウントの「本番」、WAVEクリア時の短い「休憩時間」で構成されている。</li>
<li>準備時間開始直後にそのWAVEで使用するメインウェポンが支給される。<br />
準備時間、休憩時間中にも、キャラを操作でき、ナワバリを広げ足場を固めること等ができる。<br />
また、水位の変化・空の暗転などの「<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81" title="サーモンラン/特殊な状況" class="rel-wiki-page">特殊な状況</a>」への環境変化が起こることもある。<br />
特に水位の変化では納品場所であるコンテナの位置が変わることもある。</li>
<li>100カウントの本番中は、ステージごとに決められた地点から<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>・オオモノシャケが定期的に現れる。<br />
さらに、バイトの難易度が上がるほど、シャケたちがより多く現れるようになる。</li>
<li>ひとつのWAVEごとに回収すべき金イクラ運搬のノルマが設定されている。<br />
「オンライン時の参加プレイヤーの称号や評価値の合計が高い」「WAVEが進む」ほどノルマは増える。</li>
<li>WAVE終了時点でイクラコンテナ外にある金イクラは、手元にあるものを含めてすべて消滅する。</li>
<li>WAVE終了後の小休憩が終わると強制的にスタート地点へスーパージャンプする。<br />
着地後はウキワ状態からでも復活し、次のWAVEの準備時間が始まる。<br />
（ただしリスポーン時間等でスーパージャンプが遅れる場合や、ウキワ状態から復活すると操作可能になるまで少し時間がかかる場合があるが、開始時間は変わらない。）</li></ul></li></ul>
<ul class="list1"><li>WAVEの成功、失敗条件
<ul class="list2"><li>成功条件は既定のノルマ数以上の納品を達成し、かつ、タイムアップまで生存状態のプレイヤーがいる(生存可能性がある)こと。<br />
(クリア後の小休憩時間に流れ弾や水没で全滅するのはセーフ)。</li>
<li>失敗条件は既定のノルマ数の納品に満たないで制限時間を終えること。<br />
あるいは、100カウント中にプレイヤー全員がやられる(生存可能性がなくなる)こと。</li></ul></li></ul>
<ul class="list1"><li>シャケとイクラ、納品について
<ul class="list2"><li>ザコ・オオモノ問わずシャケにダメージを与えると、ダメージを与えたプレイヤーがイクラ（金イクラではない）を自動入手する。<br />
（止めを刺せなくとも一部入手できる）</li>
<li>オオモノシャケなど特定のシャケを倒すとその場に金イクラを落とす。<br />
（水中などプレイヤーが侵入できない場所で倒した場合はプレイヤーが獲得できる別地点に落ちることがある。）</li>
<li>金イクラに接触することで回収し、プレイヤー1人につき1つまで保持できる。<br />
保持状態でやられても金イクラは奪われることはない。<br />
保持状態でイクラコンテナ前まで運搬し、生存状態であればAボタンを押すことで納品できる。<br />
保持しただけの金イクラや出現した金イクラはノルマ数には一切カウントされない。<br />
コンテナに納品した分のみがカウントされる。</li></ul></li></ul>
</div>
</div>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>のジレンマ</div>
    <div class="fold-content visible-on-open"><p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>においては「納品」と「討伐」二つの行動にジレンマがある。</p>
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>とは
<ul class="list2"><li>WAVEを3回成功すればクリア</li>
<li>WAVEを成功させるには金イクラをコンテナへ「納品」しないといけない。</li>
<li>金イクラを「納品」するには（オオモノ）シャケを「討伐」しないといけない。</li>
<li>しかしコンテナへ「納品」している間は「討伐」ができない。</li>
<li>もちろん「討伐」している間は「納品」ができない。</li>
<li>しかし「納品」しないと成功条件が満たせない、では「討伐」しないと……以下ループする。
<div class="spacer">&nbsp;</div></li></ul></li>
<li>ちなみに
<ul class="list2"><li>「納品」だけした場合<br />
そもそも納品するイクラがない。<br />
またシャケ軍団の攻勢がチームの殲滅力より上回り、コンテナへの道が封鎖される。<br />
最後に行きつく先はゼンメツだ。</li>
<li>「討伐」だけした場合<br />
納品数のノルマが達成できずに失敗する。</li></ul></li></ul>
<div class="spacer">&nbsp;</div>
<p>つまり「納品」←→「討伐」はまさにジレンマでありどちらか片方だけでは成功条件に不十分だ。<br />
また「納品」は「目的」であり「討伐」はその「手段」である。<br />
この2つのバランスを個人とチームで分け合い、目まぐるしくその役割分担を切り替えるのが<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>の難しさにして楽しさそのもの。<br />
攻略をするうえでも最終的に行き着くのはこの「納品」「討伐」をいかに効率よくするかに集約されていく。<br />
この2つの軸を理解しているかどうかで指南ページなどの知識の吸収率も変わってくるだろう。</p>
</div>
</div>

<div id="pc-caption-300x600-ad-container">
<!-- /19033742/WIKIWIKI_SP_CAPTION_300x600 -->
<div id='div-gpt-ad-1731135777754-0' class="hidden-switch-class"></div>
</div><h2 id="h2_content_1_11" class="heading-after-first">バイト専用のブキ・<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>・インクタンク  <a class="anchor_super" name ="weaponandgear"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=weaponandgear" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>ではバイト専用のブキ・<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>・インクタンクが支給される。<br />
通常のバトルで使用するものとは違いがあるので注意されたし。</p>
<h3 id="h3_content_8_0" ><a class="anchor" name ="weapon"></a>バイト専用ブキ</h3>

<p>バイトでは、クマサン商会が用意した対シャケ仕様のブキを借りて使うことになる。<br />
そのため、自身がブキを所有している必要はない。逆に自前のブキを持ち込むこともできない。</p>
<p>支給されるブキの多くはバイト用にチューニングされているのか、バトルで使うものとは威力・燃費が異なる。<br />
支給されるブキは全て基本モデルであり、コラボやカスタムと言ったマイナーチェンジ版は登場しない。</p>
<p>支給される可能性のあるブキは以下。</p>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">バイト専用ブキ一覧</div>
    <div class="fold-content visible-on-open"><div class="h-scrollable"><table><thead><tr><th style="text-align:center; width:50px;">Ver.</th><th style="text-align:center;">ブキ</th><th style="text-align:center; width:120px;">備考</th></tr></thead><tbody><tr><td style="text-align:center; width:50px;">1.0.0</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%9C%E3%83%BC%E3%83%AB%E3%83%89%E3%83%9E%E3%83%BC%E3%82%AB%E3%83%BC.png?rev=6e3c4434ece589bd5cb6e7cad05cc8d5&amp;t=20230627135358" alt="ボールドマーカー.png" title="ボールドマーカー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%9C%E3%83%BC%E3%83%AB%E3%83%89%E3%83%9E%E3%83%BC%E3%82%AB%E3%83%BC" title="ブキ/ボールドマーカー" class="rel-wiki-page">ボールドマーカー</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%8F%E3%81%8B%E3%81%B0%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC.png?rev=71c835cfbea476bbea062d8b083a62c6&amp;t=20220905214729" alt="わかばシューター.png" title="わかばシューター.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%8F%E3%81%8B%E3%81%B0%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC" title="ブキ/わかばシューター" class="rel-wiki-page">わかばシューター</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B7%E3%83%A3%E3%83%BC%E3%83%97%E3%83%9E%E3%83%BC%E3%82%AB%E3%83%BC.png?rev=1f53326ed2f779537426c3ce02a55134&amp;t=20230627135402" alt="シャープマーカー.png" title="シャープマーカー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B7%E3%83%A3%E3%83%BC%E3%83%97%E3%83%9E%E3%83%BC%E3%82%AB%E3%83%BC" title="ブキ/シャープマーカー" class="rel-wiki-page">シャープマーカー</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%97%E3%83%AD%E3%83%A2%E3%83%87%E3%83%A9%E3%83%BCMG.png?rev=ffd5754f538379f7283b678366cb4b96&amp;t=20220905214705" alt="プロモデラーMG.png" title="プロモデラーMG.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%97%E3%83%AD%E3%83%A2%E3%83%87%E3%83%A9%E3%83%BCMG" title="ブキ/プロモデラーMG" class="rel-wiki-page">プロモデラーMG</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B9%E3%83%97%E3%83%A9%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC.png?rev=4d70126a9b68e76b463e182d3d42218d&amp;t=20220905214644" alt="スプラシューター.png" title="スプラシューター.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC" title="ブキ/スプラシューター" class="rel-wiki-page">スプラシューター</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/.52%E3%82%AC%E3%83%AD%E3%83%B3.png?rev=18c6eaed972b85a7ed9a01503afd8aff&amp;t=20220905214540" alt=".52ガロン.png" title=".52ガロン.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/.52%E3%82%AC%E3%83%AD%E3%83%B3" title="ブキ/.52ガロン" class="rel-wiki-page">.52ガロン</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/N-ZAP85.png?rev=1dc33e3c88bda7c5644ced653ea31886&amp;t=20220905214615" alt="N-ZAP85.png" title="N-ZAP85.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/N-ZAP85" title="ブキ/N-ZAP85" class="rel-wiki-page">N-ZAP85</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%97%E3%83%A9%E3%82%A4%E3%83%A0%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC.png?rev=7250edc0e3c7e4bb6432d25f1b83711b&amp;t=20220905214655" alt="プライムシューター.png" title="プライムシューター.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%97%E3%83%A9%E3%82%A4%E3%83%A0%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC" title="ブキ/プライムシューター" class="rel-wiki-page">プライムシューター</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/.96%E3%82%AC%E3%83%AD%E3%83%B3.png?rev=064da5391cf8591ffe192d7e74f644c5&amp;t=20220905214558" alt=".96ガロン.png" title=".96ガロン.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/.96%E3%82%AC%E3%83%AD%E3%83%B3" title="ブキ/.96ガロン" class="rel-wiki-page">.96ガロン</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88%E3%82%B9%E3%82%A4%E3%83%BC%E3%83%91%E3%83%BC.png?rev=859c320f86fd727ddbec3f1526388c2a&amp;t=20220905214623" alt="ジェットスイーパー.png" title="ジェットスイーパー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88%E3%82%B9%E3%82%A4%E3%83%BC%E3%83%91%E3%83%BC" title="ブキ/ジェットスイーパー" class="rel-wiki-page">ジェットスイーパー</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/L3%E3%83%AA%E3%83%BC%E3%83%AB%E3%82%AC%E3%83%B3.png?rev=db5d9c167521f57ae951636b4e0c56e1&amp;t=20220905214609" alt="L3リールガン.png" title="L3リールガン.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/L3%E3%83%AA%E3%83%BC%E3%83%AB%E3%82%AC%E3%83%B3" title="ブキ/L3リールガン" class="rel-wiki-page">L3リールガン</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/H3%E3%83%AA%E3%83%BC%E3%83%AB%E3%82%AC%E3%83%B3.png?rev=fc08cf7b11fc72433c85efd244561bf6&amp;t=20220905214605" alt="H3リールガン.png" title="H3リールガン.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/H3%E3%83%AA%E3%83%BC%E3%83%AB%E3%82%AC%E3%83%B3" title="ブキ/H3リールガン" class="rel-wiki-page">H3リールガン</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%9C%E3%83%88%E3%83%AB%E3%82%AC%E3%82%A4%E3%82%B6%E3%83%BC.png?rev=edbc84198a4a2d44dc0648462083f058&amp;t=20220905214719" alt="ボトルガイザー.png" title="ボトルガイザー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%9C%E3%83%88%E3%83%AB%E3%82%AC%E3%82%A4%E3%82%B6%E3%83%BC" title="ブキ/ボトルガイザー" class="rel-wiki-page">ボトルガイザー</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AB%E3%83%BC%E3%83%9C%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC.png?rev=2d3ede75f6260c236cbdeca7d4f8b50d&amp;t=20220905220112" alt="カーボンローラー.png" title="カーボンローラー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AB%E3%83%BC%E3%83%9C%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC" title="ブキ/カーボンローラー" class="rel-wiki-page">カーボンローラー</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC.png?rev=35e16e1b1929197aacb3b358faca81da&amp;t=20220905220143" alt="スプラローラー.png" title="スプラローラー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC" title="ブキ/スプラローラー" class="rel-wiki-page">スプラローラー</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%80%E3%82%A4%E3%83%8A%E3%83%A2%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC.png?rev=4caedd3918f8834252a601f42b95f43a&amp;t=20220905220149" alt="ダイナモローラー.png" title="ダイナモローラー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%80%E3%82%A4%E3%83%8A%E3%83%A2%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC" title="ブキ/ダイナモローラー" class="rel-wiki-page">ダイナモローラー</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%B4%E3%82%A1%E3%83%AA%E3%82%A2%E3%83%96%E3%83%AB%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC.png?rev=ca05919a5b43e3f8795a2be2eb28bbfc&amp;t=20220905220053" alt="ヴァリアブルローラー.png" title="ヴァリアブルローラー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%B4%E3%82%A1%E3%83%AA%E3%82%A2%E3%83%96%E3%83%AB%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC" title="ブキ/ヴァリアブルローラー" class="rel-wiki-page">ヴァリアブルローラー</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B9%E3%82%AF%E3%82%A4%E3%83%83%E3%82%AF%E3%83%AA%E3%83%B3%CE%B1.png?rev=615c1848d4f7049c08ece6b1d11dfc6e&amp;t=20220905220120" alt="スクイックリンα.png" title="スクイックリンα.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%82%AF%E3%82%A4%E3%83%83%E3%82%AF%E3%83%AA%E3%83%B3%CE%B1" title="ブキ/スクイックリンα" class="rel-wiki-page">スクイックリンα</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC.png?rev=cedd669f551f86440a8bd380540044a6&amp;t=20220905220137" alt="スプラチャージャー.png" title="スプラチャージャー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC" title="ブキ/スプラチャージャー" class="rel-wiki-page">スプラチャージャー</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%AA%E3%83%83%E3%82%BF%E3%83%BC4K.png?rev=4a0657ab4f525dfc5b33cd1bb2ce976a&amp;t=20220906111947" alt="リッター4K.png" title="リッター4K.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%AA%E3%83%83%E3%82%BF%E3%83%BC4K" title="ブキ/リッター4K" class="rel-wiki-page">リッター4K</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/14%E5%BC%8F%E7%AB%B9%E7%AD%92%E9%8A%83%E3%83%BB%E7%94%B2.png?rev=b413ea93f22227adc5bfc11c5c014212&amp;t=20220905220105" alt="14式竹筒銃・甲.png" title="14式竹筒銃・甲.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/14%E5%BC%8F%E7%AB%B9%E7%AD%92%E9%8A%83%E3%83%BB%E7%94%B2" title="ブキ/14式竹筒銃・甲" class="rel-wiki-page">14式竹筒銃・甲</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%BD%E3%82%A4%E3%83%81%E3%83%A5%E3%83%BC%E3%83%90%E3%83%BC.png?rev=d3cc8b41a12db0aad13ccceef78290c1&amp;t=20220905220218" alt="ソイチューバー.png" title="ソイチューバー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%BD%E3%82%A4%E3%83%81%E3%83%A5%E3%83%BC%E3%83%90%E3%83%BC" title="ブキ/ソイチューバー" class="rel-wiki-page">ソイチューバー</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%90%E3%82%B1%E3%83%83%E3%83%88%E3%82%B9%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC.png?rev=a584176d80465fdf6e5790982da674ec&amp;t=20220906103852" alt="バケットスロッシャー.png" title="バケットスロッシャー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%90%E3%82%B1%E3%83%83%E3%83%88%E3%82%B9%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC" title="ブキ/バケットスロッシャー" class="rel-wiki-page">バケットスロッシャー</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%92%E3%83%83%E3%82%BB%E3%83%B3.png?rev=a5e9a5352ff6f8785117db986a0eecc7&amp;t=20220906103905" alt="ヒッセン.png" title="ヒッセン.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%92%E3%83%83%E3%82%BB%E3%83%B3" title="ブキ/ヒッセン" class="rel-wiki-page">ヒッセン</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%A5%E3%83%BC%E3%82%B9%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC.png?rev=5db66c3f1fdca3b8fde652de4a08af46&amp;t=20220906103807" alt="スクリュースロッシャー.png" title="スクリュースロッシャー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%A5%E3%83%BC%E3%82%B9%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC" title="ブキ/スクリュースロッシャー" class="rel-wiki-page">スクリュースロッシャー</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AA%E3%83%BC%E3%83%90%E3%83%BC%E3%83%95%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC.png?rev=afe5a9cc21242502cfc0347951e61fe4&amp;t=20220906103738" alt="オーバーフロッシャー.png" title="オーバーフロッシャー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AA%E3%83%BC%E3%83%90%E3%83%BC%E3%83%95%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC" title="ブキ/オーバーフロッシャー" class="rel-wiki-page">オーバーフロッシャー</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%A8%E3%82%AF%E3%82%B9%E3%83%97%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC.png?rev=581571f8d0ed8584aeb4abff65482137&amp;t=20220906103732" alt="エクスプロッシャー.png" title="エクスプロッシャー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%A8%E3%82%AF%E3%82%B9%E3%83%97%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC" title="ブキ/エクスプロッシャー" class="rel-wiki-page">エクスプロッシャー</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B9%E3%83%97%E3%83%A9%E3%82%B9%E3%83%94%E3%83%8A%E3%83%BC.png?rev=a030420253495ac7d3cbada380741cd6&amp;t=20220906103818" alt="スプラスピナー.png" title="スプラスピナー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%82%B9%E3%83%94%E3%83%8A%E3%83%BC" title="ブキ/スプラスピナー" class="rel-wiki-page">スプラスピナー</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%90%E3%83%AC%E3%83%AB%E3%82%B9%E3%83%94%E3%83%8A%E3%83%BC.png?rev=65b52dcb9159bfc35c2d107b12b8da64&amp;t=20220906103859" alt="バレルスピナー.png" title="バレルスピナー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%90%E3%83%AC%E3%83%AB%E3%82%B9%E3%83%94%E3%83%8A%E3%83%BC" title="ブキ/バレルスピナー" class="rel-wiki-page">バレルスピナー</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%8F%E3%82%A4%E3%83%89%E3%83%A9%E3%83%B3%E3%83%88.png?rev=ab6a736dc2e4c56fcda0cb2ec6bd1d5e&amp;t=20220906103846" alt="ハイドラント.png" title="ハイドラント.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%8F%E3%82%A4%E3%83%89%E3%83%A9%E3%83%B3%E3%83%88" title="ブキ/ハイドラント" class="rel-wiki-page">ハイドラント</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%BC%E3%82%B2%E3%83%AB%E3%82%B7%E3%83%A5%E3%83%A9%E3%82%A4%E3%83%90%E3%83%BC.png?rev=e256f3e325fe520d1b10093d33dc53df&amp;t=20220906103755" alt="クーゲルシュライバー.png" title="クーゲルシュライバー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%BC%E3%82%B2%E3%83%AB%E3%82%B7%E3%83%A5%E3%83%A9%E3%82%A4%E3%83%90%E3%83%BC" title="ブキ/クーゲルシュライバー" class="rel-wiki-page">クーゲルシュライバー</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%8E%E3%83%BC%E3%83%81%E3%83%A9%E3%82%B947.png?rev=ac1b50a2695c156f0b34ce72050f6a5a&amp;t=20220906103841" alt="ノーチラス47.png" title="ノーチラス47.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%8E%E3%83%BC%E3%83%81%E3%83%A9%E3%82%B947" title="ブキ/ノーチラス47" class="rel-wiki-page">ノーチラス47</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B9%E3%83%91%E3%83%83%E3%82%BF%E3%83%AA%E3%83%BC.png?rev=9c1e988714c460deb369e6c5dad974cc&amp;t=20220906103812" alt="スパッタリー.png" title="スパッタリー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%91%E3%83%83%E3%82%BF%E3%83%AA%E3%83%BC" title="ブキ/スパッタリー" class="rel-wiki-page">スパッタリー</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%9E%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%90%E3%83%BC.png?rev=be5d57005fd92c7aaae40b61da015b9d&amp;t=20220906103827" alt="スプラマニューバー.png" title="スプラマニューバー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%9E%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%90%E3%83%BC" title="ブキ/スプラマニューバー" class="rel-wiki-page">スプラマニューバー</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B1%E3%83%AB%E3%83%93%E3%83%B3525.png?rev=d3ba307e5af6a60aafe3cbdf5668c8a7&amp;t=20220906103800" alt="ケルビン525.png" title="ケルビン525.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B1%E3%83%AB%E3%83%93%E3%83%B3525" title="ブキ/ケルビン525" class="rel-wiki-page">ケルビン525</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%87%E3%83%A5%E3%82%A2%E3%83%AB%E3%82%B9%E3%82%A4%E3%83%BC%E3%83%91%E3%83%BC.png?rev=20b850827dcfff36a7eb059b742ff117&amp;t=20220906103833" alt="デュアルスイーパー.png" title="デュアルスイーパー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%87%E3%83%A5%E3%82%A2%E3%83%AB%E3%82%B9%E3%82%A4%E3%83%BC%E3%83%91%E3%83%BC" title="ブキ/デュアルスイーパー" class="rel-wiki-page">デュアルスイーパー</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%82%A2%E3%83%83%E3%83%89%E3%83%9B%E3%83%83%E3%83%91%E3%83%BC%E3%83%96%E3%83%A9%E3%83%83%E3%82%AF.png?rev=de6749c30cf1e625e20619fe3fc60aed&amp;t=20220906103748" alt="クアッドホッパーブラック.png" title="クアッドホッパーブラック.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%82%A2%E3%83%83%E3%83%89%E3%83%9B%E3%83%83%E3%83%91%E3%83%BC%E3%83%96%E3%83%A9%E3%83%83%E3%82%AF" title="ブキ/クアッドホッパーブラック" class="rel-wiki-page">クアッドホッパーブラック</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%91%E3%83%A9%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%BF%E3%83%BC.png?rev=b37a3174dd7867802d15de24c5bb0f3a&amp;t=20220906104623" alt="パラシェルター.png" title="パラシェルター.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%91%E3%83%A9%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%BF%E3%83%BC" title="ブキ/パラシェルター" class="rel-wiki-page">パラシェルター</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%94%E3%83%B3%E3%82%B0%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%BF%E3%83%BC.png?rev=829b5f70eaabdff2b130d24dc4927151&amp;t=20220906104534" alt="キャンピングシェルター.png" title="キャンピングシェルター.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%94%E3%83%B3%E3%82%B0%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%BF%E3%83%BC" title="ブキ/キャンピングシェルター" class="rel-wiki-page">キャンピングシェルター</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B9%E3%83%91%E3%82%A4%E3%82%AC%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88.png?rev=e566b90aee9cfdf1a15f1a70bfadc5ac&amp;t=20220906104548" alt="スパイガジェット.png" title="スパイガジェット.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%91%E3%82%A4%E3%82%AC%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88" title="ブキ/スパイガジェット" class="rel-wiki-page">スパイガジェット</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%8E%E3%83%B4%E3%82%A1%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC.png?rev=903f8c162cfbf6fbb2b194759c8bfc7c&amp;t=20220906104611" alt="ノヴァブラスター.png" title="ノヴァブラスター.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%8E%E3%83%B4%E3%82%A1%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC" title="ブキ/ノヴァブラスター" class="rel-wiki-page">ノヴァブラスター</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%9B%E3%83%83%E3%83%88%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC.png?rev=b3bb1bd6dccefa222fe7e5c900771c08&amp;t=20220906104633" alt="ホットブラスター.png" title="ホットブラスター.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%9B%E3%83%83%E3%83%88%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC" title="ブキ/ホットブラスター" class="rel-wiki-page">ホットブラスター</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%AD%E3%83%B3%E3%82%B0%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC.png?rev=0c6a2b501b46cbcf8a2b5c5d78349793&amp;t=20220906104642" alt="ロングブラスター.png" title="ロングブラスター.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%AD%E3%83%B3%E3%82%B0%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC" title="ブキ/ロングブラスター" class="rel-wiki-page">ロングブラスター</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC.png?rev=1a0a11ec5a618ee936b01b62ed1a17da&amp;t=20220906104732" alt="クラッシュブラスター.png" title="クラッシュブラスター.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC" title="ブキ/クラッシュブラスター" class="rel-wiki-page">クラッシュブラスター</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%A9%E3%83%94%E3%83%83%E3%83%89%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC.png?rev=b6c1d6630bd7b0eb09fdce30b06c04d1&amp;t=20230918121459" alt="ラピッドブラスター.png" title="ラピッドブラスター.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%A9%E3%83%94%E3%83%83%E3%83%89%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC" title="ブキ/ラピッドブラスター" class="rel-wiki-page">ラピッドブラスター</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/R%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC%E3%82%A8%E3%83%AA%E3%83%BC%E3%83%88.png?rev=fcce0157a057946bd3cffed1dc249664&amp;t=20230918121455" alt="Rブラスターエリート.png" title="Rブラスターエリート.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/R%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC%E3%82%A8%E3%83%AA%E3%83%BC%E3%83%88" title="ブキ/Rブラスターエリート" class="rel-wiki-page">Rブラスターエリート</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%91%E3%83%96%E3%83%AD.png?rev=693c3a8ddd528cb106340d2430d4ef42&amp;t=20220906104619" alt="パブロ.png" title="パブロ.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%91%E3%83%96%E3%83%AD" title="ブキ/パブロ" class="rel-wiki-page">パブロ</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%9B%E3%82%AF%E3%82%B5%E3%82%A4.png?rev=4caeadaa7f73c847a1126a2880aefaa2&amp;t=20220906104629" alt="ホクサイ.png" title="ホクサイ.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%9B%E3%82%AF%E3%82%B5%E3%82%A4" title="ブキ/ホクサイ" class="rel-wiki-page">ホクサイ</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%88%E3%83%A9%E3%82%A4%E3%82%B9%E3%83%88%E3%83%AA%E3%83%B3%E3%82%AC%E3%83%BC.png?rev=e6f62e9de49038a72766380f8cfd0a36&amp;t=20220906104558" alt="トライストリンガー.png" title="トライストリンガー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%88%E3%83%A9%E3%82%A4%E3%82%B9%E3%83%88%E3%83%AA%E3%83%B3%E3%82%AC%E3%83%BC" title="ブキ/トライストリンガー" class="rel-wiki-page">トライストリンガー</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/LACT-450.png?rev=2e2470dd345a460e841dd8578cb349d3&amp;t=20221004145801" alt="LACT-450.png" title="LACT-450.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/LACT-450" title="ブキ/LACT-450" class="rel-wiki-page">LACT-450</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%89%E3%83%A9%E3%82%A4%E3%83%96%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC.png?rev=b6018aed936af11ce2336c8c55f7d7d8&amp;t=20220906104603" alt="ドライブワイパー.png" title="ドライブワイパー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%89%E3%83%A9%E3%82%A4%E3%83%96%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC" title="ブキ/ドライブワイパー" class="rel-wiki-page">ドライブワイパー</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B8%E3%83%A0%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC.png?rev=25412cd375d23230ee114f8c91a98af1&amp;t=20220906104541" alt="ジムワイパー.png" title="ジムワイパー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B8%E3%83%A0%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC" title="ブキ/ジムワイパー" class="rel-wiki-page">ジムワイパー</a></td><td style="text-align:center; width:120px;">全52種類</td></tr><tr><td style="text-align:center; width:50px;">2.0.0</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%B9%E3%83%9A%E3%83%BC%E3%82%B9%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC.png?rev=72407d7eeb73003b9c450c614e8f34c4&amp;t=20221201093754" alt="スペースシューター.png" title="スペースシューター.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%83%BC%E3%82%B9%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC" title="ブキ/スペースシューター" class="rel-wiki-page">スペースシューター</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%AF%E3%82%A4%E3%83%89%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC.png?rev=92ad01bb0d912e69be0ebe69586fb8bf&amp;t=20221201093807" alt="ワイドローラー.png" title="ワイドローラー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%AF%E3%82%A4%E3%83%89%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC" title="ブキ/ワイドローラー" class="rel-wiki-page">ワイドローラー</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/R-PEN%EF%BC%8F5H.png?rev=caf96679d5ab5dc7cc717f886d4e0380&amp;t=20221201094005" alt="R-PEN／5H.png" title="R-PEN／5H.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/R-PEN%EF%BC%8F5H" title="ブキ/R-PEN／5H" class="rel-wiki-page">R-PEN／5H</a></td><td style="text-align:center; width:120px;">3種類追加<br class="spacer">全55種類</td></tr><tr><td style="text-align:center; width:50px;">4.0.0</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/S-BLAST92.png?rev=98a3cd103faa65c7307b0d11d5ed9584&amp;t=20230602152512" alt="S-BLAST92.png" title="S-BLAST92.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/S-BLAST92" title="ブキ/S-BLAST92" class="rel-wiki-page">S-BLAST92</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%95%E3%82%A3%E3%83%B3%E3%82%BB%E3%83%B3%E3%83%88.png?rev=4b603cb2dce31f5c0d8929f2dfedeb1b&amp;t=20230602152520" alt="フィンセント.png" title="フィンセント.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%95%E3%82%A3%E3%83%B3%E3%82%BB%E3%83%B3%E3%83%88" title="ブキ/フィンセント" class="rel-wiki-page">フィンセント</a></td><td style="text-align:center; width:120px;">2種類追加<br class="spacer">全57種類</td></tr><tr><td style="text-align:center; width:50px;">5.0.0</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%A2%E3%83%83%E3%83%97%E3%83%AA%E3%83%B3.png?rev=ead8a9e0a5bc61a925ffec4ac382334a&amp;t=20230902112614" alt="モップリン.png" title="モップリン.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%A2%E3%83%83%E3%83%97%E3%83%AA%E3%83%B3" title="ブキ/モップリン" class="rel-wiki-page">モップリン</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%A4%E3%82%B0%E3%82%B6%E3%83%9F%E3%83%8A%E3%83%BC.png?rev=ece8f62ace7229a26fac66755ea7b2aa&amp;t=20230902112810" alt="イグザミナー.png" title="イグザミナー.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%A4%E3%82%B0%E3%82%B6%E3%83%9F%E3%83%8A%E3%83%BC" title="ブキ/イグザミナー" class="rel-wiki-page">イグザミナー</a></td><td style="text-align:center; width:120px;">2種類追加<br class="spacer">全59種類</td></tr><tr><td style="text-align:center; width:50px;">7.0.0</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AC%E3%82%A8%E3%83%B3FF.png.webp?rev=c59ffedf75a4c75c89c11f6b80984cd3&amp;t=20240302124703" alt="ガエンFF.png" title="ガエンFF.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AC%E3%82%A8%E3%83%B3FF" title="ブキ/ガエンFF" class="rel-wiki-page">ガエンFF</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/24%E5%BC%8F%E5%BC%B5%E6%9B%BF%E5%82%98%E3%83%BB%E7%94%B2.png?rev=90601185def0aa32e513a2fd8fac9f37&amp;t=20240302124644" alt="24式張替傘・甲.png" title="24式張替傘・甲.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/24%E5%BC%8F%E5%BC%B5%E6%9B%BF%E5%82%98%E3%83%BB%E7%94%B2" title="ブキ/24式張替傘・甲" class="rel-wiki-page">24式張替傘・甲</a></td><td style="text-align:center; width:120px;">2種類追加<br class="spacer">全61種類</td></tr><tr><td style="text-align:center; width:50px;">8.0.0</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%95%E3%83%AB%E3%82%A4%E3%83%89V.png.webp?rev=c944225c8294454c88576758a02a0bfc&amp;t=20240603134357" alt="フルイドV.png" title="フルイドV.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%95%E3%83%AB%E3%82%A4%E3%83%89V" title="ブキ/フルイドV" class="rel-wiki-page">フルイドV</a> / <img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%83%87%E3%83%B3%E3%82%BF%E3%83%AB%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC%E3%83%9F%E3%83%B3%E3%83%88.png.webp?rev=736086270d4b8468d43786bb5e35c5ba&amp;t=20240603134347" alt="デンタルワイパーミント.png" title="デンタルワイパーミント.png" width="24" height="24"  loading="lazy"> <a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%87%E3%83%B3%E3%82%BF%E3%83%AB%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC%E3%83%9F%E3%83%B3%E3%83%88" title="ブキ/デンタルワイパーミント" class="rel-wiki-page">デンタルワイパーミント</a></td><td style="text-align:center; width:120px;">2種類追加<br class="spacer">全63種類</td></tr></tbody></table></div>
</div>
</div>
<p>性能の詳細は以下のページで確認されたし。<br />
▼<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%90%E3%82%A4%E3%83%88%E5%B0%82%E7%94%A8%E3%83%96%E3%82%AD%E3%81%AE%E8%A3%9C%E6%AD%A3" title="サーモンラン/バイト専用ブキの補正" class="rel-wiki-page">バイト専用ブキの補正</a><br />
▼<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A" title="サーモンラン/ブキ別立ち回り" class="rel-wiki-page">ブキ別立ち回り</a><br />
過去に支給されたブキについては<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E9%96%8B%E5%82%AC%E5%B1%A5%E6%AD%B4" title="サーモンラン/開催履歴" class="rel-wiki-page">サーモンラン/開催履歴</a>を参照。</p>
<div class="spacer">&nbsp;</div>
<h4 id="h4_content_10_0" ><a class="anchor" name ="mainweapon"></a>メインウェポン</h4>

<p>オンラインの<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>では「支給ブキ」として4種類のメインウェポンが告知されている。<br />
（<a href="/splatoon3mix/%E3%82%A4%E3%82%AB%E3%83%AA%E3%83%B3%E3%82%B03" title="イカリング3" class="rel-wiki-page">イカリング3</a>、メニュー画面のステージ情報などからも確認ができる。）<br />
WAVE開始時に、この4種類のブキが4人のメンバーにランダムで配られる。<br />
WAVEが終わるとブキは一度回収され、次のWAVE開始時に再び支給される。このとき、同じ人に同じブキが配られないように、毎回異なるブキが支給される。<br />
なので、1人のアルバイターは1回のバイトで3種類のブキを使うことになる。（<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/Extra%20Wave" title="サーモンラン/特殊な状況/Extra Wave" class="rel-wiki-page">Extra Wave</a>が発生すれば4種類。）</p>
<p><a class="anchor" name ="grizzco_weapons"></a><br />
「今回支給されるブキ」には<strong><span class="wikicolor" style="color:springgreen; background-color:black">？</span></strong>または<strong><span class="wikicolor" style="color:gold; background-color:black">？</span></strong>が含まれていることがある。<br />
この場合、ブキの支給のされ方は通常とは少し異なったものになる。</p>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open"><strong><span class="wikicolor" style="color:springgreen; background-color:black">？</span></strong>と<strong><span class="wikicolor" style="color:gold; background-color:black">？</span></strong>について</div>
    <div class="fold-content visible-on-open"><p><span class="ref-external-image">
    <img src="https://cdn.wikiwiki.jp/proxy-image/w/splatoon3mix?url=https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FF3xtqe-bEAAV6_w.jpg" alt="ワタシ個人の持ち物が混ざってしまいました。見つけても絶対に持ち出さず、口外しないでください。" title="ワタシ個人の持ち物が混ざってしまいました。見つけても絶対に持ち出さず、口外しないでください。" width="384" height="216"  loading="lazy">
    <span class="ref-external-info tooltip" data-tippy-content="オリジナルは外部のホストによって提供されています。 (配信元: pbs.twimg.com)"><i class="fa-solid fa-square-quote"></i></span>
</span><br />
<span class="wikicolor" style="color:Maroon"><span style="font-size:9px">▲画像は公式Twitter(@SplatoonJP)の<a class="ext" href="https://wikiwiki.jp/p/cushion?to=https%3A%2F%2Ftwitter.com%2FSplatoonJP%2Fstatus%2F1692462337222218086"  rel="nofollow">2023年8月18日のツイート<span class="system-icon ext pukiwiki-open-uri" data-href="https://twitter.com/SplatoonJP/status/1692462337222218086" data-frame="_blank"></span></a>より。</span></span></p>
<p><strong><span class="wikicolor" style="color:springgreen; background-color:black">？</span></strong>枠を引くと、上記の「支給される可能性のあるブキ」と「<strong><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3#weaponandgear" title="サーモンラン" class="rel-wiki-page">レアブキ</a></strong>」の中からランダムで選ばれたブキが支給される。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3#weaponandgear" title="サーモンラン" class="rel-wiki-page">レアブキ</a>とはいうものの、その<strong>支給確率は20%</strong>ほどとされており、他のブキよりも遭遇率が高い。<br />
出現するブキは完全にランダムなので、バイト中にすでに使ったブキが支給されることもある。また、選出内容によっては違うプレイヤーが同じブキを持つこともありうる。</p>
<p><strong><span class="wikicolor" style="color:gold; background-color:black">？</span></strong>枠を引くと、<strong>必ず「<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3#weaponandgear" title="サーモンラン" class="rel-wiki-page">レアブキ</a>」が支給される</strong>。内容は全種類の「<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3#weaponandgear" title="サーモンラン" class="rel-wiki-page">レアブキ</a>」の中からランダム。<br />
こちらも選出内容によってブキ被りが発生する。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3#weaponandgear" title="サーモンラン" class="rel-wiki-page">レアブキ</a>とはイカのブキのこと。<br />
どのブキも「クマサン印の○○」という名前で統一されている。通称クマブキ。</p>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%82%B9%E3%83%88%E3%83%AA%E3%83%B3%E3%82%AC%E3%83%BC" title="ブキ/クマサン印のストリンガー" class="rel-wiki-page">クマサン印のストリンガー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC" title="ブキ/クマサン印のブラスター" class="rel-wiki-page">クマサン印のブラスター</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%BF%E3%83%BC" title="ブキ/クマサン印のシェルター" class="rel-wiki-page">クマサン印のシェルター</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC" title="ブキ/クマサン印のワイパー" class="rel-wiki-page">クマサン印のワイパー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%82%B9%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC" title="ブキ/クマサン印のスロッシャー" class="rel-wiki-page">クマサン印のスロッシャー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC" title="ブキ/クマサン印のチャージャー" class="rel-wiki-page">クマサン印のチャージャー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%83%9E%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%90%E3%83%BC" title="ブキ/クマサン印のマニューバー" class="rel-wiki-page">クマサン印のマニューバー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC" title="ブキ/クマサン印のローラー" class="rel-wiki-page">クマサン印のローラー</a></li></ul>
<p>詳細は個別ページを参照。</p>
</div>
</div>
<h4 id="h4_content_12_0" ><a class="anchor" name ="subweapon"></a><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/サブウェポン" class="rel-wiki-page">サブウェポン</a></h4>

<p><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/サブウェポン" class="rel-wiki-page">サブウェポン</a>は全員<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5%E3%83%9C%E3%83%A0" title="ブキ/サブウェポン/スプラッシュボム" class="rel-wiki-page">スプラッシュボム</a>に固定される。<br />
性能はバトル用のものとほぼ同じだが、爆風が少し大きくなっている。<br />
一部オオモノシャケの撃破にはほぼ必須になる。</p>
<p><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5%E3%83%9C%E3%83%A0" title="ブキ/サブウェポン/スプラッシュボム" class="rel-wiki-page">スプラッシュボム</a>の有効な使い方の詳細は<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%82%B5%E3%83%96%E3%83%BB%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%83%BB%E3%82%A4%E3%82%AF%E3%83%A9%E6%8A%95%E3%81%92#splashbomb" title="サーモンラン/ブキ別立ち回り/サブ・スペシャル・イクラ投げ" class="rel-wiki-page">サーモンラン/ブキ別立ち回り/サブ・スペシャル・イクラ投げ</a>にて解説されている。</p>
<h4 id="h4_content_13_0" ><a class="anchor" name ="specialweapon"></a><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャルウェポン</a></h4>

<p>バイト中は特殊な装備で作業するために、自らの力で<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>を溜めることができない<a id="notetext_2"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;バイトマニュアルの説明&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_2&quot;&gt;脚注 *2 へ&lt;/a&gt;&lt;/div&gt;">*2</a>。<br />
その代わり、バイト開始時に、ある1種類の「<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>パウチ<a id="notetext_3"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;バイトマニュアルでの呼称&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_3&quot;&gt;脚注 *3 へ&lt;/a&gt;&lt;/div&gt;">*3</a>」が2個支給される。<br />
<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>パウチが残っていれば、いつでも<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>を使うことができる。<br />
<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>を1回使うと、<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>パウチが1個消費される。<br />
1回のバイトで最大で2回使用することが可能だ。<a id="notetext_4"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/Extra%20Wave&quot; title=&quot;サーモンラン/特殊な状況/Extra Wave&quot; class=&quot;rel-wiki-page&quot;&gt;Extra Wave&lt;/a&gt;が発生した場合は3回、&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AA%E3%82%AB%E3%82%B7%E3%83%A9%E9%80%A3%E5%90%88&quot; title=&quot;サーモンラン/シャケの種類/オカシラ連合&quot; class=&quot;rel-wiki-page&quot;&gt;オカシラ連合&lt;/a&gt;が襲来した場合は4回使える。&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_4&quot;&gt;脚注 *4 へ&lt;/a&gt;&lt;/div&gt;">*4</a><br />
2回使ってしまうと<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>が使えなくなるため、ここぞという時に使うといい。</p>
<p><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>は、以下の9種類<a id="notetext_5"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;Ver.5.2.0以前では7種類&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_5&quot;&gt;脚注 *5 へ&lt;/a&gt;&lt;/div&gt;">*5</a>から4種類がランダムに選ばれ、その4種が4人のプレイヤーに配られる。</p>
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%82%B5%E3%83%96%E3%83%BB%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%83%BB%E3%82%A4%E3%82%AF%E3%83%A9%E6%8A%95%E3%81%92#ReefSlider" title="サーモンラン/ブキ別立ち回り/サブ・スペシャル・イクラ投げ" class="rel-wiki-page">サメライド</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%82%B5%E3%83%96%E3%83%BB%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%83%BB%E3%82%A4%E3%82%AF%E3%83%A9%E6%8A%95%E3%81%92#CrabTank" title="サーモンラン/ブキ別立ち回り/サブ・スペシャル・イクラ投げ" class="rel-wiki-page">カニタンク</a>★</li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%82%B5%E3%83%96%E3%83%BB%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%83%BB%E3%82%A4%E3%82%AF%E3%83%A9%E6%8A%95%E3%81%92#WaveBreaker" title="サーモンラン/ブキ別立ち回り/サブ・スペシャル・イクラ投げ" class="rel-wiki-page">ホップソナー</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%82%B5%E3%83%96%E3%83%BB%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%83%BB%E3%82%A4%E3%82%AF%E3%83%A9%E6%8A%95%E3%81%92#TripleInkstrike" title="サーモンラン/ブキ別立ち回り/サブ・スペシャル・イクラ投げ" class="rel-wiki-page">トリプルトルネード</a>★</li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%82%B5%E3%83%96%E3%83%BB%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%83%BB%E3%82%A4%E3%82%AF%E3%83%A9%E6%8A%95%E3%81%92#KillerWail5-1ch" title="サーモンラン/ブキ別立ち回り/サブ・スペシャル・イクラ投げ" class="rel-wiki-page">メガホンレーザー5.1ch</a>★</li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%82%B5%E3%83%96%E3%83%BB%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%83%BB%E3%82%A4%E3%82%AF%E3%83%A9%E6%8A%95%E3%81%92#BooyahBomb" title="サーモンラン/ブキ別立ち回り/サブ・スペシャル・イクラ投げ" class="rel-wiki-page">ナイスダマ</a>★</li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%82%B5%E3%83%96%E3%83%BB%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%83%BB%E3%82%A4%E3%82%AF%E3%83%A9%E6%8A%95%E3%81%92#inkjet" title="サーモンラン/ブキ別立ち回り/サブ・スペシャル・イクラ投げ" class="rel-wiki-page">ジェットパック</a>★</li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%82%B5%E3%83%96%E3%83%BB%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%83%BB%E3%82%A4%E3%82%AF%E3%83%A9%E6%8A%95%E3%81%92#KrakenRoyale" title="サーモンラン/ブキ別立ち回り/サブ・スペシャル・イクラ投げ" class="rel-wiki-page">テイオウイカ</a><a id="notetext_6"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;Ver.6.0.0以降&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_6&quot;&gt;脚注 *6 へ&lt;/a&gt;&lt;/div&gt;">*6</a></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%82%B5%E3%83%96%E3%83%BB%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%83%BB%E3%82%A4%E3%82%AF%E3%83%A9%E6%8A%95%E3%81%92#TripleSplashdown" title="サーモンラン/ブキ別立ち回り/サブ・スペシャル・イクラ投げ" class="rel-wiki-page">ウルトラチャクチ</a><a id="notetext_7"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;Ver.6.0.0以降&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_7&quot;&gt;脚注 *7 へ&lt;/a&gt;&lt;/div&gt;">*7</a></li></ul>
<p>★マークの付いた<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>(遠くのシャケに攻撃できるもの)のうち2種類は必ず支給されるようになっている。<a id="notetext_8"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;Ver.6.0.0以降&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_8&quot;&gt;脚注 *8 へ&lt;/a&gt;&lt;/div&gt;">*8</a></p>
<p>使わなかった<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>パウチはWAVE3終了後に回収されるため、余りを<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/Extra%20Wave" title="サーモンラン/特殊な状況/Extra Wave" class="rel-wiki-page">Extra Wave</a>や次回以降のバイトに持ち越すことはできない。<br />
WAVE3が終わるまでに使い切ってしまう方がダンゼンお得だ。</p>
<p><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>パウチは帽子にくくりつけられている。<br />
他プレイヤーの<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>の残り使用回数は、帽子についているパウチの数で判断できる。</p>
<p><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>の有効な使い方の詳細は<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%96%E3%82%AD%E5%88%A5%E7%AB%8B%E3%81%A1%E5%9B%9E%E3%82%8A/%E3%82%B5%E3%83%96%E3%83%BB%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%83%BB%E3%82%A4%E3%82%AF%E3%83%A9%E6%8A%95%E3%81%92" title="サーモンラン/ブキ別立ち回り/サブ・スペシャル・イクラ投げ" class="rel-wiki-page">サーモンラン/ブキ別立ち回り/サブ・スペシャル・イクラ投げ</a>にて解説されている。<br />
<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>のダメージ早見表は<strong><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%90%E3%82%A4%E3%83%88%E5%B0%82%E7%94%A8%E3%83%96%E3%82%AD%E3%81%AE%E8%A3%9C%E6%AD%A3#dd49a0bc" title="サーモンラン/バイト専用ブキの補正" class="rel-wiki-page">ここ</a></strong>で見られる。</p>
<h3 id="h3_content_14_0" ><a class="anchor" name ="gear"></a>バイト専用<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></h3>

<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>では通常のバトルで使用する<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>は使えず、代わりに支給された専用の作業着を着用してバイトに挑むこととなる。<br />
初期から所持している作業着は「バイトツナギ オレンジ」のみとなっている。<br />
また、交換所でシャケのウロコを使用して、色違いの作業着や過去作の作業着と交換できる。</p>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">バイト作業着一覧</div>
    <div class="fold-content visible-on-open"><div class="h-scrollable"><table><tbody><tr><th>Ver.</th><th style="text-align:center;">作業着</th><th style="text-align:center;">入手方法・必要ウロコ数</th></tr><tr><td>1.0.0</td><td>バイトツナギ オレンジ</td><td>初期から所持</td></tr><tr><td>1.0.0</td><td>バイトツナギ イエロー</td><td>銀のウロコ×10</td></tr><tr><td>1.0.0</td><td>バイトツナギ グリーン</td><td>銀のウロコ×10</td></tr><tr><td>1.0.0</td><td>バイトツナギ ピンク</td><td>銀のウロコ×30</td></tr><tr><td>1.0.0</td><td>バイトツナギ ブルー</td><td>銀のウロコ×30</td></tr><tr><td>1.0.0</td><td>バイトツナギ ブラック</td><td>銀のウロコ×100</td></tr><tr><td>1.0.0</td><td>バイトツナギ ホワイト</td><td>銀のウロコ×100</td></tr><tr><td>3.0.0</td><td>バイトウェーダー オレンジ</td><td>銀のウロコ×15</td></tr><tr><td>3.0.0</td><td>バイトウェーダー イエロー</td><td>銀のウロコ×50</td></tr><tr><td>3.0.0</td><td>バイトウェーダー ブラウン</td><td>銀のウロコ×75</td></tr><tr><td>3.0.0</td><td>バイトウェーダー ブラック</td><td>銀のウロコ×150</td></tr><tr><td>5.0.0</td><td>バイトツナギ ドット</td><td>銀のウロコ×150</td></tr><tr><td>5.0.0</td><td>バイトツナギ カモ</td><td>銀のウロコ×150</td></tr><tr><td>5.0.0</td><td>バイトツナギ ニシキ</td><td>銀のウロコ×150</td></tr><tr><td>7.0.0</td><td>バイトウェーダー ピーチ</td><td>銀のウロコ×50</td></tr><tr><td>7.0.0</td><td>バイトウェーダー ライム</td><td>銀のウロコ×50</td></tr><tr><td>7.0.0</td><td>バイトウェーダー ベリー</td><td>銀のウロコ×150</td></tr><tr><td>8.0.0</td><td>バイトツナギ シルバー</td><td>銀のウロコ×150</td></tr><tr><td>8.0.0</td><td>バイトツナギ ゴールド</td><td>銀のウロコ×150</td></tr><tr><td>8.0.0</td><td>バイトツナギ プリズム</td><td>銀のウロコ×150</td></tr><tr><td>9.0.0</td><td>バイトツナギ ブ<a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC" title="ロッカー" class="rel-wiki-page">ロッカー</a></td><td>ゲームニュースより配布</td></tr></tbody></table></div>
</div>
</div>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>で支給される<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>には<a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC" title="ギア/ギアパワー" class="rel-wiki-page">ギアパワー</a>という概念がない。<br />
当然ながらそのときバトル用につけていた<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC" title="ギア/ギアパワー" class="rel-wiki-page">ギアパワー</a>の効果は発揮されない。<br />
服装自由、制服貸与という仕様だ。</p>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">ちょっとお得？な余談</div>
    <div class="fold-content visible-on-open"><p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>モード中の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>装備は無意味なのは前述通り。<br />
しかし<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>に無頓着なのはもったいないという話だ。<br />
というのも、クマサン商会の前には一つ前のバイトでマッチングしたプレイヤー3名が現れるからだ。<br />
街のイカと同様、そのプレイヤーの装備は確認、及びスパイキーに注文可能だ。</p>
<p>つまり<strong><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC" title="ギア/ギアパワー" class="rel-wiki-page">ギアパワー</a>が揃った自慢の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>を着ていけば、同僚がスパイキーに注文をかけてくれるかもしれない。</strong><br />
フレンドと一緒にやる場合、そのフレンドが別の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>シフトに参加しない限り、確実に注文が可能。<br />
日をまたいでもプレイヤーは出現しっぱなし。再注文も可能だ。<br />
自慢の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>を見せたり、フレンドが欲しがっている<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>の間接的な受け渡しにも利用できる。<br />
この場合着ていく<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>は、3種の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>でバトルを考慮した組合せ≒注文するメリットが薄いものよりも、<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>単体で見たときの実用性を重視したものが喜ばれる。<br />
早い話が<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/サブウェポン" class="rel-wiki-page">サブ</a><a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>が揃っているもののほうが喜ばれる。</p>
<p>また、<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>効果がないということは、好きな<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>を着られるということでもある。<br />
細かいことを気にせず自分のファッションを見せるため、見た目にこだわった<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>を着るのも良いだろう。<br />
Splatoonではバトルでの強さを追い求めて妙な服装になりがちだが、バイト中は純粋に着せ替えだけを楽しめる数少ない機会にできる。<br />
みんなが楽しめるようにこのチャンスを各々利用しよう。</p>
</div>
</div>
<h3 id="h3_content_17_0" ><a class="anchor" name ="inktank"></a>バイト専用インクタンク</h3>

<p>バイト中は、いつものインクタンクの代わりに背負った「ウキワタンク<a id="notetext_9"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;バイトマニュアルでの呼称&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_9&quot;&gt;脚注 *9 へ&lt;/a&gt;&lt;/div&gt;">*9</a>」にインク残量が表示される。<br />
ウキワタンクにはインク残量30%と70%の目盛りがあり、「100％からボム・イクラ投げを使った時にインクがどのくらい減るか」と「インクがどのくらい残っていればボム・イクラ投げを使えるか」が一目で分かるようになっている。</p>
<p>他プレイヤーのインク残量はウキワタンクを見れば確認できる。戦況把握に役立てよう。</p>
<h4 id="h4_content_18_0" >ウキワ状態</h4>

<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>では、シャケに倒されたり海に転落したりすると、リスポーン地点に戻る代わりにその場<a id="notetext_10"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;正確にはやられた時に最後に地面にいた場所&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_10&quot;&gt;脚注 *10 へ&lt;/a&gt;&lt;/div&gt;">*10</a>で<strong>ウキワ状態</strong>となる。<br />
また、デスしてからウキワ状態になるまで5秒かかる。<br />
(ちなみに公式名は「簡易型<ruby>再発生<rp>(</rp><rt>リスポーン</rt><rp>)</rp></ruby>機器 救命フロート」、または「復活待機状態<a id="notetext_11"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;バイトマニュアルでの呼称&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_11&quot;&gt;脚注 *11 へ&lt;/a&gt;&lt;/div&gt;">*11</a>」)<br />
(…と思いきや、<a class="ext" href="https://wikiwiki.jp/p/cushion?to=https%3A%2F%2Fwww.nintendo.co.jp%2Fsupport%2Fswitch%2Fsoftware_support%2Fav5ja%2F120.html"  rel="nofollow">公式サイトの更新のお知らせ<span class="system-icon ext pukiwiki-open-uri" data-href="https://www.nintendo.co.jp/support/switch/software_support/av5ja/120.html" data-frame="_blank"></span></a>では普通に「ウキワ状態」という言葉が使われている。チュートリアルでは「ウキワタンク状態」と呼ばれている)</p>
<p>ウキワ状態になると多くの行動が制限される。具体的にはイカのような性質がある。</p>
<ul class="list1"><li><strong>攻撃ができない</strong><br />
メイン・<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/サブウェポン" class="rel-wiki-page">サブ</a>・<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>全て使用できない。</li>
<li><strong>センプクができない</strong><br />
インクを塗った壁を登ることもできない。</li>
<li><strong>移動が遅い</strong><br />
遠くでやられると戻るのに時間がかかる。</li>
<li><strong>ジャンプが低い</strong><br />
ちょっとした段差も登れない。<br />
ただし、味方の<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%9B%E3%83%83%E3%83%97%E3%82%BD%E3%83%8A%E3%83%BC" title="ブキ/スペシャルウェポン/ホップソナー" class="rel-wiki-page">ホップソナー</a>の衝撃波はジャンプ中は当たらなくなるので注意。<br />
<span class="wikicolor" style="color:blue">味方に救助を求めるアピールとしてピョンピョンとジャンプを連打する</span>のはあまり推奨されない行為である。ジャンプ連打ではなく後述の「ヘルプ！」を使うことが望ましい。</li>
<li><strong>納品ができない</strong><br />
ただし回収は可能。</li>
<li><strong>十字キー↑の「カモン！」が「ヘルプ！」に変わる</strong><br />
仲間に自分がやられてしまったことを気づいてもらおう。<br />
<strong><span class="wikicolor" style="color:Red">場所を知らせるため、救助されるまで何度も押そう！</span></strong>連打しても一定間隔につき1回のみ送られるので迷惑にはならない。</li>
<li><strong>水没はする</strong><br />
ウキワだが水には浮かない。水に入ると水没となり、ウキワとして再度浮上してくるまでの間は味方からの救助を受けられなくなるので、水には落ちないようにしておこう。</li></ul>
<p>ウキワ状態からは、仲間にインクをかけてもらう(インク攻撃を受ける)ことで復活できる。<br />
復活には合計で30ダメージ分の攻撃が必要。メインの射撃だけでなく、ボムや<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>も有効だ。<br />
<strong><span class="wikicolor" style="color:Red"><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%8F%E3%81%8B%E3%81%B0%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC" title="ブキ/わかばシューター" class="rel-wiki-page"><strong><span class="wikicolor" style="color:Red">わかばシューター</span></strong></a>・<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B7%E3%83%A3%E3%83%BC%E3%83%97%E3%83%9E%E3%83%BC%E3%82%AB%E3%83%BC" title="ブキ/シャープマーカー" class="rel-wiki-page"><strong><span class="wikicolor" style="color:Red">シャープマーカー</span></strong></a>(攻撃力28)や、<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%97%E3%83%AD%E3%83%A2%E3%83%87%E3%83%A9%E3%83%BCMG" title="ブキ/プロモデラーMG" class="rel-wiki-page"><strong><span class="wikicolor" style="color:Red">プロモデラーMG</span></strong></a>(攻撃力24)は2発必要なので注意！</span></strong><a id="notetext_12"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;これ以外のブキはバイト専用の補正がかかっており攻撃力は30以上となっている。ただし、減衰によって1発で復活させられない場合もあるので注意。&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_12&quot;&gt;脚注 *12 へ&lt;/a&gt;&lt;/div&gt;">*12</a><br />
また、当然ながら、インクがかからなければ救助できないので、<strong><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a>のバリアの中や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a>の上にとどまることは避け</strong>、「ヘルプ！」を出しつつ味方の射撃が届くところへ移動しよう。<br />
その他、ウキワになってしまった後の心得については<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B5%E3%83%90%E3%82%A4%E3%83%90%E3%83%AB%E6%8C%87%E5%8D%97#h7545d99" title="サーモンラン/サバイバル指南" class="rel-wiki-page">サバイバル指南/それでもデスしてしまったら</a>を参照。</p>
<h2 id="h2_content_1_12" class="heading-after-first">評価 <a class="anchor_super" name ="paygrade"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=paygrade" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<p>クマサン商会では各アルバイターに『かけだし 40』や『でんせつ 100』のような「評価」が与えられる。<br />
評価のうち『かけだし』の部分を「称号」と呼び、『40』の部分を（ここでは）「評価値」と呼ぶ。</p>
<p>評価はバイトの難易度である「キケン度」や、クマサンポイントの算出に使われる「評価レート」に影響する。<br />
また、マッチングにも影響しており、自身の評価と近いプレイヤーとマッチしやすい模様。</p>
<h3 id="h3_content_19_0" >称号と評価値</h3>

<p>評価には9段階の区分がある。</p>
<div class="h-scrollable"><table><thead><tr><th>称号</th><th>評価値の幅</th></tr></thead><tbody><tr><td>かけだし</td><td>0-99</td></tr><tr><td>はんにんまえ</td><td>0-99</td></tr><tr><td>いちにんまえ</td><td>0-99</td></tr><tr><td>じゅくれん</td><td>0-99</td></tr><tr><td>たつじん</td><td>0-99</td></tr><tr><td>たつじん+1</td><td>0-99</td></tr><tr><td>たつじん+2</td><td>0-99</td></tr><tr><td>たつじん+3</td><td>0-99</td></tr><tr><td>でんせつ</td><td>0-999</td></tr></tbody></table></div>
<p>現在の称号の幅を超えて評価値が上がると、1つ上の称号に昇格し、評価値が40になる。<br />
逆に現在の称号の幅を超えて評価値が下がると、1つ下の称号に降格し、評価値が40になる。<br />
ぴったり0では降格しない。<br />
ただし、『かけだし 0』は評価の下限、『でんせつ 999』は上限となっており、<br />
それらを超えての変動は行われずにカウンターストップとなる。</p>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">評価変動の例</div>
    <div class="fold-content visible-on-open"><ul class="list1"><li>『はんにんまえ 80』の評価+20は『いちにんまえ 40』</li>
<li>『でんせつ 15』の評価-20は『たつじん+3 40』</li>
<li>『でんせつ 20』の評価-20は『でんせつ 0』</li></ul>
<ul class="list1"><li>『かけだし 0』の評価-20は『かけだし 0』</li>
<li>『でんせつ 999』の評価+20は『でんせつ 999』</li></ul>
</div>
</div>
<h3 id="h3_content_21_0" >評価の増減・変動</h3>

<p>評価は、バイトを終えた時と、シフト（バイトのステージ）が変わった時に変動する。</p>
<h4 id="h4_content_22_0" >バイト終了時</h4>

<p>バイトを終えた時、評価は乗り切ったWAVE数によって増減する。</p>
<div class="h-scrollable"><table><tbody><tr><td>WAVE1で失敗</td><td>-20</td></tr><tr><td>WAVE2で失敗</td><td>-10</td></tr><tr><td>WAVE3で失敗</td><td>±0</td></tr><tr><td>WAVE3まで成功</td><td>+20</td></tr></tbody></table></div>
<p>※ただし、回線落ちした仲間がいたときには減少量が半減する。<br />
※<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/Extra%20Wave" title="サーモンラン/特殊な状況/Extra Wave" class="rel-wiki-page">Extra Wave</a>の有無・成否は評価値変動に影響しない。<br />
※回線落ちなどによりバイトが正常に終わらなかった場合、評価は-20される。</p>
<h4 id="h4_content_23_0" >シフト変更時</h4>

<p>シフトが変わった時、評価は、前回バイトを終えた時の『称号 40』になる。</p>
<ul class="list1"><li>例えば、最後にバイトに参加した時の評価が…
<ul class="list2"><li>『たつじん 0』だったなら、シフト変更後は『たつじん 40』になる。</li>
<li>『でんせつ 390』だったなら、シフト変更後は『でんせつ 40』になる。</li></ul></li></ul>
<p>ただし、シフト変更後のステージに対応する<a href="/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%90%E3%83%83%E3%82%B8" title="ネームプレート/バッジ" class="rel-wiki-page">バッジ</a>を持っている場合は、<a href="/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%90%E3%83%83%E3%82%B8" title="ネームプレート/バッジ" class="rel-wiki-page">バッジ</a>の色に応じて以下の評価からになる。<a id="notetext_13"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;Ver.6.0.0以降&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_13&quot;&gt;脚注 *13 へ&lt;/a&gt;&lt;/div&gt;">*13</a><br />
これは前のシフトで『でんせつ』より下の称号になっていても適用される。</p>
<div class="h-scrollable"><table><tbody><tr><th>持っている<a href="/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%90%E3%83%83%E3%82%B8" title="ネームプレート/バッジ" class="rel-wiki-page">バッジ</a>の種類</th><th>スタート時のバイト評価</th></tr><tr><td style="background-color:NavajoWhite;">銅の<a href="/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%90%E3%83%83%E3%82%B8" title="ネームプレート/バッジ" class="rel-wiki-page">バッジ</a><br class="spacer">（でんせつ 400で獲得）</td><td>でんせつ 200</td></tr><tr><td style="background-color:LightGray;">銀の<a href="/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%90%E3%83%83%E3%82%B8" title="ネームプレート/バッジ" class="rel-wiki-page">バッジ</a><br class="spacer">（でんせつ 600で獲得）</td><td>でんせつ 300</td></tr><tr><td style="background-color:LightGoldenrodYellow;">金の<a href="/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%90%E3%83%83%E3%82%B8" title="ネームプレート/バッジ" class="rel-wiki-page">バッジ</a><br class="spacer">（でんせつ 999で獲得）</td><td>でんせつ 400</td></tr></tbody></table></div>
<p>※通常色の<a href="/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%90%E3%83%83%E3%82%B8" title="ネームプレート/バッジ" class="rel-wiki-page">バッジ</a>(でんせつ 200で獲得)はこれに影響しない。</p>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">Ver.5.2.0以前</div>
    <div class="fold-content visible-on-open"><p>評価値が40になる。称号は変わらない。<br />
(シフトが変わると、例えば『でんせつ 0』でも『でんせつ 999』でも、次のシフトでは『でんせつ 40』になる)</p>
</div>
</div>
<h3 id="h3_content_25_0" >評価リセット</h3>

<p>現在の評価が『いちにんまえ 40』よりも高い場合、「評価リセット」が可能になる。<br />
評価リセットをすると、自主的に評価を下げることができる。<br />
バイトが難しすぎると感じたら使ってみてもいいだろう。</p>
<p>評価リセットをするには、クマサン商会で[L]を押してロビーメニューを開き、[ZL]を押す。</p>
<p>なお、<a href="/splatoon3mix/%E3%83%90%E3%83%B3%E3%82%AB%E3%83%A9%E3%83%9E%E3%83%83%E3%83%81" title="バンカラマッチ" class="rel-wiki-page">バンカラマッチ</a>のウデマエリセットとは異なり回数制限はないため、一度に下げられる下限はない。<br />
かなりもったいないが、評価値カンストの『でんせつ 999』から、リセットできる評価値下限の『いちにんまえ 40』まで一気に下げることも一応可能。</p>
<p>評価リセットをすると、次の評価のうち、現在の評価よりも低いもので最も近い評価へと下がる。</p>
<ul class="list1"><li>『でんせつ 900』</li>
<li>『でんせつ 800』</li>
<li>『でんせつ 700』</li>
<li>『でんせつ 600』</li>
<li>『でんせつ 500』</li>
<li>『でんせつ 400』</li>
<li>『でんせつ 300』</li>
<li>『でんせつ 200』</li>
<li>『でんせつ 100』</li>
<li>『でんせつ 40』</li>
<li>『たつじん+3 40』</li>
<li>『たつじん+2 40』</li>
<li>『たつじん+1 40』</li>
<li>『たつじん 40』</li>
<li>『じゅくれん 40』</li>
<li>『いちにんまえ 40』</li></ul>
<p>下限は『いちにんまえ 40』まで。それより下には下げられない。</p>
<h2 id="h2_content_1_13" class="heading-after-first">キケン度  <a class="anchor_super" name ="hazardlevel"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=hazardlevel" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<p>「キケン度」とは、バイトの難易度を表す数値のこと。<br />
キケン度はバイトに参加したプレイヤー全員の評価の合計によって決まる。<br />
評価の合計が高いほど、キケン度も高くなる。</p>
<p>過去のバイトのキケン度は、ゲーム中のロビーメニューかクマサン端末から履歴を見ると確認できる。また、<a href="/splatoon3mix/%E3%82%A4%E3%82%AB%E3%83%AA%E3%83%B3%E3%82%B03" title="イカリング3" class="rel-wiki-page">イカリング3</a>からも確認できる。<br />
現在プレイ中のバイトのキケン度を確認する方法はない（キケン度MAXのときを除く）。</p>
<p>キケン度は0.2%刻みで、0.0～333.0%の値を取る。<br />
ゲーム内のメニューや<a href="/splatoon3mix/%E3%82%A4%E3%82%AB%E3%83%AA%E3%83%B3%E3%82%B03" title="イカリング3" class="rel-wiki-page">イカリング3</a>に表示されるキケン度は小数点以下が四捨五入されている。</p>
<p>キケン度はバイトの難易度だけでなく、オカシラシャケから得られる「ウロコ」のレア度にも影響する。</p>
<h3 id="h3_content_26_0" >キケン度MAX</h3>

<p>バイトのキケン度が<strong>333%</strong>の場合、バイト開始時に特徴的なジングルが鳴って「<strong>キケン度MAX!!</strong>」と表示される。<br />
キケン度MAXのバイトをクリアすると専用の<a href="/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%90%E3%83%83%E3%82%B8" title="ネームプレート/バッジ" class="rel-wiki-page">バッジ</a>が貰える。</p>
<p>キケン度MAXのバイトは、チームの平均評価が『でんせつ 865』以上のとき発生する。</p>
<h3 id="h3_content_27_0" >キケン度の算出方法</h3>

<p>キケン度は次の計算式によって求まる。</p>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">キケン度の算出式</div>
    <div class="fold-content visible-on-open"><p>キケン度(%) = 平均累計評価値 ÷ 5<br />
ただし上限は333.0%。</p>
<dl class="list1"><dt>平均累計評価値</dt>
<dd>バイトに参加したアルバイター全員の累計評価値の合計の平均。</dd>
<dt>累計評価値</dt>
<dd>1人のアルバイターの「かけだし0 ～ 現在の評価値」を合計した値。
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">称号＆評価値と累計評価値の対応表</div>
    <div class="fold-content visible-on-open"><div class="h-scrollable"><table><tbody><tr><td>称号</td><td>評価値の幅</td><td>累計評価値の幅</td></tr><tr><td>かけだし</td><td>0-99</td><td>0-99</td></tr><tr><td>はんにんまえ</td><td>0-99</td><td>100-199</td></tr><tr><td>いちにんまえ</td><td>0-99</td><td>200-299</td></tr><tr><td>じゅくれん</td><td>0-99</td><td>300-399</td></tr><tr><td>たつじん</td><td>0-99</td><td>400-499</td></tr><tr><td>たつじん+1</td><td>0-99</td><td>500-599</td></tr><tr><td>たつじん+2</td><td>0-99</td><td>600-699</td></tr><tr><td>たつじん+3</td><td>0-99</td><td>700-799</td></tr><tr><td>でんせつ</td><td>0-999</td><td>800-1799</td></tr></tbody></table></div>
</div>
</div>
でんせつ0における累計評価値が800なので、称号「でんせつ」バイターに限る場合、キケン度は「平均評価値 ÷ 5 + 160」と算出できる。</dd></dl>
</div>
</div>
<h3 id="h3_content_1_14" class="heading-after-first">キケン度による変化  <a class="anchor_super" name ="r99a8579"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=r99a8579" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<p>キケン度が高くなると、次の点が変化する。</p>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">キケン度による変化</div>
    <div class="fold-content visible-on-open"><ul class="list1"><li>ノルマが増える</li>
<li>オオモノシャケの出現数が増える</li>
<li>シャケたちの出現間隔が短くなる</li></ul>
<ul class="list1"><li>通常
<ul class="list2"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#cohock" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ドスコイ</a>が同時に存在できる上限数が増える</li></ul></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%82%B0%E3%83%AA%E3%83%AB%E7%99%BA%E9%80%B2" title="サーモンラン/特殊な状況/グリル発進" class="rel-wiki-page">グリル発進</a>
<ul class="list2"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>の移動速度が速くなる</li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>が2体に増えるまでの時間が短くなる</li></ul></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%8F%E3%82%B3%E3%83%93%E3%83%A4%E8%A5%B2%E6%9D%A5" title="サーモンラン/特殊な状況/ハコビヤ襲来" class="rel-wiki-page">ハコビヤ襲来</a>
<ul class="list2"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B3%E3%83%93%E3%83%A4%E3%81%9F%E3%81%A1#mothership" title="サーモンラン/シャケの種類/ハコビヤたち" class="rel-wiki-page">ハコビヤ</a>の体力が増える</li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B3%E3%83%93%E3%83%A4%E3%81%9F%E3%81%A1#chinooks" title="サーモンラン/シャケの種類/ハコビヤたち" class="rel-wiki-page">シャケコプター</a>の移動速度が速くなる</li></ul></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E5%B7%A8%E5%A4%A7%E3%82%BF%E3%83%84%E3%83%9E%E3%82%AD" title="サーモンラン/特殊な状況/巨大タツマキ" class="rel-wiki-page">巨大タツマキ</a>
<ul class="list2"><li>箱から出る金イクラの数が増える</li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>が同時に存在できる上限数が増える</li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>が降り続ける時間が長くなる</li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>が降らない時間が短くなる</li></ul></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>
<ul class="list2"><li>シャケたちが同時に存在できる上限数が増える</li>
<li>シャケたちの移動速度が速くなる</li></ul></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%89%E3%83%AD%E3%82%B7%E3%83%A3%E3%82%B1%E5%99%B4%E5%87%BA" title="サーモンラン/特殊な状況/ドロシャケ噴出" class="rel-wiki-page">ドロシャケ噴出</a>
<ul class="list2"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%89%E3%83%AD%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ドロシャケ" class="rel-wiki-page">ドロシャケ</a>が<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>を吐き出す間隔が短くなる</li>
<li>一定時間ごとに出現する<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%89%E3%83%AD%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ドロシャケ" class="rel-wiki-page">ドロシャケ</a>の出現間隔が短くなる</li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%89%E3%83%AD%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ドロシャケ" class="rel-wiki-page">ドロシャケ</a>が同時に存在できる上限数が増える</li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#cohock" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ドスコイ</a>が同時に存在できる上限数が増える</li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%89%E3%83%AD%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ドロシャケ" class="rel-wiki-page">ドロシャケ</a>が吐き出す<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>の種類が、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>になりやすくなる</li></ul></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/Extra%20Wave" title="サーモンラン/特殊な状況/Extra Wave" class="rel-wiki-page">Extra Wave</a>
<ul class="list2"><li>オカシラシャケの体力が増える</li>
<li>オカシラシャケが落とすウロコのレア度が高くなる</li></ul></li></ul>
</div>
</div>
<h4 id="h4_content_1_15" class="heading-after-first">ノルマ＆オオモノ出現数の表  <a class="anchor_super" name ="de6bdadb"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=de6bdadb" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h4>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">ノルマ＆オオモノ出現数の表（キケン度10%ごと）</div>
    <div class="fold-content visible-on-open"><p>※この表は解析データに基づいて作られている。実際にこの値となるかは要検証。<br />
※オオモノシャケがステージ上に存在できる数は15匹までに制限されている<a id="notetext_14"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;Ver. 2.0.0 更新データ詳細より。&amp;quot;一度に出現するオオモノシャケの数の上限を15匹までに制限しました。&amp;quot;&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_14&quot;&gt;脚注 *14 へ&lt;/a&gt;&lt;/div&gt;">*14</a>ため、高キケン度のバイトではこの表通りの数のオオモノシャケが出現することは稀だと考えられる。</p>
<div class="h-scrollable"><table><thead><tr><th rowspan="2">キケン度（%）</th><th rowspan="2">平均評価</th><th colspan="2">WAVE1</th><th colspan="2">WAVE2</th><th colspan="2">WAVE3</th></tr><tr><th>オオモノ</th><th>ノルマ</th><th>オオモノ</th><th>ノルマ</th><th>オオモノ</th><th>ノルマ</th></tr></thead><tfoot><tr><th rowspan="2">キケン度（%）</th><th rowspan="2">平均評価</th><th>オオモノ</th><th>ノルマ</th><th>オオモノ</th><th>ノルマ</th><th>オオモノ</th><th>ノルマ</th></tr><tr><th colspan="2">WAVE1</th><th colspan="2">WAVE2</th><th colspan="2">WAVE3</th></tr></tfoot><tbody><tr><td style="text-align:center;vertical-align:middle;">0</td><td>かけだし 0</td><td style="text-align:right; background-color:pink; width:65px;">3</td><td style="text-align:right; background-color:pink; width:65px;">3</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">3</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">4</td><td style="text-align:right; background-color:lavender; width:65px;">3</td><td style="text-align:right; background-color:lavender; width:65px;">5</td></tr><tr><td style="text-align:center;vertical-align:middle;">10</td><td>かけだし 50</td><td style="text-align:right; background-color:pink; width:65px;">3</td><td style="text-align:right; background-color:pink; width:65px;">5</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">3</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">6</td><td style="text-align:right; background-color:lavender; width:65px;">4</td><td style="text-align:right; background-color:lavender; width:65px;">7</td></tr><tr><td style="text-align:center;vertical-align:middle;">20</td><td>はんにんまえ 0</td><td style="text-align:right; background-color:pink; width:65px;">5</td><td style="text-align:right; background-color:pink; width:65px;">8</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">6</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">9</td><td style="text-align:right; background-color:lavender; width:65px;">7</td><td style="text-align:right; background-color:lavender; width:65px;">10</td></tr><tr><td style="text-align:center;vertical-align:middle;">30</td><td>はんにんまえ 50</td><td style="text-align:right; background-color:pink; width:65px;">5</td><td style="text-align:right; background-color:pink; width:65px;">8</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">6</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">9</td><td style="text-align:right; background-color:lavender; width:65px;">8</td><td style="text-align:right; background-color:lavender; width:65px;">11</td></tr><tr><td style="text-align:center;vertical-align:middle;">40</td><td>いちにんまえ 0</td><td style="text-align:right; background-color:pink; width:65px;">6</td><td style="text-align:right; background-color:pink; width:65px;">9</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">7</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">10</td><td style="text-align:right; background-color:lavender; width:65px;">9</td><td style="text-align:right; background-color:lavender; width:65px;">12</td></tr><tr><td style="text-align:center;vertical-align:middle;">50</td><td>いちにんまえ 50</td><td style="text-align:right; background-color:pink; width:65px;">6</td><td style="text-align:right; background-color:pink; width:65px;">10</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">8</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">11</td><td style="text-align:right; background-color:lavender; width:65px;">10</td><td style="text-align:right; background-color:lavender; width:65px;">13</td></tr><tr><td style="text-align:center;vertical-align:middle;">60</td><td>じゅくれん 0</td><td style="text-align:right; background-color:pink; width:65px;">7</td><td style="text-align:right; background-color:pink; width:65px;">11</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">9</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">12</td><td style="text-align:right; background-color:lavender; width:65px;">11</td><td style="text-align:right; background-color:lavender; width:65px;">14</td></tr><tr><td style="text-align:center;vertical-align:middle;">70</td><td>じゅくれん 50</td><td style="text-align:right; background-color:pink; width:65px;">8</td><td style="text-align:right; background-color:pink; width:65px;">12</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">10</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">13</td><td style="text-align:right; background-color:lavender; width:65px;">12</td><td style="text-align:right; background-color:lavender; width:65px;">15</td></tr><tr><td style="text-align:center;vertical-align:middle;">80</td><td>たつじん 0</td><td style="text-align:right; background-color:pink; width:65px;">9</td><td style="text-align:right; background-color:pink; width:65px;">13</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">11</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">14</td><td style="text-align:right; background-color:lavender; width:65px;">13</td><td style="text-align:right; background-color:lavender; width:65px;">16</td></tr><tr><td style="text-align:center;vertical-align:middle;">90</td><td>たつじん 50</td><td style="text-align:right; background-color:pink; width:65px;">10</td><td style="text-align:right; background-color:pink; width:65px;">14</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">12</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">15</td><td style="text-align:right; background-color:lavender; width:65px;">14</td><td style="text-align:right; background-color:lavender; width:65px;">17</td></tr><tr><td style="text-align:center;vertical-align:middle;">100</td><td>たつじん+1 0</td><td style="text-align:right; background-color:pink; width:65px;">11</td><td style="text-align:right; background-color:pink; width:65px;">16</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">13</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">17</td><td style="text-align:right; background-color:lavender; width:65px;">15</td><td style="text-align:right; background-color:lavender; width:65px;">19</td></tr><tr><td style="text-align:center;vertical-align:middle;">110</td><td>たつじん+1 50</td><td style="text-align:right; background-color:pink; width:65px;">11</td><td style="text-align:right; background-color:pink; width:65px;">17</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">13</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">18</td><td style="text-align:right; background-color:lavender; width:65px;">15</td><td style="text-align:right; background-color:lavender; width:65px;">20</td></tr><tr><td style="text-align:center;vertical-align:middle;">120</td><td>たつじん+2 0</td><td style="text-align:right; background-color:pink; width:65px;">12</td><td style="text-align:right; background-color:pink; width:65px;">18</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">14</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">19</td><td style="text-align:right; background-color:lavender; width:65px;">16</td><td style="text-align:right; background-color:lavender; width:65px;">21</td></tr><tr><td style="text-align:center;vertical-align:middle;">130</td><td>たつじん+2 50</td><td style="text-align:right; background-color:pink; width:65px;">13</td><td style="text-align:right; background-color:pink; width:65px;">19</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">15</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">20</td><td style="text-align:right; background-color:lavender; width:65px;">17</td><td style="text-align:right; background-color:lavender; width:65px;">22</td></tr><tr><td style="text-align:center;vertical-align:middle;">140</td><td>たつじん+3 0</td><td style="text-align:right; background-color:pink; width:65px;">14</td><td style="text-align:right; background-color:pink; width:65px;">20</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">16</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">21</td><td style="text-align:right; background-color:lavender; width:65px;">18</td><td style="text-align:right; background-color:lavender; width:65px;">23</td></tr><tr><td style="text-align:center;vertical-align:middle;">150</td><td>たつじん+3 50</td><td style="text-align:right; background-color:pink; width:65px;">15</td><td style="text-align:right; background-color:pink; width:65px;">21</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">17</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">22</td><td style="text-align:right; background-color:lavender; width:65px;">19</td><td style="text-align:right; background-color:lavender; width:65px;">24</td></tr><tr><td style="text-align:center;vertical-align:middle;">160</td><td>でんせつ 0</td><td style="text-align:right; background-color:pink; width:65px;">16</td><td style="text-align:right; background-color:pink; width:65px;">22</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">18</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">23</td><td style="text-align:right; background-color:lavender; width:65px;">20</td><td style="text-align:right; background-color:lavender; width:65px;">25</td></tr><tr><td style="text-align:center;vertical-align:middle;">170</td><td>でんせつ 50</td><td style="text-align:right; background-color:pink; width:65px;">17</td><td style="text-align:right; background-color:pink; width:65px;">23</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">19</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">24</td><td style="text-align:right; background-color:lavender; width:65px;">21</td><td style="text-align:right; background-color:lavender; width:65px;">26</td></tr><tr><td style="text-align:center;vertical-align:middle;">180</td><td>でんせつ 100</td><td style="text-align:right; background-color:pink; width:65px;">18</td><td style="text-align:right; background-color:pink; width:65px;">24</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">20</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">25</td><td style="text-align:right; background-color:lavender; width:65px;">22</td><td style="text-align:right; background-color:lavender; width:65px;">27</td></tr><tr><td style="text-align:center;vertical-align:middle;">190</td><td>でんせつ 150</td><td style="text-align:right; background-color:pink; width:65px;">19</td><td style="text-align:right; background-color:pink; width:65px;">25</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">21</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">26</td><td style="text-align:right; background-color:lavender; width:65px;">23</td><td style="text-align:right; background-color:lavender; width:65px;">28</td></tr><tr><td style="text-align:center;vertical-align:middle;">200</td><td>でんせつ 200</td><td style="text-align:right; background-color:pink; width:65px;">20</td><td style="text-align:right; background-color:pink; width:65px;">26</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">22</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">28</td><td style="text-align:right; background-color:lavender; width:65px;">24</td><td style="text-align:right; background-color:lavender; width:65px;">30</td></tr><tr><td style="text-align:center;vertical-align:middle;">210</td><td>でんせつ 250</td><td style="text-align:right; background-color:pink; width:65px;">20</td><td style="text-align:right; background-color:pink; width:65px;">26</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">22</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">28</td><td style="text-align:right; background-color:lavender; width:65px;">24</td><td style="text-align:right; background-color:lavender; width:65px;">30</td></tr><tr><td style="text-align:center;vertical-align:middle;">220</td><td>でんせつ 300</td><td style="text-align:right; background-color:pink; width:65px;">21</td><td style="text-align:right; background-color:pink; width:65px;">26</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">23</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">28</td><td style="text-align:right; background-color:lavender; width:65px;">25</td><td style="text-align:right; background-color:lavender; width:65px;">30</td></tr><tr><td style="text-align:center;vertical-align:middle;">230</td><td>でんせつ 350</td><td style="text-align:right; background-color:pink; width:65px;">22</td><td style="text-align:right; background-color:pink; width:65px;">26</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">24</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">28</td><td style="text-align:right; background-color:lavender; width:65px;">26</td><td style="text-align:right; background-color:lavender; width:65px;">31</td></tr><tr><td style="text-align:center;vertical-align:middle;">240</td><td>でんせつ 400</td><td style="text-align:right; background-color:pink; width:65px;">23</td><td style="text-align:right; background-color:pink; width:65px;">27</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">25</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">29</td><td style="text-align:right; background-color:lavender; width:65px;">27</td><td style="text-align:right; background-color:lavender; width:65px;">31</td></tr><tr><td style="text-align:center;vertical-align:middle;">250</td><td>でんせつ 450</td><td style="text-align:right; background-color:pink; width:65px;">23</td><td style="text-align:right; background-color:pink; width:65px;">27</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">25</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">29</td><td style="text-align:right; background-color:lavender; width:65px;">28</td><td style="text-align:right; background-color:lavender; width:65px;">31</td></tr><tr><td style="text-align:center;vertical-align:middle;">260</td><td>でんせつ 500</td><td style="text-align:right; background-color:pink; width:65px;">24</td><td style="text-align:right; background-color:pink; width:65px;">27</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">26</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">29</td><td style="text-align:right; background-color:lavender; width:65px;">28</td><td style="text-align:right; background-color:lavender; width:65px;">32</td></tr><tr><td style="text-align:center;vertical-align:middle;">270</td><td>でんせつ 550</td><td style="text-align:right; background-color:pink; width:65px;">25</td><td style="text-align:right; background-color:pink; width:65px;">28</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">27</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">30</td><td style="text-align:right; background-color:lavender; width:65px;">29</td><td style="text-align:right; background-color:lavender; width:65px;">32</td></tr><tr><td style="text-align:center;vertical-align:middle;">280</td><td>でんせつ 600</td><td style="text-align:right; background-color:pink; width:65px;">26</td><td style="text-align:right; background-color:pink; width:65px;">28</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">28</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">30</td><td style="text-align:right; background-color:lavender; width:65px;">30</td><td style="text-align:right; background-color:lavender; width:65px;">33</td></tr><tr><td style="text-align:center;vertical-align:middle;">290</td><td>でんせつ 650</td><td style="text-align:right; background-color:pink; width:65px;">26</td><td style="text-align:right; background-color:pink; width:65px;">28</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">28</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">30</td><td style="text-align:right; background-color:lavender; width:65px;">31</td><td style="text-align:right; background-color:lavender; width:65px;">33</td></tr><tr><td style="text-align:center;vertical-align:middle;">300</td><td>でんせつ 700</td><td style="text-align:right; background-color:pink; width:65px;">27</td><td style="text-align:right; background-color:pink; width:65px;">29</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">29</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">31</td><td style="text-align:right; background-color:lavender; width:65px;">32</td><td style="text-align:right; background-color:lavender; width:65px;">33</td></tr><tr><td style="text-align:center;vertical-align:middle;">310</td><td>でんせつ 750</td><td style="text-align:right; background-color:pink; width:65px;">28</td><td style="text-align:right; background-color:pink; width:65px;">29</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">30</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">31</td><td style="text-align:right; background-color:lavender; width:65px;">33</td><td style="text-align:right; background-color:lavender; width:65px;">34</td></tr><tr><td style="text-align:center;vertical-align:middle;">320</td><td>でんせつ 800</td><td style="text-align:right; background-color:pink; width:65px;">29</td><td style="text-align:right; background-color:pink; width:65px;">29</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">31</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">31</td><td style="text-align:right; background-color:lavender; width:65px;">33</td><td style="text-align:right; background-color:lavender; width:65px;">34</td></tr><tr><td style="text-align:center;vertical-align:middle;">330</td><td>でんせつ 850</td><td style="text-align:right; background-color:pink; width:65px;">29</td><td style="text-align:right; background-color:pink; width:65px;">29</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">31</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">31</td><td style="text-align:right; background-color:lavender; width:65px;">34</td><td style="text-align:right; background-color:lavender; width:65px;">34</td></tr><tr><td style="text-align:center;vertical-align:middle;">333</td><td>でんせつ 865</td><td style="text-align:right; background-color:pink; width:65px;">30</td><td style="text-align:right; background-color:pink; width:65px;">30</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">32</td><td style="text-align:right; background-color:lemonchiffon; width:65px;">32</td><td style="text-align:right; background-color:lavender; width:65px;">35</td><td style="text-align:right; background-color:lavender; width:65px;">35</td></tr></tbody></table></div>
</div>
</div>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">金イクラ回収率の表（キケン度10%ごと）</div>
    <div class="fold-content visible-on-open"><p>昼Waveで出現した全てのオオモノシャケを倒した場合、それによって発生した全ての金イクラのうち何%を納品すればノルマクリアとなるかを一覧で示した表。</p>
<p>※この表は解析データに基づいて作られている。実際にこの値となるかは要検証。<br />
※オオモノシャケがステージ上に存在できる数は15匹までに制限されている<a id="notetext_15"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;Ver. 2.0.0 更新データ詳細より。&amp;quot;一度に出現するオオモノシャケの数の上限を15匹までに制限しました。&amp;quot;&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_15&quot;&gt;脚注 *15 へ&lt;/a&gt;&lt;/div&gt;">*15</a>ため、処理が滞った場合には必要回収率はこれよりも高くなることに注意。</p>
<div class="h-scrollable"><table><thead><tr><th rowspan="2">キケン度（%）</th><th rowspan="2">平均評価</th><th colspan="3">必要回収率</th></tr><tr><th>WAVE1</th><th>WAVE2</th><th>WAVE3</th></tr></thead><tfoot><tr><th rowspan="2">キケン度（%）</th><th rowspan="2">平均評価</th><th>WAVE1</th><th>WAVE2</th><th>WAVE3</th></tr><tr><th colspan="3">必要回収率</th></tr></tfoot><tbody><tr><td style="text-align:center;vertical-align:middle;">0</td><td>かけだし 0</td><td style="background-color:#FFFFFF; text-align:right;">33.33%</td><td style="background-color:#FBAAA1; text-align:right;">44.44%</td><td style="background-color:#F96A5A; text-align:right;">55.56%</td></tr><tr><td style="text-align:center;vertical-align:middle;">10</td><td>かけだし 50</td><td style="background-color:#F96A5A; text-align:right;">55.56%</td><td style="background-color:#F7402B; text-align:right;">66.67%</td><td style="background-color:#F8604E; text-align:right;">58.33%</td></tr><tr><td style="text-align:center;vertical-align:middle;">20</td><td>はんにんまえ 0</td><td style="background-color:#F97363; text-align:right;">53.33%</td><td style="background-color:#FA8072; text-align:right;">50.00%</td><td style="background-color:#FA9286; text-align:right;">47.62%</td></tr><tr><td style="text-align:center;vertical-align:middle;">30</td><td>はんにんまえ 50</td><td style="background-color:#F97363; text-align:right;">53.33%</td><td style="background-color:#FA8072; text-align:right;">50.00%</td><td style="background-color:#FB9F95; text-align:right;">45.83%</td></tr><tr><td style="text-align:center;vertical-align:middle;">40</td><td>いちにんまえ 0</td><td style="background-color:#FA8072; text-align:right;">50.00%</td><td style="background-color:#FA9286; text-align:right;">47.62%</td><td style="background-color:#FBAAA1; text-align:right;">44.44%</td></tr><tr><td style="text-align:center;vertical-align:middle;">50</td><td>いちにんまえ 50</td><td style="background-color:#F96A5A; text-align:right;">55.56%</td><td style="background-color:#FB9F95; text-align:right;">45.83%</td><td style="background-color:#FCB2AA; text-align:right;">43.33%</td></tr><tr><td style="text-align:center;vertical-align:middle;">60</td><td>じゅくれん 0</td><td style="background-color:#F97667; text-align:right;">52.38%</td><td style="background-color:#FBAAA1; text-align:right;">44.44%</td><td style="background-color:#FCB9B2; text-align:right;">42.42%</td></tr><tr><td style="text-align:center;vertical-align:middle;">70</td><td>じゅくれん 50</td><td style="background-color:#FA8072; text-align:right;">50.00%</td><td style="background-color:#FCB2AA; text-align:right;">43.33%</td><td style="background-color:#FCBFB8; text-align:right;">41.67%</td></tr><tr><td style="text-align:center;vertical-align:middle;">80</td><td>たつじん 0</td><td style="background-color:#FA8E81; text-align:right;">48.15%</td><td style="background-color:#FCB9B2; text-align:right;">42.42%</td><td style="background-color:#FCC4BD; text-align:right;">41.03%</td></tr><tr><td style="text-align:center;vertical-align:middle;">90</td><td>たつじん 50</td><td style="background-color:#FB998E; text-align:right;">46.67%</td><td style="background-color:#FCBFB8; text-align:right;">41.67%</td><td style="background-color:#FCC8C2; text-align:right;">40.48%</td></tr><tr><td style="text-align:center;vertical-align:middle;">100</td><td>たつじん+1 0</td><td style="background-color:#FA8B7E; text-align:right;">48.48%</td><td style="background-color:#FBB0A8; text-align:right;">43.59%</td><td style="background-color:#FCBBB3; text-align:right;">42.22%</td></tr><tr><td style="text-align:center;vertical-align:middle;">110</td><td>たつじん+1 50</td><td style="background-color:#F97A6B; text-align:right;">51.52%</td><td style="background-color:#FB9D92; text-align:right;">46.15%</td><td style="background-color:#FBAAA1; text-align:right;">44.44%</td></tr><tr><td style="text-align:center;vertical-align:middle;">120</td><td>たつじん+2 0</td><td style="background-color:#FA8072; text-align:right;">50.00%</td><td style="background-color:#FBA49A; text-align:right;">45.24%</td><td style="background-color:#FBAFA6; text-align:right;">43.75%</td></tr><tr><td style="text-align:center;vertical-align:middle;">130</td><td>たつじん+2 50</td><td style="background-color:#FA897C; text-align:right;">48.72%</td><td style="background-color:#FBAAA1; text-align:right;">44.44%</td><td style="background-color:#FCB4AC; text-align:right;">43.14%</td></tr><tr><td style="text-align:center;vertical-align:middle;">140</td><td>たつじん+3 0</td><td style="background-color:#FA9286; text-align:right;">47.62%</td><td style="background-color:#FBAFA6; text-align:right;">43.75%</td><td style="background-color:#FCB8B0; text-align:right;">42.59%</td></tr><tr><td style="text-align:center;vertical-align:middle;">150</td><td>たつじん+3 50</td><td style="background-color:#FB998E; text-align:right;">46.67%</td><td style="background-color:#FCB4AC; text-align:right;">43.14%</td><td style="background-color:#FCBCB4; text-align:right;">42.11%</td></tr><tr><td style="text-align:center;vertical-align:middle;">160</td><td>でんせつ 0</td><td style="background-color:#FB9F95; text-align:right;">45.83%</td><td style="background-color:#FCB8B0; text-align:right;">42.59%</td><td style="background-color:#FCBFB8; text-align:right;">41.67%</td></tr><tr><td style="text-align:center;vertical-align:middle;">170</td><td>でんせつ 50</td><td style="background-color:#FBA59B; text-align:right;">45.10%</td><td style="background-color:#FCBCB4; text-align:right;">42.11%</td><td style="background-color:#FCC2BB; text-align:right;">41.27%</td></tr><tr><td style="text-align:center;vertical-align:middle;">180</td><td>でんせつ 100</td><td style="background-color:#FBAAA1; text-align:right;">44.44%</td><td style="background-color:#FCBFB8; text-align:right;">41.67%</td><td style="background-color:#FCC5BE; text-align:right;">40.91%</td></tr><tr><td style="text-align:center;vertical-align:middle;">190</td><td>でんせつ 150</td><td style="background-color:#FBAEA5; text-align:right;">43.86%</td><td style="background-color:#FCC2BB; text-align:right;">41.27%</td><td style="background-color:#FCC7C1; text-align:right;">40.58%</td></tr><tr><td style="text-align:center;vertical-align:middle;">200</td><td>でんせつ 200</td><td style="background-color:#FCB2AA; text-align:right;">43.33%</td><td style="background-color:#FCB9B2; text-align:right;">42.42%</td><td style="background-color:#FCBFB8; text-align:right;">41.67%</td></tr><tr><td style="text-align:center;vertical-align:middle;">210</td><td>でんせつ 250</td><td style="background-color:#FCB2AA; text-align:right;">43.33%</td><td style="background-color:#FCB9B2; text-align:right;">42.42%</td><td style="background-color:#FCBFB8; text-align:right;">41.67%</td></tr><tr><td style="text-align:center;vertical-align:middle;">220</td><td>でんせつ 300</td><td style="background-color:#FCC2BB; text-align:right;">41.27%</td><td style="background-color:#FCC7C1; text-align:right;">40.58%</td><td style="background-color:#FDCCC6; text-align:right;">40.00%</td></tr><tr><td style="text-align:center;vertical-align:middle;">230</td><td>でんせつ 350</td><td style="background-color:#FDD0CB; text-align:right;">39.39%</td><td style="background-color:#FDD4CF; text-align:right;">38.89%</td><td style="background-color:#FDCEC8; text-align:right;">39.74%</td></tr><tr><td style="text-align:center;vertical-align:middle;">240</td><td>でんせつ 400</td><td style="background-color:#FDD2CD; text-align:right;">39.13%</td><td style="background-color:#FDD6D1; text-align:right;">38.67%</td><td style="background-color:#FDD9D5; text-align:right;">38.27%</td></tr><tr><td style="text-align:center;vertical-align:middle;">250</td><td>でんせつ 450</td><td style="background-color:#FDD2CD; text-align:right;">39.13%</td><td style="background-color:#FDD6D1; text-align:right;">38.67%</td><td style="background-color:#FDE3E0; text-align:right;">36.90%</td></tr><tr><td style="text-align:center;vertical-align:middle;">260</td><td>でんせつ 500</td><td style="background-color:#FDDFDB; text-align:right;">37.50%</td><td style="background-color:#FDE1DE; text-align:right;">37.18%</td><td style="background-color:#FDDAD6; text-align:right;">38.10%</td></tr><tr><td style="text-align:center;vertical-align:middle;">270</td><td>でんせつ 550</td><td style="background-color:#FDE0DD; text-align:right;">37.33%</td><td style="background-color:#FDE2DF; text-align:right;">37.04%</td><td style="background-color:#FDE4E1; text-align:right;">36.78%</td></tr><tr><td style="text-align:center;vertical-align:middle;">280</td><td>でんせつ 600</td><td style="background-color:#FEEBE9; text-align:right;">35.90%</td><td style="background-color:#FEECEA; text-align:right;">35.71%</td><td style="background-color:#FEE5E2; text-align:right;">36.67%</td></tr><tr><td style="text-align:center;vertical-align:middle;">290</td><td>でんせつ 650</td><td style="background-color:#FEEBE9; text-align:right;">35.90%</td><td style="background-color:#FEECEA; text-align:right;">35.71%</td><td style="background-color:#FEEEEC; text-align:right;">35.48%</td></tr><tr><td style="text-align:center;vertical-align:middle;">300</td><td>でんせつ 700</td><td style="background-color:#FEECEA; text-align:right;">35.80%</td><td style="background-color:#FEEDEB; text-align:right;">35.63%</td><td style="background-color:#FEF7F6; text-align:right;">34.38%</td></tr><tr><td style="text-align:center;vertical-align:middle;">310</td><td>でんせつ 750</td><td style="background-color:#FEF5F4; text-align:right;">34.52%</td><td style="background-color:#FEF6F5; text-align:right;">34.44%</td><td style="background-color:#FEF7F6; text-align:right;">34.34%</td></tr><tr><td style="text-align:center;vertical-align:middle;">320</td><td>でんせつ 800</td><td style="background-color:#FFFFFF; text-align:right;">33.33%</td><td style="background-color:#FFFFFF; text-align:right;">33.33%</td><td style="background-color:#FEF7F6; text-align:right;">34.34%</td></tr><tr><td style="text-align:center;vertical-align:middle;">330</td><td>でんせつ 850</td><td style="background-color:#FFFFFF; text-align:right;">33.33%</td><td style="background-color:#FFFFFF; text-align:right;">33.33%</td><td style="background-color:#FFFFFF; text-align:right;">33.33%</td></tr><tr><td style="text-align:center;vertical-align:middle;">333</td><td>でんせつ 865</td><td style="background-color:#FFFFFF; text-align:right;">33.33%</td><td style="background-color:#FFFFFF; text-align:right;">33.33%</td><td style="background-color:#FFFFFF; text-align:right;">33.33%</td></tr></tbody></table></div>
</div>
</div>
<h4 id="h4_content_1_16" class="heading-after-first">シャケの出現間隔の表  <a class="anchor_super" name ="wea530d1"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=wea530d1" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h4>
<p>シャケたちは一定時間ごとに出現しており、この間隔はキケン度に応じて変化する。<br />
この間隔は「72/n 秒」（nは自然数）となっており、nはキケン度によって決まる。</p>
<p>オオモノシャケは「100～28秒」の出現タイミングでのみ現れる。<br />
残り「28秒」の出現タイミングではオオモノシャケは1体のみ現れる。<br />
それより後の出現タイミングではオオモノシャケは現れず、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>のみになる（いわゆる「<strong>28秒ルール</strong>」）。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>のヒカリバエの切り替わり間隔は、この出現間隔と同じ。</p>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">シャケの出現間隔の表</div>
    <div class="fold-content visible-on-open"><p>※この表は解析データに基づいて作られている。実際にこの値となるかは要検証。<br />
※評価目安はあくまで目安で、実際にはあり得ない値を含む。<br />
※出現時刻は小数点以下を四捨五入してある。</p>
<div class="h-scrollable"><table><tbody><tr><th>キケン度(%)</th><td>0.0 ～ 19.8</td><td>20.0 ～ 59.8</td><td>60.0 ～ 99.8</td><td>100.0 ～ 149.8</td><td>150.0 ～ 199.8</td><td>200.0 ～ 266.4</td><td>266.6 ～ 329.8</td><td>333</td></tr><tr><th>評価目安</th><td>かけだし 0 ～</td><td>はんにんまえ 0 ～</td><td>じゅくれん 0 ～</td><td>たつじん+1 0 ～</td><td>たつじん+3 50 ～</td><td>でんせつ 200 ～</td><td>でんせつ 533 ～</td><td>でんせつ 865</td></tr><tr><th>ノルマ</th><td>3/4/5 ～ 7/8/9</td><td>8/9/10 ～ 10/11/13</td><td>11/12/14 ～ 15/16/18</td><td>16/17/19 ～ 20/22/24</td><td>21/22/24 ～ 25/27/29</td><td>26/28/30 ～ 27/29/32</td><td>28/30/32 ～ 29/31/34</td><td>30/32/35</td></tr><tr><th>出現間隔(秒)</th><td>36.0</td><td>24.0</td><td>18.0</td><td>14.4</td><td>12.0</td><td>10.3</td><td>9.0</td><td>8.0</td></tr><tr><th rowspan="10">出現時刻(オオモノあり)</th><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td></tr><tr><td>64</td><td>76</td><td>82</td><td>86</td><td>88</td><td>90</td><td>91</td><td>92</td></tr><tr><td>28</td><td>52</td><td>64</td><td>71</td><td>76</td><td>79</td><td>82</td><td>84</td></tr><tr><td rowspan="7" style="background-color:whitesmoke;"></td><td>28</td><td>46</td><td>57</td><td>64</td><td>69</td><td>73</td><td>76</td></tr><tr><td rowspan="6" style="background-color:whitesmoke;"></td><td>28</td><td>42</td><td>52</td><td>59</td><td>64</td><td>68</td></tr><tr><td rowspan="5" style="background-color:whitesmoke;"></td><td>28</td><td>40</td><td>49</td><td>55</td><td>60</td></tr><tr><td rowspan="4" style="background-color:whitesmoke;"></td><td>28</td><td>38</td><td>46</td><td>52</td></tr><tr><td rowspan="3" style="background-color:whitesmoke;"></td><td>28</td><td>37</td><td>44</td></tr><tr><td rowspan="2" style="background-color:whitesmoke;"></td><td>28</td><td>36</td></tr><tr><td style="background-color:whitesmoke;"></td><td>28</td></tr><tr><th rowspan="3">出現時刻(オオモノなし)</th><td rowspan="3" style="background-color:whitesmoke;"></td><td>4</td><td>10</td><td>14</td><td>16</td><td>18</td><td>19</td><td>20</td></tr><tr><td rowspan="2" style="background-color:whitesmoke;"></td><td rowspan="2" style="background-color:whitesmoke;"></td><td rowspan="2" style="background-color:whitesmoke;"></td><td>4</td><td>7</td><td>10</td><td>12</td></tr><tr><td style="background-color:whitesmoke;"></td><td style="background-color:whitesmoke;"></td><td>1</td><td>4</td></tr></tbody></table></div>
</div>
</div>
<h2 id="h2_content_1_17" class="heading-after-first">報酬  <a class="anchor_super" name ="w9c55236"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=w9c55236" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<h3 id="h3_content_1_18" class="heading-after-first">クマサンポイントとプレゼント  <a class="anchor_super" name ="k0bdd097"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=k0bdd097" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<h4 id="h4_content_34_0" >クマサンポイント</h4>

<p>バイトが終わると「クマサンポイント」が貰える。<br />
一回のシフト中にポイントを一定量集めるとプレゼントが貰える。</p>
<p>クマサンポイントはバイトの成績が良いほど、そして自身の評価が高いほど多く貰える。</p>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">クマサンポイントの計算式</div>
    <div class="fold-content visible-on-open"><p>クマサンポイントは<strong>「バイトスコア×評価レート＋クリアボーナス」</strong>で算出される。</p>
<dl class="list1"><dt>バイトスコア</dt>
<dd>チーム全体の金イクラ＆赤イクラの数から算出される。
<dl class="list2"><dt>計算式</dt>
<dd>金イクラ納品数+(赤イクラ取得数÷200)（小数点以下切り捨て）</dd></dl></dd>
<dt>評価レート</dt>
<dd>バイト終了後の自分の評価に応じた倍率。<br />
0.05刻みで、範囲は1.50～3.25。<br />
（イカリング3ではなぜか『でんせつ 40』で×2.29と表示されるが、補間ミスと思われる）
<dl class="list2"><dt>計算式</dt>
<dd>『かけだし 0』で1.50で、評価が50上がるごとに0.05を足す。<br />
= 1.50 + FLOOR(バイト終了後の自分の累計評価値÷50)×0.05<br />
目安として『たつじん+1 0』(累計評価値500)なら2.00、『でんせつ 200』(累計評価値1000)なら2.50、『でんせつ 700』(累計評価値1500)なら3.00となる。</dd></dl></dd>
<dt>クリアボーナス</dt>
<dd>WAVE3成功で+50、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/Extra%20Wave" title="サーモンラン/特殊な状況/Extra Wave" class="rel-wiki-page">Extra Wave</a>突入(成否は問わない)でさらに+50（評価レートは乗らない）</dd></dl>
</div>
</div>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">簡単にまとめると</div>
    <div class="fold-content visible-on-open"><ul class="list1"><li>金イクラ納品数が報酬に直結する。</li>
<li>赤イクラ取得数は微量ながら響く。</li>
<li>クリアボーナスも重要。
<ul class="list2"><li>WAVE3成功ボーナスは概ね金イクラ21コ相当（バイト終了時に『でんせつ 60』の場合）</li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/Extra%20Wave" title="サーモンラン/特殊な状況/Extra Wave" class="rel-wiki-page">Extra Wave</a>成功ボーナスも概ね金イクラ21コ相当（バイト終了時に『でんせつ 60』の場合）</li>
<li>ちなみに、その他の評価では
<ul class="list3"><li>『じゅくれん 60』なら27.0コ相当</li>
<li>『たつじん+2 60』なら24.4コ相当</li>
<li>『でんせつ 460』なら18.2コ相当</li></ul></li></ul></li></ul>
</div>
</div>
<p>シフトが変わると、現在のクマサンポイントは0になる。<br />
（それとは別に、今まで集めた累計ポイントも記録されている。）</p>
<h4 id="h4_content_37_0" >プレゼント</h4>

<p>現在のシフトで集めたクマサンポイントが一定値に達するとプレゼント<a id="notetext_16"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;バイトマニュアルでの呼称&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_16&quot;&gt;脚注 *16 へ&lt;/a&gt;&lt;/div&gt;">*16</a>が貰える。<br />
「ほうしゅうメーター」を見れば、どれ位のクマサンポイントでプレゼントが貰えるか確認できる。<br />
プレゼントはクマサン商会に入って正面にある交換所で受け取ることができる。</p>
<p>プレゼントを貯めておけるのは99コまで。それ以上は自動で破棄されてしまうので、忘れずに受け取ろう。<br />
(新シフトで0コから始めた場合、33200ptでカンストする。)</p>
<p>シフトが変わると、ほうしゅうメーターはリセットされる。</p>
<p><strong>ほうしゅうメーター</strong></p>
<div class="h-scrollable"><table><thead><tr><th>ポイント</th><th>報酬</th><th>ポイント</th><th>報酬</th><th>ポイント</th><th>報酬</th><th>ポイント</th><th>報酬</th></tr></thead><tbody><tr><td style="background-color:pink;">100</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">1300</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">2500</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">3700</td><td style="background-color:lemonchiffon;"></td></tr><tr><td style="background-color:pink;">200</td><td style="background-color:pink;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lemonchiffon;">1400</td><td style="background-color:lemonchiffon;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lemonchiffon;">2600</td><td style="background-color:lemonchiffon;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lemonchiffon;">3800</td><td style="background-color:lemonchiffon;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td></tr><tr><td style="background-color:pink;">300</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">1500</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">2700</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">3900</td><td style="background-color:lemonchiffon;"></td></tr><tr><td style="background-color:pink;">400</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">1600</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lemonchiffon;">2800</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lavender;">4000</td><td style="background-color:lavender;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td></tr><tr><td style="background-color:pink;">500</td><td style="background-color:pink;">銀カプセル</td><td style="background-color:lemonchiffon;">1700</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">2900</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lavender;">4100</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">600</td><td style="background-color:pink;">カプセル<br class="spacer">（ベリーレア確定）</td><td style="background-color:lemonchiffon;">1800</td><td style="background-color:lemonchiffon;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lemonchiffon;">3000</td><td style="background-color:lemonchiffon;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lavender;">4200</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">700</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">1900</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">3100</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lavender;">4300</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">800</td><td style="background-color:pink;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lemonchiffon;">2000</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lemonchiffon;">3200</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lavender;">4400</td><td style="background-color:lavender;">桃カプセル</td></tr><tr><td style="background-color:pink;">900</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">2100</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">3300</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lavender;">4500</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">1000</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">2200</td><td style="background-color:lemonchiffon;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lemonchiffon;">3400</td><td style="background-color:lemonchiffon;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lavender;">4600</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">1100</td><td style="background-color:pink;">金カプセル</td><td style="background-color:lemonchiffon;">2300</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">3500</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lavender;">4700</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">1200</td><td style="background-color:pink;">カプセル<br class="spacer">（ベリーレア確定）</td><td style="background-color:lemonchiffon;">2400</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lemonchiffon;">3600</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:white;">以降紫部分を繰り返し</td><td style="background-color:white;"></td></tr></tbody></table></div>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">ほうしゅうメーター(Ver9.0.0以前)</div>
    <div class="fold-content visible-on-open"><p><strong>ほうしゅうメーター</strong></p>
<div class="h-scrollable"><table><thead><tr><th>ポイント</th><th>報酬</th><th>ポイント</th><th>報酬</th><th>ポイント</th><th>報酬</th><th>ポイント</th><th>報酬</th></tr></thead><tbody><tr><td style="background-color:pink;">100</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">1300</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">2500</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">3700</td><td style="background-color:lemonchiffon;"></td></tr><tr><td style="background-color:pink;">200</td><td style="background-color:pink;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lemonchiffon;">1400</td><td style="background-color:lemonchiffon;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lemonchiffon;">2600</td><td style="background-color:lemonchiffon;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lemonchiffon;">3800</td><td style="background-color:lemonchiffon;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td></tr><tr><td style="background-color:pink;">300</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">1500</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">2700</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">3900</td><td style="background-color:lemonchiffon;"></td></tr><tr><td style="background-color:pink;">400</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">1600</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lemonchiffon;">2800</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lavender;">4000</td><td style="background-color:lavender;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td></tr><tr><td style="background-color:pink;">500</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">1700</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">2900</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lavender;">4100</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">600</td><td style="background-color:pink;">カプセル<br class="spacer">（ベリーレア確定）</td><td style="background-color:lemonchiffon;">1800</td><td style="background-color:lemonchiffon;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lemonchiffon;">3000</td><td style="background-color:lemonchiffon;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lavender;">4200</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">700</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">1900</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">3100</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lavender;">4300</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">800</td><td style="background-color:pink;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lemonchiffon;">2000</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lemonchiffon;">3200</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lavender;">4400</td><td style="background-color:lavender;">桃カプセル</td></tr><tr><td style="background-color:pink;">900</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">2100</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">3300</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lavender;">4500</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">1000</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">2200</td><td style="background-color:lemonchiffon;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lemonchiffon;">3400</td><td style="background-color:lemonchiffon;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lavender;">4600</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">1100</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">2300</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">3500</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lavender;">4700</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">1200</td><td style="background-color:pink;">カプセル<br class="spacer">（ベリーレア確定）</td><td style="background-color:lemonchiffon;">2400</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lemonchiffon;">3600</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:white;">以降紫部分を繰り返し</td><td style="background-color:white;"></td></tr></tbody></table></div>
</div>
</div>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">ほうしゅうメーター（<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>）</div>
    <div class="fold-content visible-on-open"><p><strong>ほうしゅうメーター（<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>）</strong><br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>のほうしゅうメーターは、報酬の多い最初の区間の長さが通常の2倍になっている。</p>
<div class="h-scrollable"><table><thead><tr><th>ポイント</th><th>報酬</th><th>ポイント</th><th>報酬</th><th>ポイント</th><th>報酬</th><th>ポイント</th><th>報酬</th><th>ポイント</th><th>報酬</th></tr></thead><tbody><tr><td style="background-color:pink;">100</td><td style="background-color:pink;">カプセル</td><td style="background-color:pink;">1300</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">2500</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">3700</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">4900</td><td style="background-color:lemonchiffon;"></td></tr><tr><td style="background-color:pink;">200</td><td style="background-color:pink;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:pink;">1400</td><td style="background-color:pink;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lemonchiffon;">2600</td><td style="background-color:lemonchiffon;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lemonchiffon;">3800</td><td style="background-color:lemonchiffon;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lemonchiffon;">5000</td><td style="background-color:lemonchiffon;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td></tr><tr><td style="background-color:pink;">300</td><td style="background-color:pink;">カプセル</td><td style="background-color:pink;">1500</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">2700</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">3900</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">5100</td><td style="background-color:lemonchiffon;"></td></tr><tr><td style="background-color:pink;">400</td><td style="background-color:pink;">カプセル</td><td style="background-color:pink;">1600</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">2800</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lemonchiffon;">4000</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lavender;">5200</td><td style="background-color:lavender;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td></tr><tr><td style="background-color:pink;">500</td><td style="background-color:pink;">カプセル</td><td style="background-color:pink;">1700</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">2900</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">4100</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lavender;">5300</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">600</td><td style="background-color:pink;">カプセル<br class="spacer">（ベリーレア確定）</td><td style="background-color:pink;">1800</td><td style="background-color:pink;">カプセル<br class="spacer">（ベリーレア確定）</td><td style="background-color:lemonchiffon;">3000</td><td style="background-color:lemonchiffon;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lemonchiffon;">4200</td><td style="background-color:lemonchiffon;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lavender;">5400</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">700</td><td style="background-color:pink;">カプセル</td><td style="background-color:pink;">1900</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">3100</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">4300</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lavender;">5500</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">800</td><td style="background-color:pink;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:pink;">2000</td><td style="background-color:pink;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lemonchiffon;">3200</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lemonchiffon;">4400</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lavender;">5600</td><td style="background-color:lavender;">桃カプセル</td></tr><tr><td style="background-color:pink;">900</td><td style="background-color:pink;">カプセル</td><td style="background-color:pink;">2100</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">3300</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">4500</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lavender;">5700</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">1000</td><td style="background-color:pink;">カプセル</td><td style="background-color:pink;">2200</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">3400</td><td style="background-color:lemonchiffon;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lemonchiffon;">4600</td><td style="background-color:lemonchiffon;">今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td><td style="background-color:lavender;">5800</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">1100</td><td style="background-color:pink;">カプセル</td><td style="background-color:pink;">2300</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">3500</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">4700</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lavender;">5900</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">1200</td><td style="background-color:pink;">カプセル<br class="spacer">（ベリーレア確定）</td><td style="background-color:pink;">2400</td><td style="background-color:pink;">カプセル<br class="spacer">（ベリーレア確定）</td><td style="background-color:lemonchiffon;">3600</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lemonchiffon;">4800</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:white;">以降紫部分を繰り返し</td><td style="background-color:white;"></td></tr></tbody></table></div>
</div>
</div>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">ほうしゅうメーター(バイトチームコンテスト)</div>
    <div class="fold-content visible-on-open"><p><strong>ほうしゅうメーター（バイトチームコンテスト）</strong><br />
バイトチームコンテストのほうしゅうメーターは、通常では今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>となっている部分が、すべて桃カプセルに置き換えられている。</p>
<div class="h-scrollable"><table><thead><tr><th>ポイント</th><th>報酬</th><th>ポイント</th><th>報酬</th><th>ポイント</th><th>報酬</th><th>ポイント</th><th>報酬</th></tr></thead><tbody><tr><td style="background-color:pink;">100</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">1300</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">2500</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">3700</td><td style="background-color:lemonchiffon;"></td></tr><tr><td style="background-color:pink;">200</td><td style="background-color:pink;">桃カプセル</td><td style="background-color:lemonchiffon;">1400</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lemonchiffon;">2600</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lemonchiffon;">3800</td><td style="background-color:lemonchiffon;">桃カプセル</td></tr><tr><td style="background-color:pink;">300</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">1500</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">2700</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">3900</td><td style="background-color:lemonchiffon;"></td></tr><tr><td style="background-color:pink;">400</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">1600</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lemonchiffon;">2800</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lavender;">4000</td><td style="background-color:lavender;">桃カプセル</td></tr><tr><td style="background-color:pink;">500</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">1700</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">2900</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lavender;">4100</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">600</td><td style="background-color:pink;">カプセル<br class="spacer">（ベリーレア確定）</td><td style="background-color:lemonchiffon;">1800</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lemonchiffon;">3000</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lavender;">4200</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">700</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">1900</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">3100</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lavender;">4300</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">800</td><td style="background-color:pink;">桃カプセル</td><td style="background-color:lemonchiffon;">2000</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lemonchiffon;">3200</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lavender;">4400</td><td style="background-color:lavender;">桃カプセル</td></tr><tr><td style="background-color:pink;">900</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">2100</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">3300</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lavender;">4500</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">1000</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">2200</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lemonchiffon;">3400</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lavender;">4600</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">1100</td><td style="background-color:pink;">カプセル</td><td style="background-color:lemonchiffon;">2300</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lemonchiffon;">3500</td><td style="background-color:lemonchiffon;"></td><td style="background-color:lavender;">4700</td><td style="background-color:lavender;"></td></tr><tr><td style="background-color:pink;">1200</td><td style="background-color:pink;">カプセル<br class="spacer">（ベリーレア確定）</td><td style="background-color:lemonchiffon;">2400</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:lemonchiffon;">3600</td><td style="background-color:lemonchiffon;">桃カプセル</td><td style="background-color:white;">以降紫部分を繰り返し</td><td style="background-color:white;"></td></tr></tbody></table></div>
</div>
</div>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">プレゼントの内容の詳細(解析情報)</div>
    <div class="fold-content visible-on-open"><p><strong>プレゼントの内容の詳細(解析情報)</strong></p>
<p><strong>プレゼントのレア度と出現率</strong><br />
プレゼントにはレア度がある。レア度はランダムに決まる。（レア度が指定されていない限り。）<br />
各レア度の出現率は次の通り。</p>
<div class="h-scrollable"><table><tbody><tr><th>レア度</th><td><strong>コモン</strong></td><td><strong>レア</strong></td><td><strong>ベリーレア</strong></td></tr><tr><th>確率</th><td>50%</td><td>40%</td><td>10%</td></tr></tbody></table></div>
<p>銀カプセルと金カプセルはコモンのレア度が存在しないため、レア/ベリーレアは80%/20%となる。</p>
<p><strong>カプセルの色と出現率</strong><br />
カプセルには色がある。色はランダムに決まる。（色が指定されていない限り。）<br />
各色の出現率は次の通り。</p>
<div class="h-scrollable"><table><thead><tr><th>カプセルの色</th><th>確率</th><th>内容の種類</th></tr></thead><tbody><tr><th style="background-color:lemonchiffon;">黄</th><td>23%</td><td>おカネ</td></tr><tr><th style="background-color:antiquewhite;">橙</th><td>23%</td><td>フードチケット</td></tr><tr><th style="background-color:lavender;">紫</th><td>23%</td><td>ドリンクチケット</td></tr><tr><th style="background-color:honeydew;">緑</th><td>23%</td><td><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC" title="ギア/ギアパワー" class="rel-wiki-page">ギアパワー</a>のかけら</td></tr><tr><th style="background-color:pink;">桃</th><td>8%/固定</td><td>過去の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td></tr><tr><th>今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></th><td>固定</td><td>今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></td></tr><tr><th style="background-color:silber;">銀</th><td>固定</td><td>銀のウロコ</td></tr><tr><th style="background-color:gold;">金</th><td>固定</td><td>金のウロコ</td></tr></tbody></table></div>
<p><strong>プレゼントの内容</strong><br />
各種プレゼントの内容は、レア度と色によって次のように決まる。</p>
<div class="h-scrollable"><table><thead><tr><th>種類</th><th>コモン</th><th>レア</th><th>ベリーレア</th></tr></thead><tbody><tr><th>今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></th><td>今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>（1スロット）</td><td>今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>（2スロット）</td><td>今月の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>（3スロット）</td></tr><tr><th style="background-color:lemonchiffon;">黄カプセル</th><td>おカネ5000</td><td>おカネ16000</td><td>おカネ32000</td></tr><tr><th style="background-color:antiquewhite;">橙カプセル</th><td>おカネ5000</td><td>1.5倍チケット×1</td><td>2倍チケット×1</td></tr><tr><th style="background-color:lavender;">紫カプセル</th><td>おカネ5000</td><td>ドリンクチケット×1</td><td>ドリンクチケット×4</td></tr><tr><th style="background-color:honeydew;">緑カプセル</th><td>おカネ5000</td><td><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC" title="ギア/ギアパワー" class="rel-wiki-page">ギアパワー</a>のかけら×2</td><td><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC" title="ギア/ギアパワー" class="rel-wiki-page">ギアパワー</a>のかけら×4</td></tr><tr><th style="background-color:pink;">桃カプセル</th><td>過去の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>（1スロット）</td><td>過去の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>（2スロット）</td><td>過去の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>（3スロット）</td></tr><tr><th style="background-color:silber;">銀カプセル</th><td>-</td><td>銀のウロコ×3</td><td>銀のウロコ×6</td></tr><tr><th style="background-color:gold;">金カプセル</th><td>-</td><td>金のウロコ×1</td><td>金のウロコ×2</td></tr></tbody></table></div>
<p>※これらプレゼントの表は解析データに基づいて作られているので、実際にこの通りかは未確認であり、要検証。</p>
</div>
</div>
<h4 id="h4_content_42_0" >プレゼント稼ぎの指針</h4>

<p>結論から言えば、次のポイントまで稼ぐといい。</p>
<ul class="list1"><li><strong>おカネが欲しい</strong></li>
<li><strong>何でもいいけど、お得に稼ぎたい</strong></li>
<li><strong>手っ取り早く銀・金のウロコが欲しい</strong><br />
→1200ptまでプレイ</li>
<li><strong><a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC" title="ギア/ギアパワー" class="rel-wiki-page">ギアパワー</a>のかけらを効率よく集めたい</strong><br />
→4000ptまでは効率がいい</li>
<li><strong>何が何でも<a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC" title="ギア/ギアパワー" class="rel-wiki-page">ギアパワー</a>のかけらが欲しい</strong><br />
→制限なし</li></ul>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">以下考察</div>
    <div class="fold-content visible-on-open"><p>『0～1200pt』区間は100ptごとに多様かつ良質な報酬が得られる。<br />
『1201～4000pt』区間は必要ptが倍の200ptごとになり、特別<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>のみが得られる。<br />
『4001pt～』区間は必要ptがさらに倍の400ptごとになり、特別<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>のみが得られる。<br />
特別<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>から得られるのは<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>に付いている<strong>追加<a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC" title="ギア/ギアパワー" class="rel-wiki-page">ギアパワー</a></strong>のかけら（または<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>本体）のみなので、1400pt以降は全くおカネが得られないことになる。<br />
時間当たりの報酬量の最大化を考えるなら1200ptまでプレイするのが良い。<br />
<a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC" title="ギア/ギアパワー" class="rel-wiki-page">ギアパワー</a>のかけらに限って考えるなら、4000ptまではかなり効率よく集められるし、クリア率にもよるが4000ptを超えてなおバトルよりバイトの方が効率よく集められるだろう。<br />
なお、欲しい<a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC" title="ギア/ギアパワー" class="rel-wiki-page">ギアパワー</a>を一つに絞って収集する場合、報酬<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>の<strong>基本<a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC" title="ギア/ギアパワー" class="rel-wiki-page">ギアパワー</a>を別の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC" title="ギア/ギアパワー" class="rel-wiki-page">ギアパワー</a>に置き換える</strong>ことでさらに増やせる<a id="notetext_17"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;例えばイカ速のかけらが欲しい場合、基本&lt;a href=&quot;/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC&quot; title=&quot;ギア/ギアパワー&quot; class=&quot;rel-wiki-page&quot;&gt;ギアパワー&lt;/a&gt;がイカ速の&lt;a href=&quot;/splatoon3mix/%E3%82%AE%E3%82%A2&quot; title=&quot;ギア&quot; class=&quot;rel-wiki-page&quot;&gt;ギア&lt;/a&gt;を引いたら、スパイキーに不要なかけら45個を払って置き換えればイカ速のかけら6個が得られる。&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_17&quot;&gt;脚注 *17 へ&lt;/a&gt;&lt;/div&gt;">*17</a>。使わないかけらが大量に余っていたらチャンスだ。<br />
評価によってクマサンポイントに倍率が掛かるのででんせつ以降ではドリンクチケットでバトルを繰り返すよりも結果的に効率が良くなる。</p>
</div>
</div>
<h3 id="h3_content_1_19" class="heading-after-first">ウロコと限定品  <a class="anchor_super" name ="a4a7708c"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=a4a7708c" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<h4 id="h4_content_44_0" >ウロコ</h4>

<p>オカシラシャケに遭遇すると、銅/銀/金のウロコが手に入る。<br />
オカシラシャケを撃退するのが速いほど多くのウロコが手に入る。<br />
また撃退できなくとも、オカシラシャケの体力を減らすほど多くのウロコが手に入る。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AA%E3%82%AB%E3%82%B7%E3%83%A9%E9%80%A3%E5%90%88" title="サーモンラン/シャケの種類/オカシラ連合" class="rel-wiki-page">オカシラ連合</a>戦ではウロコの数が3倍になる。ドロップ判定数は通常と変わらず、そこから3倍となる。</p>
<p>バイトのキケン度が高いほど、レア度の高いウロコが出現しやすい。</p>
<p>詳細は<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/Extra%20Wave" title="サーモンラン/特殊な状況/Extra Wave" class="rel-wiki-page">Extra Wave</a>を参照。</p>
<p>ver .9.0.0以降、従来で報酬に代わって500ptの報酬で銀ウロコ3枚、1100ptの報酬で金ウロコ1枚が手に入るようになった。両者ともレア報酬のエフェクトが出た場合は2倍になる。</p>
<h4 id="h4_content_45_0" >限定品</h4>

<p>ウロコは限定品(作業着/<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>/<a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E" title="ロッカー/オキモノ" class="rel-wiki-page">オキモノ</a>/<a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/%E3%82%B9%E3%83%86%E3%83%83%E3%82%AB%E3%83%BC" title="ロッカー/ステッカー" class="rel-wiki-page">ステッカー</a>/<a href="/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88" title="ネームプレート/プレート" class="rel-wiki-page">プレート</a>)と交換できる。<br />
交換する場所はプレゼントと同じで、クマサン商会に入って正面にある交換所で交換できる。</p>
<p>「？」表示の限定品は初めはロックされており、交換を繰り返して一定数のウロコを使うと解放される。</p>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">限定品の解放条件</div>
    <div class="fold-content visible-on-open"><p>限定品の解放段階は2段階ある。</p>
<ul class="list1"><li><strong>ランク1の解放条件</strong><br />
<span class="wikicolor" style="color:brown">銅</span>/<span class="wikicolor" style="color:dimgray">銀</span>/<span class="wikicolor" style="color:darkgoldenrod">金</span>のウロコ を <span class="wikicolor" style="color:brown">100</span>/<span class="wikicolor" style="color:dimgray">10</span>/<span class="wikicolor" style="color:darkgoldenrod">0</span> 個 使う。</li>
<li><strong>ランク2の解放条件</strong><br />
ランク1の解放条件に加えて、<br />
<span class="wikicolor" style="color:brown">銅</span>/<span class="wikicolor" style="color:dimgray">銀</span>/<span class="wikicolor" style="color:darkgoldenrod">金</span>のウロコ を <span class="wikicolor" style="color:brown">250</span>/<span class="wikicolor" style="color:dimgray">30</span>/<span class="wikicolor" style="color:darkgoldenrod">4</span> 個 使う。<br />
（累計で <span class="wikicolor" style="color:brown">350</span>/<span class="wikicolor" style="color:dimgray">40</span>/<span class="wikicolor" style="color:darkgoldenrod">4</span> 個使う。）</li></ul>
</div>
</div>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">交換できる限定品</div>
    <div class="fold-content visible-on-open"><p>交換できる限定品</p>
<div class="h-scrollable"><table><tbody><tr><th>アイテム</th><th>ウロコ数</th><th>交換条件</th></tr><tr><th colspan="3">作業着</th></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%82%B0%E3%83%AA%E3%83%BC%E3%83%B3.png?rev=168fdb987b42eceed02be753c234511c&amp;t=20220920182918" title="バイトツナギグリーン.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%82%B0%E3%83%AA%E3%83%BC%E3%83%B3.png.webp?rev=168fdb987b42eceed02be753c234511c&amp;t=20220920182918" alt="バイトツナギグリーン.png" title="バイトツナギグリーン.png" width="100" height="100"  loading="lazy"></a><br class="spacer">バイトツナギ グリーン</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×10</td><td rowspan="3">最初から</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%82%A4%E3%82%A8%E3%83%AD%E3%83%BC.png?rev=cd9176f5e56f6884810e596790cec06f&amp;t=20220920182936" title="バイトツナギイエロー.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%82%A4%E3%82%A8%E3%83%AD%E3%83%BC.png.webp?rev=cd9176f5e56f6884810e596790cec06f&amp;t=20220920182936" alt="バイトツナギイエロー.png" title="バイトツナギイエロー.png" width="100" height="100"  loading="lazy"></a><br class="spacer">バイトツナギ イエロー</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×10</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%83%90%E3%82%A4%E3%83%88%E3%82%A6%E3%82%A7%E3%83%BC%E3%83%80%E3%83%BC%E3%82%AA%E3%83%AC%E3%83%B3%E3%82%B8.png?rev=67478febdae72a6d389a87ee309580ce&amp;t=20231001135825" title="バイトウェーダーオレンジ.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%83%90%E3%82%A4%E3%83%88%E3%82%A6%E3%82%A7%E3%83%BC%E3%83%80%E3%83%BC%E3%82%AA%E3%83%AC%E3%83%B3%E3%82%B8.png.webp?rev=67478febdae72a6d389a87ee309580ce&amp;t=20231001135825" alt="バイトウェーダーオレンジ.png" title="バイトウェーダーオレンジ.png" width="100" height="100"  loading="lazy"></a><br class="spacer">バイトウェーダー オレンジ</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×15</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%83%94%E3%83%B3%E3%82%AF.png?rev=83880b3aecf0ef0efe166e422c967c74&amp;t=20220920182947" title="バイトツナギピンク.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%83%94%E3%83%B3%E3%82%AF.png.webp?rev=83880b3aecf0ef0efe166e422c967c74&amp;t=20220920182947" alt="バイトツナギピンク.png" title="バイトツナギピンク.png" width="100" height="100"  loading="lazy"></a><br class="spacer">バイトツナギ ピンク</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×30</td><td rowspan="6">ランク1</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%83%96%E3%83%AB%E3%83%BC.png?rev=cff5b9ae0317f4c319583bbddbbe6378&amp;t=20220920182958" title="バイトツナギブルー.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%83%96%E3%83%AB%E3%83%BC.png.webp?rev=cff5b9ae0317f4c319583bbddbbe6378&amp;t=20220920182958" alt="バイトツナギブルー.png" title="バイトツナギブルー.png" width="100" height="100"  loading="lazy"></a><br class="spacer">バイトツナギ ブルー</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×30</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%83%90%E3%82%A4%E3%83%88%E3%82%A6%E3%82%A7%E3%83%BC%E3%83%80%E3%83%BC%E3%82%A4%E3%82%A8%E3%83%AD%E3%83%BC.png?rev=20ce0e5b06a829db32085e2d97b22682&amp;t=20231001135834" title="バイトウェーダーイエロー.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%83%90%E3%82%A4%E3%83%88%E3%82%A6%E3%82%A7%E3%83%BC%E3%83%80%E3%83%BC%E3%82%A4%E3%82%A8%E3%83%AD%E3%83%BC.png.webp?rev=20ce0e5b06a829db32085e2d97b22682&amp;t=20231001135834" alt="バイトウェーダーイエロー.png" title="バイトウェーダーイエロー.png" width="100" height="100"  loading="lazy"></a><br class="spacer">バイトウェーダー イエロー</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×50</td></tr><tr><td style="text-align:center;">(画像待ち)<br class="spacer">バイトウェーダー ピーチ</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×50</td></tr><tr><td style="text-align:center;">(画像待ち)<br class="spacer">バイトウェーダー ライム</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×50</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%83%90%E3%82%A4%E3%83%88%E3%82%A6%E3%82%A7%E3%83%BC%E3%83%80%E3%83%BC%E3%83%96%E3%83%A9%E3%82%A6%E3%83%B3.png?rev=b1ad6108719f476c4529380e5313c2d6&amp;t=20231001135842" title="バイトウェーダーブラウン.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%83%90%E3%82%A4%E3%83%88%E3%82%A6%E3%82%A7%E3%83%BC%E3%83%80%E3%83%BC%E3%83%96%E3%83%A9%E3%82%A6%E3%83%B3.png.webp?rev=b1ad6108719f476c4529380e5313c2d6&amp;t=20231001135842" alt="バイトウェーダーブラウン.png" title="バイトウェーダーブラウン.png" width="100" height="100"  loading="lazy"></a><br class="spacer">バイトウェーダー ブラウン</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×75</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%83%96%E3%83%A9%E3%83%83%E3%82%AF.png?rev=f3c1bf288117f2ee65f0455f2d3c1875&amp;t=20220920183023" title="バイトツナギブラック.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%83%96%E3%83%A9%E3%83%83%E3%82%AF.png.webp?rev=f3c1bf288117f2ee65f0455f2d3c1875&amp;t=20220920183023" alt="バイトツナギブラック.png" title="バイトツナギブラック.png" width="100" height="100"  loading="lazy"></a><br class="spacer">バイトツナギ ブラック</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×100</td><td rowspan="10">ランク2</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%83%9B%E3%83%AF%E3%82%A4%E3%83%88.png?rev=3afa51f6e01095e2779342358ff142e5&amp;t=20220920183037" title="バイトツナギホワイト.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%83%9B%E3%83%AF%E3%82%A4%E3%83%88.png.webp?rev=3afa51f6e01095e2779342358ff142e5&amp;t=20220920183037" alt="バイトツナギホワイト.png" title="バイトツナギホワイト.png" width="100" height="100"  loading="lazy"></a><br class="spacer">バイトツナギ ホワイト</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×100</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%83%90%E3%82%A4%E3%83%88%E3%82%A6%E3%82%A7%E3%83%BC%E3%83%80%E3%83%BC%E3%83%96%E3%83%A9%E3%83%83%E3%82%AF.png?rev=d5fd66e1caf0da3dc10fe1243d38c0c0&amp;t=20231001135859" title="バイトウェーダーブラック.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%83%90%E3%82%A4%E3%83%88%E3%82%A6%E3%82%A7%E3%83%BC%E3%83%80%E3%83%BC%E3%83%96%E3%83%A9%E3%83%83%E3%82%AF.png.webp?rev=d5fd66e1caf0da3dc10fe1243d38c0c0&amp;t=20231001135859" alt="バイトウェーダーブラック.png" title="バイトウェーダーブラック.png" width="100" height="100"  loading="lazy"></a><br class="spacer">バイトウェーダー ブラック</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×150</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%83%89%E3%83%83%E3%83%88.png?rev=5a3a18b0f6e7a9d8bb8e853f2b80f93c&amp;t=20231001135906" title="バイトツナギドット.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%83%89%E3%83%83%E3%83%88.png.webp?rev=5a3a18b0f6e7a9d8bb8e853f2b80f93c&amp;t=20231001135906" alt="バイトツナギドット.png" title="バイトツナギドット.png" width="100" height="100"  loading="lazy"></a><br class="spacer">バイトツナギ ドット</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×150</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%82%AB%E3%83%A2.png?rev=09213a61066ae110270c6d6f3eabf0bc&amp;t=20231001135914" title="バイトツナギカモ.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%82%AB%E3%83%A2.png.webp?rev=09213a61066ae110270c6d6f3eabf0bc&amp;t=20231001135914" alt="バイトツナギカモ.png" title="バイトツナギカモ.png" width="100" height="100"  loading="lazy"></a><br class="spacer">バイトツナギ カモ</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×150</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%83%8B%E3%82%B7%E3%82%AD.png?rev=064d3067f9a0f2a3e490aebd1fadbb8d&amp;t=20231001135920" title="バイトツナギニシキ.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%83%8B%E3%82%B7%E3%82%AD.png.webp?rev=064d3067f9a0f2a3e490aebd1fadbb8d&amp;t=20231001135920" alt="バイトツナギニシキ.png" title="バイトツナギニシキ.png" width="100" height="100"  loading="lazy"></a><br class="spacer">バイトツナギ ニシキ</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×150</td></tr><tr><td style="text-align:center;">(画像待ち)<br class="spacer">バイトウェーダー ベリー</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×150</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%82%B7%E3%83%AB%E3%83%90%E3%83%BC.jpg?rev=a798eaf82dc6794c2df6f76a8d93000e&amp;t=20250408101521" title="バイトツナギシルバー.jpg" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%82%B7%E3%83%AB%E3%83%90%E3%83%BC.jpg?rev=a798eaf82dc6794c2df6f76a8d93000e&amp;t=20250408101521" alt="バイトツナギシルバー.jpg" title="バイトツナギシルバー.jpg" width="100" height="100"  loading="lazy"></a><br class="spacer">バイトツナギシルバー</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×150</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%82%B4%E3%83%BC%E3%83%AB%E3%83%89.png?rev=9e88c37e07e820bbef420e64a5a04e0e&amp;t=20250408101546" title="バイトツナギゴールド.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%82%B4%E3%83%BC%E3%83%AB%E3%83%89.png?rev=9e88c37e07e820bbef420e64a5a04e0e&amp;t=20250408101546" alt="バイトツナギゴールド.png" title="バイトツナギゴールド.png" width="100" height="100"  loading="lazy"></a><br class="spacer">バイトツナギゴールド</td><td><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20250408102131" title="銀のウロコ.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20250408102131" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy"></a>×150</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%83%97%E3%83%AA%E3%82%BA%E3%83%A0.png?rev=eec5f015b5166a032f9895771061ba3c&amp;t=20250408101608" title="バイトツナギプリズム.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%83%90%E3%82%A4%E3%83%88%E3%83%84%E3%83%8A%E3%82%AE%E3%83%97%E3%83%AA%E3%82%BA%E3%83%A0.png?rev=eec5f015b5166a032f9895771061ba3c&amp;t=20250408101608" alt="バイトツナギプリズム.png" title="バイトツナギプリズム.png" width="100" height="100"  loading="lazy"></a><br class="spacer">バイトツナギプリズム</td><td><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3_0.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20250408102149" title="銀のウロコ_0.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3_0.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20250408102149" alt="銀のウロコ_0.png" title="銀のウロコ_0.png" width="16" height="16"  loading="lazy"></a>×150</td></tr><tr><th colspan="3"><a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a></th></tr><tr><td style="text-align:center;">(画像待ち)<br class="spacer">ガーディアンアーミーハット</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×100</td><td rowspan="7">最初から</td></tr><tr><td style="text-align:center;"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%AE%E3%82%A2%E3%83%AA%E3%82%B9%E3%83%88/::ref/%E3%82%A2%E3%82%BB%E3%82%B9%E3%83%88%E3%83%83%E3%83%97%E3%82%BD%E3%82%B7%E3%83%8A.png.webp?rev=e9d64867a7ac581d14f7095cf561911e&amp;t=20240320103514" alt="アセストップソシナ.png" title="アセストップソシナ.png" width="75" height="75"  loading="lazy"><br class="spacer">アセストップソシナ</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×100</td></tr><tr><td style="text-align:center;"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%AE%E3%82%A2%E3%83%AA%E3%82%B9%E3%83%88/::ref/%E3%82%A4%E3%82%AB%E3%83%86%E3%83%B3%E3%81%8F%E3%82%93%E3%83%9D%E3%83%AD.png.webp?rev=51d136c17ea40de9651fe63b365e2a23&amp;t=20230401170028" alt="イカテンくんポロ.png" title="イカテンくんポロ.png" width="75" height="75"  loading="lazy"><br class="spacer">イカテンくんポロ</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×100</td></tr><tr><td style="text-align:center;"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%AE%E3%82%A2%E3%83%AA%E3%82%B9%E3%83%88/::ref/%E3%82%A2%E3%82%B2%E3%82%A2%E3%82%B2%E3%83%BB%E3%83%86%E3%83%B3%E3%83%BB%E3%83%97%E3%83%A9%E3%83%BCXXL.png.webp?rev=65cf2dd46675684eba6affd522b6664a&amp;t=20240320193159" alt="アゲアゲ・テン・プラーXXL.png" title="アゲアゲ・テン・プラーXXL.png" width="75" height="75"  loading="lazy"><br class="spacer">アゲアゲ・テン・プラーXXL</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×100</td></tr><tr><td style="text-align:center;"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%AE%E3%82%A2%E3%83%AA%E3%82%B9%E3%83%88/::ref/%E3%83%9E%E3%83%83%E3%83%89%E3%83%A9%E3%83%90%E3%83%BC.png.webp?rev=8066f344b0aa8829d5b11e5638a5925e&amp;t=20230401173235" alt="マッドラバー.png" title="マッドラバー.png" width="75" height="75"  loading="lazy"><br class="spacer">マッドラバー</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×15</td></tr><tr><td style="text-align:center;"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%AE%E3%82%A2%E3%83%AA%E3%82%B9%E3%83%88/::ref/%E3%83%8E%E3%83%B3%E3%82%B9%E3%83%AA%E3%83%83%E3%83%97%E3%82%BF%E3%82%AF%E3%83%9F.png.webp?rev=6e36a3a1927a7881491b9d2968d8adb0&amp;t=20240320193204" alt="ノンスリップタクミ.png" title="ノンスリップタクミ.png" width="75" height="75"  loading="lazy"><br class="spacer">ノンスリップタクミ</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×15</td></tr><tr><td style="text-align:center;">(画像待ち)<br class="spacer">バンカラコロン</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×15</td></tr><tr><td style="text-align:center;"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%AE%E3%82%A2%E3%83%AA%E3%82%B9%E3%83%88/::ref/%E3%83%98%E3%83%83%E3%83%89%E3%83%A9%E3%82%A4%E3%83%88%E3%83%98%E3%83%AB%E3%83%A0.png.webp?rev=14384a1ee38befcc18848201070a586d&amp;t=20230401154033" alt="ヘッドライトヘルム.png" title="ヘッドライトヘルム.png" width="75" height="75"  loading="lazy"><br class="spacer">ヘッドライトヘルム</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×300</td><td rowspan="8">ランク1</td></tr><tr><td style="text-align:center;">(画像待ち)<br class="spacer">フロムキクダニ87</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×300</td></tr><tr><td style="text-align:center;">(画像待ち)<br class="spacer">ジムパーソンアーマー</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×300</td></tr><tr><td style="text-align:center;"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%AE%E3%82%A2%E3%83%AA%E3%82%B9%E3%83%88/::ref/%E3%82%B2%E3%82%BD%E3%83%90%E3%82%BF%E3%82%A2%E3%82%B7%E3%82%B9%E3%83%88.png.webp?rev=6da92d2408fb6083053e70fe7a9518e9&amp;t=20231001143841" alt="ゲソバタアシスト.png" title="ゲソバタアシスト.png" width="75" height="75"  loading="lazy"><br class="spacer">ゲソバタアシスト</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×300</td></tr><tr><td style="text-align:center;"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%AE%E3%82%A2%E3%83%AA%E3%82%B9%E3%83%88/::ref/%E3%82%A2%E3%83%B3%E3%82%AB%E3%83%BC%E3%83%99%E3%82%B9%E3%83%88.png.webp?rev=275ead925e4eeb015ec3c4ee78a6d605&amp;t=20230401165645" alt="アンカーベスト.png" title="アンカーベスト.png" width="75" height="75"  loading="lazy"><br class="spacer">アンカーベスト</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×5</td></tr><tr><td style="text-align:center;"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%AE%E3%82%A2%E3%83%AA%E3%82%B9%E3%83%88/::ref/%E3%83%9E%E3%82%AF%E3%83%ACGT.png.webp?rev=d5c4e8dc54e11622bc4068f5e2889ecc&amp;t=20240320193208" alt="マクレGT.png" title="マクレGT.png" width="75" height="75"  loading="lazy"><br class="spacer">マクレGT</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×5</td></tr><tr><td style="text-align:center;"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%AE%E3%82%A2%E3%83%AA%E3%82%B9%E3%83%88/::ref/%E3%83%87%E3%83%99%E3%83%AD%E3%83%83%E3%83%91%E3%83%BC%E3%82%BA%E3%83%AF%E3%83%BC%E3%82%AF%E3%82%A6%E3%82%A7%E3%82%A2.png.webp?rev=53c69847aeeeb48fd645d7ef214696fc&amp;t=20240320104620" alt="デベロッパーズワークウェア.png" title="デベロッパーズワークウェア.png" width="75" height="75"  loading="lazy"><br class="spacer">デベロッパーズワークウェア</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×5</td></tr><tr><td style="text-align:center;">(画像待ち)<br class="spacer">チギリノヒモ</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×5</td></tr><tr><td style="text-align:center;"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%AE%E3%82%A2%E3%83%AA%E3%82%B9%E3%83%88/::ref/%E3%83%80%E3%82%B9%E3%83%88%E3%83%96%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC%202.5.png.webp?rev=e4cfcd030d10864b3f2b7c3c85ed26ec&amp;t=20230401153941" alt="ダストブロッカー 2.5.png" title="ダストブロッカー 2.5.png" width="75" height="75"  loading="lazy"><br class="spacer">ダストブ<a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC" title="ロッカー" class="rel-wiki-page">ロッカー</a> 2.5</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×800</td><td rowspan="10">ランク2</td></tr><tr><td style="text-align:center;"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%AE%E3%82%A2%E3%83%AA%E3%82%B9%E3%83%88/::ref/%E3%82%A2%E3%82%A4%E3%82%A2%E3%83%B3%E3%83%9E%E3%82%B9%E3%82%AB%E3%83%AC%E3%82%A4%E3%83%89.png.webp?rev=a3a834314e4e7df43f6bc83ad7d43d4f&amp;t=20231001143710" alt="アイアンマスカレイド.png" title="アイアンマスカレイド.png" width="75" height="75"  loading="lazy"><br class="spacer">アイアンマスカレイド</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×800</td></tr><tr><td style="text-align:center;"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%AE%E3%82%A2%E3%83%AA%E3%82%B9%E3%83%88/::ref/%E3%82%BE%E3%83%8D%E3%82%B9%E3%83%86%E3%82%A3%E3%83%83%E3%82%AF%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%97.png.webp?rev=0b144cd07d17a1f819994b5031bf31c4&amp;t=20240320103551" alt="ゾネスティックスコープ.png" title="ゾネスティックスコープ.png" width="75" height="75"  loading="lazy"><br class="spacer">ゾネスティックスコープ</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×800</td></tr><tr><td style="text-align:center;">(画像待ち)<br class="spacer">マリリンハットウィズピンズ</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×800</td></tr><tr><td style="text-align:center;"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%AE%E3%82%A2%E3%83%AA%E3%82%B9%E3%83%88/::ref/%E3%82%BE%E3%83%8D%E3%82%B9%E3%83%86%E3%82%A3%E3%83%83%E3%82%AF%E3%83%97%E3%83%AD%E3%83%86%E3%82%AF%E3%82%BF%E3%83%BC.png.webp?rev=fafde2bcca34d7916fbcfb0522ea5c52&amp;t=20240320103557" alt="ゾネスティックプロテクター.png" title="ゾネスティックプロテクター.png" width="75" height="75"  loading="lazy"><br class="spacer">ゾネスティックプロテクター</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×800</td></tr><tr><td style="text-align:center;">(画像待ち)<br class="spacer">アカシックコート</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×800</td></tr><tr><td style="text-align:center;"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%AE%E3%82%A2%E3%83%AA%E3%82%B9%E3%83%88/::ref/%E3%82%BE%E3%83%8D%E3%82%B9%E3%83%86%E3%82%A3%E3%83%83%E3%82%AF%E3%83%96%E3%83%BC%E3%83%84.png.webp?rev=86ef599342f00caa7bdd099a6deaf804&amp;t=20240320103604" alt="ゾネスティックブーツ.png" title="ゾネスティックブーツ.png" width="75" height="75"  loading="lazy"><br class="spacer">ゾネスティックブーツ</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×800</td></tr><tr><td style="text-align:center;"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%AE%E3%82%A2%E3%83%AA%E3%82%B9%E3%83%88/::ref/%E3%83%AC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%89%E3%81%AE%E3%81%BC%E3%81%86%E3%81%97.png.webp?rev=7ff51a454391f29f2bc4733e3a7fc8bd&amp;t=20231001143702" alt="レジェンドのぼうし.png" title="レジェンドのぼうし.png" width="75" height="75"  loading="lazy"><br class="spacer">レジェンドのぼうし</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×30</td></tr><tr><td style="text-align:center;">(画像待ち)<br class="spacer">スペボウ レプリカ</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×30</td></tr><tr><td style="text-align:center;"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%AE%E3%82%A2%E3%83%AA%E3%82%B9%E3%83%88/::ref/%E3%83%95%E3%83%A5%E3%83%BC%E3%82%A8%E3%83%AB%E3%83%96%E3%83%AB%E3%82%BE%E3%83%B3.png.webp?rev=2d72e2b730c67d846ea7dfcd80804fa5&amp;t=20230401165839" alt="フューエルブルゾン.png" title="フューエルブルゾン.png" width="75" height="75"  loading="lazy"><br class="spacer">フューエルブルゾン</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×30</td></tr><tr><th colspan="3"><a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E" title="ロッカー/オキモノ" class="rel-wiki-page">オキモノ</a></th></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%83%80%E3%82%A4%E3%83%90%E3%83%BC.png?rev=57166e4030eca8a4c61c12eb783634ee&amp;t=20231001141127" title="オキモノ_ダイバー.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%83%80%E3%82%A4%E3%83%90%E3%83%BC.png?rev=57166e4030eca8a4c61c12eb783634ee&amp;t=20231001141127" alt="オキモノ_ダイバー.png" title="オキモノ_ダイバー.png" width="128" height="128"  loading="lazy"></a><br class="spacer"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%80%E3%82%A4%E3%83%90%E3%83%BC" title="サーモンラン/シャケの種類/ダイバー" class="rel-wiki-page">ダイバー</a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×50</td><td rowspan="7">最初から</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%83%86%E3%83%83%E3%83%91%E3%83%B3.png?rev=6fa96d535a7ce6afadae08e4e3fbdb76&amp;t=20220920183834" title="オキモノ_テッパン.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%83%86%E3%83%83%E3%83%91%E3%83%B3.png?rev=6fa96d535a7ce6afadae08e4e3fbdb76&amp;t=20220920183834" alt="オキモノ_テッパン.png" title="オキモノ_テッパン.png" width="128" height="128"  loading="lazy"></a><br class="spacer"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×80</td></tr><tr><td style="text-align:center;">(画像待ち)<br class="spacer"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B3%E3%83%93%E3%83%A4%E3%81%9F%E3%81%A1#chinooks" title="サーモンラン/シャケの種類/ハコビヤたち" class="rel-wiki-page">シャケコプター</a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×5</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3.png?rev=1c30b0656f6289e7c2cd9b24e7597756&amp;t=20220920183930" title="オキモノ_バクダン.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3.png.webp?rev=1c30b0656f6289e7c2cd9b24e7597756&amp;t=20220920183930" alt="オキモノ_バクダン.png" title="オキモノ_バクダン.png" width="128" height="128"  loading="lazy"></a><br class="spacer"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×5</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%81%AF%E3%81%93%E3%81%A5%E3%82%81%E9%87%91%E3%82%A4%E3%82%AF%E3%83%A9.png?rev=3ccfaa4d0da6db89bb0ce90b0d185667&amp;t=20231001141136" title="オキモノ_はこづめ金イクラ.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%81%AF%E3%81%93%E3%81%A5%E3%82%81%E9%87%91%E3%82%A4%E3%82%AF%E3%83%A9.png.webp?rev=3ccfaa4d0da6db89bb0ce90b0d185667&amp;t=20231001141136" alt="オキモノ_はこづめ金イクラ.png" title="オキモノ_はこづめ金イクラ.png" width="128" height="128"  loading="lazy"></a><br class="spacer">はこづめ金イクラ</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×1</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%82%B3%E3%82%B8%E3%83%A3%E3%82%B1.png?rev=ba4bb792336bfee1ea690f9a9de3a97f&amp;t=20220920183944" title="オキモノ_コジャケ.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%82%B3%E3%82%B8%E3%83%A3%E3%82%B1.png?rev=ba4bb792336bfee1ea690f9a9de3a97f&amp;t=20220920183944" alt="オキモノ_コジャケ.png" title="オキモノ_コジャケ.png" width="128" height="128"  loading="lazy"></a><br class="spacer"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×1</td></tr><tr><td style="text-align:center;">(画像待ち)<br class="spacer">シャケの<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×1</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%83%8F%E3%82%B7%E3%83%A9.png?rev=334151b7fdd2b9f3b210fe2eb728b6f6&amp;t=20231001141146" title="オキモノ_ハシラ.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%83%8F%E3%82%B7%E3%83%A9.png?rev=334151b7fdd2b9f3b210fe2eb728b6f6&amp;t=20231001141146" alt="オキモノ_ハシラ.png" title="オキモノ_ハシラ.png" width="128" height="128"  loading="lazy"></a><br class="spacer"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×120</td><td rowspan="7">ランク1</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%83%A2%E3%82%B0%E3%83%A9.png?rev=a3f29019da5a16c5537fc85aaafcba1b&amp;t=20220920183958" title="オキモノ_モグラ.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%83%A2%E3%82%B0%E3%83%A9.png.webp?rev=a3f29019da5a16c5537fc85aaafcba1b&amp;t=20220920183958" alt="オキモノ_モグラ.png" title="オキモノ_モグラ.png" width="128" height="128"  loading="lazy"></a><br class="spacer"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%A2%E3%82%B0%E3%83%A9" title="サーモンラン/シャケの種類/モグラ" class="rel-wiki-page">モグラ</a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×160</td></tr><tr><td style="text-align:center;">(画像待ち)<br class="spacer"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B3%E3%83%93%E3%83%A4%E3%81%9F%E3%81%A1#mothership" title="サーモンラン/シャケの種類/ハコビヤたち" class="rel-wiki-page">ハコビヤ</a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×20</td></tr><tr><td style="text-align:center;">(画像待ち)<br class="spacer"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%89%E3%83%AD%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ドロシャケ" class="rel-wiki-page">ドロシャケ</a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×20</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%82%BF%E3%83%AF%E3%83%BC.png?rev=6cacaf5e0b1375205465cf7bd4ed0a9c&amp;t=20220920184013" title="オキモノ_タワー.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%82%BF%E3%83%AF%E3%83%BC.png?rev=6cacaf5e0b1375205465cf7bd4ed0a9c&amp;t=20220920184013" alt="オキモノ_タワー.png" title="オキモノ_タワー.png" width="128" height="128"  loading="lazy"></a><br class="spacer"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×20</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%82%B7%E3%83%A3%E3%82%B1.png?rev=589466f01b82c0816b99bebeccb96353&amp;t=20220920184028" title="オキモノ_シャケ.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%82%B7%E3%83%A3%E3%82%B1.png?rev=589466f01b82c0816b99bebeccb96353&amp;t=20220920184028" alt="オキモノ_シャケ.png" title="オキモノ_シャケ.png" width="128" height="128"  loading="lazy"></a><br class="spacer">シャケ</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×4</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%82%BF%E3%83%9E%E3%83%92%E3%83%AD%E3%82%A4.png?rev=ac6c3c37133ab02492101ed60588a568&amp;t=20231001141157" title="オキモノ_タマヒロイ.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%82%BF%E3%83%9E%E3%83%92%E3%83%AD%E3%82%A4.png?rev=ac6c3c37133ab02492101ed60588a568&amp;t=20231001141157" alt="オキモノ_タマヒロイ.png" title="オキモノ_タマヒロイ.png" width="128" height="128"  loading="lazy"></a><br class="spacer"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#snatcher" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">タマヒロイ</a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×5</td></tr><tr><td style="text-align:center;">(画像待ち)<br class="spacer"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×320</td><td rowspan="10">ランク2</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA.png?rev=0d16e3b9b89a9f164a2ee6a9f47989de&amp;t=20220920184103" title="オキモノ_コウモリ.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA.png?rev=0d16e3b9b89a9f164a2ee6a9f47989de&amp;t=20220920184103" alt="オキモノ_コウモリ.png" title="オキモノ_コウモリ.png" width="128" height="128"  loading="lazy"></a><br class="spacer"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA" title="サーモンラン/シャケの種類/コウモリ" class="rel-wiki-page">コウモリ</a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×320</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF.png?rev=0deddf6f2f2988f108ee19579cfd3b1d&amp;t=20231001141204" title="オキモノ_ナベブタ.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF.png?rev=0deddf6f2f2988f108ee19579cfd3b1d&amp;t=20231001141204" alt="オキモノ_ナベブタ.png" title="オキモノ_ナベブタ.png" width="128" height="128"  loading="lazy"></a><br class="spacer"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×320</td></tr><tr><td style="text-align:center;">(画像待ち)<br class="spacer">クマサンのレプリカ ウッド</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×999</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89.png?rev=b2edc50fcf33b64fb6246fd713cbeac6&amp;t=20220920184117" title="オキモノ_カタパッド.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89.png?rev=b2edc50fcf33b64fb6246fd713cbeac6&amp;t=20220920184117" alt="オキモノ_カタパッド.png" title="オキモノ_カタパッド.png" width="128" height="128"  loading="lazy"></a><br class="spacer"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×80</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%83%86%E3%83%83%E3%82%AD%E3%83%A5%E3%82%A6.png?rev=a386362e57d36b117f87b8592deb15e5&amp;t=20231001141212" title="オキモノ_テッキュウ.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%83%86%E3%83%83%E3%82%AD%E3%83%A5%E3%82%A6.png?rev=a386362e57d36b117f87b8592deb15e5&amp;t=20231001141212" alt="オキモノ_テッキュウ.png" title="オキモノ_テッキュウ.png" width="128" height="128"  loading="lazy"></a><br class="spacer"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%82%AD%E3%83%A5%E3%82%A6" title="サーモンラン/シャケの種類/テッキュウ" class="rel-wiki-page">テッキュウ</a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×120</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%83%89%E3%82%B9%E3%82%B3%E3%82%A4.png?rev=9846bb8a7c9772abcb63c5483bed9e47&amp;t=20220920184135" title="オキモノ_ドスコイ.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%83%89%E3%82%B9%E3%82%B3%E3%82%A4.png?rev=9846bb8a7c9772abcb63c5483bed9e47&amp;t=20220920184135" alt="オキモノ_ドスコイ.png" title="オキモノ_ドスコイ.png" width="128" height="128"  loading="lazy"></a><br class="spacer"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#cohock" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ドスコイ</a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×15</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%83%98%E3%83%93.png?rev=5ff2444b0007dcb6ba2e7576b85a5d02&amp;t=20220920184205" title="オキモノ_ヘビ.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%83%98%E3%83%93.png?rev=5ff2444b0007dcb6ba2e7576b85a5d02&amp;t=20220920184205" alt="オキモノ_ヘビ.png" title="オキモノ_ヘビ.png" width="128" height="128"  loading="lazy"></a><br class="spacer"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×15</td></tr><tr><td style="text-align:center;">(画像待ち)<br class="spacer">イクラコンテナ</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×15</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::attach/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1.png?rev=5498c6bbd58fa367af722fccbd94f0bb&amp;t=20220920184218" title="オキモノ_キンシャケ.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/::ref/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E_%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1.png?rev=5498c6bbd58fa367af722fccbd94f0bb&amp;t=20220920184218" alt="オキモノ_キンシャケ.png" title="オキモノ_キンシャケ.png" width="128" height="128"  loading="lazy"></a><br class="spacer"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/キンシャケ" class="rel-wiki-page">キンシャケ</a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×100</td></tr><tr><th colspan="3"><a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/%E3%82%B9%E3%83%86%E3%83%83%E3%82%AB%E3%83%BC" title="ロッカー/ステッカー" class="rel-wiki-page">ステッカー</a></th></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SK-MTG</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×15</td><td rowspan="12">最初から</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SK-SKF</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×30</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">ひょうしき SR-IRC</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×30</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer"><a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/%E3%82%B9%E3%83%86%E3%83%83%E3%82%AB%E3%83%BC" title="ロッカー/ステッカー" class="rel-wiki-page">ステッカー</a> KS-OFM</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×30</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SK-KIS</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×50</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">ポスター KS-TAB</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×50</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">ひょうしき SR-ROK</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×50</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">ネオン KS-TGY</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×3</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SK-TMA</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×3</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SG-SHT</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×3</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">ロゴ クマサンしょうかい</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×1</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SG-UMK</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×2</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SK-TWD</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×60</td><td rowspan="13">ランク1</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SK-DSK</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×80</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SK-KBT</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×80</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SG-TWS</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×80</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer"><a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/%E3%82%B9%E3%83%86%E3%83%83%E3%82%AB%E3%83%BC" title="ロッカー/ステッカー" class="rel-wiki-page">ステッカー</a> KS-OSK</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×80</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SK-BKD</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×5</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SK-HBN</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×5</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SK-ZMN</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×5</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SK-HKG</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×5</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SK-KRS</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×5</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">ネオン KS-FSY</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×10</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">ひょうしき SR-GKN</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×10</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">ポスター KS-MDK</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×3</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SK-UZU</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×160</td><td rowspan="15">ランク2</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SK-KZK</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×160</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SK-OOG</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×160</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SK-ITS</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×160</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">ポスター SK-SNB</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×160</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">ポスター KS-BAB</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×160</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">ポスター KS-SYK</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×160</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">ネオン KS-SHK</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×25</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">ひょうしき SR-NST</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×25</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">ネオン KS-OOZ</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×50</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SK-KRM</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×50</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SG-AHT</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×50</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SK-MGR</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×10</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SK-TOG</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×10</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::attach/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" title="クマサン台詞.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8F%B0%E8%A9%9E.png.webp?rev=c629dc53df0ce823e06edebea60d66b1&amp;t=20230512182206" alt="クマサン台詞.png" title="クマサン台詞.png" width="50" height="50"  loading="lazy"></a><br class="spacer">グラフィティ SK-YDN</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×10</td></tr><tr><th colspan="3"><a href="/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88" title="ネームプレート/プレート" class="rel-wiki-page">プレート</a></th></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::attach/Sg-image-splatoon-3-banner-07.jpg?rev=4d4072cadcd4d6a406715118fe0cdbce&amp;t=20220916235234" title="Sg-image-splatoon-3-banner-07.jpg" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::ref/Sg-image-splatoon-3-banner-07.jpg?rev=4d4072cadcd4d6a406715118fe0cdbce&amp;t=20220916235234" alt="Sg-image-splatoon-3-banner-07.jpg" title="Sg-image-splatoon-3-banner-07.jpg" width="350" height="100"  loading="lazy"></a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×10</td><td rowspan="6">最初から</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::attach/S3_Banner_2101.png?rev=77c17013787b92b46a041e9b535e71c5&amp;t=20230425140258" title="S3_Banner_2101.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::ref/S3_Banner_2101.png?rev=77c17013787b92b46a041e9b535e71c5&amp;t=20230425140258" alt="S3_Banner_2101.png" title="S3_Banner_2101.png" width="350" height="100"  loading="lazy"></a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×60</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::attach/Sg-image-splatoon-3-banner-08.jpg?rev=6ec14c062ea7138c2acfdcd01d915460&amp;t=20220916235239" title="Sg-image-splatoon-3-banner-08.jpg" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::ref/Sg-image-splatoon-3-banner-08.jpg?rev=6ec14c062ea7138c2acfdcd01d915460&amp;t=20220916235239" alt="Sg-image-splatoon-3-banner-08.jpg" title="Sg-image-splatoon-3-banner-08.jpg" width="350" height="100"  loading="lazy"></a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×100</td></tr><tr><td style="text-align:center;">(画像待ち)</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×100</td></tr><tr><td style="text-align:center;">(画像待ち)</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×100</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::attach/Sg-image-splatoon-3-banner-09.jpg?rev=06a6d6980f2a5126ae02fdf769d35354&amp;t=20220916235242" title="Sg-image-splatoon-3-banner-09.jpg" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::ref/Sg-image-splatoon-3-banner-09.jpg?rev=06a6d6980f2a5126ae02fdf769d35354&amp;t=20220916235242" alt="Sg-image-splatoon-3-banner-09.jpg" title="Sg-image-splatoon-3-banner-09.jpg" width="350" height="100"  loading="lazy"></a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×2</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::attach/S3_Banner_2104.png?rev=24feabda82f3643b0a97604388223d57&amp;t=20230425140319" title="S3_Banner_2104.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::ref/S3_Banner_2104.png.webp?rev=24feabda82f3643b0a97604388223d57&amp;t=20230425140319" alt="S3_Banner_2104.png" title="S3_Banner_2104.png" width="350" height="100"  loading="lazy"></a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×150</td><td rowspan="8">ランク1</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::attach/S3_Banner_2201.png?rev=16d64d7f017cacfbaab0a38bbc3300b3&amp;t=20231001145624" title="S3_Banner_2201.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::ref/S3_Banner_2201.png.webp?rev=16d64d7f017cacfbaab0a38bbc3300b3&amp;t=20231001145624" alt="S3_Banner_2201.png" title="S3_Banner_2201.png" width="350" height="100"  loading="lazy"></a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×150</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::attach/Sg-image-splatoon-3-banner-21.jpg?rev=40ecb322d08a0ddb8983565c5ce1aeaa&amp;t=20220916235246" title="Sg-image-splatoon-3-banner-21.jpg" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::ref/Sg-image-splatoon-3-banner-21.jpg?rev=40ecb322d08a0ddb8983565c5ce1aeaa&amp;t=20220916235246" alt="Sg-image-splatoon-3-banner-21.jpg" title="Sg-image-splatoon-3-banner-21.jpg" width="350" height="100"  loading="lazy"></a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×250</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::attach/Sg-image-splatoon-3-banner-22.jpg?rev=021bf081544026e4dcab2863cda6ab34&amp;t=20220916235250" title="Sg-image-splatoon-3-banner-22.jpg" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::ref/Sg-image-splatoon-3-banner-22.jpg?rev=021bf081544026e4dcab2863cda6ab34&amp;t=20220916235250" alt="Sg-image-splatoon-3-banner-22.jpg" title="Sg-image-splatoon-3-banner-22.jpg" width="350" height="100"  loading="lazy"></a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×250</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::attach/S3_Banner_2204.png?rev=feff9fd5df4c05c61b6aa4cfb9933141&amp;t=20231001145639" title="S3_Banner_2204.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::ref/S3_Banner_2204.png.webp?rev=feff9fd5df4c05c61b6aa4cfb9933141&amp;t=20231001145639" alt="S3_Banner_2204.png" title="S3_Banner_2204.png" width="350" height="100"  loading="lazy"></a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×250</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::attach/Sg-image-splatoon-3-banner-25.jpg?rev=b6fb03b2616ff62e7b61769b9211224b&amp;t=20220916235307" title="Sg-image-splatoon-3-banner-25.jpg" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::ref/Sg-image-splatoon-3-banner-25.jpg?rev=b6fb03b2616ff62e7b61769b9211224b&amp;t=20220916235307" alt="Sg-image-splatoon-3-banner-25.jpg" title="Sg-image-splatoon-3-banner-25.jpg" width="350" height="100"  loading="lazy"></a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×5</td></tr><tr><td style="text-align:center;">(画像待ち)</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×5</td></tr><tr><td style="text-align:center;">(画像待ち)</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×5</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::attach/S3_Banner_2102.png?rev=09b5b2558b314e178e443a4662c5413d&amp;t=20230425140333" title="S3_Banner_2102.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::ref/S3_Banner_2102.png.webp?rev=09b5b2558b314e178e443a4662c5413d&amp;t=20230425140333" alt="S3_Banner_2102.png" title="S3_Banner_2102.png" width="350" height="100"  loading="lazy"></a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×400</td><td rowspan="12">ランク2</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::attach/Sg-image-splatoon-3-banner-23.jpg?rev=c9fddd6403879a619c627bf1fafe42f7&amp;t=20220916235254" title="Sg-image-splatoon-3-banner-23.jpg" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::ref/Sg-image-splatoon-3-banner-23.jpg?rev=c9fddd6403879a619c627bf1fafe42f7&amp;t=20220916235254" alt="Sg-image-splatoon-3-banner-23.jpg" title="Sg-image-splatoon-3-banner-23.jpg" width="350" height="100"  loading="lazy"></a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×600</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::attach/Sg-image-splatoon-3-banner-24.jpg?rev=c8f4d0df071fdbd4ebfbdbadf73ae428&amp;t=20220916235301" title="Sg-image-splatoon-3-banner-24.jpg" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::ref/Sg-image-splatoon-3-banner-24.jpg?rev=c8f4d0df071fdbd4ebfbdbadf73ae428&amp;t=20220916235301" alt="Sg-image-splatoon-3-banner-24.jpg" title="Sg-image-splatoon-3-banner-24.jpg" width="350" height="100"  loading="lazy"></a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×600</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::attach/S3_Banner_2203.png?rev=a01bd9a1200ac21144212170bd02582f&amp;t=20231001145649" title="S3_Banner_2203.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::ref/S3_Banner_2203.png.webp?rev=a01bd9a1200ac21144212170bd02582f&amp;t=20231001145649" alt="S3_Banner_2203.png" title="S3_Banner_2203.png" width="350" height="100"  loading="lazy"></a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×800</td></tr><tr><td style="text-align:center;">(画像待ち)</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×800</td></tr><tr><td style="text-align:center;">(画像待ち)</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%85%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5d6a254f4d944232376ec9671151380f&amp;t=20230203114744" alt="銅のウロコ.png" title="銅のウロコ.png" width="16" height="16"  loading="lazy">×800</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::attach/Sg-image-splatoon-3-banner-27.jpg?rev=eec2d6c005c0c31f2669173cc39069de&amp;t=20220916235313" title="Sg-image-splatoon-3-banner-27.jpg" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::ref/Sg-image-splatoon-3-banner-27.jpg?rev=eec2d6c005c0c31f2669173cc39069de&amp;t=20220916235313" alt="Sg-image-splatoon-3-banner-27.jpg" title="Sg-image-splatoon-3-banner-27.jpg" width="350" height="100"  loading="lazy"></a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%8A%80%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=ad19fe8fc28c236c03c7f6e04f8a9475&amp;t=20230203114740" alt="銀のウロコ.png" title="銀のウロコ.png" width="16" height="16"  loading="lazy">×999</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::attach/Sg-image-splatoon-3-banner-26.jpg?rev=d263a80e344a85a29e8a7f30aecd3105&amp;t=20220916235310" title="Sg-image-splatoon-3-banner-26.jpg" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::ref/Sg-image-splatoon-3-banner-26.jpg?rev=d263a80e344a85a29e8a7f30aecd3105&amp;t=20220916235310" alt="Sg-image-splatoon-3-banner-26.jpg" title="Sg-image-splatoon-3-banner-26.jpg" width="350" height="100"  loading="lazy"></a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×20</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::attach/S3_Banner_2202.png?rev=87831f6c0d84b3f0936d7edf4e2c9d9d&amp;t=20231001145654" title="S3_Banner_2202.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::ref/S3_Banner_2202.png?rev=87831f6c0d84b3f0936d7edf4e2c9d9d&amp;t=20231001145654" alt="S3_Banner_2202.png" title="S3_Banner_2202.png" width="350" height="100"  loading="lazy"></a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×33</td></tr><tr><td style="text-align:center;"><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::attach/S3_Banner_2103.png?rev=c62fe281233180247647bb2bb66383d6&amp;t=20230425140345" title="S3_Banner_2103.png" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/::ref/S3_Banner_2103.png.webp?rev=c62fe281233180247647bb2bb66383d6&amp;t=20230425140345" alt="S3_Banner_2103.png" title="S3_Banner_2103.png" width="350" height="100"  loading="lazy"></a></td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×333</td></tr><tr><td style="text-align:center;">(画像待ち)</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×333</td></tr><tr><td style="text-align:center;">(画像待ち)</td><td><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/icon/::ref/%E9%87%91%E3%81%AE%E3%82%A6%E3%83%AD%E3%82%B3.png?rev=5877f38e04c909e757d9a4b062fbe85b&amp;t=20230203114737" alt="金のウロコ.png" title="金のウロコ.png" width="16" height="16"  loading="lazy">×333</td></tr></tbody></table></div>
</div>
</div>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">全ての限定品を交換するのに必要なウロコ数</div>
    <div class="fold-content visible-on-open"><p>ver.10.0.0での情報。</p>
<p><strong>全ての作業着を交換する場合</strong><br />
<span class="wikicolor" style="color:dimgray">銀</span>のウロコ が<span class="wikicolor" style="color:dimgray">1270</span>個 必要。</p>
<p><strong>全ての<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>を交換する場合</strong><br />
<span class="wikicolor" style="color:brown">銅</span>/<span class="wikicolor" style="color:dimgray">銀</span>/<span class="wikicolor" style="color:darkgoldenrod">金</span>のウロコ が <span class="wikicolor" style="color:brown">5200</span>/<span class="wikicolor" style="color:dimgray">30</span>/<span class="wikicolor" style="color:darkgoldenrod">75</span> 個 必要。</p>
<p><strong>全ての<a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E" title="ロッカー/オキモノ" class="rel-wiki-page">オキモノ</a>を1つずつ交換する場合</strong><br />
<span class="wikicolor" style="color:brown">銅</span>/<span class="wikicolor" style="color:dimgray">銀</span>/<span class="wikicolor" style="color:darkgoldenrod">金</span>のウロコ が <span class="wikicolor" style="color:brown">1370</span>/<span class="wikicolor" style="color:dimgray">250</span>/<span class="wikicolor" style="color:darkgoldenrod">140</span> 個 必要。<br />
<strong>全ての<a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E" title="ロッカー/オキモノ" class="rel-wiki-page">オキモノ</a>を上限(10個)まで交換する場合</strong><br />
<span class="wikicolor" style="color:brown">銅</span>/<span class="wikicolor" style="color:dimgray">銀</span>/<span class="wikicolor" style="color:darkgoldenrod">金</span>のウロコ が <span class="wikicolor" style="color:brown">13700</span>/<span class="wikicolor" style="color:dimgray">2500</span>/<span class="wikicolor" style="color:darkgoldenrod">1400</span> 個 必要。</p>
<p><strong>全ての<a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/%E3%82%B9%E3%83%86%E3%83%83%E3%82%AB%E3%83%BC" title="ロッカー/ステッカー" class="rel-wiki-page">ステッカー</a>を1つずつ交換する場合</strong><br />
<span class="wikicolor" style="color:brown">銅</span>/<span class="wikicolor" style="color:dimgray">銀</span>/<span class="wikicolor" style="color:darkgoldenrod">金</span>のウロコ が <span class="wikicolor" style="color:brown">1515</span>/<span class="wikicolor" style="color:dimgray">246</span>/<span class="wikicolor" style="color:darkgoldenrod">26</span> 個 必要。<br />
<strong>全ての<a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/%E3%82%B9%E3%83%86%E3%83%83%E3%82%AB%E3%83%BC" title="ロッカー/ステッカー" class="rel-wiki-page">ステッカー</a>を上限(10個)まで交換する場合</strong><br />
<span class="wikicolor" style="color:brown">銅</span>/<span class="wikicolor" style="color:dimgray">銀</span>/<span class="wikicolor" style="color:darkgoldenrod">金</span>のウロコ が <span class="wikicolor" style="color:brown">15150</span>/<span class="wikicolor" style="color:dimgray">2460</span>/<span class="wikicolor" style="color:darkgoldenrod">260</span> 個 必要。</p>
<p><strong>全ての<a href="/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88" title="ネームプレート/プレート" class="rel-wiki-page">プレート</a>を交換する場合</strong><br />
<span class="wikicolor" style="color:brown">銅</span>/<span class="wikicolor" style="color:dimgray">銀</span>/<span class="wikicolor" style="color:darkgoldenrod">金</span>のウロコ が <span class="wikicolor" style="color:brown">4520</span>/<span class="wikicolor" style="color:dimgray">999</span>/<span class="wikicolor" style="color:darkgoldenrod">1064</span> 個 必要。<br />
<span class="wikicolor" style="color:darkgoldenrod">金</span>のウロコで交換できる<a href="/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88" title="ネームプレート/プレート" class="rel-wiki-page">プレート</a>は、<span class="wikicolor" style="color:darkgoldenrod">333</span>個必要なものが3つあり、それらが必要数の9割以上を占める。<br />
その3点を除いた場合、<span class="wikicolor" style="color:darkgoldenrod">金</span>のウロコは<span class="wikicolor" style="color:darkgoldenrod">65</span> 個必要となる。</p>
<p><strong>全ての品物を1つずつ交換する場合</strong><br />
<span class="wikicolor" style="color:brown">銅</span>/<span class="wikicolor" style="color:dimgray">銀</span>/<span class="wikicolor" style="color:darkgoldenrod">金</span>のウロコ が <span class="wikicolor" style="color:brown">12605</span>/<span class="wikicolor" style="color:dimgray">2795</span>/<span class="wikicolor" style="color:darkgoldenrod">1306</span> 個 必要。<br />
<strong>全ての品物を上限まで交換する場合</strong><br />
<span class="wikicolor" style="color:brown">銅</span>/<span class="wikicolor" style="color:dimgray">銀</span>/<span class="wikicolor" style="color:darkgoldenrod">金</span>のウロコ が <span class="wikicolor" style="color:brown">38570</span>/<span class="wikicolor" style="color:dimgray">7259</span>/<span class="wikicolor" style="color:darkgoldenrod">2799</span> 個 必要。</p>
</div>
</div>
<p>なお、作業着はクマサン商会建物内の<a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC" title="ロッカー" class="rel-wiki-page">ロッカー</a>(入り口から見て右奥)にて着替えることが可能だ。</p>
<div class="caption-flybox">
<div id="pc-caption-20th-ad-container">
<!-- /19033742/WIKIWIKI_PC_CAPTION_20TH -->
<div id='div-gpt-ad-1566473930452-0' class="hidden-switch-class">
<script>
    googletag.cmd.push(function() {googletag.display('div-gpt-ad-1566473930452-0'); });
</script>
</div>
</div>
</div>
<h2 id="h2_content_1_20" class="heading-after-first"><a href="/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%90%E3%83%83%E3%82%B8" title="ネームプレート/バッジ" class="rel-wiki-page">バッジ</a>  <a class="anchor_super" name ="mf0a5025"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=mf0a5025" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open"><a href="/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%90%E3%83%83%E3%82%B8" title="ネームプレート/バッジ" class="rel-wiki-page">バッジ</a>一覧</div>
    <div class="fold-content visible-on-open"><p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>関連<a href="/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%90%E3%83%83%E3%82%B8" title="ネームプレート/バッジ" class="rel-wiki-page">バッジ</a>の獲得条件</p>
<ul class="list1"><li>クマサンポイント達成
<ul class="list2"><li>通常色:なし</li>
<li>銅:10,000pt</li>
<li>銀:100,000pt</li>
<li>金:9,999,999pt</li></ul></li>
<li>キケン度MAXクリア
<ul class="list2"><li>通常色:初クリア(通常色のみ)</li></ul></li>
<li>オオモノシャケ討伐数達成(種類別)
<ul class="list2"><li>通常色:100体討伐</li>
<li>銅:なし</li>
<li>銀:1,000体討伐</li>
<li>金:10,000体討伐</li></ul></li>
<li>オカシラシャケ討伐数達成(種類別)
<ul class="list2"><li>通常色:10体討伐</li>
<li>銅:なし</li>
<li>銀:100体討伐</li>
<li>金:1,000体討伐</li></ul></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AA%E3%82%AB%E3%82%B7%E3%83%A9%E9%80%A3%E5%90%88" title="サーモンラン/シャケの種類/オカシラ連合" class="rel-wiki-page">オカシラ連合</a>討伐数達成
<ul class="list2"><li>通常色:初討伐(通常色のみ)</li></ul></li>
<li>評価達成(ステージ別)
<ul class="list2"><li>通常色:でんせつ200</li>
<li>銅:でんせつ400</li>
<li>銀:でんせつ600</li>
<li>金:でんせつ999</li></ul></li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3" title="サーモンラン/ビッグラン" class="rel-wiki-page">ビッグラン</a>報酬
<ul class="list2"><li>通常色:銅以上の<a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E" title="ロッカー/オキモノ" class="rel-wiki-page">オキモノ</a>を貰う</li>
<li>銅:なし</li>
<li>銀:銀以上の<a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E" title="ロッカー/オキモノ" class="rel-wiki-page">オキモノ</a>を貰う</li>
<li>金:金の<a href="/splatoon3mix/%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/%E3%82%AA%E3%82%AD%E3%83%A2%E3%83%8E" title="ロッカー/オキモノ" class="rel-wiki-page">オキモノ</a>を貰う</li></ul></li>
<li>バイトチームコンテスト報酬
<ul class="list2"><li>通常色:なし</li>
<li>銅:上位50％以上に入る</li>
<li>銀:上位20％以上に入る</li>
<li>金:上位5％以上に入る</li></ul></li></ul>
</div>
</div>
<p>&#10145;&#65038;<a href="/splatoon3mix/%E3%83%8D%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88/%E3%83%90%E3%83%83%E3%82%B8" title="ネームプレート/バッジ" class="rel-wiki-page">バッジ</a>を参照</p>

<h2 id="h2_content_1_21" class="heading-after-first">イカリング3  <a class="anchor_super" name ="c8dedbcc"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=c8dedbcc" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<p>イカリング3では<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>のスケジュールやリザルトといった情報が確認できる。<br />
詳細は「<a href="/splatoon3mix/%E3%82%A4%E3%82%AB%E3%83%AA%E3%83%B3%E3%82%B03#salmon_run" title="イカリング3" class="rel-wiki-page">イカリング3(サーモンラン)</a>」を参照。</p>
<h2 id="h2_content_1_22" class="heading-after-first">開催履歴  <a class="anchor_super" name ="q451c880"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=q451c880" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<p>「<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E9%96%8B%E5%82%AC%E5%B1%A5%E6%AD%B4" title="サーモンラン/開催履歴" class="rel-wiki-page">サーモンラン/開催履歴</a>」のページ参照。</p>
<h2 id="h2_content_1_23" class="heading-after-first">編成評価  <a class="anchor_super" name ="nff9673b"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=nff9673b" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<p>「<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%B7%A8%E6%88%90%E8%A9%95%E4%BE%A1" title="サーモンラン/編成評価" class="rel-wiki-page">サーモンラン/編成評価</a>」のページ参照。</p>
<div class="spacer">&nbsp;</div>
<div class="spacer">&nbsp;</div>
<div class="caption-flybox">
<div id="div-gpt-ad-other-ad-container">
<div id="div-gpt-ad-other" class="hidden-switch-class">
<script>
    googletag.cmd.push(function() {googletag.display('div-gpt-ad-other'); });
</script>
</div>
</div>
</div>
<h2 id="h2_content_1_24" class="heading-after-first">コメント(攻略・質問)  <a class="anchor_super" name ="commentB"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=commentB" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<div class="accordion-container ">
    <h3 class="accordion-header">
        <i class="fas fa-plus-square hidden-on-open"></i>
        <i class="fas fa-minus-square visible-on-open"></i>
        攻略に関わる情報提供・質問などはこちらへ。
    </h3>
    <div class="accordion-content"><p>こちらは攻略・質問用のコメント欄です。<br />
<strong>雑談等はコメント(雑談)欄への書き込みをお願いします。</strong></p>
<div style="text-align:right"><a href="#strategyCom">◆コメントフォームへのリンク</a></div>
    <iframe id="zawazawa-embed-13fd257c805cef4ff4270df69a9cc11f-57" class="zawazawa-embed" src="https://z.wikiwiki.jp/em/spla3/topic/31?size=10&style=default"
        frameborder="0" scrolling="no" marginheight="0" marginwidth="0"
        style="width:100%; min-width: 100%; max-width: 100%; *width: 100%; min-height: 350px; height: 200px;"
        sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-modals allow-popups allow-popups-to-escape-sandbox allow-forms allow-top-navigation"
    ></iframe>
<p><a class="anchor" name ="strategyCom"></a></p>
</div>
</div>
<div class="spacer">&nbsp;</div>
<h2 id="h2_content_1_25" class="heading-after-first">雑談用コメント  <a class="anchor_super" name ="commentA"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&id=commentA" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">以下の行為は荒らし行為として対処することがあります。</div>
    <div class="fold-content visible-on-open"><ul class="list1"><li>スパムコメントの投稿</li>
<li>煽り、荒らしコメントへの反応</li>
<li><strong>特定IDに対する粘着</strong></li>
<li><strong>複数行</strong>にわたるAA貼付</li>
<li>その他見やすさを損なうようなコマンドの使用</li>
<li>一度削除されたコメントを再度投稿すること</li>
<li>「サムネイルリンク」及び「テキストリンク」以外での画像の貼り付け</li></ul>
</div>
</div>
<p>こちらは<strong>雑談用</strong>のコメント欄です。<br />
バイトシナリオの共有は<a href="/splatoon3mix/%E3%83%90%E3%82%A4%E3%83%88%E3%82%B7%E3%83%8A%E3%83%AA%E3%82%AA" title="バイトシナリオ" class="rel-wiki-page">バイトシナリオ</a>へお願いします。<br />
バイトメンバー募集をしたい場合は<a href="/splatoon3mix/%E3%83%81%E3%83%A3%E3%83%B3%E3%83%8D%E3%83%AB" title="チャンネル" class="rel-wiki-page">チャンネル</a>だと募集が流れにくく便利です。<br />
<strong>サーモンラ&#12531;用のチャンネル名が変更されています。<a class="inn" href="https://wikiwiki.jp/splatoon3mix/チャンネル#z54ba58b"  rel="nofollow">詳しくはこちら</a></strong></p>
<div class="accordion-container ">
    <h3 class="accordion-header">
        <i class="fas fa-plus-square hidden-on-open"></i>
        <i class="fas fa-minus-square visible-on-open"></i>
        サーモンラン雑談過去ログ
    </h3>
    <div class="accordion-content">    <iframe id="zawazawa-embed-ef11223945e98a969116b8356ca7200f-61" class="zawazawa-embed" src="https://z.wikiwiki.jp/em/spla3/topic/30?size=10&style=default"
        frameborder="0" scrolling="no" marginheight="0" marginwidth="0"
        style="width:100%; min-width: 100%; max-width: 100%; *width: 100%; min-height: 350px; height: 200px;"
        sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-modals allow-popups allow-popups-to-escape-sandbox allow-forms allow-top-navigation"
    ></iframe>
</div>
</div>
    <iframe id="zawazawa-embed-f712fd7930b406bbbde0089e77728a59-62" class="zawazawa-embed" src="https://z.wikiwiki.jp/em/spla3/topic/244?size=10&style=default"
        frameborder="0" scrolling="no" marginheight="0" marginwidth="0"
        style="width:100%; min-width: 100%; max-width: 100%; *width: 100%; min-height: 350px; height: 200px;"
        sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-modals allow-popups allow-popups-to-escape-sandbox allow-forms allow-top-navigation"
    ></iframe>
<p><strong><span class="wikicolor" style="color:red">※不適切だと思うコメントに対しては積極的に通報していただくようお願いいたします。特に、煽りコメントに対しては見かけても決して反応することなく通報してください。</span></strong>通報の際は、通報理由も記入してください。<br />
<span class="wikicolor" style="color:blue">※コメントのツリー化を意識してください。</span></p>
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
<form action="/splatoon3mix/::cmd/lookup?refer=%E3%83%96%E3%82%AD%2F%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3%2F%E3%82%A2%E3%83%A1%E3%83%95%E3%83%A9%E3%82%B7" method="post">
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
<span class="small">任天堂公式サイトの「<a class="ext" href="https://www.nintendo.co.jp/interview/av5ja/index.html"  rel="nofollow">開発者に訊きました スプラトゥーン３<span class="system-icon ext pukiwiki-open-uri" data-href="https://www.nintendo.co.jp/interview/av5ja/index.html" data-frame="_blank"></span></a>」にスプラトゥーン世界の地図が載っており、「バンカラ湾」と「ハイカラ湾」に「シャケのナワバリ」があることを確認できる。</span><br>
<a id="notefoot_2" href="#notetext_2" class="note_super">*2</a>
<span class="small">バイトマニュアルの説明</span><br>
<a id="notefoot_3" href="#notetext_3" class="note_super">*3</a>
<span class="small">バイトマニュアルでの呼称</span><br>
<a id="notefoot_4" href="#notetext_4" class="note_super">*4</a>
<span class="small"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/Extra%20Wave" title="サーモンラン/特殊な状況/Extra Wave" class="rel-wiki-page">Extra Wave</a>が発生した場合は3回、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AA%E3%82%AB%E3%82%B7%E3%83%A9%E9%80%A3%E5%90%88" title="サーモンラン/シャケの種類/オカシラ連合" class="rel-wiki-page">オカシラ連合</a>が襲来した場合は4回使える。</span><br>
<a id="notefoot_5" href="#notetext_5" class="note_super">*5</a>
<span class="small">Ver.5.2.0以前では7種類</span><br>
<a id="notefoot_6" href="#notetext_6" class="note_super">*6</a>
<span class="small">Ver.6.0.0以降</span><br>
<a id="notefoot_7" href="#notetext_7" class="note_super">*7</a>
<span class="small">Ver.6.0.0以降</span><br>
<a id="notefoot_8" href="#notetext_8" class="note_super">*8</a>
<span class="small">Ver.6.0.0以降</span><br>
<a id="notefoot_9" href="#notetext_9" class="note_super">*9</a>
<span class="small">バイトマニュアルでの呼称</span><br>
<a id="notefoot_10" href="#notetext_10" class="note_super">*10</a>
<span class="small">正確にはやられた時に最後に地面にいた場所</span><br>
<a id="notefoot_11" href="#notetext_11" class="note_super">*11</a>
<span class="small">バイトマニュアルでの呼称</span><br>
<a id="notefoot_12" href="#notetext_12" class="note_super">*12</a>
<span class="small">これ以外のブキはバイト専用の補正がかかっており攻撃力は30以上となっている。ただし、減衰によって1発で復活させられない場合もあるので注意。</span><br>
<a id="notefoot_13" href="#notetext_13" class="note_super">*13</a>
<span class="small">Ver.6.0.0以降</span><br>
<a id="notefoot_14" href="#notetext_14" class="note_super">*14</a>
<span class="small">Ver. 2.0.0 更新データ詳細より。&quot;一度に出現するオオモノシャケの数の上限を15匹までに制限しました。&quot;</span><br>
<a id="notefoot_15" href="#notetext_15" class="note_super">*15</a>
<span class="small">Ver. 2.0.0 更新データ詳細より。&quot;一度に出現するオオモノシャケの数の上限を15匹までに制限しました。&quot;</span><br>
<a id="notefoot_16" href="#notetext_16" class="note_super">*16</a>
<span class="small">バイトマニュアルでの呼称</span><br>
<a id="notefoot_17" href="#notetext_17" class="note_super">*17</a>
<span class="small">例えばイカ速のかけらが欲しい場合、基本<a href="/splatoon3mix/%E3%82%AE%E3%82%A2/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC" title="ギア/ギアパワー" class="rel-wiki-page">ギアパワー</a>がイカ速の<a href="/splatoon3mix/%E3%82%AE%E3%82%A2" title="ギア" class="rel-wiki-page">ギア</a>を引いたら、スパイキーに不要なかけら45個を払って置き換えればイカ速のかけら6個が得られる。</span><br>            </div>
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
</style><div id="pageload" style="display: none" data-pageload="{&quot;time&quot;:{&quot;all&quot;:{&quot;real&quot;:0.020252227783203125,&quot;cost&quot;:0.3857746124267578},&quot;body&quot;:{&quot;real&quot;:0.008744001388549805,&quot;cost&quot;:0.286344051361084},&quot;main&quot;:{&quot;real&quot;:0.2776000499725342,&quot;cost&quot;:0.2776000499725342},&quot;menu&quot;:{&quot;real&quot;:0.0876312255859375,&quot;cost&quot;:0.0876312255859375},&quot;head&quot;:{&quot;real&quot;:0.0001780986785888672,&quot;cost&quot;:0.0001780986785888672},&quot;foot&quot;:{&quot;real&quot;:0.00011301040649414062,&quot;cost&quot;:0.00011301040649414062}},&quot;include&quot;:2,&quot;memory&quot;:2346032,&quot;io&quot;:{&quot;read&quot;:{&quot;files&quot;:1,&quot;bytes&quot;:8,&quot;locks&quot;:1},&quot;write&quot;:{&quot;files&quot;:0,&quot;bytes&quot;:0,&quot;locks&quot;:0},&quot;directory&quot;:{&quot;traversals&quot;:0,&quot;files&quot;:0},&quot;misc&quot;:44},&quot;contentSize&quot;:{&quot;all&quot;:532976,&quot;body&quot;:356974},&quot;timestamp&quot;:&quot;2026-01-16 19:26:20&quot;}"></div>

<script type="text/javascript" src="https://cdn.wikiwiki.jp/to/w/common/assets/dist/wikiwiki-2ee375d6199d21f58b1a.min.js"></script>
<script type="text/javascript">
    bootLazy.addJqPluginInit('.fold-container', function() {
        this.fold({
            buttonSelector: '.fold-toggle-button',
            openClassName: 'fold-open'
        });
    });
</script>
<script type="text/javascript">
    bootLazy.addJqPluginInit('.accordion-container', function() {
        this.accordion({
            headerSelector: '.accordion-header',
            contentSelector: '.accordion-content',
            openClassName: 'accordion-open'
        });
    });
</script>
    <script>
    bootLazy.addJqPluginInit('.ref-external-image', function() {
        this.refExtImageFix();
    });
    </script>
<script>
    bootLazy.addJqPluginInit('.zawazawa-embed', function() {
        this.zcommentResize();
    });
</script>
<div id="wikiwiki-pageview-counter" data-endpoint="https://counter.wikiwiki.jp/c/splatoon3mix/pv/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" style="display: none;"></div>
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
            title: "サーモンラン NEXT WAVE - Splatoon3 - スプラトゥーン3 攻略＆検証  Wiki*",
            controlPanelUrl: "https:\/\/c.wikiwiki.jp\/wiki\/splatoon3mix\/design",
            imageUrl: "https:\/\/icon.wikiwiki.jp\/symbolicon\/splatoon3mix\/ogImage\/f1fa837847c5.png",
            description: "このサイトは、スプラトゥーン3の攻略・検証を目的とした非公式wikiです。",
            shareUrl: "https:\/\/wikiwiki.jp\/splatoon3mix\/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3",
            shortUrlRequestUrl: "\/splatoon3mix\/::cmd\/short_url?mode=json&page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3",
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
    url: '/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3',
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
