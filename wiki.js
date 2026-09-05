/* ==========================================================================
   Knowledge Wiki Common Script (wiki.js)
   최초 작성일시: 2026-09-01 오전 11:25:20 (KST, UTC+9)
   최종 수정일시: 2026-09-01 오후 01:45:00 (KST, UTC+9)
   기능: 스크롤 시 슬림 스티키 헤더 바 표시 (레이아웃 시프트 0%, 번들거림/진동 원천 방지)
   ========================================================================== */

(function () {
    "use strict";

    function initStickyBar() {
        var origHeader = document.querySelector("header");
        if (!origHeader) return;

        var h1 = origHeader.querySelector("h1");
        var titleText = h1 ? h1.textContent.trim() : document.title;
        var isAdmin = origHeader.classList.contains("admin-theme");

        // 슬림 스티키 헤더 바 생성 및 문서 최상단 삽입 (기존 문서 흐름에 영향 없음)
        var stickyBar = document.getElementById("wiki-sticky-bar");
        if (!stickyBar) {
            stickyBar = document.createElement("div");
            stickyBar.id = "wiki-sticky-bar";
            stickyBar.className = "sticky-header-bar" + (isAdmin ? " admin-theme" : "");

            var titleDiv = document.createElement("div");
            titleDiv.className = "sticky-title";
            titleDiv.textContent = titleText;
            stickyBar.appendChild(titleDiv);

            document.body.prepend(stickyBar);
        }

        var isVisible = false;
        var ticking = false;

        function updateStickyBar() {
            var scrollY = window.scrollY || window.pageYOffset || 0;
            // 원본 헤더가 화면 위로 완전히 스크롤되어 지나갔을 때 슬림 바 노출
            var threshold = (origHeader.offsetTop + origHeader.offsetHeight) || 160;

            if (!isVisible && scrollY > threshold) {
                isVisible = true;
                stickyBar.classList.add("visible");
            } else if (isVisible && scrollY <= threshold) {
                isVisible = false;
                stickyBar.classList.remove("visible");
            }
            ticking = false;
        }

        window.addEventListener("scroll", function () {
            if (!ticking) {
                window.requestAnimationFrame(updateStickyBar);
                ticking = true;
            }
        }, { passive: true });

        updateStickyBar();
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initStickyBar);
    } else {
        initStickyBar();
    }
})();