# -*- coding: utf-8 -*-

js_content = """/* ==========================================================================
   Knowledge Wiki Common Script (wiki.js)
   최초 작성일시: 2026-09-01 오전 11:25:20 (KST, UTC+9)
   기능: 스크롤 시 상단 헤더 컴팩트 축소 (시야 높이 확장)
   ========================================================================== */

(function () {
    "use strict";

    function initStickyHeader() {
        var header = document.querySelector("header");
        if (!header) return;

        var ticking = false;
        var threshold = 40; // 스크롤 40px 초과 시 컴팩트 헤더로 전환

        function updateHeader() {
            if (window.scrollY > threshold) {
                header.classList.add("is-scrolled");
            } else {
                header.classList.remove("is-scrolled");
            }
            ticking = false;
        }

        window.addEventListener("scroll", function () {
            if (!ticking) {
                window.# -*- coding: utf-8 -*-

js_content = """/* ==========================================================================
   Knowledge Wiki Common Script (wiki.js)
   최초 작성일시: 2026-09-01 오전 11:25:20 (KST, UTC+9)
   최종 수정일시: 2026-09-01 오후 12:25:00 (KST, UTC+9)
   기능: 스크롤 시 상단 헤더 컴팩트 축소 (히스테리시스 임계값 분리로 진동/번들거림 방지)
   ========================================================================== */

(function () {
    "use strict";

    function initStickyHeader() {
        var header = document.querySelector("header");
        if (!header) return;

        var isScrolled = false;
        // 히스테리시스(Hysteresis) 임계값 분리:
        // 축소 시점(90px)과 복원 시점(15px)을 분리하여 레이아웃 시프트로 인한 경계면 무한 진동(Flickering) 원천 차단
        var COLLAPSE_THRESHOLD = 90;
        var EXPAND_THRESHOLD = 15;
        var ticking = false;

        function updateHeader() {
            var currentScroll = window.scrollY || window.pageYOffset || 0;

            if (!isScrolled && currentScroll > COLLAPSE_THRESHOLD) {
                isScrolled = true;
                header.classList.add("is-scrolled");
            } else if (isScrolled && currentScroll <= EXPAND_THRESHOLD) {
                isScrolled = false;
                header.classList.remove("is-scrolled");
            }
            ticking = false;
        }

        window.addEventListener("scroll", function () {
            if (!ticking) {
                window.requestAnimationFrame(updateHeader);
                ticking = true;
            }
        }, { passive: true });

        // 초기 스크롤 위치 검사
        updateHeader();
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initStickyHeader);
    } else {
        initStickyHeader();
    }
})();
"""

with open('Z:/wiki/wiki.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
print('Successfully updated Z:/wiki/wiki.js with hysteresis scroll logic.')
