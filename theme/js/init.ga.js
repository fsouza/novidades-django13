(function (window) {
    if (window.location.href.indexOf('p.souza.cc') >= 0) {
        var _gaq = _gaq || [];
        _gaq.push(['_setAccount', 'UA-8088829-13']);
        _gaq.push(['_trackPageview']);

        (function() {
         var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
         ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
         var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
         })();
    }
})(window);