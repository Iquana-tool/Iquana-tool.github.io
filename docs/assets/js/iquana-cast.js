/* Mounts an asciinema player on every <div class="iq-cast" data-cast="...">.
 *
 * Material's navigation.instant is enabled, so pages are swapped in over XHR
 * and a plain DOMContentLoaded listener would fire exactly once -- on the first
 * page loaded -- leaving the player dead on every subsequent navigation. The
 * theme exposes `document$`, an RxJS subject that emits after each swap, which
 * is the supported place to (re)initialise third-party widgets. The mounted
 * flag keeps a re-emit from stacking a second player onto the same element. */
document$.subscribe(function () {
  document.querySelectorAll(".iq-cast[data-cast]").forEach(function (el) {
    if (el.dataset.mounted === "1") return;
    el.dataset.mounted = "1";

    AsciinemaPlayer.create(el.dataset.cast, el, {
      // Long installs are mostly waiting. The cast is recorded with
      // --idle-time-limit 2 as well, but setting it here too means a cast that
      // was recorded without the flag still replays without dead air.
      idleTimeLimit: 2,
      // No autoplay: the player sits below the copy-pasteable commands, and a
      // terminal that starts typing on its own steals attention from them.
      autoPlay: false,
      preload: true,
      fit: "width",
      terminalFontFamily: "JetBrains Mono, ui-monospace, monospace",
    });
  });
});
