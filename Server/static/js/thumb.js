(function ($) {
    $.extend({
        tipsBox: function (options) {
            options = $.extend({
                obj: null,
                str: "+1",
                startSize: "12px",
                endSize: "30px",
                interval: 600,
                color: "red",
                callback: function () {
                }
            }, options);
            $("body").append("<span class='num'>" + options.str + "</span>");
            var box = $(".num");
            var left = options.obj.offset().left + options.obj.width() / 2;
            var top = options.obj.offset().top - options.obj.height();
            box.css({
                "position": "absolute",
                "left": left + "px",
                "top": top + "px",
                "z-index": 9999,
                "font-size": options.startSize,
                "line-height": options.endSize,
                "color": options.color
            });
            box.animate({
                "font-size": options.endSize,
                "opacity": "0",
                "top": top - parseInt(options.endSize) + "px"
            }, options.interval, function () {
                box.remove();
                options.callback();
            });
        }
    });
})(jQuery);

function niceIn(prop) {
    prop.find('i').addClass('niceIn');
    setTimeout(function () {
        prop.find('i').removeClass('niceIn');
    }, 1000);
}

$(function () {
    $("#thumb-btn").click(function () {
        $.tipsBox({
            obj: $(this),
            str: "+1",
            callback: function () {
            }
        });
        $.post("/view/thumb/" + $("#view-id").attr("data-id") + "/");
        niceIn($(this));
    });
});