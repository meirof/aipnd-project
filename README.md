<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />

<title>Image Classifier Project</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>



<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.7.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.7.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.7.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0') format('woff2'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.7.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.7.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.7.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.fa-pull-left {
  float: left;
}
.fa-pull-right {
  float: right;
}
.fa.fa-pull-left {
  margin-right: .3em;
}
.fa.fa-pull-right {
  margin-left: .3em;
}
/* Deprecated as of 4.4.0 */
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
  animation: fa-spin 1s infinite steps(8);
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-feed:before,
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before,
.fa-gratipay:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper-pp:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-resistance:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-y-combinator-square:before,
.fa-yc-square:before,
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
.fa-buysellads:before {
  content: "\f20d";
}
.fa-connectdevelop:before {
  content: "\f20e";
}
.fa-dashcube:before {
  content: "\f210";
}
.fa-forumbee:before {
  content: "\f211";
}
.fa-leanpub:before {
  content: "\f212";
}
.fa-sellsy:before {
  content: "\f213";
}
.fa-shirtsinbulk:before {
  content: "\f214";
}
.fa-simplybuilt:before {
  content: "\f215";
}
.fa-skyatlas:before {
  content: "\f216";
}
.fa-cart-plus:before {
  content: "\f217";
}
.fa-cart-arrow-down:before {
  content: "\f218";
}
.fa-diamond:before {
  content: "\f219";
}
.fa-ship:before {
  content: "\f21a";
}
.fa-user-secret:before {
  content: "\f21b";
}
.fa-motorcycle:before {
  content: "\f21c";
}
.fa-street-view:before {
  content: "\f21d";
}
.fa-heartbeat:before {
  content: "\f21e";
}
.fa-venus:before {
  content: "\f221";
}
.fa-mars:before {
  content: "\f222";
}
.fa-mercury:before {
  content: "\f223";
}
.fa-intersex:before,
.fa-transgender:before {
  content: "\f224";
}
.fa-transgender-alt:before {
  content: "\f225";
}
.fa-venus-double:before {
  content: "\f226";
}
.fa-mars-double:before {
  content: "\f227";
}
.fa-venus-mars:before {
  content: "\f228";
}
.fa-mars-stroke:before {
  content: "\f229";
}
.fa-mars-stroke-v:before {
  content: "\f22a";
}
.fa-mars-stroke-h:before {
  content: "\f22b";
}
.fa-neuter:before {
  content: "\f22c";
}
.fa-genderless:before {
  content: "\f22d";
}
.fa-facebook-official:before {
  content: "\f230";
}
.fa-pinterest-p:before {
  content: "\f231";
}
.fa-whatsapp:before {
  content: "\f232";
}
.fa-server:before {
  content: "\f233";
}
.fa-user-plus:before {
  content: "\f234";
}
.fa-user-times:before {
  content: "\f235";
}
.fa-hotel:before,
.fa-bed:before {
  content: "\f236";
}
.fa-viacoin:before {
  content: "\f237";
}
.fa-train:before {
  content: "\f238";
}
.fa-subway:before {
  content: "\f239";
}
.fa-medium:before {
  content: "\f23a";
}
.fa-yc:before,
.fa-y-combinator:before {
  content: "\f23b";
}
.fa-optin-monster:before {
  content: "\f23c";
}
.fa-opencart:before {
  content: "\f23d";
}
.fa-expeditedssl:before {
  content: "\f23e";
}
.fa-battery-4:before,
.fa-battery:before,
.fa-battery-full:before {
  content: "\f240";
}
.fa-battery-3:before,
.fa-battery-three-quarters:before {
  content: "\f241";
}
.fa-battery-2:before,
.fa-battery-half:before {
  content: "\f242";
}
.fa-battery-1:before,
.fa-battery-quarter:before {
  content: "\f243";
}
.fa-battery-0:before,
.fa-battery-empty:before {
  content: "\f244";
}
.fa-mouse-pointer:before {
  content: "\f245";
}
.fa-i-cursor:before {
  content: "\f246";
}
.fa-object-group:before {
  content: "\f247";
}
.fa-object-ungroup:before {
  content: "\f248";
}
.fa-sticky-note:before {
  content: "\f249";
}
.fa-sticky-note-o:before {
  content: "\f24a";
}
.fa-cc-jcb:before {
  content: "\f24b";
}
.fa-cc-diners-club:before {
  content: "\f24c";
}
.fa-clone:before {
  content: "\f24d";
}
.fa-balance-scale:before {
  content: "\f24e";
}
.fa-hourglass-o:before {
  content: "\f250";
}
.fa-hourglass-1:before,
.fa-hourglass-start:before {
  content: "\f251";
}
.fa-hourglass-2:before,
.fa-hourglass-half:before {
  content: "\f252";
}
.fa-hourglass-3:before,
.fa-hourglass-end:before {
  content: "\f253";
}
.fa-hourglass:before {
  content: "\f254";
}
.fa-hand-grab-o:before,
.fa-hand-rock-o:before {
  content: "\f255";
}
.fa-hand-stop-o:before,
.fa-hand-paper-o:before {
  content: "\f256";
}
.fa-hand-scissors-o:before {
  content: "\f257";
}
.fa-hand-lizard-o:before {
  content: "\f258";
}
.fa-hand-spock-o:before {
  content: "\f259";
}
.fa-hand-pointer-o:before {
  content: "\f25a";
}
.fa-hand-peace-o:before {
  content: "\f25b";
}
.fa-trademark:before {
  content: "\f25c";
}
.fa-registered:before {
  content: "\f25d";
}
.fa-creative-commons:before {
  content: "\f25e";
}
.fa-gg:before {
  content: "\f260";
}
.fa-gg-circle:before {
  content: "\f261";
}
.fa-tripadvisor:before {
  content: "\f262";
}
.fa-odnoklassniki:before {
  content: "\f263";
}
.fa-odnoklassniki-square:before {
  content: "\f264";
}
.fa-get-pocket:before {
  content: "\f265";
}
.fa-wikipedia-w:before {
  content: "\f266";
}
.fa-safari:before {
  content: "\f267";
}
.fa-chrome:before {
  content: "\f268";
}
.fa-firefox:before {
  content: "\f269";
}
.fa-opera:before {
  content: "\f26a";
}
.fa-internet-explorer:before {
  content: "\f26b";
}
.fa-tv:before,
.fa-television:before {
  content: "\f26c";
}
.fa-contao:before {
  content: "\f26d";
}
.fa-500px:before {
  content: "\f26e";
}
.fa-amazon:before {
  content: "\f270";
}
.fa-calendar-plus-o:before {
  content: "\f271";
}
.fa-calendar-minus-o:before {
  content: "\f272";
}
.fa-calendar-times-o:before {
  content: "\f273";
}
.fa-calendar-check-o:before {
  content: "\f274";
}
.fa-industry:before {
  content: "\f275";
}
.fa-map-pin:before {
  content: "\f276";
}
.fa-map-signs:before {
  content: "\f277";
}
.fa-map-o:before {
  content: "\f278";
}
.fa-map:before {
  content: "\f279";
}
.fa-commenting:before {
  content: "\f27a";
}
.fa-commenting-o:before {
  content: "\f27b";
}
.fa-houzz:before {
  content: "\f27c";
}
.fa-vimeo:before {
  content: "\f27d";
}
.fa-black-tie:before {
  content: "\f27e";
}
.fa-fonticons:before {
  content: "\f280";
}
.fa-reddit-alien:before {
  content: "\f281";
}
.fa-edge:before {
  content: "\f282";
}
.fa-credit-card-alt:before {
  content: "\f283";
}
.fa-codiepie:before {
  content: "\f284";
}
.fa-modx:before {
  content: "\f285";
}
.fa-fort-awesome:before {
  content: "\f286";
}
.fa-usb:before {
  content: "\f287";
}
.fa-product-hunt:before {
  content: "\f288";
}
.fa-mixcloud:before {
  content: "\f289";
}
.fa-scribd:before {
  content: "\f28a";
}
.fa-pause-circle:before {
  content: "\f28b";
}
.fa-pause-circle-o:before {
  content: "\f28c";
}
.fa-stop-circle:before {
  content: "\f28d";
}
.fa-stop-circle-o:before {
  content: "\f28e";
}
.fa-shopping-bag:before {
  content: "\f290";
}
.fa-shopping-basket:before {
  content: "\f291";
}
.fa-hashtag:before {
  content: "\f292";
}
.fa-bluetooth:before {
  content: "\f293";
}
.fa-bluetooth-b:before {
  content: "\f294";
}
.fa-percent:before {
  content: "\f295";
}
.fa-gitlab:before {
  content: "\f296";
}
.fa-wpbeginner:before {
  content: "\f297";
}
.fa-wpforms:before {
  content: "\f298";
}
.fa-envira:before {
  content: "\f299";
}
.fa-universal-access:before {
  content: "\f29a";
}
.fa-wheelchair-alt:before {
  content: "\f29b";
}
.fa-question-circle-o:before {
  content: "\f29c";
}
.fa-blind:before {
  content: "\f29d";
}
.fa-audio-description:before {
  content: "\f29e";
}
.fa-volume-control-phone:before {
  content: "\f2a0";
}
.fa-braille:before {
  content: "\f2a1";
}
.fa-assistive-listening-systems:before {
  content: "\f2a2";
}
.fa-asl-interpreting:before,
.fa-american-sign-language-interpreting:before {
  content: "\f2a3";
}
.fa-deafness:before,
.fa-hard-of-hearing:before,
.fa-deaf:before {
  content: "\f2a4";
}
.fa-glide:before {
  content: "\f2a5";
}
.fa-glide-g:before {
  content: "\f2a6";
}
.fa-signing:before,
.fa-sign-language:before {
  content: "\f2a7";
}
.fa-low-vision:before {
  content: "\f2a8";
}
.fa-viadeo:before {
  content: "\f2a9";
}
.fa-viadeo-square:before {
  content: "\f2aa";
}
.fa-snapchat:before {
  content: "\f2ab";
}
.fa-snapchat-ghost:before {
  content: "\f2ac";
}
.fa-snapchat-square:before {
  content: "\f2ad";
}
.fa-pied-piper:before {
  content: "\f2ae";
}
.fa-first-order:before {
  content: "\f2b0";
}
.fa-yoast:before {
  content: "\f2b1";
}
.fa-themeisle:before {
  content: "\f2b2";
}
.fa-google-plus-circle:before,
.fa-google-plus-official:before {
  content: "\f2b3";
}
.fa-fa:before,
.fa-font-awesome:before {
  content: "\f2b4";
}
.fa-handshake-o:before {
  content: "\f2b5";
}
.fa-envelope-open:before {
  content: "\f2b6";
}
.fa-envelope-open-o:before {
  content: "\f2b7";
}
.fa-linode:before {
  content: "\f2b8";
}
.fa-address-book:before {
  content: "\f2b9";
}
.fa-address-book-o:before {
  content: "\f2ba";
}
.fa-vcard:before,
.fa-address-card:before {
  content: "\f2bb";
}
.fa-vcard-o:before,
.fa-address-card-o:before {
  content: "\f2bc";
}
.fa-user-circle:before {
  content: "\f2bd";
}
.fa-user-circle-o:before {
  content: "\f2be";
}
.fa-user-o:before {
  content: "\f2c0";
}
.fa-id-badge:before {
  content: "\f2c1";
}
.fa-drivers-license:before,
.fa-id-card:before {
  content: "\f2c2";
}
.fa-drivers-license-o:before,
.fa-id-card-o:before {
  content: "\f2c3";
}
.fa-quora:before {
  content: "\f2c4";
}
.fa-free-code-camp:before {
  content: "\f2c5";
}
.fa-telegram:before {
  content: "\f2c6";
}
.fa-thermometer-4:before,
.fa-thermometer:before,
.fa-thermometer-full:before {
  content: "\f2c7";
}
.fa-thermometer-3:before,
.fa-thermometer-three-quarters:before {
  content: "\f2c8";
}
.fa-thermometer-2:before,
.fa-thermometer-half:before {
  content: "\f2c9";
}
.fa-thermometer-1:before,
.fa-thermometer-quarter:before {
  content: "\f2ca";
}
.fa-thermometer-0:before,
.fa-thermometer-empty:before {
  content: "\f2cb";
}
.fa-shower:before {
  content: "\f2cc";
}
.fa-bathtub:before,
.fa-s15:before,
.fa-bath:before {
  content: "\f2cd";
}
.fa-podcast:before {
  content: "\f2ce";
}
.fa-window-maximize:before {
  content: "\f2d0";
}
.fa-window-minimize:before {
  content: "\f2d1";
}
.fa-window-restore:before {
  content: "\f2d2";
}
.fa-times-rectangle:before,
.fa-window-close:before {
  content: "\f2d3";
}
.fa-times-rectangle-o:before,
.fa-window-close-o:before {
  content: "\f2d4";
}
.fa-bandcamp:before {
  content: "\f2d5";
}
.fa-grav:before {
  content: "\f2d6";
}
.fa-etsy:before {
  content: "\f2d7";
}
.fa-imdb:before {
  content: "\f2d8";
}
.fa-ravelry:before {
  content: "\f2d9";
}
.fa-eercast:before {
  content: "\f2da";
}
.fa-microchip:before {
  content: "\f2db";
}
.fa-snowflake-o:before {
  content: "\f2dc";
}
.fa-superpowers:before {
  content: "\f2dd";
}
.fa-wpexplorer:before {
  content: "\f2de";
}
.fa-meetup:before {
  content: "\f2e0";
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
div.traceback-wrapper pre.traceback {
  max-height: 600px;
  overflow: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 5px;
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
[dir="rtl"] #ipython_notebook {
  margin-right: 10px;
  margin-left: 0;
}
[dir="rtl"] #ipython_notebook.pull-left {
  float: right !important;
  float: right;
}
.flex-spacer {
  flex: 1;
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#kernel_logo_widget {
  margin: 0 10px;
}
span#login_widget {
  float: right;
}
[dir="rtl"] span#login_widget {
  float: left;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
