// coding: utf-8
/* 
 * arp_calendarで使用するAjax等のJavaScript
*/

var url = "/calendar/api/holidays/"+year+"/"+month+"/";
 
// $(function(){}) は $(document).ready(function(){})と等価．これはドキュ
// メントがロードされた際にjQueryにより実行されるハンドラを登録する．こ
// の場合ドキュメントがロードされたらajax処理により対象月の休暇情報をカ
// レンダーに反映させる．
$(function(){
    $.ajax({
        "url" : url,
        "type" : "GET",
        "dataType": "json",
        "success" : function(data, textStatus, xhr) {
            for (var i = 0; i < data.length; i++) {
		var d = data[i];
		var day1 = d.date.split('/')[2];
		var namecls = "";
		if (d.type.id == 1) {
		    namecls = "legal_holiday";
		} else if (d.type.id == 2) {
		    namecls = "not_legal_holiday";
		} else {
		    namecls = "other_day";
		}
		$("table.month td.dayCell[date="+day1+"] div.dayContent")
		    .append("<div class='"+namecls+"'>" + d.type.name +"</div>");
            }
        },
        "error" : function(xhr, textStatus, error) {
            alert("status = " + xhr.status);
        }
    });

    $('#dialogdemo1').dialog({
        autoOpen: false,
        title: '祝日設定',
        closeOnEscape: false,
        modal: true,
    });

    $('.dayCell:not(.noday)').click(function(){
        var cell = $(this);
        var date = cell.attr('date');
        $("#dialogdemo1")
            .dialog({
		title: date + "日 設定",
		buttons: {
		    "Cancel": function(){
			$(this).dialog('close');
		    },
		    "OK": function(){
			$(this).dialog('close');
			sendAjaxRequest();
		    },
		}
            })
            .dialog('open');
    });
});
