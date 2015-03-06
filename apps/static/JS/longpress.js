/**
 * Created by xulei on 2015-03-06.
 */
// 长按鼠标左键
//// 调用方法
/*$(obj).longPress(function() {
    $(this).html("test success!");
}, 500)*/
(function($) {
	$.extend($.fn, {
		longPress: function(callback, time) {
			time = time || 1000;
			var timer = null;
			$(this).mousedown(function() {
				var i = 0;
				timer = setInterval(function() {
					i += 10;
					if (i >= time) {
						clearInterval(timer);
						typeof callback == 'function' && callback.call();
					}
				}, 10)
			}).mouseup(function() {
				clearInterval(timer);
			})
		}
	});
})(jQuery);