.modal-header {
  cursor: move;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
[dir="rtl"] .center-nav form.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] .center-nav .navbar-text {
  float: right;
}
[dir="rtl"] .navbar-inner {
  text-align: right;
}
[dir="rtl"] div.text-left {
  text-align: right;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  position: absolute;
  display: block;
  width: 100%;
  height: 100%;
  overflow: hidden;
  cursor: pointer;
  opacity: 0;
  z-index: 2;
}
.alternate_upload .btn-xs > input.fileinput {
  margin: -1px -5px;
}
.alternate_upload .btn-upload {
  position: relative;
  height: 22px;
}
::-webkit-file-upload-button {
  cursor: pointer;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
[dir="rtl"] ul#tabs.nav-tabs > li {
  float: right;
}
[dir="rtl"] ul#tabs.nav.nav-tabs {
  padding-right: 0;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
[dir="rtl"] .list_toolbar .tree-buttons .pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .list_toolbar .col-sm-4,
[dir="rtl"] .list_toolbar .col-sm-8 {
  float: right;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: text-bottom;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
[dir="rtl"] .list_item > div input {
  margin-right: 0;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_modified {
  margin-right: 7px;
  margin-left: 7px;
}
[dir="rtl"] .item_modified.pull-right {
  float: left !important;
  float: left;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
[dir="rtl"] .item_buttons.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .item_buttons .kernel-name {
  margin-left: 7px;
  float: right;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
.sort_button {
  display: inline-block;
  padding-left: 7px;
}
[dir="rtl"] .sort_button.pull-right {
  float: left !important;
  float: left;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
[dir="rtl"] #button-select-all.btn {
  float: right ;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
  margin-top: 2px;
  height: 16px;
}
[dir="rtl"] #select-all.pull-left {
  float: right !important;
  float: right;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.fa-pull-left {
  margin-right: .3em;
}
.folder_icon:before.fa-pull-right {
  margin-left: .3em;
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.fa-pull-left {
  margin-right: .3em;
}
.file_icon:before.fa-pull-right {
  margin-left: .3em;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
#new-menu .dropdown-header {
  font-size: 10px;
  border-bottom: 1px solid #e5e5e5;
  padding: 0 0 3px;
  margin: -3px 20px 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.move-button {
  display: none;
}
.download-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
.CodeMirror-dialog {
  background-color: #fff;
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI escape sequences */
/* The color values are a mix of
   http://www.xcolors.net/dl/baskerville-ivorylight and
   http://www.xcolors.net/dl/euphrasia */
.ansi-black-fg {
  color: #3E424D;
}
.ansi-black-bg {
  background-color: #3E424D;
}
.ansi-black-intense-fg {
  color: #282C36;
}
.ansi-black-intense-bg {
  background-color: #282C36;
}
.ansi-red-fg {
  color: #E75C58;
}
.ansi-red-bg {
  background-color: #E75C58;
}
.ansi-red-intense-fg {
  color: #B22B31;
}
.ansi-red-intense-bg {
  background-color: #B22B31;
}
.ansi-green-fg {
  color: #00A250;
}
.ansi-green-bg {
  background-color: #00A250;
}
.ansi-green-intense-fg {
  color: #007427;
}
.ansi-green-intense-bg {
  background-color: #007427;
}
.ansi-yellow-fg {
  color: #DDB62B;
}
.ansi-yellow-bg {
  background-color: #DDB62B;
}
.ansi-yellow-intense-fg {
  color: #B27D12;
}
.ansi-yellow-intense-bg {
  background-color: #B27D12;
}
.ansi-blue-fg {
  color: #208FFB;
}
.ansi-blue-bg {
  background-color: #208FFB;
}
.ansi-blue-intense-fg {
  color: #0065CA;
}
.ansi-blue-intense-bg {
  background-color: #0065CA;
}
.ansi-magenta-fg {
  color: #D160C4;
}
.ansi-magenta-bg {
  background-color: #D160C4;
}
.ansi-magenta-intense-fg {
  color: #A03196;
}
.ansi-magenta-intense-bg {
  background-color: #A03196;
}
.ansi-cyan-fg {
  color: #60C6C8;
}
.ansi-cyan-bg {
  background-color: #60C6C8;
}
.ansi-cyan-intense-fg {
  color: #258F8F;
}
.ansi-cyan-intense-bg {
  background-color: #258F8F;
}
.ansi-white-fg {
  color: #C5C1B4;
}
.ansi-white-bg {
  background-color: #C5C1B4;
}
.ansi-white-intense-fg {
  color: #A1A6B2;
}
.ansi-white-intense-bg {
  background-color: #A1A6B2;
}
.ansi-default-inverse-fg {
  color: #FFFFFF;
}
.ansi-default-inverse-bg {
  background-color: #000000;
}
.ansi-bold {
  font-weight: bold;
}
.ansi-underline {
  text-decoration: underline;
}
/* The following styles are deprecated an will be removed in a future version */
.ansibold {
  font-weight: bold;
}
.ansi-inverse {
  outline: 0.5px dotted;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  position: relative;
  overflow: visible;
}
div.cell:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: transparent;
}
div.cell.jupyter-soft-selected {
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected,
div.cell.selected.jupyter-soft-selected {
  border-color: #ababab;
}
div.cell.selected:before,
div.cell.selected.jupyter-soft-selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #42A5F5;
}
@media print {
  div.cell.selected,
  div.cell.selected.jupyter-soft-selected {
    border-color: transparent;
  }
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
}
.edit_mode div.cell.selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #66BB6A;
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  /* Note that this should set vertical padding only, since CodeMirror assumes
       that horizontal padding will be set on CodeMirror pre */
  padding: 0.4em 0;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. This sets horizontal padding only,
    use .CodeMirror-lines for vertical */
  padding: 0 0.4em;
  border: 0;
  border-radius: 0;
}
.CodeMirror-cursor {
  border-left: 1.4px solid black;
}
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .CodeMirror-cursor {
    border-left: 2px solid black;
  }
}
@media screen and (min-width: 4320px) {
  .CodeMirror-cursor {
    border-left: 4px solid black;
  }
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
div.output_area .mglyph > img {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 1px 0 1px 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul:not(.list-inline),
.rendered_html ol:not(.list-inline) {
  padding-left: 2em;
}
.rendered_html ul {
  list-style: disc;
}
.rendered_html ul ul {
  list-style: square;
  margin-top: 0;
}
.rendered_html ul ul ul {
  list-style: circle;
}
.rendered_html ol {
  list-style: decimal;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin-top: 0;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
  padding: 0px;
  background-color: #fff;
}
.rendered_html code {
  background-color: #eff0f1;
}
.rendered_html p code {
  padding: 1px 5px;
}
.rendered_html pre code {
  background-color: #fff;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  color: #000;
  font-size: 100%;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: none;
  border-collapse: collapse;
  border-spacing: 0;
  color: black;
  font-size: 12px;
  table-layout: fixed;
}
.rendered_html thead {
  border-bottom: 1px solid black;
  vertical-align: bottom;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  text-align: right;
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html tbody tr:nth-child(odd) {
  background: #f5f5f5;
}
.rendered_html tbody tr:hover {
  background: rgba(66, 165, 245, 0.2);
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
.rendered_html .alert {
  margin-bottom: initial;
}
.rendered_html * + .alert {
  margin-top: 1em;
}
[dir="rtl"] .rendered_html p {
  text-align: right;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.rendered .rendered_html tr,
.text_cell.rendered .rendered_html th,
.text_cell.rendered .rendered_html td {
  max-width: none;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.text_cell .dropzone .input_area {
  border: 2px dashed #bababa;
  margin: -1px;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
.jupyter-keybindings {
  padding: 1px;
  line-height: 24px;
  border-bottom: 1px solid gray;
}
.jupyter-keybindings input {
  margin: 0;
  padding: 0;
  border: none;
}
.jupyter-keybindings i {
  padding: 6px;
}
.well code {
  background-color: #ffffff;
  border-color: #ababab;
  border-width: 1px;
  border-style: solid;
  padding: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.tags_button_container {
  width: 100%;
  display: flex;
}
.tag-container {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  overflow: hidden;
  position: relative;
}
.tag-container > * {
  margin: 0 4px;
}
.remove-tag-btn {
  margin-left: 4px;
}
.tags-input {
  display: flex;
}
.cell-tag:last-child:after {
  content: "";
  position: absolute;
  right: 0;
  width: 40px;
  height: 100%;
  /* Fade to background color of cell toolbar */
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #EEE);
}
.tags-input > * {
  margin-left: 4px;
}
.cell-tag,
.tags-input input,
.tags-input button {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  box-shadow: none;
  width: inherit;
  font-size: inherit;
  height: 22px;
  line-height: 22px;
  padding: 0px 4px;
  display: inline-block;
}
.cell-tag:focus,
.tags-input input:focus,
.tags-input button:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.cell-tag::-moz-placeholder,
.tags-input input::-moz-placeholder,
.tags-input button::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.cell-tag:-ms-input-placeholder,
.tags-input input:-ms-input-placeholder,
.tags-input button:-ms-input-placeholder {
  color: #999;
}
.cell-tag::-webkit-input-placeholder,
.tags-input input::-webkit-input-placeholder,
.tags-input button::-webkit-input-placeholder {
  color: #999;
}
.cell-tag::-ms-expand,
.tags-input input::-ms-expand,
.tags-input button::-ms-expand {
  border: 0;
  background-color: transparent;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
.cell-tag[readonly],
.tags-input input[readonly],
.tags-input button[readonly],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  background-color: #eeeeee;
  opacity: 1;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  cursor: not-allowed;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button {
  height: auto;
}
select.cell-tag,
select.tags-input input,
select.tags-input button {
  height: 30px;
  line-height: 30px;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button,
select[multiple].cell-tag,
select[multiple].tags-input input,
select[multiple].tags-input button {
  height: auto;
}
.cell-tag,
.tags-input button {
  padding: 0px 4px;
}
.cell-tag {
  background-color: #fff;
  white-space: nowrap;
}
.tags-input input[type=text]:focus {
  outline: none;
  box-shadow: none;
  border-color: #ccc;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
[dir="rtl"] #kernel_logo_widget {
  float: left !important;
  float: left;
}
.modal .modal-body .move-path {
  display: flex;
  flex-direction: row;
  justify-content: space;
  align-items: center;
}
.modal .modal-body .move-path .server-root {
  padding-right: 20px;
}
.modal .modal-body .move-path .path-input {
  flex: 1;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
[dir="rtl"] #menubar .navbar-toggle {
  float: right;
}
[dir="rtl"] #menubar .navbar-collapse {
  clear: right;
}
[dir="rtl"] #menubar .navbar-nav {
  float: right;
}
[dir="rtl"] #menubar .nav {
  padding-right: 0px;
}
[dir="rtl"] #menubar .navbar-nav > li {
  float: right;
}
[dir="rtl"] #menubar .navbar-right {
  float: left !important;
}
[dir="rtl"] ul.dropdown-menu {
  text-align: right;
  left: auto;
}
[dir="rtl"] ul#new-menu.dropdown-menu {
  right: auto;
  left: 0;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
[dir="rtl"] i.menu-icon.pull-right {
  float: left !important;
  float: left;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
[dir="rtl"] ul#help_menu li a {
  padding-left: 2.2em;
}
[dir="rtl"] ul#help_menu li a i {
  margin-right: 0;
  margin-left: -1.2em;
}
[dir="rtl"] ul#help_menu li a i.pull-right {
  float: left !important;
  float: left;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
[dir="rtl"] .dropdown-submenu > .dropdown-menu {
  right: 100%;
  margin-right: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.fa-pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.fa-pull-right {
  margin-left: .3em;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
[dir="rtl"] .dropdown-submenu > a:after {
  float: left;
  content: "\f0d9";
  margin-right: 0;
  margin-left: -10px;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
[dir="rtl"] #notification_area {
  float: left !important;
  float: left;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] .indicator_area {
  float: left !important;
  float: left;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
[dir="rtl"] #kernel_indicator {
  float: left !important;
  float: left;
  border-left: 0;
  border-right: 1px solid;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] #modal_indicator {
  float: left !important;
  float: left;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 21ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  height: 30px;
  margin-top: 4px;
  display: flex;
  justify-content: flex-start;
  align-items: baseline;
  width: 50%;
  flex: 1;
}
span.save_widget span.filename {
  height: 100%;
  line-height: 1em;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
[dir="rtl"] span.save_widget.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] span.save_widget span.filename {
  margin-left: 0;
  margin-right: 16px;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
  white-space: nowrap;
  padding: 0 5px;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
    padding: 0 0 0 5px;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
.toolbar-btn-label {
  margin-left: 6px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
[dir="rtl"] .btn-group > .btn,
.btn-group-vertical > .btn {
  float: right;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
[dir="rtl"] ul.typeahead-list i {
  margin-left: 0;
  margin-right: -10px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
ul.typeahead-list  > li > a.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .typeahead-list {
  text-align: right;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  min-width: 20px;
  color: transparent;
}
[dir="rtl"] .no-shortcut.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .command-shortcut.pull-right {
  float: left !important;
  float: left;
}
.command-shortcut:before {
  content: "(command mode)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
[dir="rtl"] .edit-shortcut.pull-right {
  float: left !important;
  float: left;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
[dir="ltr"] #find-and-replace .input-group-btn + .form-control {
  border-left: none;
}
[dir="rtl"] #find-and-replace .input-group-btn + .form-control {
  border-right: none;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  width: 100%;
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal .xterm-rows {
  padding: 10px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>
<style type="text/css">
    
/* Temporary definitions which will become obsolete with Notebook release 5.0 */
.ansi-black-fg { color: #3E424D; }
.ansi-black-bg { background-color: #3E424D; }
.ansi-black-intense-fg { color: #282C36; }
.ansi-black-intense-bg { background-color: #282C36; }
.ansi-red-fg { color: #E75C58; }
.ansi-red-bg { background-color: #E75C58; }
.ansi-red-intense-fg { color: #B22B31; }
.ansi-red-intense-bg { background-color: #B22B31; }
.ansi-green-fg { color: #00A250; }
.ansi-green-bg { background-color: #00A250; }
.ansi-green-intense-fg { color: #007427; }
.ansi-green-intense-bg { background-color: #007427; }
.ansi-yellow-fg { color: #DDB62B; }
.ansi-yellow-bg { background-color: #DDB62B; }
.ansi-yellow-intense-fg { color: #B27D12; }
.ansi-yellow-intense-bg { background-color: #B27D12; }
.ansi-blue-fg { color: #208FFB; }
.ansi-blue-bg { background-color: #208FFB; }
.ansi-blue-intense-fg { color: #0065CA; }
.ansi-blue-intense-bg { background-color: #0065CA; }
.ansi-magenta-fg { color: #D160C4; }
.ansi-magenta-bg { background-color: #D160C4; }
.ansi-magenta-intense-fg { color: #A03196; }
.ansi-magenta-intense-bg { background-color: #A03196; }
.ansi-cyan-fg { color: #60C6C8; }
.ansi-cyan-bg { background-color: #60C6C8; }
.ansi-cyan-intense-fg { color: #258F8F; }
.ansi-cyan-intense-bg { background-color: #258F8F; }
.ansi-white-fg { color: #C5C1B4; }
.ansi-white-bg { background-color: #C5C1B4; }
.ansi-white-intense-fg { color: #A1A6B2; }
.ansi-white-intense-bg { background-color: #A1A6B2; }

.ansi-bold { font-weight: bold; }

    </style>
<style type="text/css">
    body[data-notebook-name] > #header #header-container:not(.show-panel), /* body has data-notebook-name attribute when 
a notebook is open. this rule won't be applied when the notebook is not open (in 404 view for example) */
body[data-notebook-name] #menubar-container #maintoolbar:not(.show-panel),
body[data-notebook-name] #menubar-container ul.navbar-nav:not(.show-panel) {
  display: none;
}

#menubar.only-panel #menus.navbar-default {
    background: #fff;
    border-color: #fff;
}

.toolbar.with-statusbar{
    margin-top: 3px;
    margin-bottom: 0;
}

    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Developing-an-AI-application">Developing an AI application<a class="anchor-link" href="#Developing-an-AI-application">&#182;</a></h1><p>Going forward, AI algorithms will be incorporated into more and more everyday applications. For example, you might want to include an image classifier in a smart phone app. To do this, you'd use a deep learning model trained on hundreds of thousands of images as part of the overall application architecture. A large part of software development in the future will be using these types of models as common parts of applications.</p>
<p>In this project, you'll train an image classifier to recognize different species of flowers. You can imagine using something like this in a phone app that tells you the name of the flower your camera is looking at. In practice you'd train this classifier, then export it for use in your application. We'll be using <a href="http://www.robots.ox.ac.uk/~vgg/data/flowers/102/index.html">this dataset</a> of 102 flower categories, you can see a few examples below.</p>
<p><img src='assets/Flowers.png' width=500px></p>
<p>The project is broken down into multiple steps:</p>
<ul>
<li>Load and preprocess the image dataset</li>
<li>Train the image classifier on your dataset</li>
<li>Use the trained classifier to predict image content</li>
</ul>
<p>We'll lead you through each part which you'll implement in Python.</p>
<p>When you've completed this project, you'll have an application that can be trained on any set of labeled images. Here your network will be learning about flowers and end up as a command line application. But, what you do with your new skills depends on your imagination and effort in building a dataset. For example, imagine an app where you take a picture of a car, it tells you what the make and model is, then looks up information about it. Go build your own dataset and make something new.</p>
<p>First up is importing the packages you'll need. It's good practice to keep all the imports at the beginning of your code. As you work through this notebook and find you need to import a package, make sure to add the import up here.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Imports here</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">torch</span> 
<span class="o">%</span><span class="k">matplotlib</span> inline
<span class="o">%</span><span class="k">config</span> InlineBackend.figure_format = &#39;retina&#39;
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">from</span> <span class="nn">collections</span> <span class="k">import</span> <span class="n">OrderedDict</span>
<span class="kn">from</span> <span class="nn">torchvision</span> <span class="k">import</span> <span class="n">datasets</span><span class="p">,</span> <span class="n">transforms</span><span class="p">,</span><span class="n">models</span>
<span class="kn">import</span> <span class="nn">torch.nn.functional</span> <span class="k">as</span> <span class="nn">F</span>
<span class="kn">from</span> <span class="nn">torch</span> <span class="k">import</span> <span class="n">nn</span><span class="p">,</span><span class="n">optim</span>
<span class="kn">from</span> <span class="nn">PIL</span> <span class="k">import</span> <span class="n">Image</span>
<span class="kn">import</span> <span class="nn">os</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Load-the-data">Load the data<a class="anchor-link" href="#Load-the-data">&#182;</a></h2><p>Here you'll use <code>torchvision</code> to load the data (<a href="http://pytorch.org/docs/0.3.0/torchvision/index.html">documentation</a>). The data should be included alongside this notebook, otherwise you can <a href="https://s3.amazonaws.com/content.udacity-data.com/nd089/flower_data.tar.gz">download it here</a>. The dataset is split into three parts, training, validation, and testing. For the training, you'll want to apply transformations such as random scaling, cropping, and flipping. This will help the network generalize leading to better performance. You'll also need to make sure the input data is resized to 224x224 pixels as required by the pre-trained networks.</p>
<p>The validation and testing sets are used to measure the model's performance on data it hasn't seen yet. For this you don't want any scaling or rotation transformations, but you'll need to resize then crop the images to the appropriate size.</p>
<p>The pre-trained networks you'll use were trained on the ImageNet dataset where each color channel was normalized separately. For all three sets you'll need to normalize the means and standard deviations of the images to what the network expects. For the means, it's <code>[0.485, 0.456, 0.406]</code> and for the standard deviations <code>[0.229, 0.224, 0.225]</code>, calculated from the ImageNet images.  These values will shift each color channel to be centered at 0 and range from -1 to 1.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">data_dir</span> <span class="o">=</span> <span class="s1">&#39;flowers&#39;</span>
<span class="n">train_dir</span> <span class="o">=</span> <span class="n">data_dir</span> <span class="o">+</span> <span class="s1">&#39;/train&#39;</span>
<span class="n">valid_dir</span> <span class="o">=</span> <span class="n">data_dir</span> <span class="o">+</span> <span class="s1">&#39;/valid&#39;</span>
<span class="n">test_dir</span> <span class="o">=</span> <span class="n">data_dir</span>  <span class="o">+</span> <span class="s1">&#39;/test&#39;</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">normalize</span> <span class="o">=</span> <span class="n">transforms</span><span class="o">.</span><span class="n">Normalize</span><span class="p">(</span><span class="n">mean</span><span class="o">=</span><span class="p">[</span><span class="mf">0.485</span><span class="p">,</span> <span class="mf">0.456</span><span class="p">,</span> <span class="mf">0.406</span><span class="p">],</span>
                                 <span class="n">std</span><span class="o">=</span><span class="p">[</span><span class="mf">0.229</span><span class="p">,</span> <span class="mf">0.224</span><span class="p">,</span> <span class="mf">0.225</span><span class="p">])</span>

<span class="n">train_transforms</span> <span class="o">=</span> <span class="n">transforms</span><span class="o">.</span><span class="n">Compose</span><span class="p">([</span><span class="n">transforms</span><span class="o">.</span><span class="n">RandomRotation</span><span class="p">(</span><span class="mi">30</span><span class="p">),</span>
                                      <span class="n">transforms</span><span class="o">.</span><span class="n">Resize</span><span class="p">(</span><span class="mi">224</span><span class="p">),</span>
                                      <span class="n">transforms</span><span class="o">.</span><span class="n">RandomResizedCrop</span><span class="p">(</span><span class="mi">224</span><span class="p">),</span>
                                      <span class="n">transforms</span><span class="o">.</span><span class="n">RandomVerticalFlip</span><span class="p">(),</span>
                                      <span class="n">transforms</span><span class="o">.</span><span class="n">ToTensor</span><span class="p">(),</span>
                                      <span class="n">normalize</span><span class="p">])</span>
<span class="n">test_valid_transforms</span> <span class="o">=</span> <span class="n">transforms</span><span class="o">.</span><span class="n">Compose</span><span class="p">([</span><span class="n">transforms</span><span class="o">.</span><span class="n">Resize</span><span class="p">(</span><span class="mi">224</span><span class="p">),</span>
                                      <span class="n">transforms</span><span class="o">.</span><span class="n">CenterCrop</span><span class="p">(</span><span class="mi">224</span><span class="p">),</span>
                                      <span class="n">transforms</span><span class="o">.</span><span class="n">ToTensor</span><span class="p">(),</span>
                                      <span class="n">normalize</span><span class="p">])</span>

<span class="c1"># TODO: Load the datasets with ImageFolder</span>

<span class="n">train_data_datasets</span> <span class="o">=</span> <span class="n">datasets</span><span class="o">.</span><span class="n">ImageFolder</span><span class="p">(</span><span class="n">train_dir</span><span class="p">,</span> <span class="n">transform</span><span class="o">=</span><span class="n">train_transforms</span><span class="p">)</span>
<span class="n">valid_data_datasets</span> <span class="o">=</span> <span class="n">datasets</span><span class="o">.</span><span class="n">ImageFolder</span><span class="p">(</span><span class="n">valid_dir</span> <span class="p">,</span> <span class="n">transform</span><span class="o">=</span><span class="n">test_valid_transforms</span><span class="p">)</span>
<span class="n">test_data_datasets</span> <span class="o">=</span> <span class="n">datasets</span><span class="o">.</span><span class="n">ImageFolder</span><span class="p">(</span><span class="n">test_dir</span> <span class="p">,</span> <span class="n">transform</span><span class="o">=</span><span class="n">test_valid_transforms</span><span class="p">)</span>
<span class="n">image_datasets</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;training_sets&#39;</span><span class="p">:</span> <span class="n">train_data_datasets</span><span class="p">,</span>
                  <span class="s1">&#39;validation_sets&#39;</span><span class="p">:</span> <span class="n">valid_data_datasets</span> <span class="p">,</span>
                  <span class="s1">&#39;testing_sets&#39;</span><span class="p">:</span> <span class="n">test_data_datasets</span> <span class="p">}</span>

<span class="c1"># TODO: Using the image datasets and the trainforms, define the dataloaders</span>
<span class="n">trainloader</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">utils</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">DataLoader</span><span class="p">(</span><span class="n">train_data_datasets</span><span class="p">,</span> <span class="n">batch_size</span><span class="o">=</span><span class="mi">64</span><span class="p">,</span> <span class="n">shuffle</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">validloader</span>  <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">utils</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">DataLoader</span><span class="p">(</span><span class="n">valid_data_datasets</span><span class="p">,</span> <span class="n">batch_size</span><span class="o">=</span><span class="mi">64</span><span class="p">)</span>
<span class="n">testloader</span>  <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">utils</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">DataLoader</span><span class="p">(</span><span class="n">test_data_datasets</span><span class="p">,</span> <span class="n">batch_size</span><span class="o">=</span><span class="mi">64</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Label-mapping">Label mapping<a class="anchor-link" href="#Label-mapping">&#182;</a></h3><p>You'll also need to load in a mapping from category label to category name. You can find this in the file <code>cat_to_name.json</code>. It's a JSON object which you can read in with the <a href="https://docs.python.org/2/library/json.html"><code>json</code> module</a>. This will give you a dictionary mapping the integer encoded categories to the actual names of the flowers.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">json</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s1">&#39;cat_to_name.json&#39;</span><span class="p">,</span> <span class="s1">&#39;r&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="n">cat_to_name</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Building-and-training-the-classifier">Building and training the classifier<a class="anchor-link" href="#Building-and-training-the-classifier">&#182;</a></h1><p>Now that the data is ready, it's time to build and train the classifier. As usual, you should use one of the pretrained models from <code>torchvision.models</code> to get the image features. Build and train a new feed-forward classifier using those features.</p>
<p>We're going to leave this part up to you. Refer to <a href="https://review.udacity.com/#!/rubrics/1663/view">the rubric</a> for guidance on successfully completing this section. Things you'll need to do:</p>
<ul>
<li>Load a <a href="http://pytorch.org/docs/master/torchvision/models.html">pre-trained network</a> (If you need a starting point, the VGG networks work great and are straightforward to use)</li>
<li>Define a new, untrained feed-forward network as a classifier, using ReLU activations and dropout</li>
<li>Train the classifier layers using backpropagation using the pre-trained network to get the features</li>
<li>Track the loss and accuracy on the validation set to determine the best hyperparameters</li>
</ul>
<p>We've left a cell open for you below, but use as many as you need. Our advice is to break the problem up into smaller parts you can run separately. Check that each part is doing what you expect, then move on to the next. You'll likely find that as you work through each part, you'll need to go back and modify your previous code. This is totally normal!</p>
<p>When training make sure you're updating only the weights of the feed-forward network. You should be able to get the validation accuracy above 70% if you build everything right. Make sure to try different hyperparameters (learning rate, units in the classifier, epochs, etc) to find the best model. Save those hyperparameters to use as default values in the next part of the project.</p>
<p>One last important tip if you're using the workspace to run your code: To avoid having your workspace disconnect during the long-running tasks in this notebook, please read in the earlier page in this lesson called Intro to
GPU Workspaces about Keeping Your Session Active. You'll want to include code from the workspace_utils.py module.</p>
<p><strong>Note for Workspace users:</strong> If your network is over 1 GB when saved as a checkpoint, there might be issues with saving backups in your workspace. Typically this happens with wide dense layers after the convolutional layers. If your saved checkpoint is larger than 1 GB (you can open a terminal and check with <code>ls -lh</code>), you should reduce the size of your hidden layers and train again.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">device</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">device</span><span class="p">(</span><span class="s2">&quot;cuda&quot;</span> <span class="k">if</span> <span class="n">torch</span><span class="o">.</span><span class="n">cuda</span><span class="o">.</span><span class="n">is_available</span><span class="p">()</span> <span class="k">else</span> <span class="s2">&quot;cpu&quot;</span><span class="p">)</span>
<span class="n">my_model</span> <span class="o">=</span>  <span class="n">models</span><span class="o">.</span><span class="n">vgg16</span><span class="p">(</span><span class="n">pretrained</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="k">for</span> <span class="n">param</span> <span class="ow">in</span> <span class="n">my_model</span><span class="o">.</span><span class="n">parameters</span><span class="p">():</span>
    <span class="n">param</span><span class="o">.</span><span class="n">requires_grad</span> <span class="o">=</span> <span class="kc">False</span>


<span class="n">classifier</span> <span class="o">=</span> <span class="n">nn</span><span class="o">.</span><span class="n">Sequential</span><span class="p">(</span><span class="n">OrderedDict</span><span class="p">([</span>
                          <span class="p">(</span><span class="s1">&#39;fc1&#39;</span><span class="p">,</span> <span class="n">nn</span><span class="o">.</span><span class="n">Linear</span><span class="p">(</span><span class="mi">25088</span><span class="p">,</span> <span class="mi">512</span><span class="p">)),</span>
                          <span class="p">(</span><span class="s1">&#39;relu&#39;</span><span class="p">,</span> <span class="n">nn</span><span class="o">.</span><span class="n">ReLU</span><span class="p">()),</span>
                          <span class="p">(</span><span class="s1">&#39;dropout&#39;</span><span class="p">,</span> <span class="n">nn</span><span class="o">.</span><span class="n">Dropout</span><span class="p">(</span><span class="mf">0.4</span><span class="p">)),</span>
                          <span class="p">(</span><span class="s1">&#39;fc2&#39;</span><span class="p">,</span> <span class="n">nn</span><span class="o">.</span><span class="n">Linear</span><span class="p">(</span><span class="mi">512</span><span class="p">,</span> <span class="mi">102</span><span class="p">)),</span>
                          <span class="p">(</span><span class="s1">&#39;output&#39;</span><span class="p">,</span> <span class="n">nn</span><span class="o">.</span><span class="n">LogSoftmax</span><span class="p">(</span><span class="n">dim</span><span class="o">=</span><span class="mi">1</span><span class="p">))</span>
                          <span class="p">]))</span>


<span class="n">my_model</span><span class="o">.</span><span class="n">classifier</span> <span class="o">=</span> <span class="n">classifier</span>

<span class="n">criterion</span> <span class="o">=</span> <span class="n">nn</span><span class="o">.</span><span class="n">NLLLoss</span><span class="p">()</span>

<span class="c1"># Only train the classifier parameters, feature parameters are frozen</span>
<span class="n">optimizer</span> <span class="o">=</span> <span class="n">optim</span><span class="o">.</span><span class="n">Adam</span><span class="p">(</span><span class="n">my_model</span><span class="o">.</span><span class="n">classifier</span><span class="o">.</span><span class="n">parameters</span><span class="p">(),</span> <span class="n">lr</span><span class="o">=</span><span class="mf">0.001</span><span class="p">)</span>
<span class="n">my_model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">);</span>

<span class="n">epochs</span> <span class="o">=</span> <span class="mi">3</span>
<span class="n">steps</span> <span class="o">=</span> <span class="mi">0</span>
<span class="n">running_loss</span> <span class="o">=</span> <span class="mi">0</span>
<span class="n">print_every</span> <span class="o">=</span> <span class="mi">15</span>
<span class="n">train_losses</span><span class="p">,</span> <span class="n">valid_losses</span> <span class="o">=</span> <span class="p">[],</span> <span class="p">[]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>Downloading: &#34;https://download.pytorch.org/models/vgg16-397923af.pth&#34; to /root/.torch/models/vgg16-397923af.pth
100%|██████████| 553433881/553433881 [00:05&lt;00:00, 109937926.20it/s]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Starting the Training&quot;</span><span class="p">)</span>

<span class="k">for</span> <span class="n">epoch</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">epochs</span><span class="p">):</span>
    <span class="k">for</span> <span class="n">inputs</span><span class="p">,</span> <span class="n">labels</span> <span class="ow">in</span> <span class="n">trainloader</span><span class="p">:</span>
        <span class="n">steps</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="c1"># Move input and label tensors to the default device</span>
        <span class="n">inputs</span><span class="p">,</span> <span class="n">labels</span> <span class="o">=</span> <span class="n">inputs</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">),</span> <span class="n">labels</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>
        
        <span class="n">optimizer</span><span class="o">.</span><span class="n">zero_grad</span><span class="p">()</span>
        
        <span class="n">logps</span> <span class="o">=</span> <span class="n">my_model</span><span class="o">.</span><span class="n">forward</span><span class="p">(</span><span class="n">inputs</span><span class="p">)</span>
        <span class="n">loss</span> <span class="o">=</span> <span class="n">criterion</span><span class="p">(</span><span class="n">logps</span><span class="p">,</span> <span class="n">labels</span><span class="p">)</span>
        
        
        <span class="n">loss</span><span class="o">.</span><span class="n">backward</span><span class="p">()</span>
        <span class="n">optimizer</span><span class="o">.</span><span class="n">step</span><span class="p">()</span>

        <span class="n">running_loss</span> <span class="o">+=</span> <span class="n">loss</span><span class="o">.</span><span class="n">item</span><span class="p">()</span>

        <span class="k">if</span> <span class="n">steps</span> <span class="o">%</span> <span class="n">print_every</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
           <span class="n">valid_loss</span> <span class="o">=</span> <span class="mi">0</span>
           <span class="n">accuracy</span> <span class="o">=</span> <span class="mi">0</span>
           <span class="n">my_model</span><span class="o">.</span><span class="n">eval</span><span class="p">()</span>
           <span class="k">with</span> <span class="n">torch</span><span class="o">.</span><span class="n">no_grad</span><span class="p">():</span>
             <span class="k">for</span> <span class="n">inputs</span><span class="p">,</span> <span class="n">labels</span> <span class="ow">in</span> <span class="n">validloader</span><span class="p">:</span>
                  <span class="n">inputs</span><span class="p">,</span> <span class="n">labels</span> <span class="o">=</span> <span class="n">inputs</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">),</span> <span class="n">labels</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>
                  <span class="n">logps</span> <span class="o">=</span> <span class="n">my_model</span><span class="o">.</span><span class="n">forward</span><span class="p">(</span><span class="n">inputs</span><span class="p">)</span>
                  <span class="n">batch_loss</span> <span class="o">=</span> <span class="n">criterion</span><span class="p">(</span><span class="n">logps</span><span class="p">,</span> <span class="n">labels</span><span class="p">)</span>
  
                  <span class="n">valid_loss</span> <span class="o">+=</span> <span class="n">batch_loss</span><span class="o">.</span><span class="n">item</span><span class="p">()</span>
  
                  
                  <span class="c1"># Calculate accuracy</span>
                  <span class="n">ps</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">exp</span><span class="p">(</span><span class="n">logps</span><span class="p">)</span>
                  <span class="n">top_p</span><span class="p">,</span> <span class="n">top_class</span> <span class="o">=</span> <span class="n">ps</span><span class="o">.</span><span class="n">topk</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">dim</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
                  <span class="n">equals</span> <span class="o">=</span> <span class="n">top_class</span> <span class="o">==</span> <span class="n">labels</span><span class="o">.</span><span class="n">view</span><span class="p">(</span><span class="o">*</span><span class="n">top_class</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
                  <span class="n">accuracy</span> <span class="o">+=</span> <span class="n">torch</span><span class="o">.</span><span class="n">mean</span><span class="p">(</span><span class="n">equals</span><span class="o">.</span><span class="n">type</span><span class="p">(</span><span class="n">torch</span><span class="o">.</span><span class="n">FloatTensor</span><span class="p">))</span><span class="o">.</span><span class="n">item</span><span class="p">()</span>
           <span class="n">train_losses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">running_loss</span><span class="o">/</span><span class="nb">len</span><span class="p">(</span><span class="n">trainloader</span><span class="p">))</span>
           <span class="n">valid_losses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">valid_loss</span><span class="o">/</span><span class="nb">len</span><span class="p">(</span><span class="n">validloader</span><span class="p">))</span>

           <span class="nb">print</span><span class="p">(</span><span class="n">f</span><span class="s2">&quot;Epoch {epoch+1}/</span><span class="si">{epochs}</span><span class="s2">.. &quot;</span>
                <span class="n">f</span><span class="s2">&quot;Train loss: {running_loss/print_every:.3f}.. &quot;</span>
                <span class="n">f</span><span class="s2">&quot;Validation loss: {valid_loss/len(validloader):.3f}.. &quot;</span>
                <span class="n">f</span><span class="s2">&quot;Validation accuracy: {100*accuracy/len(validloader):.3f}%&quot;</span><span class="p">)</span>
           <span class="n">running_loss</span> <span class="o">=</span> <span class="mi">0</span>
           <span class="n">my_model</span><span class="o">.</span><span class="n">train</span><span class="p">()</span>
                
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">train_losses</span><span class="p">,</span> <span class="n">label</span> <span class="o">=</span> <span class="s1">&#39;Training loss&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">valid_losses</span><span class="p">,</span> <span class="n">label</span> <span class="o">=</span> <span class="s1">&#39;Validation loss&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">legend</span><span class="p">(</span><span class="n">frameon</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Starting the Training
Epoch 1/3.. Train loss: 4.451.. Validation loss: 3.275.. Validation accuracy: 30.591%
Epoch 1/3.. Train loss: 3.418.. Validation loss: 2.357.. Validation accuracy: 45.558%
Epoch 1/3.. Train loss: 2.953.. Validation loss: 1.901.. Validation accuracy: 52.250%
Epoch 1/3.. Train loss: 2.571.. Validation loss: 1.445.. Validation accuracy: 63.370%
Epoch 1/3.. Train loss: 2.227.. Validation loss: 1.276.. Validation accuracy: 68.077%
Epoch 1/3.. Train loss: 2.165.. Validation loss: 1.117.. Validation accuracy: 70.462%
Epoch 2/3.. Train loss: 1.952.. Validation loss: 1.041.. Validation accuracy: 73.519%
Epoch 2/3.. Train loss: 1.715.. Validation loss: 0.966.. Validation accuracy: 73.909%
Epoch 2/3.. Train loss: 1.712.. Validation loss: 0.919.. Validation accuracy: 74.082%
Epoch 2/3.. Train loss: 1.594.. Validation loss: 0.806.. Validation accuracy: 76.692%
Epoch 2/3.. Train loss: 1.787.. Validation loss: 0.825.. Validation accuracy: 76.264%
Epoch 2/3.. Train loss: 1.667.. Validation loss: 0.764.. Validation accuracy: 79.144%
Epoch 2/3.. Train loss: 1.498.. Validation loss: 0.745.. Validation accuracy: 80.087%
Epoch 3/3.. Train loss: 1.474.. Validation loss: 0.802.. Validation accuracy: 77.962%
Epoch 3/3.. Train loss: 1.434.. Validation loss: 0.707.. Validation accuracy: 80.038%
Epoch 3/3.. Train loss: 1.325.. Validation loss: 0.639.. Validation accuracy: 82.149%
Epoch 3/3.. Train loss: 1.338.. Validation loss: 0.697.. Validation accuracy: 80.880%
Epoch 3/3.. Train loss: 1.392.. Validation loss: 0.634.. Validation accuracy: 83.005%
Epoch 3/3.. Train loss: 1.403.. Validation loss: 0.655.. Validation accuracy: 82.784%
Epoch 3/3.. Train loss: 1.379.. Validation loss: 0.641.. Validation accuracy: 83.538%
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt output_prompt">Out[7]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.legend.Legend at 0x7f681cad55c0&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAusAAAH0CAYAAACEkWPuAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAWJQAAFiUBSVIk8AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4wLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvpW3flQAAIABJREFUeJzs3Xl4FeXB/vHvE8K+ySKr7CLuCygoouy4K3Vp61b1rdpWrUuhWltRqFZ9XVrXura4vj+r1YKlRVF2EFBBW1FEREERARFkUUSSzO+PSTiEJBLISeYk+X6ua64z85w5kxvUy5vhOc+EKIqQJEmSlHmykg4gSZIkqXiWdUmSJClDWdYlSZKkDGVZlyRJkjKUZV2SJEnKUJZ1SZIkKUNZ1iVJkqQMZVmXJEmSMpRlXZIkScpQlnVJkiQpQ1nWJUmSpAxlWZckSZIylGVdkiRJylCWdUmSJClDWdYlSZKkDGVZlyRJkjJUdtIBKlII4WOgEbAk4SiSJEmq2joC66Mo6lSWi1Srsg40qlu3btN99tmnadJBJEmSVHUtWLCATZs2lfk61a2sL9lnn32azp07N+kckiRJqsJ69OjBvHnzlpT1Os5ZlyRJkjKUZV2SJEnKUJZ1SZIkKUNZ1iVJkqQMZVmXJEmSMpRlXZIkScpQlnVJkiQpQ1nWJUmSpAxlWZckSZIylGVdkiRJylCWdUmSJClDWdYlSZKkDGVZlyRJkjKUZV2SJEnKUJZ1SZIkKUNZ1ivKd1/DsrlJp5AkSVIlYlkvb1s2weMnwf92hMeOj48lSVKVt3HjRkIInHjiiWW+1qGHHkqDBg3SkCp97rvvPkII/P3vf086SpVmWS9vNevChhWQ+x3kfAufzEo6kSRJVVoIYae2xx57LOnIUomykw5QLXTuD6s/iPcXT4IuA5LNI0lSFXbDDTcUGbvrrrtYt24dV1xxBbvttluh9w4++OByyVG/fn0WLFiQljvizz//PJs3b05DKlU2lvWK0GUAvP5QvL94SqJRJEmq6kaOHFlk7LHHHmPdunVceeWVdOzYsUJyhBDYe++903KtDh06pOU6qnycBlMROvaBrJrx/sp3YMPKZPNIkqQiCuaFb9q0ieuuu44999yTWrVqcdlllwHw5Zdfcuutt9K3b1/atGlDrVq1aNmyJaeddhrz5s0rcr2S5qwPHz6cEAJvvvkmTz/9ND169KBu3bo0b96cc889l1WrVpWYbVvjxo0jhMAdd9zB66+/zjHHHEPjxo1p0KABgwYNYu7c4he2+OSTTzjnnHNo3rw59erVo0ePHvztb38rdL2ymjVrFqeccgrNmzendu3adO7cmSuvvJIvvviiyLnLly/niiuuYK+99qJevXo0adKEffbZh5/+9Kd8+umnW8/Ly8vjkUceoVevXjRv3py6devSvn17jj/+eMaMGVPmzJnKO+sVoXYDaNcTls6Mjz+aAgf9KNFIkiSpqLy8PE488UQWLlzIMcccQ7Nmzbbe1X7rrbe44YYb6NevH6eccgqNGzfm448/5sUXX2TcuHG88sorHH300aX+Wbfddhvjxo3jlFNOoX///sycOZOnnnqK+fPn8+abb1KjRo1SXWfGjBlcd9119OvXj4suuoiPPvqIMWPG0K9fP+bPn1/orvyyZcs44ogjWL58OQMHDuSwww7js88+47zzzuO4447bud+sEjz77LOcffbZ1KhRgzPOOIM99tiD2bNnc/fddzN27FhmzpxJmzZtAFi/fj29evVi+fLlDBkyhKFDh7JlyxaWLl3K3//+d84991zatWsHwJVXXsm9995L165dOfPMM2nQoAHLly9nzpw5jBkzhqFDh6Ylf6axrFeULv23KeuTLeuSJGWgTZs2sWHDBubPn19kbnv37t1ZsWIFTZo0KTS+ePFievXqxbBhw3jjjTdK/bMmTpzI22+/zV577QVAFEUMHTqUF198kZdffpnjjz++VNcZO3Yszz33HKeffvrWsTvvvJPhw4dz//33c9ttt20dHzZsGMuXL+f3v/89I0aM2Dp+ySWX0KdPn1JnL8maNWu48MILCSEwY8YMDj300K3vjRgxgptuuonLLruMF154AYB//etfLFu2jOuuu44bb7yx0LW+/fZbcnJygNRd9S5duvDOO+9Qu3btQueuXr26zNkzlWW9onQeAJNuivcXT4YoghCSzSRJqnY6/uZfSUcotSW3npDIz73llluKFHWApk2bFnt+ly5dOPnkkxk9ejRffvklzZo1K9XP+fWvf721qEM8x/3CCy/kxRdf5PXXXy91WT/mmGMKFXWAiy++mOHDh/P6669vHduwYQMvvPACLVq04Ne//nWh8w8//HDOOOMMnnnmmVL9zJI899xzbNiwgYsuuqhQUQf43e9+x6OPPsrYsWNZvXo1zZs33/pe3bp1i1yrTp06hY5DCNSqVavYv3HY9lpVjXPWK0qbg6FO/n/4G1fAqgXJ5pEkScXq2bNnie9NnjyZU089lT322INatWptXf5x9OjRQDz/urS2L7PA1ikfa9euLdN1GjZsSOPGjQtdZ/78+eTk5NCjR48iRRhIy531grn7AwYUXfmuTp069O7dm7y8PP7zn/8AMHjwYHbffXdGjBjBiSeeyP3338/bb79NXl5eoc9mZWXx4x//mAULFrD//vszYsQIJkyYwIYNG8qcOdN5Z72iZNWAzv3gvfwvQCyeBC33TTKRJEnaTr169WjYsGGx7z311FP85Cc/oUGDBgwePJhOnTpRv359QghMmDCBWbNm7dTyisXdvc/OjqtZbm5uma5TcK1tr7Nu3ToAWrZsWez5JY3vjIKf0bp162LfLxj/6quvgPiO+Jw5cxg5ciTjxo3jX//619Ysl19+Oddcc83WO+kPPfQQe++9N48//jg33RTPVqhZsyYnn3wyd955Z5VdMceyXpG69C9c1ntflmweSVK1k9TUksoifM8U1euuu46GDRvy1ltv0blz50LvLVq0iFmzMvvBh40aNQJg5criV6UraXxnNG7cGIAVK1YU+/7nn39e6DyATp068fjjj5OXl8f8+fOZOHEi9913H7/73e+oUaMG11xzDRAX86uvvpqrr76aFStWMH36dJ566imef/553n//ff7zn/+U+ku5lYnTYCpS5/6p/aWvwZZvk8siSZJKLScnh6VLl3LwwQcXKepbtmzJ+KIOcMABB5Cdnc3cuXP59tuiHWTGjBll/hmHHHIIAFOmTCny3ubNm5k1axYhhGIfRJWVlcWBBx7IVVddxbhx4wBKXJKxVatWnHHGGYwdO5aePXvy7rvv8uGHH5Y5fyayrFekJh2g2Z7xfs4m+HR2snkkSVKpZGdn07ZtW959991CK4/k5eVx7bXX8vHHHyeYrnQaNmzI0KFDWbVqFbfffnuh9+bMmcNzzz1X5p/xwx/+kAYNGjB69Oit89IL3HLLLXz++edb118HePvtt1m2bFmR6xTc5a9Xrx4Qr1k/derUIudt3rx569Sb4r6kWhU4Daaide4PX+b/yW/xpHgeuyRJynhXXXUVw4cP58ADD+TUU08lKyuLqVOnsmTJEo477jjGjx+fdMQduvPOO5kxYwbXX38906ZN47DDDmPZsmU8++yznHTSSYwZM4asrF2/l9u0aVMefvhhzj33XI444gjOOOMM2rZty+zZs5k8eTLt2rXjvvvu23r+uHHjuOGGG+jTpw/dunWjefPmLF26lLFjx1KjRg2GDx8OxHPc+/XrR5cuXejZsyft27fnm2++4aWXXmLRokWcddZZtG/fvsy/P5nIsl7RugyANx6J9xdPhsHJxpEkSaXzq1/9igYNGnDffffx17/+lfr169OvXz+effZZHnnkkUpR1tu3b8/s2bO59tprefnll5kxYwb77rsvjz/+OJs2bWLMmDFb57bvqjPPPJP27dtz6623Mm7cODZs2ECbNm345S9/yXXXXUeLFi22nnvyySfzxRdfMH36dF544QU2btxI69atOemkkxg2bNjWlW6aNWvGzTffzOTJk5k+fTpffPEFjRo1omvXrlxzzTWcd955ZcqcyUIURUlnqDAhhLndu3fvXtLjdyvEt+vhtk6QFy/yz/APocHuyeWRJEkCrrjiCu655x5mzJjBkUcemXScSq9Hjx7MmzdvXhRFPcpyHeesV7Q6jWCPw1LHH01JLIokSap+ilsL/o033uDhhx+mTZs29OrVK4FUKonTYJLQZQB8kv+t8Y8mw4FnJJtHkiRVG/vssw/du3dnv/32o06dOixcuHDrFJ77779/61rvygzeWU9Cl22e6rV4ElSjqUiSJClZl1xyCWvWrOHpp5/m7rvvZs6cOZx44olMmzaNoUOHJh1P2/GPTklocwjUaQzfroMNn8MX70OLfZJOJUmSqoFbbrmFW265JekYKiXvrCchqwZ06ps6Xjw5uSySJEnKWJb1pHTZ5mmmiycll0OSJEkZy7KelG3nrS+ZATmbk8siSZKkjGRZT0qTjtC0c7yfswk+nZNoHEmSJGUey3qSOjsVRpIkSSWzrCep0BKOfslUkiRJhVnWk9TpKAg14v3P/wNfr042jyRJkjKKZT1JdRrDHofmH0Tw0ZQk00iSJCnDWNaTtu1UmI+cCiNJkqQUy3rStp+3HkXJZZEkSTvlww8/JITAhRdeWGj8nHPOIYTAsmXLSn2tPfbYgz333DPdEQspKW+SXn31VUII3HTTTUlHyUhpKeshhP8NIUwMIXwaQtgUQlgTQngrhHBDCKHZTl5rjxDCX0MIy0MIm0MIS0IId4UQmqQja8Zp0x1qN473138Gqz9INo8kSZXcWWedRQiBBx54YIfnDh48mBACY8aMqYBk5S8nJ4cQAoMGDUo6itIkXXfWrwLqA68AdwNPAznASOC/IYR2pblICKELMBe4AHgd+BPwEXAFMGtni3+lUCM7/qJpAVeFkSSpTC6++GIAHnnkke89b8mSJUycOJHWrVtz4oknpjXD7bffzoIFC2jVqlVar1tWHTp0YMGCBd7FrkTSVdYbRVF0eBRF/xNF0W+iKPplFEWHATcDbYBrS3mdPwMtgMujKBqaf60BxKW9G/CHNOXNLIWmwrjeuiRJZdGvXz/22msv3nrrLebNm1fieX/5y1+IoogLLriA7OzstGZo3bo1e++9d9qvW1Y1a9Zk7733zrg/RKhkaSnrURR9W8Jbz+a/dt3RNUIInYEhwBLg/u3evgH4Gjg3hFB/F2Nmri7bPBxpyQzI+S65LJIkVQEXXXQRUPLd9dzcXEaPHl1k/vZnn33GqFGj6N27N61ataJWrVq0bduWs88+m/fff7/UP7+kOetRFHHPPfew7777Urt2bdq2bcvll1/O+vXri73OV199xW233Ub//v1p27YttWrVokWLFgwdOpTXX3+90LmPPvooNWvWBGDixImEELZuBXfSv2/O+vLly/nFL35Bhw4dqF27Ni1atOC0007jrbfeKnLuo48+SgiBp556iokTJ9K3b18aNGhA48aNOemkk1i4cGGpf6++z8KFCzn33HNp06YNtWrVok2bNpx33nksXry4yLnr169n1KhR7L///jRs2JCGDRuy5557cuaZZxb5NYwZM4YBAwbQqlWrrf8c+vXrx4MPPpiW3OlU3l8wPSn/9b+lOLfg9vKEKIrytn0jiqINwEygHnB4+uJliKadoUnHeH/L17Ds9e89XZIkfb/zzjuPWrVq8X//93988803Rd4fP348n332GYMGDaJTp05bxydPnsxtt91G06ZNOe2007jyyivp2bMnzz77LD179mT+/PllynXZZZdxxRVXsG7dOn72s5/xox/9iHHjxjFkyBC2bNlS5Pz58+dz3XXXkZ2dzUknncSvfvUrBg4cyCuvvEKfPn149dVXt57bvXt3RowYAUCnTp244YYbtm5HH3309+ZavHgxPXr04MEHH2SvvfbiV7/6FYMHD+af//wnRxxxBOPHjy/2c2PGjOHYY49lt9124xe/+AW9e/dm3Lhx9O3blzVr1pThdwpmz57NYYcdxtNPP02vXr0YNmwYvXr14sknn+TQQw8t9LcmURQxZMgQRo4cSePGjbnooov4+c9/zmGHHcbkyZOZM2fO1nP//Oc/84Mf/ID333+fk08+mWHDhnHcccfx9ddf8/jjj5cpc7mIoihtGzCceJ76n4DpQAT8B9i9FJ+9Pf/8YSW8f1/++78oQ7653bt3jzLSi1dE0Q2N4u3VUUmnkSSp0vvhD38YAdHo0aOLvHfyySdHQPTcc88VGl+xYkW0YcOGIufPmzcvqlevXnTiiScWGl+0aFEERD/96U8LjZ999tkREH366adbx6ZOnRoBUdeuXaM1a9ZsHf/mm2+iww47LAKiLl26FLrO2rVro9WrVxfJs2TJkqhly5bR/vvvX2h8y5YtERANHDiwyGe+L++AAQMiILr11lsLjU+bNi3KysqKmjdvHn399ddbxx955JEIiLKzs6PJkycX+szw4cMjILrzzjuLzbC9V155JQKiG2+8cetYbm5u1LVr1wiInnnmmULnP/XUUxEQ7bffflFeXl4URfE/HyA6/fTTi1w/Jyen0O/3gQceGNWpUyf64osvipxb3Niu6t69ewTMjcrYr9M9kWo40HKb45eA86Mo+qIUn81fEoV1JbxfML7bji4UQphbwlt7lyJHMroMgLmj4/3Fk2Dg9cnmkSRVTSMb7/icTDGypEpQOhdffDHPPvssjz76KOeff/7W8c8//5x///vftGzZklNOOaXQZ1q2bElxDjnkEPr27cvEiRPJzc2lRo0aO51n9Oj4//MjRoygSZPUInd169bl5ptvZvDgwUU+s9tuxdeeDh06cOqpp/LAAw+wfPly2rRps9N5CixZsoRJkybRqVMnhg0bVui9o446ih/+8Ic888wzjBkzhrPOOqvQ+2effTb9+vUrNHbxxRdzxx13FJmmszOmT5/OokWLOOqoo/jRj35U5Gfed999zJ49m1mzZtG7d++t79WtW7fItWrUqFHo9xviufsFU4a21bx5813OXF7SOg0miqJWURQFoBVwKtAZeCuE0D0Nlw8FPyYN18o8nY6GkP+PY/nb8E3Z/upIkqTqbsCAAXTp0oWZM2eyYMGCreOjR48mJyeH888/v9jC9uKLL3LCCSfQqlUratasuXXe9/jx49m0adMuT+8omLbRt2/fIu8dffTRZGUVX8umT5/OGWecQbt27ahdu/bWPAVLU3722We7lKdAwXzuo48+utgvxA4YMKDQeds69NBDi4y1axcvArh27dpdzlTwe1Xws3eU6YADDuCAAw7gySef5KijjuL2229n1qxZxU4tOvvss9mwYQP77rsvv/rVrxg7diyrV6/e5azlrVy+ohxF0UrgHyGEecAHwBPA/jv4WMEfn0v6I3+j7c77vp/fo7jx/Dvu6fiDQ/rV3Q3a9oBlbwARfDQF9j816VSSJFVaBV+kvPbaa3n00Ue58847iaKIv/71ryV+yfKPf/wjw4YNo2nTpgwaNIgOHTpQt25dQgi88MILvPPOO2zevHmX8qxbF1eY4u7e16pVq8jdX4DnnnuOH//4x9StW5fBgwfTuXNn6tevT1ZWFpMmTWL69Om7nGf7XK1bty72/YLxr776qsh7xd35Lyj8ubm5FZYpOzubKVOmMGrUKJ5//nmuvvpqABo1asT555/PzTffTP368RolV199NS1atOCBBx7grrvu4k9/+hMhBPr378/tt99O9+6ZVRXLdT2hKIqWhhDeAw4OITSPouj7/thS8LXhvUp4v2BFmar71KAuA/LLOvFUGMu6JCndyji1pLK54IILuP7663niiSe45ZZbmD59OosXL2bAgAFFnha6ZcsWRo4cSZs2bZg3b16RUj19+vQyZWncOL4fuXLlStq3b1/ove+++461a9cWKb8jRoygTp06zJ07l27duhV679NPPy1zpm1zrVixotj3P//880LnVYRdydS0aVPuvvtu7r77bhYtWsSUKVN46KGHuOeee1i/fv3WaUgA559/Pueffz5r167ltdde44UXXmD06NEcc8wxvP/++zRrljmP9inv1WAgXmcdYEd/vCp4GtCQEEKhXCGEhsCRwCZgdnrjZZBt11v/aApEVXPGjyRJFaVly5acfPLJrF69mjFjxvDoo48CqQcnbWvlypVs2LCBPn36FCnq69evL3YayM4ouGM7derUIu9NmzaNvLy8IuOLFy9m//33L1LUc3NzmTlzZpHzC6bS7Mxd7UMOOQSI/zBS3OcmT55cKH9FKMg0ZcqUYt8vGC8pU9euXbnooouYOnUqdevWLfEJtU2aNOGEE07gL3/5C+eeey6rV69mxowZZc6f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
"
width=373
height=250
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Testing-your-network">Testing your network<a class="anchor-link" href="#Testing-your-network">&#182;</a></h2><p>It's good practice to test your trained network on test data, images the network has never seen either in training or validation. This will give you a good estimate for the model's performance on completely new images. Run the test images through the network and measure the accuracy, the same way you did validation. You should be able to reach around 70% accuracy on the test set if the model has been trained well.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># TODO: Do validation on the test set</span>
<span class="n">device</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">device</span><span class="p">(</span><span class="s2">&quot;cuda&quot;</span> <span class="k">if</span> <span class="n">torch</span><span class="o">.</span><span class="n">cuda</span><span class="o">.</span><span class="n">is_available</span><span class="p">()</span> <span class="k">else</span> <span class="s2">&quot;cpu&quot;</span><span class="p">)</span>
<span class="n">my_model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">);</span>
<span class="n">my_model</span><span class="o">.</span><span class="n">eval</span><span class="p">()</span>
<span class="n">accuracy</span> <span class="o">=</span> <span class="mi">0</span>
<span class="n">test_loss</span> <span class="o">=</span> <span class="mi">0</span>
<span class="k">with</span> <span class="n">torch</span><span class="o">.</span><span class="n">no_grad</span><span class="p">():</span>
   <span class="k">for</span> <span class="n">inputs</span><span class="p">,</span> <span class="n">labels</span> <span class="ow">in</span> <span class="n">testloader</span><span class="p">:</span>
        <span class="n">inputs</span><span class="p">,</span> <span class="n">labels</span> <span class="o">=</span> <span class="n">inputs</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">),</span> <span class="n">labels</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>
        <span class="n">logps</span> <span class="o">=</span> <span class="n">my_model</span><span class="o">.</span><span class="n">forward</span><span class="p">(</span><span class="n">inputs</span><span class="p">)</span>
        <span class="n">batch_loss</span> <span class="o">=</span> <span class="n">criterion</span><span class="p">(</span><span class="n">logps</span><span class="p">,</span> <span class="n">labels</span><span class="p">)</span>

        <span class="n">test_loss</span> <span class="o">+=</span> <span class="n">batch_loss</span><span class="o">.</span><span class="n">item</span><span class="p">()</span>

        <span class="c1"># Calculate accuracy</span>
        <span class="n">ps</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">exp</span><span class="p">(</span><span class="n">logps</span><span class="p">)</span>
        <span class="n">top_p</span><span class="p">,</span> <span class="n">top_class</span> <span class="o">=</span> <span class="n">ps</span><span class="o">.</span><span class="n">topk</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">dim</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
        <span class="n">equals</span> <span class="o">=</span> <span class="n">top_class</span> <span class="o">==</span> <span class="n">labels</span><span class="o">.</span><span class="n">view</span><span class="p">(</span><span class="o">*</span><span class="n">top_class</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
        <span class="n">accuracy</span> <span class="o">+=</span> <span class="n">torch</span><span class="o">.</span><span class="n">mean</span><span class="p">(</span><span class="n">equals</span><span class="o">.</span><span class="n">type</span><span class="p">(</span><span class="n">torch</span><span class="o">.</span><span class="n">FloatTensor</span><span class="p">))</span><span class="o">.</span><span class="n">item</span><span class="p">()</span>

<span class="nb">print</span><span class="p">(</span><span class="n">f</span><span class="s2">&quot;Test Loss: {test_loss/len(testloader):.3f}.. &quot;</span>
        <span class="n">f</span><span class="s2">&quot;Test accuracy: {100*accuracy/len(testloader):.3f} %&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Test Loss: 0.815.. Test accuracy: 78.957 %
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Save-the-checkpoint">Save the checkpoint<a class="anchor-link" href="#Save-the-checkpoint">&#182;</a></h2><p>Now that your network is trained, save the model so you can load it later for making predictions. You probably want to save other things such as the mapping of classes to indices which you get from one of the image datasets: <code>image_datasets['train'].class_to_idx</code>. You can attach this to the model as an attribute which makes inference easier later on.</p>
<p><code>model.class_to_idx = image_datasets['train'].class_to_idx</code></p>
<p>Remember that you'll want to completely rebuild the model later so you can use it for inference. Make sure to include any information you need in the checkpoint. If you want to load the model and keep training, you'll want to save the number of epochs as well as the optimizer state, <code>optimizer.state_dict</code>. You'll likely want to use this trained model in the next part of the project, so best to save it now.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># TODO: Save the checkpoint</span>
<span class="n">checkpoint</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;state_dict&#39;</span><span class="p">:</span> <span class="n">my_model</span><span class="o">.</span><span class="n">state_dict</span><span class="p">(),</span>
              <span class="s1">&#39;input_size&#39;</span><span class="p">:</span> <span class="mi">25088</span><span class="p">,</span>
              <span class="s1">&#39;hidden_layer&#39;</span><span class="p">:</span> <span class="mi">512</span>
              <span class="s1">&#39;output_size&#39;</span><span class="p">:</span> <span class="mi">102</span><span class="p">,</span> 
              <span class="s1">&#39;epochs&#39;</span><span class="p">:</span> <span class="n">epochs</span><span class="p">,</span>
              <span class="s1">&#39;learning_rate&#39;</span><span class="p">:</span> <span class="mf">0.001</span><span class="p">,</span>
              <span class="s1">&#39;class_to_idx&#39;</span><span class="p">:</span> <span class="n">train_data_datasets</span><span class="o">.</span><span class="n">class_to_idx</span><span class="p">,</span>
              <span class="s1">&#39;classifier&#39;</span><span class="p">:</span> <span class="n">my_model</span><span class="o">.</span><span class="n">classifier</span><span class="p">,</span>
              <span class="s1">&#39;optimizer&#39;</span><span class="p">:</span> <span class="n">optimizer</span><span class="o">.</span><span class="n">state_dict</span><span class="p">()}</span>
<span class="c1">#Save chesckpoint</span>
<span class="n">torch</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="n">checkpoint</span><span class="p">,</span> <span class="s1">&#39;cuba_my_checkpoint.pth&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Loading-the-checkpoint">Loading the checkpoint<a class="anchor-link" href="#Loading-the-checkpoint">&#182;</a></h2><p>At this point it's good to write a function that can load a checkpoint and rebuild the model. That way you can come back to this project and keep working on it without having to retrain the network.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># TODO: Write a function that loads a checkpoint and rebuilds the model</span>
<span class="n">device</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">device</span><span class="p">(</span><span class="s2">&quot;cuda&quot;</span> <span class="k">if</span> <span class="n">torch</span><span class="o">.</span><span class="n">cuda</span><span class="o">.</span><span class="n">is_available</span><span class="p">()</span> <span class="k">else</span> <span class="s2">&quot;cpu&quot;</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">load_checkpoint</span><span class="p">(</span><span class="n">filepath</span><span class="p">):</span>
    <span class="n">checkpoint</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">filepath</span><span class="p">,</span><span class="n">map_location</span><span class="o">=</span><span class="s2">&quot;cpu&quot;</span><span class="p">)</span>
    <span class="n">my_model</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">vgg16</span><span class="p">(</span><span class="n">pretrained</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
    <span class="n">my_model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">);</span>
    <span class="k">for</span> <span class="n">param</span> <span class="ow">in</span> <span class="n">my_model</span><span class="o">.</span><span class="n">parameters</span><span class="p">():</span>
        <span class="n">param</span><span class="o">.</span><span class="n">requires_grad</span> <span class="o">=</span> <span class="kc">False</span> 
    
    <span class="n">classifier</span> <span class="o">=</span> <span class="n">nn</span><span class="o">.</span><span class="n">Sequential</span><span class="p">(</span><span class="n">OrderedDict</span><span class="p">([</span>
                 <span class="p">(</span><span class="s1">&#39;fc1&#39;</span><span class="p">,</span><span class="n">nn</span><span class="o">.</span><span class="n">Linear</span><span class="p">(</span><span class="n">checkpoint</span><span class="p">[</span><span class="s1">&#39;input_size&#39;</span><span class="p">],</span><span class="n">checkpoint</span><span class="p">[</span><span class="s1">&#39;hidden_layer&#39;</span><span class="p">])),</span> 
                 <span class="p">(</span><span class="s1">&#39;relu&#39;</span><span class="p">,</span><span class="n">nn</span><span class="o">.</span><span class="n">ReLU</span><span class="p">()),</span>
                 <span class="p">(</span><span class="s1">&#39;Dropout&#39;</span><span class="p">,</span><span class="n">nn</span><span class="o">.</span><span class="n">Dropout</span><span class="p">(</span><span class="mf">0.4</span><span class="p">)),</span>
                 <span class="p">(</span><span class="s1">&#39;fc2&#39;</span><span class="p">,</span><span class="n">nn</span><span class="o">.</span><span class="n">Linear</span><span class="p">(</span><span class="n">checkpoint</span><span class="p">[</span><span class="s1">&#39;hidden_layer&#39;</span><span class="p">],</span><span class="n">checkpoint</span><span class="p">[</span><span class="s1">&#39;output_size&#39;</span><span class="p">])),</span>
                 <span class="p">(</span><span class="s1">&#39;output&#39;</span><span class="p">,</span><span class="n">nn</span><span class="o">.</span><span class="n">LogSoftmax</span><span class="p">(</span><span class="n">dim</span><span class="o">=</span><span class="mi">1</span><span class="p">))]))</span>
    <span class="n">my_model</span><span class="o">.</span><span class="n">classifier</span> <span class="o">=</span> <span class="n">classifier</span>
    <span class="n">my_model</span><span class="o">.</span><span class="n">optimizer</span>  <span class="o">=</span> <span class="n">checkpoint</span><span class="p">[</span><span class="s1">&#39;optimizer&#39;</span><span class="p">]</span>
    <span class="n">my_model</span><span class="o">.</span><span class="n">load_state_dict</span><span class="p">(</span><span class="n">checkpoint</span><span class="p">[</span><span class="s1">&#39;state_dict&#39;</span><span class="p">])</span>
    <span class="n">my_model</span><span class="o">.</span><span class="n">class_to_index</span> <span class="o">=</span> <span class="n">checkpoint</span><span class="p">[</span><span class="s1">&#39;class_to_idx&#39;</span><span class="p">]</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">f</span><span class="s2">&quot;Load Model Hyper paramter Values: </span><span class="se">\n</span><span class="s2">&quot;</span> 
               <span class="c1"># f&quot;optimizer:  {checkpoint[&#39;optimizer&#39;]} \n&quot;</span>
                <span class="c1">#f&quot;classifier: {checkpoint[&#39;classifier&#39;] }\n&quot;</span>
                <span class="n">f</span><span class="s2">&quot;input_size: {checkpoint[&#39;input_size&#39;] }</span><span class="se">\n</span><span class="s2">&quot;</span>
                <span class="n">f</span><span class="s2">&quot;output_size: </span><span class="si">{checkpoint[&#39;output_size&#39;]}</span><span class="se">\n</span><span class="s2">&quot;</span>
                <span class="n">f</span><span class="s2">&quot;epochs: {checkpoint[&#39;epochs&#39;] }&quot;</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">my_model</span>
<span class="n">loaded_model</span> <span class="o">=</span> <span class="kc">None</span>
<span class="n">loaded_model</span> <span class="o">=</span> <span class="n">load_checkpoint</span><span class="p">(</span><span class="s1">&#39;cuba_my_checkpoint.pth&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>Downloading: &#34;https://download.pytorch.org/models/vgg16-397923af.pth&#34; to /root/.torch/models/vgg16-397923af.pth
100%|██████████| 553433881/553433881 [00:07&lt;00:00, 69744391.47it/s]
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Load Model Hyper paramter Values: 
input_size: 25088
output_size: 102
epochs: 3
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Inference-for-classification">Inference for classification<a class="anchor-link" href="#Inference-for-classification">&#182;</a></h1><p>Now you'll write a function to use a trained network for inference. That is, you'll pass an image into the network and predict the class of the flower in the image. Write a function called <code>predict</code> that takes an image and a model, then returns the top $K$ most likely classes along with the probabilities. It should look like</p>
<div class="highlight"><pre><span></span><span class="n">probs</span><span class="p">,</span> <span class="n">classes</span> <span class="o">=</span> <span class="n">predict</span><span class="p">(</span><span class="n">image_path</span><span class="p">,</span> <span class="n">model</span><span class="p">)</span>
<span class="k">print</span><span class="p">(</span><span class="n">probs</span><span class="p">)</span>
<span class="k">print</span><span class="p">(</span><span class="n">classes</span><span class="p">)</span>
<span class="o">&gt;</span> <span class="p">[</span> <span class="mf">0.01558163</span>  <span class="mf">0.01541934</span>  <span class="mf">0.01452626</span>  <span class="mf">0.01443549</span>  <span class="mf">0.01407339</span><span class="p">]</span>
<span class="o">&gt;</span> <span class="p">[</span><span class="s1">&#39;70&#39;</span><span class="p">,</span> <span class="s1">&#39;3&#39;</span><span class="p">,</span> <span class="s1">&#39;45&#39;</span><span class="p">,</span> <span class="s1">&#39;62&#39;</span><span class="p">,</span> <span class="s1">&#39;55&#39;</span><span class="p">]</span>
</pre></div>
<p>First you'll need to handle processing the input image such that it can be used in your network.</p>
<h2 id="Image-Preprocessing">Image Preprocessing<a class="anchor-link" href="#Image-Preprocessing">&#182;</a></h2><p>You'll want to use <code>PIL</code> to load the image (<a href="https://pillow.readthedocs.io/en/latest/reference/Image.html">documentation</a>). It's best to write a function that preprocesses the image so it can be used as input for the model. This function should process the images in the same manner used for training.</p>
<p>First, resize the images where the shortest side is 256 pixels, keeping the aspect ratio. This can be done with the <a href="http://pillow.readthedocs.io/en/3.1.x/reference/Image.html#PIL.Image.Image.thumbnail"><code>thumbnail</code></a> or <a href="http://pillow.readthedocs.io/en/3.1.x/reference/Image.html#PIL.Image.Image.thumbnail"><code>resize</code></a> methods. Then you'll need to crop out the center 224x224 portion of the image.</p>
<p>Color channels of images are typically encoded as integers 0-255, but the model expected floats 0-1. You'll need to convert the values. It's easiest with a Numpy array, which you can get from a PIL image like so <code>np_image = np.array(pil_image)</code>.</p>
<p>As before, the network expects the images to be normalized in a specific way. For the means, it's <code>[0.485, 0.456, 0.406]</code> and for the standard deviations <code>[0.229, 0.224, 0.225]</code>. You'll want to subtract the means from each color channel, then divide by the standard deviation.</p>
<p>And finally, PyTorch expects the color channel to be the first dimension but it's the third dimension in the PIL image and Numpy array. You can reorder dimensions using <a href="https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.ndarray.transpose.html"><code>ndarray.transpose</code></a>. The color channel needs to be first and retain the order of the other two dimensions.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[14]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">process_image</span><span class="p">(</span><span class="n">image</span><span class="p">):</span>
    <span class="n">im</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>
    <span class="c1">##normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],</span>
    <span class="c1">#                             std=[0.229, 0.224, 0.225])</span>
    <span class="c1">#test_valid_transforms = transforms.Compose([transforms.Resize(224),</span>
    <span class="c1">#                                  transforms.CenterCrop(224),</span>
    <span class="c1">#                                  transforms.ToTensor(),</span>
    <span class="c1">#                                  normalize])</span>
    <span class="c1">#image_tensor = test_valid_transforms(im).float()</span>
    <span class="c1">#image_tensor = image_tensor.unsqueeze_(0)</span>
    <span class="c1">#input = Variable(image_tensor)</span>
    <span class="c1">#input = input.to(device)</span>
    
    <span class="c1">#return image_tensor</span>
    <span class="sd">&#39;&#39;&#39; Scales, crops, and normalizes a PIL image for a PyTorch model,</span>
<span class="sd">        returns an Numpy array</span>
<span class="sd">    &#39;&#39;&#39;</span>
 <span class="c1">#   print(f&quot; Image : {image}&quot;)</span>
    <span class="n">im</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>
    <span class="n">width</span><span class="p">,</span> <span class="n">height</span> <span class="o">=</span> <span class="n">im</span><span class="o">.</span><span class="n">size</span>
    <span class="n">size_r</span> <span class="o">=</span> <span class="nb">float</span><span class="p">(</span><span class="n">width</span><span class="o">/</span><span class="n">height</span><span class="p">)</span>
    <span class="n">n_width</span>  <span class="o">=</span> <span class="mi">256</span> <span class="k">if</span> <span class="n">size_r</span> <span class="o">&lt;=</span> <span class="mi">1</span> <span class="k">else</span> <span class="mi">256</span><span class="o">*</span><span class="n">size_r</span>
    <span class="n">n_height</span> <span class="o">=</span> <span class="mi">256</span> <span class="k">if</span> <span class="n">size_r</span> <span class="o">&gt;=</span> <span class="mi">1</span> <span class="k">else</span> <span class="mi">256</span><span class="o">*</span><span class="n">size_r</span>
    <span class="n">im</span><span class="o">=</span><span class="n">im</span><span class="o">.</span><span class="n">resize</span><span class="p">((</span><span class="nb">int</span><span class="p">(</span><span class="n">n_width</span><span class="p">),</span><span class="nb">int</span><span class="p">(</span><span class="n">n_height</span><span class="p">)))</span>
    <span class="c1">#crop_size = (256 - 224)/2.</span>
    <span class="c1">#im=im.crop((crop_size, crop_size, crop_size, crop_size))</span>
    <span class="n">im</span><span class="o">=</span><span class="n">im</span><span class="o">.</span><span class="n">crop</span><span class="p">(((</span><span class="mi">256</span> <span class="o">-</span> <span class="mi">224</span><span class="p">)</span> <span class="o">/</span> <span class="mf">2.</span><span class="p">,</span> <span class="p">(</span><span class="mi">256</span> <span class="o">-</span> <span class="mi">224</span><span class="p">)</span> <span class="o">/</span> <span class="mf">2.</span><span class="p">,</span> <span class="p">(</span><span class="mi">256</span> <span class="o">+</span> <span class="mi">224</span><span class="p">)</span> <span class="o">/</span> <span class="mf">2.</span><span class="p">,</span> <span class="p">(</span><span class="mi">256</span> <span class="o">+</span> <span class="mi">224</span><span class="p">)</span> <span class="o">/</span> <span class="mf">2.</span><span class="p">))</span>
    <span class="n">im</span> <span class="o">=</span>  <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">im</span><span class="p">)</span><span class="o">/</span><span class="mi">255</span>
    <span class="n">mean</span> <span class="o">=</span> <span class="p">[</span><span class="mf">0.485</span><span class="p">,</span> <span class="mf">0.456</span><span class="p">,</span> <span class="mf">0.406</span><span class="p">]</span>
    <span class="n">std</span> <span class="o">=</span> <span class="p">[</span><span class="mf">0.229</span><span class="p">,</span> <span class="mf">0.224</span><span class="p">,</span> <span class="mf">0.225</span><span class="p">]</span>
    <span class="n">im</span> <span class="o">=</span> <span class="p">(</span><span class="n">im</span> <span class="o">-</span> <span class="n">mean</span><span class="p">)</span> <span class="o">/</span> <span class="n">std</span>
    <span class="n">im</span> <span class="o">=</span> <span class="n">im</span><span class="o">.</span><span class="n">transpose</span><span class="p">((</span><span class="mi">2</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">))</span>
    <span class="n">tns_im</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">from_numpy</span><span class="p">(</span><span class="n">im</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">tns_im</span>

    <span class="c1"># TODO: Process a PIL image for use in a PyTorch model</span>
<span class="n">d</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">103</span><span class="p">,</span><span class="n">size</span><span class="o">=</span><span class="mi">1</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">image_dir</span> <span class="o">=</span> <span class="n">test_dir</span><span class="o">+</span><span class="s2">&quot;/&quot;</span><span class="o">+</span><span class="nb">str</span><span class="p">(</span><span class="n">d</span><span class="p">)</span>
<span class="n">i_file</span> <span class="o">=</span> <span class="n">image_dir</span> <span class="o">+</span> <span class="s2">&quot;/&quot;</span> <span class="o">+</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="n">image_dir</span><span class="p">))</span>
<span class="n">tns_image</span><span class="o">=</span><span class="n">process_image</span><span class="p">(</span><span class="n">i_file</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">i_file</span><span class="p">)</span>
<span class="n">imshow</span><span class="p">(</span><span class="n">tns_image</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>flowers/test/24/image_06849.jpg
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt output_prompt">Out[14]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.axes._subplots.AxesSubplot at 0x7fe3c95adf60&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
width=259
height=251
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>To check your work, the function below converts a PyTorch tensor and displays it in the notebook. If your <code>process_image</code> function works, running the output through this function should return the original image (except for the cropped out portions).</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">imshow</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">ax</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Imshow for Tensor.&quot;&quot;&quot;</span>
    <span class="k">if</span> <span class="n">ax</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>
    
    <span class="c1"># PyTorch tensors assume the color channel is the first dimension</span>
    <span class="c1"># but matplotlib assumes is the third dimension</span>
    <span class="n">image</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">numpy</span><span class="p">()</span><span class="o">.</span><span class="n">transpose</span><span class="p">((</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">0</span><span class="p">))</span>
    
    <span class="c1"># Undo preprocessing</span>
    <span class="n">mean</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mf">0.485</span><span class="p">,</span> <span class="mf">0.456</span><span class="p">,</span> <span class="mf">0.406</span><span class="p">])</span>
    <span class="n">std</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mf">0.229</span><span class="p">,</span> <span class="mf">0.224</span><span class="p">,</span> <span class="mf">0.225</span><span class="p">])</span>
    <span class="n">image</span> <span class="o">=</span> <span class="n">std</span> <span class="o">*</span> <span class="n">image</span> <span class="o">+</span> <span class="n">mean</span>
    
    <span class="c1"># Image needs to be clipped between 0 and 1 or it looks like noise when displayed</span>
    <span class="n">image</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
    
    <span class="n">ax</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>
    
    <span class="k">return</span> <span class="n">ax</span>
<span class="n">d</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">103</span><span class="p">,</span><span class="n">size</span><span class="o">=</span><span class="mi">1</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">image_dir</span> <span class="o">=</span> <span class="n">test_dir</span><span class="o">+</span><span class="s2">&quot;/&quot;</span><span class="o">+</span><span class="nb">str</span><span class="p">(</span><span class="n">d</span><span class="p">)</span>
<span class="n">i_file</span> <span class="o">=</span> <span class="n">image_dir</span> <span class="o">+</span> <span class="s2">&quot;/&quot;</span> <span class="o">+</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="n">image_dir</span><span class="p">))</span>
<span class="n">tns_image</span><span class="o">=</span><span class="n">process_image</span><span class="p">(</span><span class="n">i_file</span><span class="p">)</span>
<span class="n">imshow</span><span class="p">(</span><span class="n">tns_image</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
width=259
height=251
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Class-Prediction">Class Prediction<a class="anchor-link" href="#Class-Prediction">&#182;</a></h2><p>Once you can get images in the correct format, it's time to write a function for making predictions with your model. A common practice is to predict the top 5 or so (usually called top-$K$) most probable classes. You'll want to calculate the class probabilities then find the $K$ largest values.</p>
<p>To get the top $K$ largest values in a tensor use <a href="http://pytorch.org/docs/master/torch.html#torch.topk"><code>x.topk(k)</code></a>. This method returns both the highest <code>k</code> probabilities and the indices of those probabilities corresponding to the classes. You need to convert from these indices to the actual class labels using <code>class_to_idx</code> which hopefully you added to the model or from an <code>ImageFolder</code> you used to load the data (<a href="#Save-the-checkpoint">see here</a>). Make sure to invert the dictionary so you get a mapping from index to class as well.</p>
<p>Again, this method should take a path to an image and a model checkpoint, then return the probabilities and classes.</p>
<div class="highlight"><pre><span></span><span class="n">probs</span><span class="p">,</span> <span class="n">classes</span> <span class="o">=</span> <span class="n">predict</span><span class="p">(</span><span class="n">image_path</span><span class="p">,</span> <span class="n">model</span><span class="p">)</span>
<span class="k">print</span><span class="p">(</span><span class="n">probs</span><span class="p">)</span>
<span class="k">print</span><span class="p">(</span><span class="n">classes</span><span class="p">)</span>
<span class="o">&gt;</span> <span class="p">[</span> <span class="mf">0.01558163</span>  <span class="mf">0.01541934</span>  <span class="mf">0.01452626</span>  <span class="mf">0.01443549</span>  <span class="mf">0.01407339</span><span class="p">]</span>
<span class="o">&gt;</span> <span class="p">[</span><span class="s1">&#39;70&#39;</span><span class="p">,</span> <span class="s1">&#39;3&#39;</span><span class="p">,</span> <span class="s1">&#39;45&#39;</span><span class="p">,</span> <span class="s1">&#39;62&#39;</span><span class="p">,</span> <span class="s1">&#39;55&#39;</span><span class="p">]</span>
</pre></div>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">predict</span><span class="p">(</span><span class="n">image_path</span><span class="p">,</span> <span class="n">i_model</span><span class="p">,</span> <span class="n">topk</span><span class="o">=</span><span class="mi">5</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39; Predict the class (or classes) of an image using a trained deep learning model.</span>
<span class="sd">    &#39;&#39;&#39;</span> 
    <span class="n">input_tns</span>  <span class="o">=</span> <span class="n">process_image</span><span class="p">(</span><span class="n">image_path</span><span class="p">)</span>
    <span class="n">input_tns</span> <span class="o">=</span> <span class="n">input_tns</span><span class="o">.</span><span class="n">unsqueeze</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
    <span class="n">input_tns</span> <span class="o">=</span> <span class="n">input_tns</span><span class="o">.</span><span class="n">float</span><span class="p">()</span>
    <span class="n">input_tns</span> <span class="o">=</span> <span class="n">input_tns</span>

    <span class="k">with</span> <span class="n">torch</span><span class="o">.</span><span class="n">no_grad</span><span class="p">():</span>
      <span class="n">logps</span> <span class="o">=</span> <span class="n">i_model</span><span class="o">.</span><span class="n">forward</span><span class="p">(</span><span class="n">input_tns</span><span class="p">)</span>        
    <span class="c1"># Calculate accuracy</span>
      <span class="n">ps</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">exp</span><span class="p">(</span><span class="n">logps</span><span class="p">)</span>
      <span class="n">probs</span><span class="p">,</span> <span class="n">classes</span> <span class="o">=</span> <span class="n">ps</span><span class="o">.</span><span class="n">topk</span><span class="p">(</span><span class="n">topk</span><span class="p">,</span> <span class="n">dim</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
      <span class="n">idx_to_class</span> <span class="o">=</span> <span class="p">{</span><span class="nb">int</span><span class="p">(</span><span class="n">val</span><span class="p">):</span> <span class="nb">int</span><span class="p">(</span><span class="n">key</span><span class="p">)</span> <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">val</span> <span class="ow">in</span> <span class="n">i_model</span><span class="o">.</span><span class="n">class_to_index</span><span class="o">.</span><span class="n">items</span><span class="p">()}</span>
      <span class="n">classes</span> <span class="o">=</span> <span class="n">classes</span><span class="o">.</span><span class="n">numpy</span><span class="p">()</span>
      <span class="n">classes</span> <span class="o">=</span> <span class="p">[</span><span class="n">idx_to_class</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">classes</span><span class="p">[</span><span class="mi">0</span><span class="p">]]</span>
      <span class="n">classes</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">from_numpy</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="n">classes</span><span class="p">]))</span>

    <span class="k">return</span>  <span class="n">probs</span><span class="p">,</span> <span class="n">classes</span>
    <span class="c1">#equals = top_class == labels.view(*top_class.shape)</span>
<span class="c1">#=============================================</span>
<span class="n">d</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">103</span><span class="p">,</span><span class="n">size</span><span class="o">=</span><span class="mi">1</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">image_dir</span> <span class="o">=</span> <span class="n">test_dir</span><span class="o">+</span><span class="s2">&quot;/&quot;</span><span class="o">+</span><span class="nb">str</span><span class="p">(</span><span class="n">d</span><span class="p">)</span>
<span class="n">i_file</span> <span class="o">=</span> <span class="n">image_dir</span> <span class="o">+</span> <span class="s2">&quot;/&quot;</span> <span class="o">+</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="n">image_dir</span><span class="p">))</span>  

<span class="n">loaded_model</span><span class="o">.</span><span class="n">eval</span><span class="p">()</span>         
<span class="n">probs</span><span class="p">,</span> <span class="n">classes</span> <span class="o">=</span> <span class="n">predict</span><span class="p">(</span><span class="n">i_file</span><span class="p">,</span> <span class="n">loaded_model</span><span class="p">,</span><span class="mi">5</span><span class="p">)</span>
    <span class="c1"># TODO: Implement the code to predict the class from an image file</span>
    <span class="c1">#probs, classes = predict(image_path, my_model)</span>

<span class="nb">print</span><span class="p">(</span><span class="n">i_file</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">probs</span><span class="o">.</span><span class="n">mean</span><span class="p">())</span>
<span class="nb">print</span><span class="p">(</span><span class="n">classes</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>flowers/test/62/image_07276.jpg
tensor(0.1428)
tensor([[ 55,  62,  65,  52,  84]])
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Sanity-Checking">Sanity Checking<a class="anchor-link" href="#Sanity-Checking">&#182;</a></h2><p>Now that you can use a trained model for predictions, check to make sure it makes sense. Even if the testing accuracy is high, it's always good to check that there aren't obvious bugs. Use <code>matplotlib</code> to plot the probabilities for the top 5 classes as a bar graph, along with the input image. It should look like this:</p>
<p><img src='assets/inference_example.png' width=300px></p>
<p>You can convert from the class integer encoding to actual flower names with the <code>cat_to_name.json</code> file (should have been loaded earlier in the notebook). To show a PyTorch tensor as an image, use the <code>imshow</code> function defined above.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># TODO: Display an image along with the top 5 classes</span>
<span class="k">def</span> <span class="nf">model_sanity</span><span class="p">(</span><span class="n">i_img</span><span class="p">,</span> <span class="n">i_model</span><span class="p">,</span><span class="n">top_n</span><span class="p">):</span>
    <span class="n">tns_input</span> <span class="o">=</span> <span class="n">process_image</span><span class="p">(</span><span class="n">i_img</span><span class="p">)</span>
    <span class="n">probs</span><span class="p">,</span> <span class="n">classes</span> <span class="o">=</span> <span class="n">predict</span><span class="p">(</span><span class="n">i_img</span><span class="p">,</span> <span class="n">i_model</span><span class="p">,</span><span class="n">top_n</span><span class="p">)</span>
    <span class="n">classes</span> <span class="o">=</span> <span class="n">classes</span><span class="o">.</span><span class="n">numpy</span><span class="p">()</span>
    <span class="n">probs</span>   <span class="o">=</span> <span class="n">probs</span><span class="o">.</span><span class="n">numpy</span><span class="p">()</span>
    <span class="n">real_class</span> <span class="o">=</span> <span class="n">i_img</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot;/&quot;</span><span class="p">)[</span><span class="o">-</span><span class="mi">2</span><span class="p">]</span>
    <span class="c1">#plt.figure(figsize = [20, 5])</span>
    <span class="n">fig</span><span class="p">,</span> <span class="p">(</span><span class="n">ax</span><span class="p">,</span> <span class="n">ax2</span><span class="p">)</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="mi">2</span><span class="p">),</span> <span class="n">ncols</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
    <span class="c1">###</span>
    
    <span class="n">pic</span> <span class="o">=</span> <span class="n">tns_input</span><span class="o">.</span><span class="n">numpy</span><span class="p">()</span><span class="o">.</span><span class="n">transpose</span><span class="p">((</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">0</span><span class="p">))</span>
    
    <span class="c1"># Undo preprocessing</span>
    <span class="n">mean</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mf">0.485</span><span class="p">,</span> <span class="mf">0.456</span><span class="p">,</span> <span class="mf">0.406</span><span class="p">])</span>
    <span class="n">std</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mf">0.229</span><span class="p">,</span> <span class="mf">0.224</span><span class="p">,</span> <span class="mf">0.225</span><span class="p">])</span>
    <span class="n">pic</span> <span class="o">=</span> <span class="n">std</span> <span class="o">*</span> <span class="n">pic</span> <span class="o">+</span> <span class="n">mean</span>
    
    <span class="c1"># Image needs to be clipped between 0 and 1 or it looks like noise when displayed</span>
    <span class="n">image</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">pic</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
    <span class="c1">#ax.axis(&#39;off&#39;) </span>
    <span class="n">ax</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="n">cat_to_name</span><span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">real_class</span><span class="p">)])</span>
    <span class="n">ax</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>
    <span class="c1">######</span>
    <span class="n">probs</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">flip</span><span class="p">(</span><span class="n">probs</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">axis</span> <span class="o">=</span> <span class="mi">0</span><span class="p">)</span>
    <span class="n">classes</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">flip</span><span class="p">(</span><span class="n">classes</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">axis</span> <span class="o">=</span> <span class="mi">0</span><span class="p">)</span>
    <span class="n">labels</span> <span class="o">=</span> <span class="p">[</span><span class="n">cat_to_name</span><span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">i</span><span class="p">)]</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">classes</span><span class="p">]</span>
    
    <span class="n">np_input</span> <span class="o">=</span> <span class="n">tns_input</span><span class="o">.</span><span class="n">numpy</span><span class="p">()</span><span class="o">.</span><span class="n">squeeze</span><span class="p">()</span>
     
    
    <span class="n">ax2</span><span class="o">.</span><span class="n">barh</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">probs</span><span class="p">)),</span> <span class="n">probs</span><span class="p">)</span>
    <span class="n">ax2</span><span class="o">.</span><span class="n">set_aspect</span><span class="p">(</span><span class="mf">0.185</span><span class="p">)</span>
    <span class="n">ax2</span><span class="o">.</span><span class="n">set_yticks</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="n">top_n</span><span class="p">))</span>
    <span class="n">ax2</span><span class="o">.</span><span class="n">set_yticklabels</span><span class="p">(</span><span class="n">labels</span><span class="p">)</span>
    <span class="n">ax2</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;Class Probability&#39;</span><span class="p">)</span>
    <span class="n">ax2</span><span class="o">.</span><span class="n">set_xlim</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mf">1.2</span><span class="p">)</span>
    
    <span class="n">plt</span><span class="o">.</span><span class="n">tight_layout</span>
<span class="n">d</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">103</span><span class="p">,</span><span class="n">size</span><span class="o">=</span><span class="mi">1</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">image_dir</span> <span class="o">=</span> <span class="n">test_dir</span><span class="o">+</span><span class="s2">&quot;/&quot;</span><span class="o">+</span><span class="nb">str</span><span class="p">(</span><span class="n">d</span><span class="p">)</span>
<span class="n">i_file</span> <span class="o">=</span> <span class="n">image_dir</span> <span class="o">+</span> <span class="s2">&quot;/&quot;</span> <span class="o">+</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="n">image_dir</span><span class="p">))</span>  
<span class="n">loaded_model</span><span class="o">.</span><span class="n">eval</span><span class="p">()</span>
<span class="n">model_sanity</span><span class="p">(</span><span class="n">i_img</span><span class="o">=</span><span class="n">i_file</span><span class="p">,</span> <span class="n">i_model</span> <span class="o">=</span> <span class="n">loaded_model</span><span class="p">,</span><span class="n">top_n</span> <span class="o">=</span> <span class="mi">5</span><span class="p">)</span>   
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
width=467
height=155
>
</div>

</div>

</div>
</div>

</div>
    </div>
  </div>
</body>

 


</html>
