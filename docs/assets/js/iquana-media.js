/* Behaviour for the screen recordings embedded in <figure class="iq-media">.
 *
 * The clips are markup-autoplaying, muted, looping and silent, so they read as
 * animated figures rather than as players. Two things still need scripting:
 *
 *  1. prefers-reduced-motion. There is no CSS way to suppress the `autoplay`
 *     attribute, so a reader who asks for reduced motion is served the poster
 *     frame with controls instead -- the clip is still watchable, just never on
 *     its own initiative.
 *  2. Off-screen clips. A guide page can hold two recordings; decoding both for
 *     the whole visit burns battery for no one's benefit. An IntersectionObserver
 *     runs only the one being looked at.
 *
 * Material's navigation.instant swaps pages in over XHR, so this hangs off the
 * theme's `document$` subject rather than DOMContentLoaded -- same reasoning as
 * iquana-cast.js. The wired flag keeps a re-emit from stacking observers. */
document$.subscribe(function () {
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  var observer = null;
  if (!reduced && "IntersectionObserver" in window) {
    observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          var video = entry.target;
          if (entry.isIntersecting) {
            var playing = video.play();
            // Autoplay can still be refused (a data-saver setting, say). The
            // poster stays up and the reader can start it by hand.
            if (playing && playing.catch) {
              playing.catch(function () {
                video.controls = true;
              });
            }
          } else {
            video.pause();
          }
        });
      },
      { rootMargin: "200px 0px" }
    );
  }

  document.querySelectorAll(".iq-media video").forEach(function (video) {
    if (video.dataset.wired === "1") return;
    video.dataset.wired = "1";

    if (reduced) {
      video.autoplay = false;
      video.loop = false;
      video.controls = true;
      video.pause();
      return;
    }

    if (observer) observer.observe(video);
  });
});
