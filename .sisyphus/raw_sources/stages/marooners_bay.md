<!DOCTYPE html>
<html lang="ja">
<head prefix="og: https://ogp.me/ns# fb: https://ogp.me/ns/fb# article: https://ogp.me/ns/article#">
    <meta charset="utf-8">
    <meta name="viewport" content="width=980">

    <meta name="description" content="このサイトは、スプラトゥーン3の攻略・検証を目的とした非公式wikiです。">
        <meta property="og:url" content="https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3" />
    <meta property="og:type" content="article" />
    <meta property="og:title" content="難破船ドン・ブラコ - Splatoon3 - スプラトゥーン3 攻略＆検証  Wiki*" />
    <meta property="og:description" content="このサイトは、スプラトゥーン3の攻略・検証を目的とした非公式wikiです。" />
    <meta property="og:site_name" content="Splatoon3 - スプラトゥーン3 攻略＆検証  Wiki*" />
    <meta property="og:image" content="https://icon.wikiwiki.jp/symbolicon/splatoon3mix/ogImage/f1fa837847c5.png" />
    <title>難破船ドン・ブラコ - Splatoon3 - スプラトゥーン3 攻略＆検証  Wiki*</title>

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
    <link rel="canonical" href="https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3">
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
                <div id="navigator">[ <a href="/splatoon3mix/">ホーム</a> | <a href="/splatoon3mix/::cmd/newpage?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3" rel="nofollow">新規</a> | <a href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3" rel="nofollow">編集</a> | <a href="/splatoon3mix/::cmd/attach?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3" rel="nofollow">添付</a> ]</div>            </div>
            <div class="toolbox toolbox-desktop toolbar-container">
                <div class="toolbar"><a href="/splatoon3mix/::cmd/list" title="一覧" rel="nofollow"><span class="system-icon toolbar list"></span></a>
<a href="/splatoon3mix/RecentChanges" title="最終更新" rel="nofollow"><span class="system-icon toolbar recent"></span></a>
<a href="/splatoon3mix/::cmd/diff?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3" title="差分" rel="nofollow"><span class="system-icon toolbar diff"></span></a>
<a href="/splatoon3mix/::cmd/backup?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3" title="バックアップ" rel="nofollow"><span class="system-icon toolbar backup"></span></a>
<a href="/splatoon3mix/::cmd/freeze?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3" title="凍結" rel="nofollow"><span class="system-icon toolbar freeze"></span></a>
<a href="/splatoon3mix/::cmd/template?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3" title="複製" rel="nofollow"><span class="system-icon toolbar copy"></span></a>
<a href="/splatoon3mix/::cmd/rename?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3" title="名前変更" rel="nofollow"><span class="system-icon toolbar rename"></span></a>
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
                <ul><li><a href="/splatoon3mix/::cmd/newpage?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3" rel="nofollow"><span class='system-icon toolbar new'></span> 新規</a></li><li><a href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3" rel="nofollow"><span class='system-icon toolbar edit'></span> 編集</a></li><li><a href="/splatoon3mix/::cmd/attach?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3" rel="nofollow"><span class='system-icon toolbar upload'></span> 添付</a></li></ul>
<ul><li><a href="/splatoon3mix/::cmd/list" rel="nofollow"><span class='system-icon toolbar list'></span> 一覧</a></li><li><a href="/splatoon3mix/RecentChanges" rel="nofollow"><span class='system-icon toolbar recent'></span> 最終更新</a></li><li><a href="/splatoon3mix/::cmd/diff?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3" rel="nofollow"><span class='system-icon toolbar diff'></span> 差分</a></li><li><a href="/splatoon3mix/::cmd/backup?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3" rel="nofollow"><span class='system-icon toolbar backup'></span> バックアップ</a></li></ul>
<ul><li><a href="/splatoon3mix/::cmd/freeze?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3" rel="nofollow"><span class='system-icon toolbar freeze'></span> 凍結</a></li><li><a href="/splatoon3mix/::cmd/template?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3" rel="nofollow"><span class='system-icon toolbar copy'></span> 複製</a></li><li><a href="/splatoon3mix/::cmd/rename?refer=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3" rel="nofollow"><span class='system-icon toolbar rename'></span> 名前変更</a></li></ul>
<ul><li><a href="/splatoon3mix/::cmd/help" rel="nofollow"><span class='system-icon toolbar help'></span> ヘルプ</a></li></ul>

            </div>
        </div>
    </div>    </div>

    <div class="container">
        <div class="clearfix">
            <div id="breadcrumbs" class="system-ui">
                <div id="topicpath"><a href="/splatoon3mix/" title="FrontPage"><i class="fa fa-home" style="margin-left: 6px; display: inline-block; min-width: 1.2em;"></i></a> &gt; <a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン">サーモンラン</a> &gt; <a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8" title="サーモンラン/ステージ">ステージ</a> &gt; 難破船ドン・ブラコ</div>            </div>
            <div id="system-icon-container" class="system-ui">
                                <span id="share-button-root"></span>                <span id="admin-contact-root" class="single-system-icon"></span>
                <div id="load-panel-root"></div>
                <span id="admin-login" class="single-system-icon">
                    
<a class="admin-login-status" href="/splatoon3mix/::cmd/admin_login?return_to=%2Fsplatoon3mix%2F%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3" title="未ログイン">
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
                                            <h1 class="title">難破船ドン・ブラコ</h1>
                                                                <div id="lastmodified">
                            Last-modified: 2026-01-13 (火) 09:25:24                                                            <span class="lastmodified-file-itself tooltip" data-tippy-content="このページ自体の更新: 2025-04-19 (土) 11:13:54"><i class="fas fa-file-signature"></i></span>
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
<ul class="list2"><li><a href="#h51f91a5">通常時 </a></li>
<li><a href="#d52a90e1">満潮時 </a></li>
<li><a href="#ff6255eb">干潮時 </a></li></ul></li>
<li><a href="#f4cf1ea5">特殊な状況 </a>
<ul class="list2"><li><a href="#d7acea18">ラッシュ </a></li>
<li><a href="#pa7df542">グリル発進 </a></li>
<li><a href="#vb03170e">ドスコイ大量発生 </a></li>
<li><a href="#ya75d597">キンシャケ探し </a></li></ul></li>
<li><a href="#comment">コメント</a></li></ul>
</div>
<hr class="full_hr" />
<p><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3/::ref/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3.png.webp?rev=59a4270751acc614f0a62a6ebf6e12a0&amp;t=20221202135418" alt="難破船ドン・ブラコ" title="難破船ドン・ブラコ" width="480" height="270"  loading="lazy"><br />
<img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3/::ref/%E3%83%89%E3%83%B3%E3%83%96%E3%83%A9%E3%82%B3%E5%85%A8%E4%BD%93%E3%83%9E%E3%83%83%E3%83%97_r2.png.webp?rev=6eab49c3adddbe71cc922492afe38e51&amp;t=20230113203813" alt="難破船ドンブラコ簡易マップ" title="難破船ドンブラコ簡易マップ" width="614" height="489"  loading="lazy"></p>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">ブイとエリアの対応</div>
    <div class="fold-content visible-on-open"><div class="h-scrollable"><table><thead><tr><th>ブイ</th><th><strong>ウインナー</strong></th><th><strong>アスパラ</strong></th><th><strong>コーン</strong></th><th><strong>カボチャ</strong></th></tr></thead><tbody><tr><th>画像</th><td><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3/::attach/%E3%83%96%E3%82%A4_%E3%82%A6%E3%82%A4%E3%83%B3%E3%83%8A%E3%83%BC.png?rev=22c1082a2d5d2709758d4c06f0282fec&amp;t=20221206131747" title="nolink" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3/::ref/%E3%83%96%E3%82%A4_%E3%82%A6%E3%82%A4%E3%83%B3%E3%83%8A%E3%83%BC.png.webp?rev=22c1082a2d5d2709758d4c06f0282fec&amp;t=20221206131747" alt="nolink" title="nolink" width="132" height="171"  loading="lazy"></a></td><td><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3/::attach/%E3%83%96%E3%82%A4_%E3%82%A2%E3%82%B9%E3%83%91%E3%83%A9.png?rev=bbc72e6748b3c96e37d4efb2dafcebe9&amp;t=20221206131802" title="nolink" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3/::ref/%E3%83%96%E3%82%A4_%E3%82%A2%E3%82%B9%E3%83%91%E3%83%A9.png.webp?rev=bbc72e6748b3c96e37d4efb2dafcebe9&amp;t=20221206131802" alt="nolink" title="nolink" width="165" height="176"  loading="lazy"></a></td><td><a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3/::attach/%E3%83%96%E3%82%A4_%E3%82%B3%E3%83%BC%E3%83%B3.png?rev=cfede866f40ea4c80b7d84dab0a50525&amp;t=20221206131812" title="nolink" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3/::ref/%E3%83%96%E3%82%A4_%E3%82%B3%E3%83%BC%E3%83%B3.png.webp?rev=cfede866f40ea4c80b7d84dab0a50525&amp;t=20221206131812" alt="nolink" title="nolink" width="132" height="182"  loading="lazy"></a></td><td></td></tr><tr><th>方角</th><td>船尾とその奥のエリア<br class="spacer">(簡易マップ左側)</td><td>桟橋のエリア<br class="spacer">(簡易マップ下側)</td><td>浜のエリア<br class="spacer">(簡易マップ上側)</td><td>干潮エリア<br class="spacer">(簡易マップ右側)</td></tr></tbody></table></div>
</div>
</div>
<h2 id="h2_content_1_0" >攻略情報  <a class="anchor_super" name ="maininfo"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3&id=maininfo" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<p>難破した船とそれが乗り上げた岩礁(？)からなるステージ。<br />
総合的に見るとステージ自体は広いが船上は狭く複数のオオモノが同時に侵攻して来やすい。<br />
またオオモノがコンテナ付近までやって来るまでに時間が掛かりやすく、納品が追い付かないケースが非常に多い。特に通常潮の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>で顕著。<br />
かなり遠方への<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>の出現、右下と呼ばれる要注意ポイントの存在、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%82%B0%E3%83%AA%E3%83%AB%E7%99%BA%E9%80%B2" title="サーモンラン/特殊な状況/グリル発進" class="rel-wiki-page">納品が追いつかないグリル</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">金イクラ不足が発生しやすいラッシュ</a>などの要因により難易度が高いと推測される。<br />
方角を船尾[ウインナー]に向かって右[コーン]、左[アスパラ]と呼ぶことが多い。また満潮時にはリフトが作動しないため、スーパージャンプの間際にボムをリフトに投げてみて作動しなかったら次WAVEは満潮である。</p>
<h3 id="h3_content_1_1" class="heading-after-first">通常時  <a class="anchor_super" name ="h51f91a5"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3&id=h51f91a5" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<p>錆びた船体の壁は塗ることができず、山もしくはEの字状にステージを仕切っている。このため敵味方双方の右下[コーン]・左下[アスパラ]から船上への移動を大きく制限している。(逆は飛び降りるだけと簡単)<br />
この構造によって右下[コーン]・左下[アスパラ]側に出現した陸路移動のシャケは船尾[ウィンナー]まで大きく迂回を強いられるため、他のマップに比べればシャケの侵攻速度は遅くなりやすい。<br />
だが、このためにむしろ難易度が上がるにつれて大量のシャケの滞留を招き、しまいには船の外側が強固な敵陣地のような様相を呈し始める。特に右下[コーン]の地上は、後述のリフト以外に有利を取れる地形がなく、シャケに包囲されやすい危険地帯となる。<br />
これが長距離型のオオモノ処理の上で大問題となり、放置すれば延々と撃たれ続け、かといって焦って飛び込みウキワになれば救助も難しい。<br />
長射程ブキ持ちなら船体上からの的確な支援、そして右側[コーン]・左側[アスパラ]に一基ずつ設置されたプロペラリフトの活用が、生還とイクラ回収の上での要となる。<br />
複数人行動したくなるが、行き来に利用するリフトの事故に注意を要す上に、初動を除けば別方向の人数不足を招く可能性が高い。特に高キケン度では1人で遠征を行い、生還し、かつ納品できるだけの技術と判断力が求められる。（後述）</p>
<p>上述の通り、戦闘で消耗した味方を下に取り残せばたいていはそのままやられてしまう。リフトに取りついたら作動前に周囲を確認し、味方がいれば少し待って一緒に乗せると良い。<br />
一応リフトの壁も塗って登れるのだが、搭乗して上昇するより時間がかかり、そもそも塗らなければならない状況に追い込まれてしまった時点でだいたいは助からない。<br />
特に連射の遅い中・長射程ブキはリフトに乗り遅れると下で<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>に囲まれてやられやすい。<br />
場合によってはリフトにこだわりすぎず、船尾側[ウィンナー]を経由して索敵・イクラ運搬をする選択もある。船尾[ウィンナー]にシャケがいないなら、右下[コーン]・左下[アスパラ]のシャケを船尾側[ウィンナー]から攻めることで包囲のリスクを減らすことができることも思い出したい。</p>
<p>リフトの側面は塗ることができるため、特に右側[コーン]リフト側面をWAVE1開始前に塗っておく手がある。<br />
リフトを上昇させてから塗る必要があるので、ブキによっては少々難しい。リフト塗りの際にプロペラを回し続けることでサポートしているイカを見かけるが大半のブキの組み合わせで2人でリフトを塗ったほうが早く、またリフトが降りてくることを前提にした塗り方をするブキもあるため、2人でそれぞれ別の面を塗るかリフトは任せて別の場所を塗ったほうが効率的である。<br />
本来リフト側面を登るというのは複数人が同方向の海岸に降り、かつ取り残された場合の次善の策であり、船上の壁をきちんと塗る方が重要度は高い。</p>
<p>金網から船尾にかけての船腹をWAVE終盤まで維持することがキケン度を問わず重要。<br />
船尾・左奥方向への主なアクセス経路となるほか、寄せにくい<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>の主なキルゾーンとなり、また左右海岸のイクラを拾う<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#snatcher" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">タマヒロイ</a>の経路ともなるため、寄せやすいオオモノが少なかった場合のノルマ達成の成否に関わる。<br />
そのほか左右へ遠征中の味方に向く可能性のあるオオモノのターゲットをとることもできる。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a>や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%A2%E3%82%B0%E3%83%A9" title="サーモンラン/シャケの種類/モグラ" class="rel-wiki-page">モグラ</a>を船上を通して寄せる際は、左右通路のうち船上で戦闘中の味方の邪魔にならない経路を選ぶこと。</p>
<p>イクラコンテナ前が金網になっているため転落に注意。(満潮時以外の金網下側は右下[コーン]⇔左下[アスパラ]間の連絡通路を兼ねている)<br />
勢いをつけてイカダッシュジャンプで、インク回復しつつ減速なしで渡れる。また<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%95%E3%83%87%E5%B1%9E" title="ブキ/フデ属" class="rel-wiki-page">フデ</a>や<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC%E5%B1%9E" title="ブキ/ローラー属" class="rel-wiki-page">ローラー</a>の塗り移動も金網を無視できる。</p>
<p>船上の道が細いので<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>の脅威度が上がる。出現直後の舷側や金網下通路を移動中は胴体も一直線で狙いやすいため、できれば船に上がられる前に手を打ちたい。<br />
段差を利用して<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>の追跡を避けよう。船体は船尾側[アスパラ]の足場が高めなので、開幕の壁塗りを意識するならばルートは右側[コーン](スタート時のカメラ右)を選択するといいだろう。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>Next Wave から追加された<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a>も厄介。船上通路の射線を封じてくる上に、雑魚シャケを召喚してくるので処理キャパシティオーバーになりがち。寄せられるオオモノではあるが脅威度は高いので安全のために視認次第遠くで処理をすることも選択肢に入れておいてよいだろう。<br />
なお、本ステージの<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a>は船上でプレス攻撃を出した際に<strong>船体外周部の壁に水平状態のまま引っかかる</strong>ことが時々ある。この現象が発生する位置にいる<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a>は上に飛び乗っての処理がほぼ不可能となるため厄介である。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a>についても、刺さる場所によっては<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a>への攻撃の妨げになったりするので、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a>ほど直接的ではないにせよ、塗り能力も含めて凶悪。しかし倒した後に残る柱に登れば前述の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a>にも攻撃しやすいので、さっさと処理して利用するのが得策か。柱上での<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%A2%E3%82%B0%E3%83%A9" title="サーモンラン/シャケの種類/モグラ" class="rel-wiki-page">モグラ</a>と<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>の<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%9E%E3%83%AB%E3%83%81%E3%83%9F%E3%82%B5%E3%82%A4%E3%83%AB" title="ブキ/スペシャルウェポン/マルチミサイル" class="rel-wiki-page">マルチミサイル</a>には注意しよう。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%80%E3%82%A4%E3%83%90%E3%83%BC" title="サーモンラン/シャケの種類/ダイバー" class="rel-wiki-page">ダイバー</a>については他のステージでもそうだが、しっかり寄せて<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;「美味い金イクラ」の略で、&lt;strong&gt;コンテナ近くに落ちて納品しやすい金イクラのこと&lt;/strong&gt;を指す。&lt;br class=&quot;spacer&quot;&gt;ウマイクラをなるべく増やし、マズイクラをなるべく減らすように立ち回ることが、スムーズな金イクラの納品、ひいては円滑なノルマクリア、評価アップへの近道となる。&lt;br class=&quot;spacer&quot;&gt;&lt;br class=&quot;spacer&quot;&gt;&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%E6%8C%87%E5%8D%97#FarAndBasketEggs&quot; title=&quot;サーモンラン/サーモンラン指南&quot; class=&quot;rel-wiki-page&quot;&gt;&lt;span class=&quot;wikicolor&quot; style=&quot;color:#808080&quot;&gt;[詳細]&lt;/span&gt;&lt;/a&gt;">ウマイクラ</span>にしたい。</p>
<p>なお新テクニックであるイクラ投げ、特にジャンプ投げを使うといわゆる「左下」や「右下」などの船外から直接イクラコンテナに納品ができる。通常ではもちろんの事、特殊な状況「<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%89%E3%83%AD%E3%82%B7%E3%83%A3%E3%82%B1%E5%99%B4%E5%87%BA" title="サーモンラン/特殊な状況/ドロシャケ噴出" class="rel-wiki-page">ドロシャケ噴出</a>」でもこの技術は役立つ。「<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E5%B7%A8%E5%A4%A7%E3%82%BF%E3%83%84%E3%83%9E%E3%82%AD" title="サーモンラン/特殊な状況/巨大タツマキ" class="rel-wiki-page">巨大タツマキ</a>」では投げ回数の関係で船上投げに効率で劣るが、余裕のある際に練習をしておけば、あと1つ足りず失敗、ということも減るかもしれない。<br />
対して「右下」からの投げによる直接納品は左下からと比べるとややシビア。自信が無ければ船上に乗せるだけにしておくか、ひとつリフトに乗せ、ひとつを持っていくくらいでも十分だろう。特にイクラに意識を取られていると周囲への警戒が鈍くなってしまうことが往々にしてあるので、危険と名高い右下での長時間作業はしっかりとタイミングを見極めよう。</p>
<p>右金網と中央カンケツセンBのある足場とは隣接してはいるが床面の角と角で繋がっている状態であり、通常シャケは金網からカンケツセン側へ直接移動しようとしない（逆方向には金網前の坂に降りてやってくることがある）。しかしプレイヤーが移動した直後などごくまれについてくることがあるようで、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>が乗ってきたという報告も上がっている。</p>
<h4 id="h4_content_5_0" >通称「右下」について</h4>

<p>開始方向から見て右下側([コーン]の地上)の砂浜地帯は敵の出現頻度が高くリフトもありついつい足を踏み入れがちだが、<span class="wikicolor" style="color:Red"><strong>この地点で戦闘を続けているとどんどん戦況が不利になるという罠を抱えている</strong></span>。<br />
一見、直線距離では近く、リフトですぐ行き来できるので何ら問題ないように思えて分かりにくいのだが、実際のリフト動作は往復7～8秒掛かり、これはイカダッシュなら船の中腹以上まで行ける時間で実は近くない。<br />
コンテナ至近への誘導撃破による高速3個回収ができない事も含め、総じてイクラ不足に陥りやすい。<br />
またリフトはあるが逆に言えばリフト以外に退避手段に乏しく、乗り遅れは勿論、乗っている最中も<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%9E%E3%83%AB%E3%83%81%E3%83%9F%E3%82%B5%E3%82%A4%E3%83%AB" title="ブキ/スペシャルウェポン/マルチミサイル" class="rel-wiki-page">マルチミサイル</a>に狙われる等の危険要素が多い。</p>
<p>そして最大の問題だが、シャケは最も近くの味方に寄り付く関係上、この地点に留まって居ると、右下だけでなくその他の地点から湧いた敵も全てこの地点に集結してくる。前述した通りこの地点は運搬に不利だが、その不利な地形に更に敵が集まり、途中で気付いたとしても他の場所にオオモノが居ないため、金イクラを得る為には分かっていてもそこで戦うしか選択肢が無くなる、という悪循環が完成してしまう。船の下部にはトンネルがあり、シャケ側からすると右下に居る味方は最短経路になりやすく、たった数人でも降りているとタゲを吸い付くして納品を困難にしてしまう。<br />
こうなる事を避ける為、<strong>右下に立つ時間は最小限に留める</strong>のが回収のコツ。<br />
金イクラが落ちている場合も迂闊には拾いに行かず、0～1個だけ拾って残りは諦める、等の選択も十分に考えられる。特にキケン度が上がってくると敵勢力とノルマの増大もあり納品せずに右下に立ち続ける＝ほぼ終了の図式が出来上がる。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>が出現した場合は迷う所だが、ボム遠投やSPでの対処もできるので必ずしも降りる必要はない。<br />
いつ何時も一切立ち入らないべきという訳ではなく、短時間で敵を殲滅して早々に去ったり、他の地点で味方が戦闘中に少人数が降りて通過する程度なら問題ない。要は長時間の滞在での誘導による悪循環発生が問題なので、そうならない範囲内ならばある程度臨機応変に対応して良い。<br />
右下を意識しすぎるあまり<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>を放置してしまっては他の場所が主戦場であろうと苦戦は必至であり、本末転倒である。</p>
<p>意思疎通が取れない中、味方がそちらに行ってしまう場合は、</p>
<ul class="list1"><li>自分も右下を援護して敵が溜まる前に急いで殲滅して撤退する（ただし金イクラが大量に転がると余計に拍車をかける可能性がある）</li>
<li>上記に加え、積極的に納品に加担する（他地点から沸いてきたオオモノのタゲに注視しよう）</li>
<li>船上の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%A2%E3%82%B0%E3%83%A9" title="サーモンラン/シャケの種類/モグラ" class="rel-wiki-page">モグラ</a>が落とした金イクラを放置しそちらを拾うことに時間を使わせる（ただし拾いに来なかった場合イクラ3個入れる絶好のチャンスを<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#snatcher" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">タマヒロイ</a>に献上してしまう）</li>
<li>船の中腹から向かい、敵のヘイトを分散させる(<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%A2%E3%82%B0%E3%83%A9" title="サーモンラン/シャケの種類/モグラ" class="rel-wiki-page">モグラ</a>のヘイトを買って船上まで連行できるとベスト)</li></ul>
<p>等が挙げられる。チームが混乱したまま時間が過ぎるのが最も危険で、その場合比較的すぐにノルマ不足の詰みの時間に入ってしまう。迷わずに落ち着いて素早く判断・対処しよう。<br />
右下を放置してあえて蘇生もせず、他の地点から湧いた敵を足止めしてそちらに戦線を移動させて戻ってくるのを待つ判断は、生きていてもウキワになっていても放置が長すぎると人数不利やタゲを奪われてかえって窮地を招きやすく、よほどの限り推奨されない。<br />
さらに長時間救助しない事に関しては通報されることもある。</p>
<p>ちなみに、右下を特別に挙げているのは敵の出現頻度が特に高く地形的にも逃げ場がないからであって、左下や正面奥でも長く敵を引きつけすぎれば金イクラがコンテナから離れ納品が不利になるので同じ事が言える。<br />
冷静に考えれば、ドンブラコは中央の山頂の一番奥にコンテナがある状態なので、元々誘導を意識せず全て徒歩で処理すると苦しくなるのは当然なのだ。ノルマ不足に悩む場合はいっそ<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>カタパ以外のオオモノは全て船上手前まで待つ位のつもりでも良い。コンテナ付近に敵が溢れかるかもしれないが、船上に敵が集まっているなら左右はがら空きなので、ピンチになったら飛び降りる事もできるので実は見た目ほどの危険はない。右下はこういう場面で特に役立つのだ。</p>
<h4 id="h4_content_6_0" >高危険度でも安定してクリアしたいなら「右下に降りよう」</h4>

<p>上記「左右に降りない」という攻略方法は、高危険度でも安定してクリアしたいという場合には通用しない。<br />
通常昼をほとんどクリアできないという方が、自分をターゲットにしている<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%A2%E3%82%B0%E3%83%A9" title="サーモンラン/シャケの種類/モグラ" class="rel-wiki-page">モグラ</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>を確実にコンテナに誘導することで、少しクリア率をましにする方法である。<br />
以下はクマサンポイント1200pでは満足できず、でんせつ400から600、さらに評価を上げていく……だけでも飽き足らず、クリア率10割を目指したい方向けの攻略法の基礎だ。</p>
<p>なぜ「左右に降りない」では安定してクリアできないのか。それは<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>のオオモノの出現がランダムであり、コンテナに誘導できるオオモノが必ずしもノルマ分出現するとは限らないからだ。</p>
<p>危険度MAXのwave3ではノルマが35、オオモノは72秒間で35体出現する。<br />
コンテナ近くにいることで<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%A2%E3%82%B0%E3%83%A9" title="サーモンラン/シャケの種類/モグラ" class="rel-wiki-page">モグラ</a>と<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a>をすべて寄せるとすると、必要な<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%A2%E3%82%B0%E3%83%A9" title="サーモンラン/シャケの種類/モグラ" class="rel-wiki-page">モグラ</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a>の数は計12体。危険度MAXを安定してクリアしようという方ならば、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%A2%E3%82%B0%E3%83%A9" title="サーモンラン/シャケの種類/モグラ" class="rel-wiki-page">モグラ</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a>が12体も出現することは少ない、運の良いwaveであることは知っているだろう。</p>
<p>そうすると<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA" title="サーモンラン/シャケの種類/コウモリ" class="rel-wiki-page">コウモリ</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%80%E3%82%A4%E3%83%90%E3%83%BC" title="サーモンラン/シャケの種類/ダイバー" class="rel-wiki-page">ダイバー</a>を寄せることになるが、左右に降りないという方針のため外回りは必然的におろそかになる。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>を倒すにはボム3個(インクタンク210%)が必要。正面とさらに左2体目位置のカタパにはボムが届かない。<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%82%AD%E3%83%A5%E3%82%A6" title="サーモンラン/シャケの種類/テッキュウ" class="rel-wiki-page">テッキュウ</a>を安全地帯から処理できるブキは数少ない。<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>にも限りがある。<br />
ミサイルとショックウェーブに追い詰められる中、寄せようと決めた<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA" title="サーモンラン/シャケの種類/コウモリ" class="rel-wiki-page">コウモリ</a>の雨に覆われ、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>と<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a>が正面から迫ってくる。しかし<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%A2%E3%82%B0%E3%83%A9" title="サーモンラン/シャケの種類/モグラ" class="rel-wiki-page">モグラ</a>と<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a>は必ずコンテナ横で倒さねばならない。<br />
船上にオオモノが集っているのだから、いざとなったら左右に逃げようなんて考えはやめておこう。時間が過ぎてゆくだけ。ノルマクリアしてからなら良い選択だ。しかし、またコンテナに戻って納品しなければならない状況で下に降りるとそれこそ時間が足りずクリア不可能。</p>
<p>そういう経験が誰しもあるだろう。<br />
つまり、高危険度で安定してクリアしたいのに左右に降りないというのは、外回りをおろそかにし、10秒かからず回収できるイクラを一切諦め、その分ノルマクリアを遅らせ、コンテナ周りを意図的にカオス状態にしてからどうにかキャラコンや<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>のごり押しでクリアしよう！という縛りプレイだと分かる。</p>
<p>では、いつ左右に降りるのか。<br />
そのタイミングを出来る限り具体的に挙げる。</p>
<ul class="list1"><li><strong>初動</strong><br />
序盤はオオモノが少なく、左右に降りることで他の方向で湧いた<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a>をコンテナから遠ざけてしまうようなことはない。<strong>降りて、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>・カタパ・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA" title="サーモンラン/シャケの種類/コウモリ" class="rel-wiki-page">コウモリ</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>は倒して回収した方が速く多く納品できる。</strong>(そもそも<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%A2%E3%82%B0%E3%83%A9" title="サーモンラン/シャケの種類/モグラ" class="rel-wiki-page">モグラ</a>や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a>を寄せる意味というのは自分が往復するよりも時間的に得だからであり、往復した方が速く、他で損が発生していない場合寄せる意味はない)<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%A2%E3%82%B0%E3%83%A9" title="サーモンラン/シャケの種類/モグラ" class="rel-wiki-page">モグラ</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a>のみが出現した場合は逆に降りる意味がないが、ターゲットの人は漫然とコンテナ横で待つのではなく、他のシャケを間引いたり索敵を行う味方の邪魔にならないルートを選んで丁寧な誘導を行うこと。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a>を倒してコンテナに帰る自信がない場合も、倒してから降りて回収という順序が生存のためには大切になる。<br />
野良での注意だが、味方に<strong>右下絶対降りないマン</strong>や<strong>寄せられるオオモノを寄せずに倒す選択ができない者</strong>がいた場合、全体の火力が大きく下がるということを意識する必要がある。つまり<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>が相対的に多くなる。小回りのきかないブキ、キャラコンに自信がない場合は味方の様子を見てから降りるか、正面の方から回り込むのが無難。</li></ul>
<ul class="list1"><li><strong>右下にイクラがあり、湧き方向が変わったとき</strong><br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>やカタパ、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA" title="サーモンラン/シャケの種類/コウモリ" class="rel-wiki-page">コウモリ</a>などを右下で倒したあと、別の方向に湧きが変わると、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>が新たに湧くという脅威なく金イクラを回収できる状況になる。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#snatcher" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">タマヒロイ</a>に金イクラを持っていかれる前に、また湧き方向が戻る前に、数個でも回収できればノルマクリアに大きく近づく。<br />
注意としては、正面が壊滅しない程度に時間を使うことだ。右下回収は大事だが、味方にオオモノ処理を任せる形になるため、オオモノ処理を手伝うのと右下を回収するのと、そのバランスを判断することが重要になる。</li></ul>
<ul class="list1"><li><strong>他方向の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>が十分生きている状態で湧き方向が変わったとき</strong><br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>の数には限りがあり、危険度ごとに決まっている。倒せば湧くが、倒さなければ増えない。そのため、正面で<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>が湧いて倒していない状態で次右下からオオモノが湧けば、オオモノのみ孤立した状態になる。<br />
それが<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>、カタパ、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA" title="サーモンラン/シャケの種類/コウモリ" class="rel-wiki-page">コウモリ</a>、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a>であればすぐに倒して楽に回収することができるだろう。<br />
他方向で<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a>を攻撃してターゲットを取っているときは誘導を優先した方がいい場合が多い。<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%A2%E3%82%B0%E3%83%A9" title="サーモンラン/シャケの種類/モグラ" class="rel-wiki-page">モグラ</a>であれば右下に行っても倒さなければ、金イクラを回収してコンテナに戻るとすぐ寄るので回収に降りてもよいだろう。</li></ul>
<ul class="list1"><li><strong>ノルマクリアまであと1個足りないというとき</strong><br />
寄せたオオモノ*3個の金イクラでは、ぎりぎりノルマに届かないとき、もしくは、ノルマまであと1個だが今からオオモノを倒して回収では難しそうなとき。<br />
右下に金イクラがあることを覚えていたら、その1個を回収しに行くという選択肢を考えよう。8秒あれば間に合う。10秒あれば余裕がある。その1個がチームを救うかもしれない。<br />
もちろん、右下でなくても正面の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a>がたむろしがちな場所などの金イクラも、覚えておけば選択肢のうちに入る。回収する金イクラが味方と被らず、安全に間に合いそうな金イクラを選びたいところ。</li></ul>
<p>初動を除き、他のプレイヤーがすでに降りていた場合は同方向には降りないこと。<br />
1人が降りられると判断したということは、すでに船上にシャケが迫りその上でさらに別方向に（場合によっては遠征の必要な）シャケが出現しているということであり、残り2人では船上の防衛・納品・別方向への遠征を両立することが困難となる。</p>
<h4 id="h4_content_7_0" >左奥に湧く<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>について</h4>

<p>本ステージで潮位が普通の時、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>が左奥[アスパラ]のL字状の桟橋に出現することがある。ここの<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>は通称「<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;&lt;strong&gt;処理が困難な位置に湧いた&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC&quot; title=&quot;サーモンラン/シャケの種類/タワー&quot; class=&quot;rel-wiki-page&quot;&gt;タワー&lt;/a&gt;のこと&lt;/strong&gt;。&lt;br class=&quot;spacer&quot;&gt;特に&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC&quot; title=&quot;サーモンラン/シャケの種類/タワー&quot; class=&quot;rel-wiki-page&quot;&gt;タワー&lt;/a&gt;の攻撃の脅威度が増す満潮時に、メイン・&lt;a href=&quot;/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3&quot; title=&quot;ブキ/サブウェポン&quot; class=&quot;rel-wiki-page&quot;&gt;サブ&lt;/a&gt;での処理が困難な位置に湧くものがこう呼ばれやすい。&lt;br class=&quot;spacer&quot;&gt;とりわけ高キケン度では、処理が困難と判断した時点で速やかに&lt;a href=&quot;/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3&quot; title=&quot;ブキ/スペシャルウェポン&quot; class=&quot;rel-wiki-page&quot;&gt;スペシャル&lt;/a&gt;を切らねば、ゼンメツ一直線となりかねない。&lt;br class=&quot;spacer&quot;&gt;&lt;br class=&quot;spacer&quot;&gt;&lt;a href=&quot;/splatoon3mix/%E7%94%A8%E8%AA%9E%E9%9B%86/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%88%E3%82%A5%E3%83%BC%E3%83%B3%E4%B8%96%E7%95%8C%E3%81%AE%E7%94%A8%E8%AA%9E#DeathTower_DethCatapa&quot; title=&quot;用語集/スプラトゥーン世界の用語&quot; class=&quot;rel-wiki-page&quot;&gt;&lt;span class=&quot;wikicolor&quot; style=&quot;color:#808080&quot;&gt;[詳細]&lt;/span&gt;&lt;/a&gt;">デスタワー</span>」「桟橋<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>」（後者は<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%B7%E3%82%A7%E3%82%B1%E3%83%8A%E3%83%80%E3%83%A0" title="サーモンラン/ステージ/シェケナダム" class="rel-wiki-page">シェケナダム</a>のと区別がつきにくい）と呼ばれ、特にノルマが高い場合は警戒しなければならない。<br />
この<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>が厄介な点として、</p>
<ul class="list1"><li>イクラコンテナから最も遠い</li>
<li>細道かつ袋小路になっているため、特に単独で向かうと付近・同地点で出現した<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a>に追い詰められやすい</li>
<li>「右下」の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>のターゲットにされやすい</li></ul>
<p>が挙げられる。味方の援護が期待できない場合は、なるべく遠距離から攻撃できる<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>で倒したいところである。<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88%E3%83%91%E3%83%83%E3%82%AF" title="ブキ/スペシャルウェポン/ジェットパック" class="rel-wiki-page">ジェットパック</a>の場合、船上で発動→<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%AA%E3%83%83%E3%82%BF%E3%83%BC4K" title="ブキ/リッター4K" class="rel-wiki-page">リッター4K</a>並の射程を活かして遠くから倒す→そのままイクラ回収or他のシャケを処理、というコンボができる。<br />
<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%88%E3%83%AA%E3%83%97%E3%83%AB%E3%83%88%E3%83%AB%E3%83%8D%E3%83%BC%E3%83%89" title="ブキ/スペシャルウェポン/トリプルトルネード" class="rel-wiki-page">トリプルトルネード</a>・<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%8A%E3%82%A4%E3%82%B9%E3%83%80%E3%83%9E" title="ブキ/スペシャルウェポン/ナイスダマ" class="rel-wiki-page">ナイスダマ</a>・<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%AB%E3%83%8B%E3%82%BF%E3%83%B3%E3%82%AF" title="ブキ/スペシャルウェポン/カニタンク" class="rel-wiki-page">カニタンク</a>は海を挟んだ向かい側から届く。<br />
長射程かつ連射が利くor一度に数段ずつ崩せるブキの場合、わざわざ<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>の麓まで行かなくても、海を挟んだ向かい側から処理することが可能。具体的にはイカのブキ。</p>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%97%E3%83%A9%E3%82%A4%E3%83%A0%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC" title="ブキ/プライムシューター" class="rel-wiki-page">プライムシューター</a> (かなりギリギリ)</li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/H3%E3%83%AA%E3%83%BC%E3%83%AB%E3%82%AC%E3%83%B3" title="ブキ/H3リールガン" class="rel-wiki-page">H3リールガン</a>(ギリギリだが、今作は減衰が掛かっても鍋1段を1発で崩せる)</li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%89%E3%83%A9%E3%82%A4%E3%83%96%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC" title="ブキ/ドライブワイパー" class="rel-wiki-page">ドライブワイパー</a>（これもギリギリ）</li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%87%E3%83%A5%E3%82%A2%E3%83%AB%E3%82%B9%E3%82%A4%E3%83%BC%E3%83%91%E3%83%BC" title="ブキ/デュアルスイーパー" class="rel-wiki-page">デュアルスイーパー</a>(通常射撃で良い。やっぱりギリギリ)</li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/.96%E3%82%AC%E3%83%AD%E3%83%B3" title="ブキ/.96ガロン" class="rel-wiki-page">.96ガロン</a>(ブレるので処理速度にややムラがある)</li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%9C%E3%83%88%E3%83%AB%E3%82%AC%E3%82%A4%E3%82%B6%E3%83%BC" title="ブキ/ボトルガイザー" class="rel-wiki-page">ボトルガイザー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88%E3%82%B9%E3%82%A4%E3%83%BC%E3%83%91%E3%83%BC" title="ブキ/ジェットスイーパー" class="rel-wiki-page">ジェットスイーパー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%AD%E3%83%B3%E3%82%B0%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC" title="ブキ/ロングブラスター" class="rel-wiki-page">ロングブラスター</a>(かなりギリギリ、あまりに隙が大きく水没しやすいため、実用性は低い)</li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%A9%E3%83%94%E3%83%83%E3%83%89%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC" title="ブキ/ラピッドブラスター" class="rel-wiki-page">ラピッドブラスター</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/R%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC%E3%82%A8%E3%83%AA%E3%83%BC%E3%83%88" title="ブキ/Rブラスターエリート" class="rel-wiki-page">Rブラスターエリート</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%97%E3%83%A9%E3%82%B9%E3%83%94%E3%83%8A%E3%83%BC" title="ブキ/スプラスピナー" class="rel-wiki-page">スプラスピナー</a>以外の<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%94%E3%83%8A%E3%83%BC%E5%B1%9E" title="ブキ/スピナー属" class="rel-wiki-page">スピナー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/14%E5%BC%8F%E7%AB%B9%E7%AD%92%E9%8A%83%E3%83%BB%E7%94%B2" title="ブキ/14式竹筒銃・甲" class="rel-wiki-page">14式竹筒銃・甲</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC" title="ブキ/クマサン印のチャージャー" class="rel-wiki-page">クマサン印のチャージャー</a>・<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC%E5%B1%9E" title="ブキ/スロッシャー属" class="rel-wiki-page">スロッシャー</a>・<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%88%E3%83%AA%E3%83%B3%E3%82%AC%E3%83%BC%E5%B1%9E" title="ブキ/ストリンガー属" class="rel-wiki-page">ストリンガー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%A8%E3%82%AF%E3%82%B9%E3%83%97%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC" title="ブキ/エクスプロッシャー" class="rel-wiki-page">エクスプロッシャー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AA%E3%83%BC%E3%83%90%E3%83%BC%E3%83%95%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC" title="ブキ/オーバーフロッシャー" class="rel-wiki-page">オーバーフロッシャー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B1%E3%83%AB%E3%83%93%E3%83%B3525" title="ブキ/ケルビン525" class="rel-wiki-page">ケルビン525</a>(構え撃ちで届くが、スライドの位置調整が難しいのでやらないほうがいい)</li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%88%E3%83%A9%E3%82%A4%E3%82%B9%E3%83%88%E3%83%AA%E3%83%B3%E3%82%AC%E3%83%BC" title="ブキ/トライストリンガー" class="rel-wiki-page">トライストリンガー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B8%E3%83%A0%E3%83%AF%E3%82%A4%E3%83%91%E3%83%BC" title="ブキ/ジムワイパー" class="rel-wiki-page">ジムワイパー</a></li>
<li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/R-PEN%EF%BC%8F5H" title="ブキ/R-PEN／5H" class="rel-wiki-page">R-PEN/5H</a>(ノンチャージでは届かないのでフルチャージ4発+ボムが素早い)</li></ul>
<p>また、<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5%E3%83%9C%E3%83%A0" title="ブキ/サブウェポン/スプラッシュボム" class="rel-wiki-page">スプラッシュボム</a>も届くので、3個投げれば処理可能。インク消費は非常に重いが、周りの状況が良い時には選択肢となりうる。</p>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">事例動画</div>
    <div class="fold-content visible-on-open"><div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">長射程<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B7%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC%E5%B1%9E" title="ブキ/シューター属" class="rel-wiki-page">シューター</a></div>
    <div class="fold-content visible-on-open"><p><script>window.twttr = (function(d, s, id) { var js, fjs = d.getElementsByTagName(s)[0], t = window.twttr || {}; if (d.getElementById(id)) return t; js = d.createElement(s); js.id = id; js.src = "https://platform.twitter.com/widgets.js"; fjs.parentNode.insertBefore(js, fjs); t._e = []; t.ready = function(f) { t._e.push(f); }; return t; }(document, "script", "twitter-wjs"));</script>
    <div class="lazy-dom-placeholder" data-content="&lt;div id=&quot;twitter-tweet-518fc66deea9d064d0a92eb73e4ea61b&quot; class=&quot;twitter-tweet&quot; style=&quot;margin-top: 10px; margin-bottom: 10px; min-height: 177px;&quot;&gt;&lt;/div&gt;&lt;script&gt; twttr.ready(function (){ twttr.widgets.createTweet( &#039;1064527539056476160&#039;, document.getElementById(&#039;twitter-tweet-518fc66deea9d064d0a92eb73e4ea61b&#039;), { }) }); &lt;/script&gt;">loading...</div><br />
<script>window.twttr = (function(d, s, id) { var js, fjs = d.getElementsByTagName(s)[0], t = window.twttr || {}; if (d.getElementById(id)) return t; js = d.createElement(s); js.id = id; js.src = "https://platform.twitter.com/widgets.js"; fjs.parentNode.insertBefore(js, fjs); t._e = []; t.ready = function(f) { t._e.push(f); }; return t; }(document, "script", "twitter-wjs"));</script>
    <div class="lazy-dom-placeholder" data-content="&lt;div id=&quot;twitter-tweet-bbeb0c1b1fd44e392c7ce2fdbd137e87&quot; class=&quot;twitter-tweet&quot; style=&quot;margin-top: 10px; margin-bottom: 10px; min-height: 177px;&quot;&gt;&lt;/div&gt;&lt;script&gt; twttr.ready(function (){ twttr.widgets.createTweet( &#039;1031274314723540992&#039;, document.getElementById(&#039;twitter-tweet-bbeb0c1b1fd44e392c7ce2fdbd137e87&#039;), { }) }); &lt;/script&gt;">loading...</div><br />
<script>window.twttr = (function(d, s, id) { var js, fjs = d.getElementsByTagName(s)[0], t = window.twttr || {}; if (d.getElementById(id)) return t; js = d.createElement(s); js.id = id; js.src = "https://platform.twitter.com/widgets.js"; fjs.parentNode.insertBefore(js, fjs); t._e = []; t.ready = function(f) { t._e.push(f); }; return t; }(document, "script", "twitter-wjs"));</script>
    <div class="lazy-dom-placeholder" data-content="&lt;div id=&quot;twitter-tweet-73c03186765e199c116224b68adc5fa0&quot; class=&quot;twitter-tweet&quot; style=&quot;margin-top: 10px; margin-bottom: 10px; min-height: 177px;&quot;&gt;&lt;/div&gt;&lt;script&gt; twttr.ready(function (){ twttr.widgets.createTweet( &#039;1074550257843789824&#039;, document.getElementById(&#039;twitter-tweet-73c03186765e199c116224b68adc5fa0&#039;), { }) }); &lt;/script&gt;">loading...</div><br />
<script>window.twttr = (function(d, s, id) { var js, fjs = d.getElementsByTagName(s)[0], t = window.twttr || {}; if (d.getElementById(id)) return t; js = d.createElement(s); js.id = id; js.src = "https://platform.twitter.com/widgets.js"; fjs.parentNode.insertBefore(js, fjs); t._e = []; t.ready = function(f) { t._e.push(f); }; return t; }(document, "script", "twitter-wjs"));</script>
    <div class="lazy-dom-placeholder" data-content="&lt;div id=&quot;twitter-tweet-142536b9b535b78e681c11b0195d962f&quot; class=&quot;twitter-tweet&quot; style=&quot;margin-top: 10px; margin-bottom: 10px; min-height: 177px;&quot;&gt;&lt;/div&gt;&lt;script&gt; twttr.ready(function (){ twttr.widgets.createTweet( &#039;1086662106479357953&#039;, document.getElementById(&#039;twitter-tweet-142536b9b535b78e681c11b0195d962f&#039;), { }) }); &lt;/script&gt;">loading...</div><br />
<script>window.twttr = (function(d, s, id) { var js, fjs = d.getElementsByTagName(s)[0], t = window.twttr || {}; if (d.getElementById(id)) return t; js = d.createElement(s); js.id = id; js.src = "https://platform.twitter.com/widgets.js"; fjs.parentNode.insertBefore(js, fjs); t._e = []; t.ready = function(f) { t._e.push(f); }; return t; }(document, "script", "twitter-wjs"));</script>
    <div class="lazy-dom-placeholder" data-content="&lt;div id=&quot;twitter-tweet-f61d6947467ccd3aa5af24db320235dd&quot; class=&quot;twitter-tweet&quot; style=&quot;margin-top: 10px; margin-bottom: 10px; min-height: 177px;&quot;&gt;&lt;/div&gt;&lt;script&gt; twttr.ready(function (){ twttr.widgets.createTweet( &#039;1102588548622901249&#039;, document.getElementById(&#039;twitter-tweet-f61d6947467ccd3aa5af24db320235dd&#039;), { }) }); &lt;/script&gt;">loading...</div></p>
</div>
</div>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open"><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%A9%E3%83%94%E3%83%83%E3%83%89%E3%83%96%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC" title="ブキ/ラピッドブラスター" class="rel-wiki-page">ラピッドブラスター</a></div>
    <div class="fold-content visible-on-open"><p><script>window.twttr = (function(d, s, id) { var js, fjs = d.getElementsByTagName(s)[0], t = window.twttr || {}; if (d.getElementById(id)) return t; js = d.createElement(s); js.id = id; js.src = "https://platform.twitter.com/widgets.js"; fjs.parentNode.insertBefore(js, fjs); t._e = []; t.ready = function(f) { t._e.push(f); }; return t; }(document, "script", "twitter-wjs"));</script>
    <div class="lazy-dom-placeholder" data-content="&lt;div id=&quot;twitter-tweet-34ed066df378efacc9b924ec161e7639&quot; class=&quot;twitter-tweet&quot; style=&quot;margin-top: 10px; margin-bottom: 10px; min-height: 177px;&quot;&gt;&lt;/div&gt;&lt;script&gt; twttr.ready(function (){ twttr.widgets.createTweet( &#039;1038408175349784576&#039;, document.getElementById(&#039;twitter-tweet-34ed066df378efacc9b924ec161e7639&#039;), { }) }); &lt;/script&gt;">loading...</div></p>
</div>
</div>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open"><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%8E%E3%83%BC%E3%83%81%E3%83%A9%E3%82%B947" title="ブキ/ノーチラス47" class="rel-wiki-page">ノーチラス47</a></div>
    <div class="fold-content visible-on-open"><p><script>window.twttr = (function(d, s, id) { var js, fjs = d.getElementsByTagName(s)[0], t = window.twttr || {}; if (d.getElementById(id)) return t; js = d.createElement(s); js.id = id; js.src = "https://platform.twitter.com/widgets.js"; fjs.parentNode.insertBefore(js, fjs); t._e = []; t.ready = function(f) { t._e.push(f); }; return t; }(document, "script", "twitter-wjs"));</script>
    <div class="lazy-dom-placeholder" data-content="&lt;div id=&quot;twitter-tweet-6de0f2761a44ff1e2ca60131058d8297&quot; class=&quot;twitter-tweet&quot; style=&quot;margin-top: 10px; margin-bottom: 10px; min-height: 177px;&quot;&gt;&lt;/div&gt;&lt;script&gt; twttr.ready(function (){ twttr.widgets.createTweet( &#039;1038406825542991873&#039;, document.getElementById(&#039;twitter-tweet-6de0f2761a44ff1e2ca60131058d8297&#039;), { }) }); &lt;/script&gt;">loading...</div></p>
</div>
</div>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open"><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%A8%E3%82%AF%E3%82%B9%E3%83%97%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC" title="ブキ/エクスプロッシャー" class="rel-wiki-page">エクスプロッシャー</a></div>
    <div class="fold-content visible-on-open"><p><script>window.twttr = (function(d, s, id) { var js, fjs = d.getElementsByTagName(s)[0], t = window.twttr || {}; if (d.getElementById(id)) return t; js = d.createElement(s); js.id = id; js.src = "https://platform.twitter.com/widgets.js"; fjs.parentNode.insertBefore(js, fjs); t._e = []; t.ready = function(f) { t._e.push(f); }; return t; }(document, "script", "twitter-wjs"));</script>
    <div class="lazy-dom-placeholder" data-content="&lt;div id=&quot;twitter-tweet-d1e39c9bda5c80ac3d8ea9d658163967&quot; class=&quot;twitter-tweet&quot; style=&quot;margin-top: 10px; margin-bottom: 10px; min-height: 177px;&quot;&gt;&lt;/div&gt;&lt;script&gt; twttr.ready(function (){ twttr.widgets.createTweet( &#039;1042056361356296192&#039;, document.getElementById(&#039;twitter-tweet-d1e39c9bda5c80ac3d8ea9d658163967&#039;), { }) }); &lt;/script&gt;">loading...</div></p>
</div>
</div>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open"><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AA%E3%83%BC%E3%83%90%E3%83%BC%E3%83%95%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC" title="ブキ/オーバーフロッシャー" class="rel-wiki-page">オーバーフロッシャー</a></div>
    <div class="fold-content visible-on-open"><p><script>window.twttr = (function(d, s, id) { var js, fjs = d.getElementsByTagName(s)[0], t = window.twttr || {}; if (d.getElementById(id)) return t; js = d.createElement(s); js.id = id; js.src = "https://platform.twitter.com/widgets.js"; fjs.parentNode.insertBefore(js, fjs); t._e = []; t.ready = function(f) { t._e.push(f); }; return t; }(document, "script", "twitter-wjs"));</script>
    <div class="lazy-dom-placeholder" data-content="&lt;div id=&quot;twitter-tweet-229aeb9e2ae66f2fac1149e5240b2fdd&quot; class=&quot;twitter-tweet&quot; style=&quot;margin-top: 10px; margin-bottom: 10px; min-height: 177px;&quot;&gt;&lt;/div&gt;&lt;script&gt; twttr.ready(function (){ twttr.widgets.createTweet( &#039;1086662497392709633&#039;, document.getElementById(&#039;twitter-tweet-229aeb9e2ae66f2fac1149e5240b2fdd&#039;), { }) }); &lt;/script&gt;">loading...</div></p>
</div>
</div>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open"><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%82%B9%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC" title="ブキ/クマサン印のスロッシャー" class="rel-wiki-page">クマサン印のスロッシャー</a></div>
    <div class="fold-content visible-on-open"><p><script>window.twttr = (function(d, s, id) { var js, fjs = d.getElementsByTagName(s)[0], t = window.twttr || {}; if (d.getElementById(id)) return t; js = d.createElement(s); js.id = id; js.src = "https://platform.twitter.com/widgets.js"; fjs.parentNode.insertBefore(js, fjs); t._e = []; t.ready = function(f) { t._e.push(f); }; return t; }(document, "script", "twitter-wjs"));</script>
    <div class="lazy-dom-placeholder" data-content="&lt;div id=&quot;twitter-tweet-e45823afe1e5120cec11fc4c379a0c67&quot; class=&quot;twitter-tweet&quot; style=&quot;margin-top: 10px; margin-bottom: 10px; min-height: 177px;&quot;&gt;&lt;/div&gt;&lt;script&gt; twttr.ready(function (){ twttr.widgets.createTweet( &#039;1008388525488631810&#039;, document.getElementById(&#039;twitter-tweet-e45823afe1e5120cec11fc4c379a0c67&#039;), { }) }); &lt;/script&gt;">loading...</div></p>
</div>
</div>
</div>
</div>
<p>コンテナから距離が非常に遠いためノルマの進捗がよろしくない状況では処理に向かうかどうかは残り時間に注意が必要。<br />
納品に関与できる時間が減ることや、残り時間次第では他のオオモノを<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;&lt;strong&gt;処理が困難な位置に湧いた&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC&quot; title=&quot;サーモンラン/シャケの種類/タワー&quot; class=&quot;rel-wiki-page&quot;&gt;タワー&lt;/a&gt;のこと&lt;/strong&gt;。&lt;br class=&quot;spacer&quot;&gt;特に&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC&quot; title=&quot;サーモンラン/シャケの種類/タワー&quot; class=&quot;rel-wiki-page&quot;&gt;タワー&lt;/a&gt;の攻撃の脅威度が増す満潮時に、メイン・&lt;a href=&quot;/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3&quot; title=&quot;ブキ/サブウェポン&quot; class=&quot;rel-wiki-page&quot;&gt;サブ&lt;/a&gt;での処理が困難な位置に湧くものがこう呼ばれやすい。&lt;br class=&quot;spacer&quot;&gt;とりわけ高キケン度では、処理が困難と判断した時点で速やかに&lt;a href=&quot;/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3&quot; title=&quot;ブキ/スペシャルウェポン&quot; class=&quot;rel-wiki-page&quot;&gt;スペシャル&lt;/a&gt;を切らねば、ゼンメツ一直線となりかねない。&lt;br class=&quot;spacer&quot;&gt;&lt;br class=&quot;spacer&quot;&gt;&lt;a href=&quot;/splatoon3mix/%E7%94%A8%E8%AA%9E%E9%9B%86/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%88%E3%82%A5%E3%83%BC%E3%83%B3%E4%B8%96%E7%95%8C%E3%81%AE%E7%94%A8%E8%AA%9E#DeathTower_DethCatapa&quot; title=&quot;用語集/スプラトゥーン世界の用語&quot; class=&quot;rel-wiki-page&quot;&gt;&lt;span class=&quot;wikicolor&quot; style=&quot;color:#808080&quot;&gt;[詳細]&lt;/span&gt;&lt;/a&gt;">デスタワー</span>の位置に誘導してしまうとそれらのオオモノをコンテナに連れ帰り納品するだけの時間が足りなくなる。<br />
上記の長射程ブキでもない場合はかなり早い段階で直接処理に向かうことを諦め、<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>で対応するか耐えるかの選択肢のみにしたほうが良い。</p>
<h4 id="h4_content_15_0" >左奥に湧く<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%82%AD%E3%83%A5%E3%82%A6" title="サーモンラン/シャケの種類/テッキュウ" class="rel-wiki-page">テッキュウ</a>について</h4>

<p><span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;&lt;strong&gt;処理が困難な位置に湧いた&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC&quot; title=&quot;サーモンラン/シャケの種類/タワー&quot; class=&quot;rel-wiki-page&quot;&gt;タワー&lt;/a&gt;のこと&lt;/strong&gt;。&lt;br class=&quot;spacer&quot;&gt;特に&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC&quot; title=&quot;サーモンラン/シャケの種類/タワー&quot; class=&quot;rel-wiki-page&quot;&gt;タワー&lt;/a&gt;の攻撃の脅威度が増す満潮時に、メイン・&lt;a href=&quot;/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3&quot; title=&quot;ブキ/サブウェポン&quot; class=&quot;rel-wiki-page&quot;&gt;サブ&lt;/a&gt;での処理が困難な位置に湧くものがこう呼ばれやすい。&lt;br class=&quot;spacer&quot;&gt;とりわけ高キケン度では、処理が困難と判断した時点で速やかに&lt;a href=&quot;/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3&quot; title=&quot;ブキ/スペシャルウェポン&quot; class=&quot;rel-wiki-page&quot;&gt;スペシャル&lt;/a&gt;を切らねば、ゼンメツ一直線となりかねない。&lt;br class=&quot;spacer&quot;&gt;&lt;br class=&quot;spacer&quot;&gt;&lt;a href=&quot;/splatoon3mix/%E7%94%A8%E8%AA%9E%E9%9B%86/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%88%E3%82%A5%E3%83%BC%E3%83%B3%E4%B8%96%E7%95%8C%E3%81%AE%E7%94%A8%E8%AA%9E#DeathTower_DethCatapa&quot; title=&quot;用語集/スプラトゥーン世界の用語&quot; class=&quot;rel-wiki-page&quot;&gt;&lt;span class=&quot;wikicolor&quot; style=&quot;color:#808080&quot;&gt;[詳細]&lt;/span&gt;&lt;/a&gt;">デスタワー</span>に倣ってデス<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%82%AD%E3%83%A5%E3%82%A6" title="サーモンラン/シャケの種類/テッキュウ" class="rel-wiki-page">テッキュウ</a>と呼ぶことがあるが、<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;&lt;strong&gt;処理が困難な位置に湧いた&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC&quot; title=&quot;サーモンラン/シャケの種類/タワー&quot; class=&quot;rel-wiki-page&quot;&gt;タワー&lt;/a&gt;のこと&lt;/strong&gt;。&lt;br class=&quot;spacer&quot;&gt;特に&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC&quot; title=&quot;サーモンラン/シャケの種類/タワー&quot; class=&quot;rel-wiki-page&quot;&gt;タワー&lt;/a&gt;の攻撃の脅威度が増す満潮時に、メイン・&lt;a href=&quot;/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3&quot; title=&quot;ブキ/サブウェポン&quot; class=&quot;rel-wiki-page&quot;&gt;サブ&lt;/a&gt;での処理が困難な位置に湧くものがこう呼ばれやすい。&lt;br class=&quot;spacer&quot;&gt;とりわけ高キケン度では、処理が困難と判断した時点で速やかに&lt;a href=&quot;/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3&quot; title=&quot;ブキ/スペシャルウェポン&quot; class=&quot;rel-wiki-page&quot;&gt;スペシャル&lt;/a&gt;を切らねば、ゼンメツ一直線となりかねない。&lt;br class=&quot;spacer&quot;&gt;&lt;br class=&quot;spacer&quot;&gt;&lt;a href=&quot;/splatoon3mix/%E7%94%A8%E8%AA%9E%E9%9B%86/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%88%E3%82%A5%E3%83%BC%E3%83%B3%E4%B8%96%E7%95%8C%E3%81%AE%E7%94%A8%E8%AA%9E#DeathTower_DethCatapa&quot; title=&quot;用語集/スプラトゥーン世界の用語&quot; class=&quot;rel-wiki-page&quot;&gt;&lt;span class=&quot;wikicolor&quot; style=&quot;color:#808080&quot;&gt;[詳細]&lt;/span&gt;&lt;/a&gt;">デスタワー</span>と比べかなり温情。<br />
発射台が<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;&lt;strong&gt;処理が困難な位置に湧いた&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC&quot; title=&quot;サーモンラン/シャケの種類/タワー&quot; class=&quot;rel-wiki-page&quot;&gt;タワー&lt;/a&gt;のこと&lt;/strong&gt;。&lt;br class=&quot;spacer&quot;&gt;特に&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC&quot; title=&quot;サーモンラン/シャケの種類/タワー&quot; class=&quot;rel-wiki-page&quot;&gt;タワー&lt;/a&gt;の攻撃の脅威度が増す満潮時に、メイン・&lt;a href=&quot;/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3&quot; title=&quot;ブキ/サブウェポン&quot; class=&quot;rel-wiki-page&quot;&gt;サブ&lt;/a&gt;での処理が困難な位置に湧くものがこう呼ばれやすい。&lt;br class=&quot;spacer&quot;&gt;とりわけ高キケン度では、処理が困難と判断した時点で速やかに&lt;a href=&quot;/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3&quot; title=&quot;ブキ/スペシャルウェポン&quot; class=&quot;rel-wiki-page&quot;&gt;スペシャル&lt;/a&gt;を切らねば、ゼンメツ一直線となりかねない。&lt;br class=&quot;spacer&quot;&gt;&lt;br class=&quot;spacer&quot;&gt;&lt;a href=&quot;/splatoon3mix/%E7%94%A8%E8%AA%9E%E9%9B%86/%E3%82%B9%E3%83%97%E3%83%A9%E3%83%88%E3%82%A5%E3%83%BC%E3%83%B3%E4%B8%96%E7%95%8C%E3%81%AE%E7%94%A8%E8%AA%9E#DeathTower_DethCatapa&quot; title=&quot;用語集/スプラトゥーン世界の用語&quot; class=&quot;rel-wiki-page&quot;&gt;&lt;span class=&quot;wikicolor&quot; style=&quot;color:#808080&quot;&gt;[詳細]&lt;/span&gt;&lt;/a&gt;">デスタワー</span>処理ポイントより更に手前側(船側)に置かれるため、ここに湧いた<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%82%AD%E3%83%A5%E3%82%A6" title="サーモンラン/シャケの種類/テッキュウ" class="rel-wiki-page">テッキュウ</a>は海岸からの移動距離(砲撃間隔)が非常に長くなっている。<br />
1サイクルに30秒程度？かかるためコンテナ周りへの影響が非常に小さく、<strong>単体湧きの場合は</strong>放置も十分に考えられる。<br />
特に残り30秒を切っている場合はわざわざ倒しに行く必要は無いだろう。</p>
<h4 id="h4_content_16_0" >船外の右下<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA" title="サーモンラン/シャケの種類/コウモリ" class="rel-wiki-page">コウモリ</a>、左下<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA" title="サーモンラン/シャケの種類/コウモリ" class="rel-wiki-page">コウモリ</a>について</h4>

<p>非常に厄介。<br />
地形に阻まれて<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;&lt;strong&gt;&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA&quot; title=&quot;サーモンラン/シャケの種類/コウモリ&quot; class=&quot;rel-wiki-page&quot;&gt;コウモリ&lt;/a&gt;が撃ち出す砲弾&lt;/strong&gt;のこと。撃ち落さないと&lt;a href=&quot;/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%A2%E3%83%A1%E3%83%95%E3%83%A9%E3%82%B7&quot; title=&quot;ブキ/スペシャルウェポン/アメフラシ&quot; class=&quot;rel-wiki-page&quot;&gt;アメフラシ&lt;/a&gt;が発生する。">雨玉</span>に気付きにくく、気付いていても地形に阻まれて<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;&lt;strong&gt;&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA&quot; title=&quot;サーモンラン/シャケの種類/コウモリ&quot; class=&quot;rel-wiki-page&quot;&gt;コウモリ&lt;/a&gt;が撃ち出す砲弾&lt;/strong&gt;のこと。撃ち落さないと&lt;a href=&quot;/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%A2%E3%83%A1%E3%83%95%E3%83%A9%E3%82%B7&quot; title=&quot;ブキ/スペシャルウェポン/アメフラシ&quot; class=&quot;rel-wiki-page&quot;&gt;アメフラシ&lt;/a&gt;が発生する。">雨玉</span>を本体に返しにくい。また、寄せるのにも時間がかかるし、寄せるのも難しいのでそもそも野良では寄せられない事が殆ど。<br />
ブラコ通常昼では船外<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA" title="サーモンラン/シャケの種類/コウモリ" class="rel-wiki-page">コウモリ</a>を如何に扱うかというのも重要。<br />
船外に<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA" title="サーモンラン/シャケの種類/コウモリ" class="rel-wiki-page">コウモリ</a>が居るなら<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;&lt;strong&gt;&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA&quot; title=&quot;サーモンラン/シャケの種類/コウモリ&quot; class=&quot;rel-wiki-page&quot;&gt;コウモリ&lt;/a&gt;が撃ち出す砲弾&lt;/strong&gt;のこと。撃ち落さないと&lt;a href=&quot;/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%A2%E3%83%A1%E3%83%95%E3%83%A9%E3%82%B7&quot; title=&quot;ブキ/スペシャルウェポン/アメフラシ&quot; class=&quot;rel-wiki-page&quot;&gt;アメフラシ&lt;/a&gt;が発生する。">雨玉</span>を撃墜し損ねないように十分警戒しておきたい。長射程<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC%E5%B1%9E" title="ブキ/チャージャー属" class="rel-wiki-page">チャージャー</a>,<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%94%E3%83%8A%E3%83%BC%E5%B1%9E" title="ブキ/スピナー属" class="rel-wiki-page">スピナー</a>や<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%88%E3%83%A9%E3%82%A4%E3%82%B9%E3%83%88%E3%83%AA%E3%83%B3%E3%82%AC%E3%83%BC" title="ブキ/トライストリンガー" class="rel-wiki-page">トライストリンガー</a>などのブキは、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA" title="サーモンラン/シャケの種類/コウモリ" class="rel-wiki-page">コウモリ</a>を直接殴って処理することも選択肢に入れておこう。</p>
<h4 id="h4_content_17_0" >地形の利用</h4>

<p><strong>移動ルート</strong></p>
<ul class="list1"><li>左の桟橋と中央の桟橋の突き当りはイカダッシュ＋ジャンプで隣に渡れる。</li>
<li>左右下に立った<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a>からイカダッシュ＋ジャンプで船上に戻れる。</li></ul>
<p><strong><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>にボムを投げ込める場所</strong></p>
<ul class="list1"><li>右側[コーン]1体目・1回目の発射時（リフト正面で発射）<br />
リフト乗り場の上り坂から立ち投げで届く。</li>
<li>同2回目の発射時（船首側に移動）<br />
船首から立ち投げでちょうど届く。</li>
<li>船尾側[ウインナー]2体目（船尾右の高台直上で発射）<br />
出現位置こそ近いものの滞空高度が高く設定されており、足元から投げ込むのと手前の高台から投げ込むのとであまり難易度が変わらない。なお今作では船尾側<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>は右坂→右高台の順に出現する。</li>
<li>左側[アスパラ]1体目・1回目の発射時（左奥の桟橋で発射）<br />
リフト乗り場から助走投げで届く。なお今作では左側<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>は左奥桟橋→船首付近の順に出現する。</li>
<li>同2回目の発射時（左奥の桟橋付近やや右で発射）<br />
リフト乗り場から立ち投げで届く。</li></ul>
<p><strong><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%80%E3%82%A4%E3%83%90%E3%83%BC" title="サーモンラン/シャケの種類/ダイバー" class="rel-wiki-page">ダイバー</a>の誘導に有効な場所</strong></p>
<ul class="list1"><li>金網上およびプロペラリフト上に立つことで<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%80%E3%82%A4%E3%83%90%E3%83%BC" title="サーモンラン/シャケの種類/ダイバー" class="rel-wiki-page">ダイバー</a>のターゲットから外れ、コンテナ側に寄せることができる。</li></ul>
<p><strong><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャルウェポン</a></strong></p>
<ul class="list1"><li><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88%E3%83%91%E3%83%83%E3%82%AF" title="ブキ/スペシャルウェポン/ジェットパック" class="rel-wiki-page">ジェットパック</a>使用時、外周から金網付近程度の高さならBボタンで上昇して船上に戻れる。</li>
<li>左手前の桟橋と中央の桟橋の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>に対して、<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%AB%E3%83%8B%E3%82%BF%E3%83%B3%E3%82%AF" title="ブキ/スペシャルウェポン/カニタンク" class="rel-wiki-page">カニタンク</a>の<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B5%E3%83%96%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/サブウェポン" class="rel-wiki-page">サブ</a>射撃が船上から届く。</li>
<li>左奥L字の桟橋に<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>が2体いるとき、<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%8A%E3%82%A4%E3%82%B9%E3%83%80%E3%83%9E" title="ブキ/スペシャルウェポン/ナイスダマ" class="rel-wiki-page">ナイスダマ</a>をその中間あたりに着弾させると2体を一度に巻き込むことができる。</li></ul>
<p><strong>イクラ投げ</strong></p>
<ul class="list1"><li>左下低地、右下低地からコンテナまでイクラ投げジャンプで届く。</li>
<li>船首の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a>、中央カンケツセン(B)の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a>、左下低地の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a>、右下低地の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a>からコンテナまで立ち投げで届く。</li>
<li>左リフト前の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a>からコンテナまで立ち投げでは届かないが、助走投げで届く。</li></ul>
<p><strong>オオモノリフト</strong> <a class="anchor" name ="salmonlift"></a><br />
シャケを未稼働のリフト上に誘導し、リフトに乗った瞬間にプロペラを稼働させ、リフトが上がりきると同時にプレイヤーが船上に移動すると、シャケはプレイヤーを追ってリフトから船上に直接移動する。これを利用してオオモノシャケを素早くコンテナ近くまで寄せることができる。今作で狙うことが出来るのは主に<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a>と霧の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/キンシャケ" class="rel-wiki-page">キンシャケ</a>。<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a>はリフト上で一時停止させる方法もあるが、移動を再開するまでプロペラを回し続ける必要がある。今作では<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a>がリフト上でもボムを起動するようになったため、船上に移動させるには遠くからボムなどでリフトを稼働させる必要がある。</p>
<h3 id="h3_content_1_2" class="heading-after-first">満潮時  <a class="anchor_super" name ="d52a90e1"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3&id=d52a90e1" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<p>満潮時は船の上のみで戦うことになる。<br />
イクラコンテナ前の金網がいきなり水没ポイントと化す。不慣れなイカは、開幕で転落しやすいため要注意。金網をすり抜けてしまう前に確実に[ZL]を離す、もしくは上を歩いているときにうっかり押さないように気をつけよう。<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%86%E3%82%A4%E3%82%AA%E3%82%A6%E3%82%A4%E3%82%AB" title="ブキ/スペシャルウェポン/テイオウイカ" class="rel-wiki-page">テイオウイカ</a>を発動した瞬間水没、なんて事にはならないように。</p>
<p>船上は縦に長く、敵の出現が常に船尾側[ウィンナー]からに限られ、オオモノが全て同じ方向に固まる都合上、船尾に居座った<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>・<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>を他のオオモノが壁となって守る布陣を打開することが今作では非常に難しい。<a id="notetext_1"  class="note_super tooltip"
            data-tippy-theme="light"
            data-tippy-allowHTML="true"
            data-tippy-interactive="true"
            data-tippy-content="&lt;p&gt;前作では船首側からのハイパープレッサーが極めて有効だった。&lt;/p&gt;&lt;div style=&quot;text-align: right;&quot;&gt;&lt;a href=&quot;#notefoot_1&quot;&gt;脚注 *1 へ&lt;/a&gt;&lt;/div&gt;">*1</a><br />
特に全員が金網よりコンテナ側にいる場合この状況になりやすいため、最低でも一人は金網より船尾側でオオモノを間引いている状態が好ましい。<br />
高すぎる寄せ意識が仇となりやすく、<strong>初動でコンテナから離れず味方に「カモン！」を出し続ける</strong>といったプレイが問題視されることも多い潮位である。寄せだけにこだわりすぎず、船上の安全確保も忘れない柔軟なプレイを心がけよう。<br />
船尾側で処理すると納品が難しくなりやすいが、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#snatcher" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">タマヒロイ</a>のルートを早めに確認してコンテナに近づけてくれる<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#snatcher" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">タマヒロイ</a>を活用して納品を進めよう。</p>
<p><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>での打開は<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%A1%E3%82%AC%E3%83%9B%E3%83%B3%E3%83%AC%E3%83%BC%E3%82%B6%E3%83%BC5.1ch" title="ブキ/スペシャルウェポン/メガホンレーザー5.1ch" class="rel-wiki-page">メガホンレーザー5.1ch</a>は他のオオモノにターゲットを吸われやすく、<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%88%E3%83%AA%E3%83%97%E3%83%AB%E3%83%88%E3%83%AB%E3%83%8D%E3%83%BC%E3%83%89" title="ブキ/スペシャルウェポン/トリプルトルネード" class="rel-wiki-page">トリプルトルネード</a>はガイド装置を他のシャケに吸着されやすい。<br />
打開策として中腹に立った<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8F%E3%82%B7%E3%83%A9" title="サーモンラン/シャケの種類/ハシラ" class="rel-wiki-page">ハシラ</a>や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%8A%E3%83%99%E3%83%96%E3%82%BF" title="サーモンラン/シャケの種類/ナベブタ" class="rel-wiki-page">ナベブタ</a>上から<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>を発動する、次善の策として前線が下がる前に<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>を<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;&lt;strong&gt;&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89&quot; title=&quot;サーモンラン/シャケの種類/カタパッド&quot; class=&quot;rel-wiki-page&quot;&gt;カタパッド&lt;/a&gt;のミサイルポッドを半分だけ破壊して倒さないでおくこと&lt;/strong&gt;。&lt;br class=&quot;spacer&quot;&gt;敢えて倒すのが面倒な&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89&quot; title=&quot;サーモンラン/シャケの種類/カタパッド&quot; class=&quot;rel-wiki-page&quot;&gt;カタパッド&lt;/a&gt;の被害を半減しつつ、他のオオモノシャケを狙う戦法。&lt;br class=&quot;spacer&quot;&gt;この戦法の代償として、&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89&quot; title=&quot;サーモンラン/シャケの種類/カタパッド&quot; class=&quot;rel-wiki-page&quot;&gt;カタパッド&lt;/a&gt;から金イクラを手に入れることができなくなる。&lt;br class=&quot;spacer&quot;&gt;他のオオモノをたくさん倒してカバーすることが必要。">片翼</span>化しておく、船首に立って<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>の攻撃を引き付ける囮となる、などの手がある。<br />
<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88%E3%83%91%E3%83%83%E3%82%AF" title="ブキ/スペシャルウェポン/ジェットパック" class="rel-wiki-page">ジェットパック</a>や<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%86%E3%82%A4%E3%82%AA%E3%82%A6%E3%82%A4%E3%82%AB" title="ブキ/スペシャルウェポン/テイオウイカ" class="rel-wiki-page">テイオウイカ</a>で船尾まで強襲する場合、帰還時にコンテナ周りがカオス化していては元も子もないので、なるべく手前のオオモノを間引きながらの前進を意識したい。<br />
いずれにせよ、船首側に追い詰められ<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>に攻撃されながらの打開は難しいため、常に先手を打って処理していきたい。</p>
<p>終盤オオモノは片付いたが納品が済んでおらず、船腹に金イクラが溜まってしまっている場合、<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>で<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ザコシャケ</a>を一掃しながら納品を行うのも一つの手だ。</p>
<h3 id="h3_content_1_3" class="heading-after-first">干潮時  <a class="anchor_super" name ="ff6255eb"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3&id=ff6255eb" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<p>干潮時は真ん中の潮だまり(タイドプールともいう)を迂回してシャケを倒していく。向かって右[アスパラ]の方角からも攻めてくるものの、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%B7%E3%82%A7%E3%82%B1%E3%83%8A%E3%83%80%E3%83%A0" title="サーモンラン/ステージ/シェケナダム" class="rel-wiki-page">シェケナダム</a>よりも見る方向が減るので連携がしやすい。<br />
実は<span class="wikicolor" style="color:Red"><strong><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88%E3%83%91%E3%83%83%E3%82%AF" title="ブキ/スペシャルウェポン/ジェットパック" class="rel-wiki-page">ジェットパック</a>は真ん中の潮だまりに落ちる事無く強引に突破できる。</strong></span><br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%BF%E3%83%AF%E3%83%BC" title="サーモンラン/シャケの種類/タワー" class="rel-wiki-page">タワー</a>や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>は奥に陣取っているため潮だまりのド真ん中でまとめて撃破するという芸当も可能。<br />
同時に<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%98%E3%83%93" title="サーモンラン/シャケの種類/ヘビ" class="rel-wiki-page">ヘビ</a>や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a>の脅威に怯える事も無くなるので打開の手段として頭の片隅に入れておこう。<br />
ただあまりモタモタしているとミサイルの直撃を受ける危険性がある。海も緑色で見えづらいのでそこだけは注意。</p>
<p>時折物議を醸すプレイとして、<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC%E5%B1%9E" title="ブキ/チャージャー属" class="rel-wiki-page">チャージャー</a>などの長射程ブキを持ったプレイヤーが船首に居座って上からの支援射撃に徹するというものがある。<br />
いくら長射程といえども遠方の敵には攻撃が届かず、本来長射程が処理するべき<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%90%E3%82%AF%E3%83%80%E3%83%B3" title="サーモンラン/シャケの種類/バクダン" class="rel-wiki-page">バクダン</a>などが戦場に溜まりがちになり、もちろん納品の人手も1人分減るといったデメリットのためあまりよくないとされることが多い。</p>
<p><span class="wikicolor" style="color:Red">満潮から干潮へ水位変化する場合、カウントが5秒を切るまでは絶対に船首から飛び降りないように。</span><br />
どうしても早めに降りたい場合は右下エリアに降りよう。<br />
干潮かつ夜WAVEの予兆が発生している場合は我先にと飛び降りず、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%89%E3%82%B9%E3%82%B3%E3%82%A4%E5%A4%A7%E9%87%8F%E7%99%BA%E7%94%9F" title="サーモンラン/特殊な状況/ドスコイ大量発生" class="rel-wiki-page">ドスコイ大量発生</a>で有用な船首キャノンを活用するためにギリギリまで船首で待機するという選択も考えられる。</p>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E5%B7%A8%E5%A4%A7%E3%82%BF%E3%83%84%E3%83%9E%E3%82%AD" title="サーモンラン/特殊な状況/巨大タツマキ" class="rel-wiki-page">巨大タツマキ</a>では船上に乗せるためのイクラ投げの技術が問われる。限定テクニックとして下から直接船首へ投げ込むこともできる。<br />
干潮のコンテナから試しうちラインおおよそ1～2本ほど船首側へ接近し、A(L)を押して投げるまでのタイムラグの間にジャンプすることで慣性が働きギリギリ上に乗せることができる。<br />
通常のジャンプ中に投擲では届かないので練習が必要だが、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E5%B7%A8%E5%A4%A7%E3%82%BF%E3%83%84%E3%83%9E%E3%82%AD" title="サーモンラン/特殊な状況/巨大タツマキ" class="rel-wiki-page">巨大タツマキ</a>自体誰かが回線落ちでもしていなければ楽勝なWAVEなので2箱目でついでに練習しておくのもいいだろう。</p>
<p>ただし向かって左側[コーン]は1投目を地形に沿ってではなく海をまたぐように投げると角度がつくのでリフトの場所から簡単にカゴ横に投げることができ<br />
反対の向かって右側[アスパラ]も同様に海をまたぐように投げれば2投目でカゴ横ないし直接納品が可能なので、船首に投げ込む必要があるのは干潮正面側[カボチャ]の箱だけである。</p>
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
<h2 id="h2_content_1_4" class="heading-after-first">特殊な状況  <a class="anchor_super" name ="f4cf1ea5"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3&id=f4cf1ea5" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<h3 id="h3_content_1_5" class="heading-after-first"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>  <a class="anchor_super" name ="d7acea18"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3&id=d7acea18" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<div class="includex" style="padding:0;margin:0;"> <a class="anchor_super" id="zf21d520005fe9127f6b4eb7822983d9f" href="#zf21d520005fe9127f6b4eb7822983d9f" title="zf21d520005fe9127f6b4eb7822983d9f"></a></div>
<div style="text-align:right"><a class="ext" href="/splatoon3mix/?cmd=edit&amp;page=サーモンラン/特殊な状況/ラッシュ&amp;id=a65351ab" title="部分編集:サーモンラン/特殊な状況/ラッシュ&amp;id=a65351ab"  rel="nofollow">[編集]<span class="system-icon ext pukiwiki-open-uri" data-href="/splatoon3mix/?cmd=edit&amp;page=サーモンラン/特殊な状況/ラッシュ&amp;id=a65351ab" data-frame="_blank"></span></a></div>
<p>ドンブラコでは、<strong><span class="wikicolor" style="color:red">右</span>の金網周辺</strong>が主な定位置となる。<br />
ここで待機することで、船尾方向からやってくるシャケの流れを船上で1つにまとめることができ、スムーズな迎撃が可能となる。<br />
<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC%E5%B1%9E" title="ブキ/ローラー属" class="rel-wiki-page">ローラー</a>や短射程ブキが前方の坂に構え、長射程ブキが金網上に構えることで射線が塞がれにくく、範囲攻撃ブキがカンケツセンに立つことで横から範囲攻撃を撒くこともでき、安全性が高まる。<br />
前寄りかつ長射程ブキが射程を活かせるため、通常潮では後述するシャケの出現上限に達する時間を比較的短くできる利点もある。<br />
しかし金イクラの多くが船腹に落ち、コンテナまで金網を挟むため納品には手間がかかる。インク切れの近いプレイヤーがイクラを拾って後退、インク回復しつつ再び前に出る、という動きを順番に繰り返す形になる。<br />
ターゲットが金網より後ろにいると<strong>両方の橋からシャケが攻めてきて</strong>挟み撃ちにあってしまう。特に満潮時に起こりやすい。この挟み撃ちは右金網、または船の右端に近いほど起きにくくなる。金網より後ろに押し込まれても、右に寄ることでシャケの進行ルートを1つにまとめることができると覚えておこう。<br />
ただし、定位置にしっかり着いていても、狂シャケは右から向かってくれるにもかかわらず<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/キンシャケ" class="rel-wiki-page">キンシャケ</a>だけは左から回ってくるというアドリブ走行をかましてくることがあるので過信はできない。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/キンシャケ" class="rel-wiki-page">キンシャケ</a>をコンテナに寄せたい場合、壁役がザコを金網付近で倒しつつ<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/キンシャケ" class="rel-wiki-page">キンシャケ</a>だけをかわして通せばよい。</p>
<p>次点が金網より後ろの<strong>コンテナ横</strong>で待機し両金網を渡ってきたシャケを一点で迎え撃つ形で、金網より後ろに押し込まれた場合に構えることになる。<br />
コンテナに近いため納品はしやすくなるが、正面からはシャケが坂を駆け上り、左からは回り込んでくる形のため、シャケを射線内に捉えられる時間が短く、安全範囲が狭い。<br />
納品自体はしやすくても、通常潮では経路が長いためシャケが出現上限になっている時間が長く、初めからここに構えてしまうと沸き方向次第では金イクラの絶対数がノルマに届かない場合も。<br />
満潮かつ<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%80%E3%82%A4%E3%83%8A%E3%83%A2%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC" title="ブキ/ダイナモローラー" class="rel-wiki-page">ダイナモローラー</a>など迎撃力の高いブキ編成であればこれらのデメリットはある程度カバーされる。<br />
しかし一般的なレベル帯の野良バイトで右金網に寄らず初めからコンテナ付近に居座ろうとするプレイヤーはリスク覚悟であえてこの作戦をチョイスしているのではなく、ただ単に「右金網の定石を知らないからなんとなくコンテナ付近に溜まっているだけ」のプレイヤーであることが多いと思われるので注意。<br />
船首先端付近でカモンを押して背水の陣で迎え撃とうという動きを見せるプレイヤーも稀にいるが、左右通路から殺到するシャケを捌き切ることが非常に難しいためNG。</p>
<p>敵の侵攻ルートが正面方向に限られるため<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%AB%E3%83%8B%E3%82%BF%E3%83%B3%E3%82%AF" title="ブキ/スペシャルウェポン/カニタンク" class="rel-wiki-page">カニタンク</a>の有効性が高い。分厚い弾幕でシャケを蹴散らして拠点防衛できるが、ノルマ未達成の場合は<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/キンシャケ" class="rel-wiki-page">キンシャケ</a>をあまり遠くで倒しすぎないように注意。上手に射線をそらして削りながら寄せよう。<br />
すでにコンテナ横まで押し込まれている場合は射程が活かせず、金網を渡ろうにも<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/キンシャケ" class="rel-wiki-page">キンシャケ</a>に落とされかねないので、コンテナ横で球体モードで耐えるしかない。</p>
<p>通常時は桟橋側からシャケが湧く際、コンテナに至るまでの経路が長いためシャケの出現数上限に達しやすく、結果として<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/キンシャケ" class="rel-wiki-page">キンシャケ</a>の出現数が少なくなってしまうことがある。<br />
射程の長いブキは狂シャケを遠くから早めに間引くことで<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/キンシャケ" class="rel-wiki-page">キンシャケ</a>の出現を促すことを意識したい。<br />
船上で倒した<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/キンシャケ" class="rel-wiki-page">キンシャケ</a>の金イクラが船外に落ちてしまうことがあり、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#snatcher" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">タマヒロイ</a>の方向によっては回収が難しい点もネックとなる。<br />
落下した金イクラを不用意に拾いに行った先でヒカリバエがついてしまうと即デスほぼ確定となり、戦線復帰にかなり時間がかかってしまうので気をつけたい。</p>
<p><strong>■<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="主に&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;&lt;strong&gt;壁に塗られたインクに潜る様子のこと&lt;/strong&gt;。&lt;br class=&quot;spacer&quot;&gt;&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;では自分をターゲットとしているシャケらをしばらくの間釘付けにできるが、あまり長くやりすぎると&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB&quot; title=&quot;サーモンラン/シャケの種類/グリル&quot; class=&quot;rel-wiki-page&quot;&gt;グリル&lt;/a&gt;のターゲット変更や&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1&quot; title=&quot;サーモンラン/シャケの種類/ザコシャケ&quot; class=&quot;rel-wiki-page&quot;&gt;ザコシャケ&lt;/a&gt;の大ジャンプにより痛い目にあう。&lt;br class=&quot;spacer&quot;&gt;また、セミ中は攻撃できないため、自軍の火力が減るという重大な欠点もある。&lt;br class=&quot;spacer&quot;&gt;「金イクラが大量だが敵の勢いが激しく納品が捗らない状況で、自分が離れた地点でセミをし敵を誘導し、その隙に味方に納品をしてもらう」「デスした味方がウキワになるまでのタイムラグを凌ぐ」など、場面や使いようによっては非常に有用。&lt;br class=&quot;spacer&quot;&gt;&lt;br class=&quot;spacer&quot;&gt;&lt;a href=&quot;/splatoon3mix/%E7%94%A8%E8%AA%9E%E9%9B%86/%E5%AF%BE%E6%88%A6%E9%96%A2%E9%80%A3%E7%94%A8%E8%AA%9E#k58821ab&quot; title=&quot;用語集/対戦関連用語&quot; class=&quot;rel-wiki-page&quot;&gt;&lt;span class=&quot;wikicolor&quot; style=&quot;color:#808080&quot;&gt;[詳細]&lt;/span&gt;&lt;/a&gt;">セミ</span>スポット、安全地帯について</strong><br />
このステージでは<span class="tooltip"
    data-tippy-theme="light"
    data-tippy-interactive="true"
    data-tippy-allowHTML="true"
    data-tippy-content="主に&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;で使われる用語。&lt;br class=&quot;spacer&quot;&gt;&lt;strong&gt;壁に塗られたインクに潜る様子のこと&lt;/strong&gt;。&lt;br class=&quot;spacer&quot;&gt;&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3&quot; title=&quot;サーモンラン&quot; class=&quot;rel-wiki-page&quot;&gt;サーモンラン&lt;/a&gt;では自分をターゲットとしているシャケらをしばらくの間釘付けにできるが、あまり長くやりすぎると&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB&quot; title=&quot;サーモンラン/シャケの種類/グリル&quot; class=&quot;rel-wiki-page&quot;&gt;グリル&lt;/a&gt;のターゲット変更や&lt;a href=&quot;/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1&quot; title=&quot;サーモンラン/シャケの種類/ザコシャケ&quot; class=&quot;rel-wiki-page&quot;&gt;ザコシャケ&lt;/a&gt;の大ジャンプにより痛い目にあう。&lt;br class=&quot;spacer&quot;&gt;また、セミ中は攻撃できないため、自軍の火力が減るという重大な欠点もある。&lt;br class=&quot;spacer&quot;&gt;「金イクラが大量だが敵の勢いが激しく納品が捗らない状況で、自分が離れた地点でセミをし敵を誘導し、その隙に味方に納品をしてもらう」「デスした味方がウキワになるまでのタイムラグを凌ぐ」など、場面や使いようによっては非常に有用。&lt;br class=&quot;spacer&quot;&gt;&lt;br class=&quot;spacer&quot;&gt;&lt;a href=&quot;/splatoon3mix/%E7%94%A8%E8%AA%9E%E9%9B%86/%E5%AF%BE%E6%88%A6%E9%96%A2%E9%80%A3%E7%94%A8%E8%AA%9E#k58821ab&quot; title=&quot;用語集/対戦関連用語&quot; class=&quot;rel-wiki-page&quot;&gt;&lt;span class=&quot;wikicolor&quot; style=&quot;color:#808080&quot;&gt;[詳細]&lt;/span&gt;&lt;/a&gt;">セミ</span>をすることが難しい。<br />
コンテナ前の穴の塗れる小さな壁、稼働させたリフトの側面で可能だが、やや難易度が高い。<br />
一応船尾の壁でも可能だが、コンテナから離れている上にシャケの侵攻ルートを掻い潜らなければならず、戦術として組み込む価値が皆無に近い。<br />
通常時はリフトのプロペラと船の隙間にめり込むように潜伏するとシャケの攻撃を受けなくなるため、これを利用して時間稼ぎをする手もある。<br />
ただし、通常時は前述の通り拾える金イクラが限られやすいため、ノルマに足りる分の金イクラを船上に確保できるまでは処理を優先したい。</p>

<h3 id="h3_content_1_6" class="heading-after-first"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%82%B0%E3%83%AA%E3%83%AB%E7%99%BA%E9%80%B2" title="サーモンラン/特殊な状況/グリル発進" class="rel-wiki-page">グリル発進</a>  <a class="anchor_super" name ="pa7df542"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3&id=pa7df542" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<div class="includex" style="padding:0;margin:0;"> <a class="anchor_super" id="zd156a9e919fe63f74b2bc418ad27637e" href="#zd156a9e919fe63f74b2bc418ad27637e" title="zd156a9e919fe63f74b2bc418ad27637e"></a></div>
<p><strong><span class="wikicolor" style="color:blue">青↑：誘導ルート</span></strong><br />
<strong><span class="wikicolor" style="color:red">赤↑：誘導すると危険なルート</span></strong><br />
<strong><span class="wikicolor" style="color:yellow; background-color:black">黄★：<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page"><span class="wikicolor" style="color:yellow">グリル</span></a>を攻撃して足止めする位置</span></strong><br />
<strong><span class="wikicolor" style="color:orange; background-color:black">橙●：味方が<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page"><span class="wikicolor" style="color:orange">グリル</span></a>を攻撃する位置</span></strong></p>

<div class="includex" style="padding:0;margin:0;"> <a class="anchor_super" id="zd156a9e919fe63f74b2bc418ad27637e" href="#zd156a9e919fe63f74b2bc418ad27637e" title="zd156a9e919fe63f74b2bc418ad27637e"></a></div>
<div style="text-align:right"><a class="ext" href="/splatoon3mix/?cmd=edit&amp;page=サーモンラン/特殊な状況/グリル発進&amp;id=xb57dd5b" title="部分編集:サーモンラン/特殊な状況/グリル発進&amp;id=xb57dd5b"  rel="nofollow">[編集]<span class="system-icon ext pukiwiki-open-uri" data-href="/splatoon3mix/?cmd=edit&amp;page=サーモンラン/特殊な状況/グリル発進&amp;id=xb57dd5b" data-frame="_blank"></span></a></div>
<p><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%82%B0%E3%83%AA%E3%83%AB%E7%99%BA%E9%80%B2/::ref/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3_%E3%82%B0%E3%83%AA%E3%83%AB%E3%83%AB%E3%83%BC%E3%83%88.png.webp?rev=beacfe45d4800e0bd025093e80951467&amp;t=20221202141135" alt="難破船ドン・ブラコ_グリルルート.png" title="難破船ドン・ブラコ_グリルルート.png" width="720" height="135"  loading="lazy"><br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>を倒すことそのもののパターン化は楽なものの、倒しやすい位置とコンテナとの位置が遠く、討伐と金イクラ納品の両立が極めて困難。<br />
そのため、全員誘導を理解していたとしても全ステージ中最も厳しい。<br />
少しでもインクに余裕が無くなってきたり、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>の処理がおぼつかなくなったら<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>（特に<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%83%A1%E3%82%AC%E3%83%9B%E3%83%B3%E3%83%AC%E3%83%BC%E3%82%B6%E3%83%BC5.1ch" title="ブキ/スペシャルウェポン/メガホンレーザー5.1ch" class="rel-wiki-page">メガホンレーザー5.1ch</a>）を使うべきである。</p>
<h4 id="h4_content_21_0" >定位置への誘導</h4>

<p>囮役は<strong><span class="wikicolor" style="color:orange; background-color:black">橙●</span></strong>の右側斜面で待機し、イクラコンテナから見て右の方向から<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>を侵入させ、赤線のルートに入る前に<strong><span class="wikicolor" style="color:orange; background-color:black">橙●</span></strong>に戻ると<strong><span class="wikicolor" style="color:yellow; background-color:black">黄★</span></strong>の位置へ誘導できる。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>が2体に増えた場合も同じように誘導すれば問題ない。2体の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>が重なるとしばらく停止してくれる上にお互いの弱点を遮らないようにしゃがんでくれるので、その間にダメージを蓄積させて倒そう。</p>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">Twitter引用</div>
    <div class="fold-content visible-on-open"><p><script>window.twttr = (function(d, s, id) { var js, fjs = d.getElementsByTagName(s)[0], t = window.twttr || {}; if (d.getElementById(id)) return t; js = d.createElement(s); js.id = id; js.src = "https://platform.twitter.com/widgets.js"; fjs.parentNode.insertBefore(js, fjs); t._e = []; t.ready = function(f) { t._e.push(f); }; return t; }(document, "script", "twitter-wjs"));</script>
    <div class="lazy-dom-placeholder" data-content="&lt;div id=&quot;twitter-tweet-2bcab9d935d219641434683dd9d18a03&quot; class=&quot;twitter-tweet&quot; style=&quot;margin-top: 10px; margin-bottom: 10px; min-height: 177px;&quot;&gt;&lt;/div&gt;&lt;script&gt; twttr.ready(function (){ twttr.widgets.createTweet( &#039;923479472493379584&#039;, document.getElementById(&#039;twitter-tweet-2bcab9d935d219641434683dd9d18a03&#039;), { }) }); &lt;/script&gt;">loading...</div><br />
<script>window.twttr = (function(d, s, id) { var js, fjs = d.getElementsByTagName(s)[0], t = window.twttr || {}; if (d.getElementById(id)) return t; js = d.createElement(s); js.id = id; js.src = "https://platform.twitter.com/widgets.js"; fjs.parentNode.insertBefore(js, fjs); t._e = []; t.ready = function(f) { t._e.push(f); }; return t; }(document, "script", "twitter-wjs"));</script>
    <div class="lazy-dom-placeholder" data-content="&lt;div id=&quot;twitter-tweet-6b5754d737784b51ec5075c0dc437bf0&quot; class=&quot;twitter-tweet&quot; style=&quot;margin-top: 10px; margin-bottom: 10px; min-height: 177px;&quot;&gt;&lt;/div&gt;&lt;script&gt; twttr.ready(function (){ twttr.widgets.createTweet( &#039;952445699790069761&#039;, document.getElementById(&#039;twitter-tweet-6b5754d737784b51ec5075c0dc437bf0&#039;), { }) }); &lt;/script&gt;">loading...</div></p>
</div>
</div>
<p>イクラ回収が追いつかず、<strong><span class="wikicolor" style="color:yellow; background-color:black">黄★</span></strong>付近に金イクラが溜まりやすい。クリアのめどが立ったら、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>が<strong><span class="wikicolor" style="color:yellow; background-color:black">黄★</span></strong>・<strong><span class="wikicolor" style="color:orange; background-color:black">橙●</span></strong>・コンテナ付近に行かないように誘導して、味方が納品に専念できるようにしよう。船尾で粘るのがオススメ。潮位普通時に限るが、どうしようもない場合は、船外に飛び降りる→エレベーターに乗らないように金網下通路も利用して逃げ回り、金イクラ納品が落ち着いたら右から定位置に復帰というようにできる。ただし、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>の処理やとっさの道作りが苦手なブキは不向き。残り時間が少ない場合は船外左側にガン逃げするのも手である。繰り返しになるが、エレベーター内には絶対に立ち入らないように注意。隔離役は最低限の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>処理能力が必要だが、納品側の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>処理能力が下がりすぎると納品どころではないので編成も考慮すること。<br />
<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%AA%E3%83%83%E3%82%BF%E3%83%BC4K" title="ブキ/リッター4K" class="rel-wiki-page">リッター4K</a>や<a href="/splatoon3mix/%E3%83%96%E3%82%AD/R-PEN%EF%BC%8F5H" title="ブキ/R-PEN／5H" class="rel-wiki-page">R-PEN/5H</a>,<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%88%E3%83%A9%E3%82%A4%E3%82%B9%E3%83%88%E3%83%AA%E3%83%B3%E3%82%AC%E3%83%BC" title="ブキ/トライストリンガー" class="rel-wiki-page">トライストリンガー</a>など、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>を遠距離から素早く止められるブキの場合、船外の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>を一旦足止めし、納品時間を無理やり作ることも可能。<br />
ちなみに、コンテナ横のエレベーターに乗ると、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>のターゲットを解除することができる。<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>は降ってくるので注意。生き残っているイカがすべてエレベーターに乗ったときの<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>の挙動は要検証。また、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>のタゲは、その時点で<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>に一番近いイカに移るようだ。（うまく使えば<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>のタゲを任意のイカに集中できる？要検証）</p>
<p>基本の定位置撃破＋金イクラ必要数ドロップ後船尾誘導で失敗するパターンは①船尾誘導中に納品すればクリア確定なのに味方が納品せずに<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>に攻撃しだす②船尾誘導を理解しているプレーヤーが<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>のターゲットにならず、納品時間が作れない③納品役Aが<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>処理を怠り、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>処理が苦手な納品役Bが<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>にやられる（または<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>処理役が誘導に行ってしまう）。高火力+低火力３人編成のときは『低火力3人全員が「他がやるだろう」と思ったのか<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>処理を怠って高火力がやられる』という事例が発生しやすい。</p>
<h4 id="h4_content_23_0" >コンテナ付近への誘導</h4>

<p>また、わざとコンテナ付近に誘導しようとするプレイヤーもいることも忘れてはならない。これは<strong>ハイリスクハイリターン</strong>の方法であり危険と隣り合わせではあるが、首尾よく撃破できれば早期ノルマ達成が可能だ。危険度MAXにおいては<strong><span class="wikicolor" style="color:yellow; background-color:black">黄★</span></strong>誘導のみではタゲ頼り故に②の失敗パターンが発生するため、その手段があることも頭に入れておこう。<br />
コンテナ誘導の方法としては<strong>定位置すぐ右の金網の前か金網に立ち、分岐地点をギリギリ超える辺りまで<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>がやってきたら定位置に移動。そして金網を通ろうとする<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>の尻尾を叩く</strong>といったもの。<br />
<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC%E5%B1%9E" title="ブキ/チャージャー属" class="rel-wiki-page">チャージャー</a>や<a href="/splatoon3mix/%E3%83%96%E3%82%AD/.96%E3%82%AC%E3%83%AD%E3%83%B3" title="ブキ/.96ガロン" class="rel-wiki-page">.96ガロン</a>などの高火力（瞬間火力が高い）ブキがあれば止めやすい。逆に<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%90%E3%82%B1%E3%83%83%E3%83%88%E3%82%B9%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC" title="ブキ/バケットスロッシャー" class="rel-wiki-page">バケットスロッシャー</a>など火力の無いブキでは自力では止めるのに難儀しやすいため注意。どのみち<strong><span class="wikicolor" style="color:yellow; background-color:black">黄★</span></strong>誘導に切り替える必要があるが、どの程度までコンテナ誘導をするかは編成や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>の状態、ノルマの達成状況で判断しよう。特にノルマ不足に陥る危険性が薄くなったら<strong><span class="wikicolor" style="color:yellow; background-color:black">黄★</span></strong>誘導に切り替えて安全に撃破していこう。<br />
前提として、4人全員が定位置誘導＋船尾隔離を理解していればコンテナ前誘導は必要ない。あくまでコンテナ前誘導はセオリーのわかっていない野良バイターの穴埋めである。1ウェーブ目で味方のレベルを見ておくべきだろう。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>が1台しか同時出現しない序盤は定位置撃破で4人×1往復＝4個納品は安定しているため、1個増やすためだけに序盤コンテナ前誘導を行うのはハイリスクローリターン。<br />
（3人で<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>処理が間に合う編成なら定位置撃破でも5個全て納品でき、そうなると序盤コンテナ前誘導はハイリスクノーリターンである）</p>
<p>また、定位置撃破の場合は<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>が中央にまとまるため一網打尽にしやすいが、コンテナ誘導を行うと<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>が散開するため処理に要する時間とインクが文字通り倍増する。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>のスタン役（特に<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%83%81%E3%83%A3%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC%E5%B1%9E" title="ブキ/チャージャー属" class="rel-wiki-page">チャージャー</a>や<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%94%E3%83%8A%E3%83%BC%E5%B1%9E" title="ブキ/スピナー属" class="rel-wiki-page">スピナー</a>）が<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>処理に回ると崩壊の原因になるので、通常以上に<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>処理に気を配ること。<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>処理役が真っ先に納品に行くなど論外。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>の数が怪しく感じたら定位置撃破で一度<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>をリセットしよう。</p>
<p><strong><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>を止めるのに失敗してコンテナを通り過ぎてしまった場合は、もう一度定位置の右に立てば戻ってきてくれるためそれを繰り返して止めよう。</strong>その際<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>にも注意すること。<br />
<strong>左通路から<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>を戻すのは論外</strong>である。定位置が<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>まみれになる。</p>
<p>納品にも注意が必要である。納品役は１～２人に抑えること。<br />
<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>スタン役は定位置から離れられないため、<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>処理の護衛と合わせて最低二人は定位置待機が必要。</p>
<div class="spacer">&nbsp;</div>
<p><strong>なお、コンテナを通り越して船首まで寄せる行為についてではあるが、<span class="wikicolor" style="color:Red">これは絶対にやってはならない。</span></strong><br />
こうなってしまうと<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>が縦横無尽に動き回り、大抵の<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3" title="ブキ/スペシャルウェポン" class="rel-wiki-page">スペシャル</a>を使ってさえも止めることができずにやがて<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>や<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>に巻き込まれ阿鼻叫喚の地獄絵図が始まってしまう。<br />
<strong>ただし<a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%9D%E3%83%B3/%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88%E3%83%91%E3%83%83%E3%82%AF" title="ブキ/スペシャルウェポン/ジェットパック" class="rel-wiki-page">ジェットパック</a>のみ、コンテナ上に位置することで安全に攻撃ができる。船首まで<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>の魔の手が及んでしまった場合、即座に発動して守り切ろう。</strong></p>
<p>定位置撃破の基本パターンが確立されている現状では、コンテナ前誘導を行う野良プレーヤーに対して過剰に疑惑の目が向けられる。<br />
コンテナ前誘導を行う野良バイターの9割は何も考えずに間違ったコンテナ前誘導を行っているため、これ以上コンテナ前誘導の印象を悪くしないためにも<strong>ケチのつけようのないコンテナ前誘導</strong>をしたい。<br />
繰り返しになるが、イカがケチのつく内容である</p>
<ol class="list1"><li>瞬間火力の乏しい編成</li>
<li>イカがコンテナ側まで渡って誘導</li>
<li>納品に3人以上が回る（スタン役の護衛放棄）</li>
<li>スタン失敗時に左通路から<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>を戻そうとする</li>
<li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#smallfry" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">コジャケ</a>の処理を怠る</li>
<li>序盤からコンテナ前誘導（編成次第）</li></ol>
<p>自チームに<strong><a href="/splatoon3mix/%E3%83%96%E3%82%AD/%E3%82%AF%E3%83%9E%E3%82%B5%E3%83%B3%E5%8D%B0%E3%81%AE%E3%82%B9%E3%83%AD%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC" title="ブキ/クマサン印のスロッシャー" class="rel-wiki-page">クマサン印のスロッシャー</a></strong>がいる場合、全員で船首に集まり、近づいてきた<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B0%E3%83%AA%E3%83%AB" title="サーモンラン/シャケの種類/グリル" class="rel-wiki-page">グリル</a>を<strong>クマスロが真正面からスタン</strong>させたところを他の味方が倒すという<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%A9%E3%83%83%E3%82%B7%E3%83%A5" title="サーモンラン/特殊な状況/ラッシュ" class="rel-wiki-page">ラッシュ</a>に近い要領でのクリアが狙える。</p>

<h3 id="h3_content_1_7" class="heading-after-first"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%89%E3%82%B9%E3%82%B3%E3%82%A4%E5%A4%A7%E9%87%8F%E7%99%BA%E7%94%9F" title="サーモンラン/特殊な状況/ドスコイ大量発生" class="rel-wiki-page">ドスコイ大量発生</a>  <a class="anchor_super" name ="vb03170e"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3&id=vb03170e" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<div class="includex" style="padding:0;margin:0;"> <a class="anchor_super" id="z09595c432907372020dbec42bf9a12cf" href="#z09595c432907372020dbec42bf9a12cf" title="z09595c432907372020dbec42bf9a12cf"></a></div>
<div style="text-align:right"><a class="ext" href="/splatoon3mix/?cmd=edit&amp;page=サーモンラン/特殊な状況/ドスコイ大量発生&amp;id=v1bd9789" title="部分編集:サーモンラン/特殊な状況/ドスコイ大量発生&amp;id=v1bd9789"  rel="nofollow">[編集]<span class="system-icon ext pukiwiki-open-uri" data-href="/splatoon3mix/?cmd=edit&amp;page=サーモンラン/特殊な状況/ドスコイ大量発生&amp;id=v1bd9789" data-frame="_blank"></span></a></div>
<p>船首に1基、コンテナ左右後ろに各1基ある。<br />
船首砲台は奥のオオモノ処理が得意。見通しが良く、高度があって<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>が倒しやすい''ため、使用を推奨する。逆にコンテナ付近には砲台の上下の可動域の関係で通常届かない。乗り込んだ直後に発射した時のみ、普段より射角がやや下に広がる（コンテナに近い位置に撃てる）ことを覚えておくとよい。<br />
左砲台は全方向を見れるので、これも使用しよう。ただし<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AB%E3%82%BF%E3%83%91%E3%83%83%E3%83%89" title="サーモンラン/シャケの種類/カタパッド" class="rel-wiki-page">カタパッド</a>は船首より処理しにくい。船首がカバーできないコンテナ付近の<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1#cohock" title="サーモンラン/シャケの種類/ザコシャケ" class="rel-wiki-page">ドスコイ</a>やオオモノを最優先に片付けよう。<br />
右砲台は左側がやや見にくく、右からのシャケのターゲットにされやすいため、左・上2基だけでシャケを処理しきれない時に回収係の片方が使用するとよい。<br />
回収役が右に行っている隙に左からの<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%A2%E3%82%B0%E3%83%A9" title="サーモンラン/シャケの種類/モグラ" class="rel-wiki-page">モグラ</a>に左砲手が喰われる→船首砲手が狙われる　のコンボに注意。<br />
船首砲手はなるべく<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a>に触らないこと。一時停止した<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a>がターゲットを自分に固定して、船上に上がってきて後ろから体当たりをかますことがある。<br />
<a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%89%E3%82%B9%E3%82%B3%E3%82%A4%E5%A4%A7%E9%87%8F%E7%99%BA%E7%94%9F/::attach/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3_%E3%83%86%E3%83%83%E3%83%91%E3%83%B3%E8%A1%9D%E7%AA%81.webp?rev=d062f73c9b7172c30f5d6de9df524640&amp;t=20221202142436" title="nolink" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%89%E3%82%B9%E3%82%B3%E3%82%A4%E5%A4%A7%E9%87%8F%E7%99%BA%E7%94%9F/::ref/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3_%E3%83%86%E3%83%83%E3%83%91%E3%83%B3%E8%A1%9D%E7%AA%81.webp?rev=d062f73c9b7172c30f5d6de9df524640&amp;t=20221202142436" alt="nolink" title="nolink" width="480" height="270"  loading="lazy"></a><br />
↑侵入してきた<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a>。<br />
<a href="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%89%E3%82%B9%E3%82%B3%E3%82%A4%E5%A4%A7%E9%87%8F%E7%99%BA%E7%94%9F/::attach/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3_%E3%83%86%E3%83%83%E3%83%91%E3%83%B3%E3%83%AB%E3%83%BC%E3%83%88.webp?rev=f48ed32adb424972375b05acf0cbcc74&amp;t=20221202142431" title="nolink" data-lightbox="imageset"><img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%83%89%E3%82%B9%E3%82%B3%E3%82%A4%E5%A4%A7%E9%87%8F%E7%99%BA%E7%94%9F/::ref/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3_%E3%83%86%E3%83%83%E3%83%91%E3%83%B3%E3%83%AB%E3%83%BC%E3%83%88.webp?rev=f48ed32adb424972375b05acf0cbcc74&amp;t=20221202142431" alt="nolink" title="nolink" width="480" height="270"  loading="lazy"></a><br />
↑<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%83%86%E3%83%83%E3%83%91%E3%83%B3" title="サーモンラン/シャケの種類/テッパン" class="rel-wiki-page">テッパン</a>の侵入経路。左砲台の右・右下リフトを通り、船の中腹でUターンしてきている。<br />
コンテナ付近に飛来した<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B3%E3%82%A6%E3%83%A2%E3%83%AA" title="サーモンラン/シャケの種類/コウモリ" class="rel-wiki-page">コウモリ</a>に船首に雨を降らせてしまうと火力が落ちてしまう。船首からはミサイルや本体に手出しができない。こいつにより船首方向に発射されたミサイルは必ず撃ち落としておこう。</p>

<h3 id="h3_content_1_8" class="heading-after-first"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1%E6%8E%A2%E3%81%97" title="サーモンラン/特殊な状況/キンシャケ探し" class="rel-wiki-page">キンシャケ探し</a>  <a class="anchor_super" name ="ya75d597"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3&id=ya75d597" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h3>
<div class="includex" style="padding:0;margin:0;"> <a class="anchor_super" id="z9e831ca05ca3941d74b4c7a7cf6755a8" href="#z9e831ca05ca3941d74b4c7a7cf6755a8" title="z9e831ca05ca3941d74b4c7a7cf6755a8"></a></div>
<div style="text-align:right"><a class="ext" href="/splatoon3mix/?cmd=edit&amp;page=サーモンラン/特殊な状況/キンシャケ探し&amp;id=l131a081" title="部分編集:サーモンラン/特殊な状況/キンシャケ探し&amp;id=l131a081"  rel="nofollow">[編集]<span class="system-icon ext pukiwiki-open-uri" data-href="/splatoon3mix/?cmd=edit&amp;page=サーモンラン/特殊な状況/キンシャケ探し&amp;id=l131a081" data-frame="_blank"></span></a></div>
<p>・<strong><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3" title="サーモンラン/ステージ/難破船ドン・ブラコ" class="rel-wiki-page">難破船ドン・ブラコ</a>―通常時：8ヶ所</strong><br />
<img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1%E6%8E%A2%E3%81%97/::ref/%E3%83%89%E3%83%B3%E3%83%96%E3%83%A9%E3%82%B3%E6%B0%B4%E8%84%88%28%E9%80%9A%E5%B8%B8%29_r2.png.webp?rev=2cb891b99b92a039785eea1fdb15e2e1&amp;t=20230519192215" alt="ドンブラコ水脈(通常)_r2.png" title="ドンブラコ水脈(通常)_r2.png" width="1024" height="816"  loading="lazy"></p>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/キンシャケ" class="rel-wiki-page">キンシャケ</a>の移動ルート</div>
    <div class="fold-content visible-on-open"><div class="h-scrollable"><table><thead><tr><th>出現したカンケツセン</th><th>逃げこむ可能性のあるカンケツセン</th></tr></thead><tbody><tr><td style="text-align:center;">A</td><td style="text-align:center;">D,E,F,G</td></tr><tr><td style="text-align:center;">B</td><td style="text-align:center;">F</td></tr><tr><td style="text-align:center;">D</td><td rowspan="4" style="text-align:center;">A,B</td></tr><tr><td style="text-align:center;">E</td></tr><tr><td style="text-align:center;">F</td></tr><tr><td style="text-align:center;">G</td></tr></tbody></table></div>
</div>
</div>
<ul class="list1"><li><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/キンシャケ" class="rel-wiki-page">キンシャケ</a>の出現地点と目指すゴールの組み合わせが<strong>「AまたはBから出現し、A・B以外へ向かう」もしくはその逆</strong>で固定されるという、他のステージでのルート決定とは規則性の異なる特殊な仕様となっている。</li>
<li>初手は開けやすい<strong>AとB</strong>を開けると良い。A・B共にハズレの場合、見えない場所で<a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/キンシャケ" class="rel-wiki-page">キンシャケ</a>を見つけられても、陸地→船上のルートが確定しているので先回りしやすい。
<ul class="list2"><li><strong>Aが大でBも大</strong>の場合、<strong>HかIの2択</strong>になる。陸地に降りる必要性の薄いHから開ける方が良い。</li>
<li><strong>Aが小でBが大</strong>の場合、<strong>D・E・Gの3択</strong>となる。これらは全て繋がっている為、最後まで確定する事はできずどれから開けても大差は無い。</li>
<li><strong>Aが小でBも小</strong>の場合、<strong>Fが確定</strong>する。補足としてBだけでも確定する。</li></ul></li></ul>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open">前作との水脈の違い&amp;小話</div>
    <div class="fold-content visible-on-open"><p>前作ではEとHが繋がっていなかった。<br />
図ではCが抜けているが、前作でかつてBの隣にCがあったのがアップデートによって減らされたため。</p>
</div>
</div>
<hr class="full_hr" />
<p>・<strong><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3" title="サーモンラン/ステージ/難破船ドン・ブラコ" class="rel-wiki-page">難破船ドン・ブラコ</a>―満潮時：4ヶ所</strong><br />
<img src="https://cdn.wikiwiki.jp/to/w/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1%E6%8E%A2%E3%81%97/::ref/%E3%83%89%E3%83%B3%E3%83%96%E3%83%A9%E3%82%B3%E6%B0%B4%E8%84%88%28%E6%BA%80%E6%BD%AE%29_r2.png.webp?rev=e68cb4e6d47dd68712848703d2dd9344&amp;t=20230519192159" alt="ドンブラコ水脈(満潮)_r2.png" title="ドンブラコ水脈(満潮)_r2.png" width="1024" height="816"  loading="lazy"></p>
<div class="fold-container  clearfix">
    <button class="fold-toggle-button hidden-on-open"><i class="fal fa-plus-square"></i></button>
    <button class="fold-toggle-button visible-on-open"><i class="fal fa-minus-square"></i></button>
    <div class="fold-summary hidden-on-open"><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%AD%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%B1" title="サーモンラン/シャケの種類/キンシャケ" class="rel-wiki-page">キンシャケ</a>の移動ルート</div>
    <div class="fold-content visible-on-open"><div class="h-scrollable"><table><thead><tr><th>出現したカンケツセン</th><th>逃げこむ可能性のあるカンケツセン</th></tr></thead><tbody><tr><td style="text-align:center;">A</td><td style="text-align:center;">D,E</td></tr><tr><td style="text-align:center;">B</td><td style="text-align:center;">B以外全て</td></tr><tr><td style="text-align:center;">C</td><td rowspan="2" style="text-align:center;">A,B</td></tr><tr><td style="text-align:center;">D</td></tr></tbody></table></div>
</div>
</div>
<ul class="list1"><li>水脈の繋がりが通常時と打って変わってわかりやすい。</li>
<li><strong>一番奥のE</strong>から開けて、<strong>大ならBかD</strong>。<strong>小ならA</strong>で確定する。</li></ul>

<h2 id="h2_content_1_9" class="heading-after-first">コメント <a class="anchor_super" name ="comment"></a> <a class="anchor_super" href="/splatoon3mix/::cmd/edit?page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3&id=comment" rel='nofollow'><span class="system-icon paraedit" title="Edit"></span></a></h2>
<p><a href="/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3" title="サーモンラン" class="rel-wiki-page">サーモンラン</a>攻略と統一。</p>
    <iframe id="zawazawa-embed-13fd257c805cef4ff4270df69a9cc11f-22" class="zawazawa-embed" src="https://z.wikiwiki.jp/em/spla3/topic/31?size=10&style=default"
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
<span class="small">前作では船首側からのハイパープレッサーが極めて有効だった。</span><br>            </div>
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
</style><div id="pageload" style="display: none" data-pageload="{&quot;time&quot;:{&quot;all&quot;:{&quot;real&quot;:0.011707067489624023,&quot;cost&quot;:0.17442798614501953},&quot;body&quot;:{&quot;real&quot;:0.0030159950256347656,&quot;cost&quot;:0.0683279037475586},&quot;main&quot;:{&quot;real&quot;:0.06531190872192383,&quot;cost&quot;:0.06531190872192383},&quot;menu&quot;:{&quot;real&quot;:0.09711790084838867,&quot;cost&quot;:0.09711790084838867},&quot;head&quot;:{&quot;real&quot;:0.0001780986785888672,&quot;cost&quot;:0.0001780986785888672},&quot;foot&quot;:{&quot;real&quot;:0.00011301040649414062,&quot;cost&quot;:0.00011301040649414062}},&quot;include&quot;:8,&quot;memory&quot;:1873000,&quot;io&quot;:{&quot;read&quot;:{&quot;files&quot;:1,&quot;bytes&quot;:8,&quot;locks&quot;:1},&quot;write&quot;:{&quot;files&quot;:0,&quot;bytes&quot;:0,&quot;locks&quot;:0},&quot;directory&quot;:{&quot;traversals&quot;:0,&quot;files&quot;:0},&quot;misc&quot;:57},&quot;contentSize&quot;:{&quot;all&quot;:360961,&quot;body&quot;:184938},&quot;timestamp&quot;:&quot;2026-01-16 19:26:42&quot;}"></div>

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
        bootLazy.addJqPluginInit('.lazy-dom-placeholder', function() {
            this.lazyDom({ rootMargin: '400px' });
        });
    </script>
<script>
    bootLazy.addJqPluginInit('.zawazawa-embed', function() {
        this.zcommentResize();
    });
</script>
<div id="wikiwiki-pageview-counter" data-endpoint="https://counter.wikiwiki.jp/c/splatoon3mix/pv/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3" style="display: none;"></div>
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
            title: "難破船ドン・ブラコ - Splatoon3 - スプラトゥーン3 攻略＆検証  Wiki*",
            controlPanelUrl: "https:\/\/c.wikiwiki.jp\/wiki\/splatoon3mix\/design",
            imageUrl: "https:\/\/icon.wikiwiki.jp\/symbolicon\/splatoon3mix\/ogImage\/f1fa837847c5.png",
            description: "このサイトは、スプラトゥーン3の攻略・検証を目的とした非公式wikiです。",
            shareUrl: "https:\/\/wikiwiki.jp\/splatoon3mix\/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3\/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8\/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3",
            shortUrlRequestUrl: "\/splatoon3mix\/::cmd\/short_url?mode=json&page=%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3%2F%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%2F%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3",
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
    url: '/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3',
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
